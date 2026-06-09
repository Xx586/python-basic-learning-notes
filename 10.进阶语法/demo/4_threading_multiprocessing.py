"""
演示多线程（I/O 任务）和多进程（CPU 任务）

本文件展示：
- threading.Thread 创建 / start / join
- Lock 线程安全（竞态条件演示）
- ThreadPoolExecutor 线程池
- multiprocessing.Process / Pool 进程池
- 进程通信 Queue
- I/O 密集 vs CPU 密集选择策略

可以独立运行，用 = 分隔线和 print 明确展示输出。
"""

import threading
import multiprocessing
import time
import os
from concurrent.futures import ThreadPoolExecutor, as_completed


# ============================================================================
# 一、threading.Thread 基础
# ============================================================================
print("=" * 60)
print("一、threading.Thread 基础")
print("=" * 60)

def worker(name: str, delay: float):
    """模拟 I/O 任务的工作函数"""
    print(f"  [{name}] 线程 {threading.current_thread().name} 开始")
    time.sleep(delay)  # 模拟 I/O 等待
    print(f"  [{name}] 线程 {threading.current_thread().name} 结束")

print("\n[1.1] 创建和启动线程:")
# 方式1：target 函数
t1 = threading.Thread(target=worker, args=("A", 0.5), name="Worker-A")
t2 = threading.Thread(target=worker, args=("B", 0.3), name="Worker-B")

start = time.time()
t1.start()  # 启动线程（非阻塞）
t2.start()

# 主线程可以继续做其他事
print(f"  [主线程] 线程已启动，等待完成...")

t1.join()   # 等待 t1 结束（阻塞）
t2.join()   # 等待 t2 结束（阻塞）
elapsed = time.time() - start
print(f"  [主线程] 全部完成，耗时: {elapsed:.2f}s（2 个任务并发）")

# 对比：如果同步执行
print(f"\n[对比] 同步执行:")
start = time.time()
worker("A", 0.5)
worker("B", 0.3)
sync_elapsed = time.time() - start
print(f"  [对比] 同步耗时: {sync_elapsed:.2f}s（2 个任务串行）")


# ============================================================================
# 二、Lock 线程安全（竞态条件演示）
# ============================================================================
print("\n" + "=" * 60)
print("二、Lock 线程安全 — 竞态条件演示")
print("=" * 60)

# --- 不加锁：结果不可预测 ---
print("\n[2.1] 不加锁（有竞态条件）:")
counter_unsafe = 0

def unsafe_increment():
    """非线程安全的计数器累加"""
    global counter_unsafe
    for _ in range(100000):
        # counter_unsafe += 1 实际是 3 个步骤：
        #   1. 读 counter
        #   2. 加 1
        #   3. 写回 counter
        # 线程可能在任一步骤被切换
        counter_unsafe += 1

threads = [threading.Thread(target=unsafe_increment) for _ in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"  期望值:  500000 (5 线程 × 100000)")
print(f"  实际值:  {counter_unsafe} (可能小于期望值)")

# --- 加锁：结果准确 ---
print("\n[2.2] 加锁（线程安全）:")
counter_safe = 0
lock = threading.Lock()

def safe_increment():
    """线程安全的计数器累加"""
    global counter_safe
    for _ in range(100000):
        with lock:  # 自动 acquire 和 release
            counter_safe += 1

threads = [threading.Thread(target=safe_increment) for _ in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"  期望值:  500000")
print(f"  实际值:  {counter_safe} (始终准确)")


# ============================================================================
# 三、ThreadPoolExecutor 线程池
# ============================================================================
print("\n" + "=" * 60)
print("三、ThreadPoolExecutor 线程池")
print("=" * 60)

def fetch_url(url: str) -> str:
    """模拟网络请求"""
    print(f"  [下载] 开始: {url}")
    time.sleep(0.5)  # 模拟网络延迟
    print(f"  [下载] 完成: {url}")
    return f"内容_{url}"

urls = [f"url_{i}" for i in range(1, 7)]  # 6 个任务

# 方式1：map（保持输入顺序）
print("\n[3.1] executor.map（保持顺序）:")
start = time.time()
with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(fetch_url, urls)
    for result in results:
        print(f"  [结果] {result}")
print(f"  6 个 URL / 3 并发，耗时: {time.time() - start:.1f}s")

# 方式2：submit + as_completed（按完成顺序）
print("\n[3.2] submit + as_completed（按完成顺序）:")
start = time.time()
with ThreadPoolExecutor(max_workers=3) as executor:
    # 提交所有任务
    futures = {executor.submit(fetch_url, url): url for url in urls}
    # 按完成顺序获取结果
    for future in as_completed(futures):
        url = futures[future]
        print(f"  [先完成] {url} → {future.result()}")
print(f"  耗时: {time.time() - start:.1f}s")


# ============================================================================
# 四、multiprocessing.Process 基础
# ============================================================================
print("\n" + "=" * 60)
print("四、multiprocessing.Process 基础")
print("=" * 60)

def cpu_task(n: int) -> int:
    """CPU 密集型任务：计算平方和"""
    pid = os.getpid()
    print(f"  [进程 {pid}] 开始计算 sum(i^2) for i in range({n})")
    result = sum(i ** 2 for i in range(n))
    print(f"  [进程 {pid}] 计算完成，结果 = {result}")
    return result

if __name__ == "__main__":
    print(f"  [主进程] PID: {os.getpid()}")
    print(f"  [CPU 核心数] {multiprocessing.cpu_count()}")

    # 对比：单进程 vs 多进程
    N = 5_000_000

    # 单进程
    print("\n[4.1] 单进程执行:")
    start = time.time()
    r1 = cpu_task(N)
    r2 = cpu_task(N)
    serial_time = time.time() - start
    print(f"  单进程耗时: {serial_time:.2f}s")

    # 多进程
    print("\n[4.2] 多进程并行:")
    start = time.time()
    p1 = multiprocessing.Process(target=cpu_task, args=(N,))
    p2 = multiprocessing.Process(target=cpu_task, args=(N,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()
    parallel_time = time.time() - start
    print(f"  多进程耗时: {parallel_time:.2f}s")
    print(f"  加速比: {serial_time / parallel_time:.2f}x")


# ============================================================================
# 五、进程池 Pool
# ============================================================================
print("\n" + "=" * 60)
print("五、multiprocessing.Pool 进程池")
print("=" * 60)

def compute_square(x: int) -> int:
    """简单计算任务"""
    time.sleep(0.1)  # 模拟一些计算开销
    return x * x

if __name__ == "__main__":
    numbers = list(range(1, 13))

    # map 方式
    print("\n[5.1] Pool.map:")
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(compute_square, numbers)
    print(f"  输入:  {numbers}")
    print(f"  输出:  {results}")

    # imap 方式（惰性迭代器）
    print("\n[5.2] Pool.imap（惰性）:")
    with multiprocessing.Pool(processes=4) as pool:
        for i, result in enumerate(pool.imap(compute_square, numbers)):
            print(f"  [{i+1}] {result}", end="")
            if (i + 1) % 3 == 0:
                print()
    print()

    # starmap 方式（多参数）
    print("\n[5.3] Pool.starmap（多参数）:")
    def power(base, exp):
        return base ** exp

    params = [(2, 3), (3, 3), (4, 3)]
    with multiprocessing.Pool(processes=3) as pool:
        results = pool.starmap(power, params)
    print(f"  power{params} = {results}")


# ============================================================================
# 六、进程通信 Queue
# ============================================================================
print("\n" + "=" * 60)
print("六、进程通信 Queue（生产者-消费者）")
print("=" * 60)

from multiprocessing import Process, Queue

def producer(q: Queue):
    """生产者：往队列放入数据"""
    for i in range(1, 6):
        time.sleep(0.1)
        msg = f"数据_{i}"
        print(f"  [生产者] 生产: {msg}")
        q.put(msg)
    q.put(None)  # 结束信号

def consumer(q: Queue):
    """消费者：从队列取出数据"""
    while True:
        item = q.get()
        if item is None:  # 结束信号
            break
        print(f"  [消费者] 消费: {item}")

if __name__ == "__main__":
    q = Queue()
    p_prod = Process(target=producer, args=(q,))
    p_cons = Process(target=consumer, args=(q,))

    p_prod.start()
    p_cons.start()
    p_prod.join()
    p_cons.join()
    print(f"  [全部完成] 生产者-消费者模式运行完毕")


# ============================================================================
# 七、I/O 密集 vs CPU 密集 —— 选择策略演示
# ============================================================================
print("\n" + "=" * 60)
print("七、I/O 密集 vs CPU 密集 —— 策略选择")
print("=" * 60)

print("""
  ┌──────────────┬────────────────┬──────────────────┐
  │   任务类型   │   推荐方式      │      原因         │
  ├──────────────┼────────────────┼──────────────────┤
  │ I/O 密集     │  多线程/协程   │ 等待 I/O 时 GIL   │
  │ (网络/磁盘)  │                │ 被释放，可并发     │
  ├──────────────┼────────────────┼──────────────────┤
  │ CPU 密集     │  多进程        │ 绕过 GIL，真正     │
  │ (计算/处理)  │                │ 并行执行          │
  ├──────────────┼────────────────┼──────────────────┤
  │ 高并发 I/O   │  asyncio(协程) │ 比线程更轻量，     │
  │ (万级连接)   │                │ 单线程内并发      │
  └──────────────┴────────────────┴──────────────────┘
""")


# ============================================================================
# 八、线程异常处理演示
# ============================================================================
print("=" * 60)
print("八、线程异常处理")
print("=" * 60)

def risky_task(name: str):
    """可能抛出异常的线程任务"""
    if name == "bad":
        raise ValueError(f"线程 {name} 异常！")
    print(f"  [线程 {name}] 正常完成")
    return f"结果_{name}"

print("\n[8.1] ThreadPoolExecutor 可以捕获线程异常:")
with ThreadPoolExecutor(max_workers=3) as executor:
    futures = {
        executor.submit(risky_task, "good1"): "good1",
        executor.submit(risky_task, "bad"): "bad",
        executor.submit(risky_task, "good2"): "good2",
    }
    for future in as_completed(futures):
        task_name = futures[future]
        try:
            result = future.result()  # 异常在这里抛出
            print(f"  [{task_name}] 成功: {result}")
        except Exception as e:
            print(f"  [{task_name}] 失败: {e}")

print("\n[8.2] 普通 threading.Thread（异常不传播到主线程）:")
# 普通 Thread 中抛异常，主线程感知不到
# 需要在 run() 中自行捕获
class SafeThread(threading.Thread):
    """安全的线程类：捕获并记录异常"""
    def run(self):
        try:
            raise ValueError("线程内部异常")
        except Exception as e:
            print(f"  [SafeThread] 捕获到: {e}")

t = SafeThread()
t.start()
t.join()
print(f"  [主线程] 不受影响，正常结束")


print("\n" + "=" * 60)
print("全部演示完成！")
print("=" * 60)
