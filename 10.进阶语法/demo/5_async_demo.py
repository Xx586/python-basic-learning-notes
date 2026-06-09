"""
演示 asyncio 基础 (async/await/gather/create_task)

本文件展示：
- 同步 vs 异步执行对比
- async def 协程函数 / await 挂起
- asyncio.run() / sleep() / gather() / create_task()
- 协程 vs 线程对比
- time.sleep vs asyncio.sleep 区别
- 异常处理 (return_exceptions)

可以独立运行，用 = 分隔线和 print 明确展示输出。
"""

import asyncio
import time


# ============================================================================
# 一、同步 vs 异步执行对比
# ============================================================================
print("=" * 60)
print("一、同步 vs 异步执行对比")
print("=" * 60)

# --- 同步版本 ---
def sync_task(name: str, delay: float):
    """同步任务：阻塞执行"""
    print(f"  [{name}] 开始")
    time.sleep(delay)  # 阻塞当前线程，CPU 空等
    print(f"  [{name}] 结束")

print("\n[1.1] 同步执行（阻塞）:")
start = time.time()
sync_task("A", 1)
sync_task("B", 1)
sync_task("C", 1)
print(f"  同步总耗时: {time.time() - start:.1f}s  (3 个任务 × 1s)")

# --- 异步版本 ---
async def async_task(name: str, delay: float):
    """异步任务：非阻塞，等待时让出控制权"""
    print(f"  [{name}] 开始")
    await asyncio.sleep(delay)  # 非阻塞！让出控制权给其他协程
    print(f"  [{name}] 结束")

async def run_async_tasks():
    """并发运行多个异步任务"""
    await asyncio.gather(
        async_task("A", 1),
        async_task("B", 1),
        async_task("C", 1),
    )

print("\n[1.2] 异步执行（非阻塞）:")
start = time.time()
asyncio.run(run_async_tasks())
print(f"  异步总耗时: {time.time() - start:.1f}s  (并发执行 ≈ 最长任务时间)")


# ============================================================================
# 二、async def / await 语法详解
# ============================================================================
print("\n" + "=" * 60)
print("二、async def / await 语法详解")
print("=" * 60)

# async def 返回一个协程对象（coroutine），不是普通返回值
async def hello():
    return "Hello, Async!"

coro = hello()  # 调用 async def 函数 → 返回协程对象
print(f"[2.1] 协程对象: type={type(coro)}")  # <class 'coroutine'>

# 必须用 await 或 asyncio.run() 来执行
result = asyncio.run(hello())
print(f"[2.2] asyncio.run() 结果: {result}")

# await 只能在 async def 函数内部使用
async def demo_await():
    """演示 await 的执行流程"""
    print("  步骤1: 开始")
    # await 挂起当前协程，等待 hello() 完成
    msg = await hello()
    print(f"  步骤2: 收到消息 '{msg}'")
    print("  步骤3: 结束")

print("\n[2.3] await 执行流程:")
asyncio.run(demo_await())


# ============================================================================
# 三、asyncio.gather() 并发运行
# ============================================================================
print("\n" + "=" * 60)
print("三、asyncio.gather() 并发运行")
print("=" * 60)

async def fetch_data(item_id: int) -> dict:
    """模拟异步获取数据"""
    await asyncio.sleep(0.2)  # 模拟网络请求
    return {"id": item_id, "data": f"内容_{item_id}"}

async def gather_demo():
    """演示 gather 的多种用法"""
    # 方式1：直接传参
    print("[3.1] 直接传参:")
    r1, r2, r3 = await asyncio.gather(
        fetch_data(1),
        fetch_data(2),
        fetch_data(3),
    )
    print(f"  结果: {r1}, {r2}, {r3}")

    # 方式2：展开列表
    print("\n[3.2] 展开列表:")
    tasks = [fetch_data(i) for i in range(4, 7)]
    results = await asyncio.gather(*tasks)
    print(f"  结果: {results}")

    # gather 保持结果顺序（不是完成顺序）
    print("\n[3.3] gather 保持输入顺序:")
    async def delayed_result(name: str, delay: float):
        await asyncio.sleep(delay)
        return f"{name} ({delay}s)"

    results = await asyncio.gather(
        delayed_result("慢", 0.3),
        delayed_result("快", 0.1),
        delayed_result("中", 0.2),
    )
    print(f"  结果顺序: {results}")
    # 即使"快"先完成，结果仍按输入顺序排列

asyncio.run(gather_demo())


# ============================================================================
# 四、asyncio.create_task() 创建后台任务
# ============================================================================
print("\n" + "=" * 60)
print("四、asyncio.create_task() 创建后台任务")
print("=" * 60)

async def background_work(name: str, duration: float) -> str:
    """模拟后台工作任务"""
    print(f"  [{name}] 后台任务开始 (耗时 {duration}s)")
    await asyncio.sleep(duration)
    print(f"  [{name}] 后台任务完成")
    return f"{name}_完成"

async def create_task_demo():
    """演示 create_task：提前提交任务，中间做其他事"""
    print("[4.1] create_task 模式:")

    # 创建 Task → 立即提交到事件循环，不阻塞
    task1 = asyncio.create_task(background_work("下载文件", 1))
    task2 = asyncio.create_task(background_work("处理图片", 0.5))

    print("  [主协程] 任务已提交，做其他事情...")
    await asyncio.sleep(0.3)
    print("  [主协程] 继续做其他事...")

    # 等待 Task 完成
    result1 = await task1
    result2 = await task2
    print(f"  全部完成: {result1}, {result2}")

asyncio.run(create_task_demo())


# ============================================================================
# 五、gather vs create_task 对比
# ============================================================================
print("\n" + "=" * 60)
print("五、gather vs create_task 对比")
print("=" * 60)

async def compare_patterns():
    """对比两种并发模式"""

    # gather 模式：适合"一起等待所有结果"
    print("[gather 模式] 适合：需要所有结果再继续")
    results = await asyncio.gather(
        fetch_data(1),
        fetch_data(2),
    )
    print(f"  gather 结果: {results}")

    # create_task 模式：适合"提前提交，中间穿插逻辑"
    print("\n[create_task 模式] 适合：提前提交 + 中间做其他事")
    t1 = asyncio.create_task(fetch_data(3))
    t2 = asyncio.create_task(fetch_data(4))

    # 在等待期间做其他事
    print("  中间处理...")
    await asyncio.sleep(0.1)
    print("  继续处理...")

    r1 = await t1
    r2 = await t2
    print(f"  create_task 结果: {r1}, {r2}")

asyncio.run(compare_patterns())


# ============================================================================
# 六、time.sleep vs asyncio.sleep（关键区别）
# ============================================================================
print("\n" + "=" * 60)
print("六、time.sleep vs asyncio.sleep（关键区别）")
print("=" * 60)

async def bad_sleep():
    """错误示范：在协程中使用 time.sleep → 阻塞整个事件循环"""
    print("  [BAD] 使用 time.sleep(1) 开始")
    time.sleep(1)  # 阻塞！所有协程都卡住
    print("  [BAD] time.sleep(1) 结束")

async def good_sleep():
    """正确示范：使用 asyncio.sleep → 只挂起当前协程"""
    print("  [GOOD] 使用 await asyncio.sleep(1) 开始")
    await asyncio.sleep(1)  # 非阻塞，让出控制权
    print("  [GOOD] asyncio.sleep(1) 结束")

async def compare_sleep():
    """对比两种 sleep 的并发效果"""
    print("\n[6.1] time.sleep（阻塞整个循环）:")
    start = time.time()
    # 虽然用了 gather，但 time.sleep 会阻塞事件循环
    # 实际上仍是串行执行
    await asyncio.gather(bad_sleep(), bad_sleep())
    print(f"  time.sleep 版本耗时: {time.time() - start:.1f}s")

    print("\n[6.2] asyncio.sleep（真正并发）:")
    start = time.time()
    await asyncio.gather(good_sleep(), good_sleep())
    print(f"  asyncio.sleep 版本耗时: {time.time() - start:.1f}s")

asyncio.run(compare_sleep())


# ============================================================================
# 七、协程异常处理
# ============================================================================
print("\n" + "=" * 60)
print("七、协程异常处理")
print("=" * 60)

async def success_task(name: str):
    """正常完成的协程"""
    await asyncio.sleep(0.1)
    return f"{name}_成功"

async def fail_task(name: str):
    """会抛异常的协程"""
    await asyncio.sleep(0.1)
    raise ValueError(f"{name} 失败了！")

async def exception_demo():
    """演示协程异常处理的两种方式"""

    # 方式1：默认行为 → 任何协程异常，gather 立即抛出
    print("[7.1] 默认行为（异常立即抛出）:")
    try:
        await asyncio.gather(
            success_task("A"),
            fail_task("B"),        # 这个会失败
            success_task("C"),     # 可能还没执行完
        )
    except ValueError as e:
        print(f"  捕获到: {e}")

    # 方式2：return_exceptions=True → 异常作为结果对象返回
    print("\n[7.2] return_exceptions=True（异常作为结果）:")
    results = await asyncio.gather(
        success_task("X"),
        fail_task("Y"),
        success_task("Z"),
        return_exceptions=True,  # 关键参数！
    )
    for i, r in enumerate(results):
        if isinstance(r, Exception):
            print(f"  结果[{i}]: 异常 → {type(r).__name__}: {r}")
        else:
            print(f"  结果[{i}]: 成功 → {r}")

asyncio.run(exception_demo())


# ============================================================================
# 八、实战示例：模拟并发 API 请求
# ============================================================================
print("\n" + "=" * 60)
print("八、实战：模拟并发 API 请求")
print("=" * 60)

async def call_api(endpoint: str, delay: float = 0.5) -> dict:
    """模拟调用一个 API 端点"""
    print(f"  [请求] {endpoint} ...")
    await asyncio.sleep(delay)  # 模拟网络延迟
    return {
        "endpoint": endpoint,
        "status": 200,
        "data": f"来自 {endpoint} 的响应数据"
    }

async def api_demo():
    """模拟同时请求多个 API"""
    endpoints = [
        "/api/users",
        "/api/orders",
        "/api/products",
        "/api/stats",
        "/api/config",
    ]

    print(f"[8.1] 并发请求 {len(endpoints)} 个 API 端点:")
    start = time.time()

    # 并发请求所有端点
    results = await asyncio.gather(
        *[call_api(ep) for ep in endpoints]
    )

    elapsed = time.time() - start
    print(f"\n  请求结果:")
    for r in results:
        print(f"    {r['endpoint']}: {r['status']}")
    print(f"  总耗时: {elapsed:.2f}s ({len(endpoints)} 个请求并发)")

    # 对比：如果同步执行
    print(f"\n[对比] 同步请求需要 ≈ {len(endpoints) * 0.5:.1f}s")

asyncio.run(api_demo())


# ============================================================================
# 九、协程 vs 线程对比总结
# ============================================================================
print("\n" + "=" * 60)
print("九、协程 vs 线程 vs 进程对比")
print("=" * 60)

print("""
  ┌──────────┬──────────┬──────────┬──────────────┐
  │   维度   │  协程    │  线程     │   进程       │
  ├──────────┼──────────┼──────────┼──────────────┤
  │ 调度方式 │ 协作式   │ 抢占式   │ 操作系统调度 │
  │ 切换开销 │ 极小     │ 较大     │ 最大         │
  │ GIL 限制 │ 不受影响 │ 受影响   │ 不受影响     │
  │ 内存占用 │ KB 级    │ MB 级    │ 独立内存空间 │
  │ 并发数量 │ 万级     │ 百级     │ 十级         │
  │ 适用场景 │ I/O密集  │ I/O密集  │ CPU密集      │
  │ 数据共享 │ 无需锁   │ 需锁     │ Queue/Pipe   │
  └──────────┴──────────┴──────────┴──────────────┘
""")


# ============================================================================
# 十、常见踩坑提醒
# ============================================================================
print("=" * 60)
print("十、常见踩坑提醒")
print("=" * 60)

async def pitfall_demo():
    """演示常见错误"""

    # 坑1：忘记 await
    print("[坑1] 忘记 await:")
    async def get_data():
        await asyncio.sleep(0.1)
        return "重要数据"

    # 错误：get_data() 返回协程对象但没被执行
    result = get_data()  # 类型是 coroutine，没有实际执行
    print(f"  忘记 await: type={type(result)} (协程没被执行!)")
    # 正确：result = await get_data()

    # 坑2：在协程中使用 time.sleep
    print("\n[坑2] 协程中用 time.sleep 阻塞整个事件循环:")
    # 已在上面第六节演示

    # 坑3：asyncio.run() 不能嵌套
    print("\n[坑3] asyncio.run() 不能嵌套:")
    print("  (无法在此演示，会直接 RuntimeError)")

asyncio.run(pitfall_demo())


print("\n" + "=" * 60)
print("全部演示完成！")
print("=" * 60)
