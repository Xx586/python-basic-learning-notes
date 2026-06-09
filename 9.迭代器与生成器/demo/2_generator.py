"""
Demo 2: 生成器
演示：yield、生成器表达式、send/close、yield from、大文件读取、itertools

运行方式：python 2_generator.py
"""

import sys
import itertools
from tempfile import NamedTemporaryFile


# ========== 1. yield 基础：函数变生成器 ==========
print("=" * 50)
print("1. yield 基础：函数变生成器")
print("=" * 50)


def simple_generator():
    """一个最简单的生成器函数"""
    print("  >>> 生成器函数开始执行")
    yield 1
    print("  >>> 恢复执行")
    yield 2
    print("  >>> 再次恢复")
    yield 3
    print("  >>> 函数体结束")


g = simple_generator()
print(f"调用生成器函数返回：{type(g)} - {g}")  # <class 'generator'>

print("\n第一次 next()：")
print(f"  产出：{next(g)}")  # 执行到第一个 yield

print("\n第二次 next()：")
print(f"  产出：{next(g)}")  # 从上次暂停处恢复

print("\n第三次 next()：")
print(f"  产出：{next(g)}")  # 最后一个 yield

print("\n第四次 next()：")
try:
    next(g)  # 函数体结束，StopIteration
except StopIteration:
    print("  StopIteration —— 生成器已耗尽！")


# ========== 2. for 循环遍历生成器 ==========
print("\n" + "=" * 50)
print("2. for 循环自动处理 StopIteration")
print("=" * 50)


def countdown(n):
    """倒计时生成器"""
    while n > 0:
        yield n
        n -= 1


print("倒计时：", end=" ")
for num in countdown(5):
    print(num, end=" ")  # 5 4 3 2 1
print()


# ========== 3. 生成器表达式 vs 列表推导式 ==========
print("\n" + "=" * 50)
print("3. 生成器表达式 vs 列表推导式")
print("=" * 50)

# 列表推导式
list_comp = [x * 2 for x in range(10)]
print(f"列表推导式：{list_comp}")        # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
print(f"类型：{type(list_comp)}")          # <class 'list'>

# 生成器表达式（方括号变圆括号）
gen_expr = (x * 2 for x in range(10))
print(f"\n生成器表达式：{gen_expr}")       # <generator object ...>
print(f"类型：{type(gen_expr)}")           # <class 'generator'>

# 逐个取出
print(f"next() 第一次：{next(gen_expr)}")  # 0
print(f"next() 第二次：{next(gen_expr)}")  # 2
print(f"剩余元素：{list(gen_expr)}")       # [4, 6, 8, 10, 12, 14, 16, 18]


# ========== 4. 内存对比：列表 vs 生成器 ==========
print("\n" + "=" * 50)
print("4. 内存对比：100 万个元素")
print("=" * 50)

SIZE = 1_000_000

big_list = [x * 2 for x in range(SIZE)]
big_gen = (x * 2 for x in range(SIZE))

list_size = sys.getsizeof(big_list)
gen_size = sys.getsizeof(big_gen)

print(f"列表推导式内存：{list_size:,} 字节 (~{list_size / 1024 / 1024:.1f} MB)")
print(f"生成器表达式内存：{gen_size:,} 字节")
print(f"内存差距约：{list_size / max(gen_size, 1):.0f} 倍")
print(f"\n注：生成器表达式的内存大小是固定的，无论 range 多大！")

# 验证
big_gen_10m = (x * 2 for x in range(10_000_000))
print(f"1000 万元素生成器内存：{sys.getsizeof(big_gen_10m):,} 字节（和 100 万一样大）")


# ========== 5. 惰性求值演示 ==========
print("\n" + "=" * 50)
print("5. 惰性求值：用到才算")
print("=" * 50)


def heavy_computation(n):
    """模拟耗时操作"""
    result = n * n
    print(f"  计算函数被调用：{n}² = {result}")
    return result


# 列表推导式：立刻算完所有值
print("--- 列表推导式（急切求值）---")
squares_list = [heavy_computation(x) for x in range(1, 6)]
print(f"列表创建完毕：{squares_list}")
# 上面的输出中，"计算函数被调用" 在 "列表创建完毕" 之前

# 生成器表达式：不先算
print("\n--- 生成器表达式（惰性求值）---")
squares_gen = (heavy_computation(x) for x in range(1, 6))
print("生成器创建完毕（没有任何计算！）")
print(f"取第一个值：{next(squares_gen)}")  # 现在才计算 1
print(f"取第二个值：{next(squares_gen)}")  # 现在才计算 2
print("剩余的 3、4、5 根本没算！")


# ========== 6. send()：向生成器发送值 ==========
print("\n" + "=" * 50)
print("6. send() —— 双向通信")
print("=" * 50)


def running_average():
    """计算动态平均值：接收数值，返回当前平均值"""
    total = 0
    count = 0
    avg = None
    while True:
        value = yield avg  # yield 拿到 send() 进来的值
        count += 1
        total += value
        avg = total / count


avg = running_average()
print(f"初始化（必须 first next）：next() 返回 {next(avg)}")

# send() 传入数值，同时拿到当前平均值
print(f"send(10) 返回平均值：{avg.send(10):.1f}")  # 10.0
print(f"send(20) 返回平均值：{avg.send(20):.1f}")  # 15.0
print(f"send(30) 返回平均值：{avg.send(30):.1f}")  # 20.0
print(f"send(40) 返回平均值：{avg.send(40):.1f}")  # 25.0

# 关闭生成器
avg.close()
print("生成器已关闭")


# ========== 7. close() 和 throw() ==========
print("\n" + "=" * 50)
print("7. close() 和 throw()")
print("=" * 50)


def controlled_gen():
    """可以善后的生成器"""
    try:
        for i in range(1, 100):
            yield i
    except GeneratorExit:
        print("  生成器收到关闭信号，正在清理资源……")
        # 这里释放资源：关文件、断连接等
        raise  # 必须重新抛出（或不捕获）GeneratorExit


# close() 演示
print("--- close() ---")
cg = controlled_gen()
print(f"取第一个：{next(cg)}")  # 1
print(f"取第二个：{next(cg)}")  # 2
cg.close()  # 关闭生成器
print("已关闭，try: next(cg) 会抛出 StopIteration")

# throw() 演示
print("\n--- throw() ---")


def resilient_gen():
    """遇到 ValueError 能恢复的生成器"""
    for i in range(1, 6):
        try:
            yield i
        except ValueError as e:
            print(f"  内部捕获到 ValueError：{e}，跳过 {i} 继续执行")


rg = resilient_gen()
print(f"产出：{next(rg)}")  # 1
print(f"产出：{next(rg)}")  # 2
rg.throw(ValueError, "外部注入的异常")  # 生成器捕获异常，继续
print(f"产出：{next(rg)}")  # 3 —— 没有中断！


# ========== 8. yield from：委托子生成器 ==========
print("\n" + "=" * 50)
print("8. yield from —— 委托子生成器")
print("=" * 50)


def sub_gen():
    """子生成器"""
    yield "A"
    yield "B"
    return "子生成器完成！"  # return 值会被 yield from 捕获


def main_gen():
    """主生成器：委托给子生成器"""
    print("  主生成器启动")
    result = yield from sub_gen()  # 委托给子生成器
    print(f"  捕获子生成器 return 值：{result}")
    yield "C"
    yield "D"


print("依次产出：")
for item in main_gen():
    print(f"  {item}")


# ========== 9. yield from 扁平化嵌套列表 ==========
print("\n--- yield from 扁平化 ---")


def flatten(nested):
    """递归扁平化任意嵌套列表"""
    for item in nested:
        if isinstance(item, (list, tuple)):
            yield from flatten(item)  # 委托给递归调用
        else:
            yield item


data = [1, [2, 3], [4, [5, 6, [7, 8]]], 9]
print(f"原始：{data}")
print(f"扁平：{list(flatten(data))}")  # [1, 2, 3, 4, 5, 6, 7, 8, 9]


# ========== 10. 生成器应用：管道式数据处理 ==========
print("\n" + "=" * 50)
print("10. 应用：管道式数据处理")
print("=" * 50)


def read_data():
    """第 1 步：产生原始数据"""
    for x in range(1, 11):
        yield x


def filter_even(nums):
    """第 2 步：过滤出偶数"""
    for x in nums:
        if x % 2 == 0:
            yield x


def multiply_by_10(nums):
    """第 3 步：乘以 10"""
    for x in nums:
        yield x * 10


def format_output(nums):
    """第 4 步：格式化输出"""
    for x in nums:
        yield f"结果：{x}"


# 管道串联：数据 → 过滤 → 计算 → 格式化
pipeline = format_output(multiply_by_10(filter_even(read_data())))
print("管道处理结果：")
for result in pipeline:
    print(f"  {result}")


# ========== 11. 生成器应用：模拟大文件逐行读取 ==========
print("\n" + "=" * 50)
print("11. 应用：大文件逐行读取")
print("=" * 50)


# 先用临时文件模拟一个日志文件
temp = NamedTemporaryFile(mode="w", suffix=".log", delete=False)
temp.write("INFO: 系统启动\n")
temp.write("INFO: 加载配置\n")
temp.write("ERROR: 数据库连接失败\n")
temp.write("WARN: 内存使用率 85%\n")
temp.write("ERROR: 请求超时\n")
temp.write("INFO: 系统就绪\n")
temp.close()


def read_large_file(file_path):
    """逐行读取文件的生成器（永远只保留一行在内存中）"""
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            yield line.strip()


def filter_errors(lines):
    """过滤：只保留 ERROR 行"""
    for line in lines:
        if "ERROR" in line:
            yield line


print("日志中的错误行：")
log_lines = read_large_file(temp.name)
for err_line in filter_errors(log_lines):
    print(f"  {err_line}")

# 清理临时文件
import os
os.unlink(temp.name)


# ========== 12. itertools 工具箱 ==========
print("\n" + "=" * 50)
print("12. itertools 工具箱")
print("=" * 50)

# count：无限递增
print(f"--- count(start=5, step=3) ---")
for x in itertools.count(5, 3):
    if x > 15:
        break
    print(f"  {x}", end=" ")
print()

# cycle：无限循环
print(f"\n--- cycle('ABC') ---")
count = 0
for ch in itertools.cycle("ABC"):
    if count >= 6:
        break
    print(f"  {ch}", end=" ")
    count += 1
print()

# repeat：重复
print(f"\n--- repeat('Hi', 3) ---")
print(f"  {list(itertools.repeat('Hi', 3))}")

# chain：串联多个可迭代对象
print(f"\n--- chain([1,2], 'ab', [3,4]) ---")
print(f"  {list(itertools.chain([1, 2], 'ab', [3, 4]))}")

# islice：切片
print(f"\n--- islice(range(100), 5, 15, 2) ---")
print(f"  {list(itertools.islice(range(100), 5, 15, 2))}")

# takewhile：取到不满足条件
print(f"\n--- takewhile(x < 5, [1,2,3,4,5,0,1]) ---")
print(f"  {list(itertools.takewhile(lambda x: x < 5, [1, 2, 3, 4, 5, 0, 1]))}")

# dropwhile：跳过直到条件不满足
print(f"\n--- dropwhile(x < 5, [1,2,3,4,5,0,1]) ---")
print(f"  {list(itertools.dropwhile(lambda x: x < 5, [1, 2, 3, 4, 5, 0, 1]))}")

# 排列组合
print(f"\n--- product('AB', '12') 笛卡尔积 ---")
print(f"  {list(itertools.product('AB', '12'))}")

print(f"\n--- permutations('ABC', 2) 排列 ---")
print(f"  {list(itertools.permutations('ABC', 2))}")

print(f"\n--- combinations('ABC', 2) 组合 ---")
print(f"  {list(itertools.combinations('ABC', 2))}")

# groupby：分组（必须先排序！）
print(f"\n--- groupby 分组 ---")
data = [("语文", 90), ("数学", 85), ("语文", 78), ("数学", 92), ("英语", 88)]
data.sort(key=lambda x: x[0])  # 必须先排序！
print(f"  排序后数据：{data}")
for subject, items in itertools.groupby(data, key=lambda x: x[0]):
    scores = [score for _, score in items]
    print(f"  {subject}：分数{scores}，最高{max(scores)}分")


# ========== 13. 生成器应用：斐波那契数列 ==========
print("\n" + "=" * 50)
print("13. 应用：无限斐波那契数列")
print("=" * 50)


def fibonacci():
    """无限斐波那契数列生成器"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib = fibonacci()
first_15 = [next(fib) for _ in range(15)]
print(f"前 15 个斐波那契数：{first_15}")


# ========== 14. 踩坑演示 ==========
print("\n" + "=" * 50)
print("14. 常见踩坑")
print("=" * 50)

# 踩坑 1：生成器只能遍历一次
print("--- 踩坑 1：生成器只能遍历一次 ---")
gen = (x * 2 for x in range(5))
print(f"第一次遍历：{list(gen)}")  # [0, 2, 4, 6, 8]
print(f"第二次遍历：{list(gen)}")  # [] —— 已空！
print("  解决：需要再次遍历时，重新创建生成器")

# 踩坑 2：send() 前必须先 next()
print("\n--- 踩坑 2：send() 必须先 next() ---")


def echo():
    received = yield "ready"
    print(f"  收到：{received}")
    yield "done"


ec = echo()
print(f"  next() 初始化：{next(ec)}")  # ready
print(f"  send('hello') 结果：{ec.send('hello')}")  # done
print("  （如果直接 send('hello') 会导致 TypeError）")


print("\n" + "=" * 50)
print("所有演示完成！")
print("=" * 50)
