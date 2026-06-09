"""
Demo 3: 演示常用标准库

演示：
  1. os — 路径操作、目录操作、环境变量
  2. sys — 命令行参数、解释器信息
  3. datetime / time — 日期时间处理、格式化、时间戳
  4. math — 数学运算、取整、三角函数
  5. random — 随机数、随机选择、洗牌、种子
  6. collections — Counter、defaultdict、OrderedDict、namedtuple、deque
  7. itertools — 无限迭代器、排列组合、chain、accumulate
  8. functools — partial、lru_cache、wraps、reduce

运行方式：python 3_stdlib_demo.py
"""

import os
import sys
import time
from datetime import datetime, timedelta
import math
import random
from collections import Counter, defaultdict, OrderedDict, namedtuple, deque
import itertools
from functools import partial, lru_cache, wraps, reduce

print("=" * 60)
print("Demo 3: 常用标准库演示")
print("=" * 60)

# =====================================================================
# 1. os 模块 — 操作系统接口
# =====================================================================
print("\n" + "=" * 60)
print("1. os — 操作系统接口")
print("=" * 60)

print(f"当前工作目录: {os.getcwd()}")
print(f"目录文件列表(前5): {os.listdir('.')[:5]}")
print(f"操作系统类型: {os.name}")
print(f"路径分隔符: {os.sep!r}")

# 路径操作
current_file = os.path.abspath(__file__)
print(f"\n当前文件的绝对路径: {current_file}")
print(f"  目录部分(dirname): {os.path.dirname(current_file)}")
print(f"  文件名(basename): {os.path.basename(current_file)}")

# 路径拼接
demo_path = os.path.join(os.getcwd(), "my_module.py")
print(f"\n路径拼接: {demo_path}")
print(f"路径是否存在: {os.path.exists(demo_path)}")

# 环境变量
print(f"\nHOME 目录: {os.environ.get('HOME', '未设置')}")
print(f"PATH(前80字符): {os.environ.get('PATH', '')[:80]}...")


# =====================================================================
# 2. sys 模块 — 解释器交互
# =====================================================================
print("\n" + "=" * 60)
print("2. sys — 解释器交互")
print("=" * 60)

print(f"Python 版本: {sys.version.split()[0]}")
print(f"平台: {sys.platform}")
print(f"解释器路径: {sys.executable}")

# sys.argv 演示
print(f"\nsys.argv 内容: {sys.argv}")
print("提示: 可以用命令行参数运行本脚本:")
print("  python 3_stdlib_demo.py hello world")

if len(sys.argv) > 1:
    print(f"\n收到的命令行参数: {sys.argv[1:]}")
else:
    print("\n(未传递额外命令行参数)")

# sys.path 前几条
print(f"\n模块搜索路径(前3条):")
for i, p in enumerate(sys.path[:3]):
    print(f"  [{i}] {p}")


# =====================================================================
# 3. datetime / time — 日期时间
# =====================================================================
print("\n" + "=" * 60)
print("3. datetime / time — 日期时间")
print("=" * 60)

# 当前时间
now = datetime.now()
print(f"当前日期时间: {now}")
print(f"  年: {now.year}, 月: {now.month}, 日: {now.day}")
print(f"  时: {now.hour}, 分: {now.minute}, 秒: {now.second}")
print(f"  周几(0=周一): {now.weekday()}")

# strftime 格式化
print(f"\n格式化示例:")
print(f"  YYYY-MM-DD: {now.strftime('%Y-%m-%d')}")
print(f"  HH:MM:SS:   {now.strftime('%H:%M:%S')}")
print(f"  中文格式:    {now.strftime('%Y年%m月%d日 %H:%M:%S')}")

# strptime 解析
date_str = "2026-10-01 08:00:00"
parsed = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print(f"\n解析 '{date_str}': {parsed}")

# timedelta 时间计算
tomorrow = now + timedelta(days=1)
three_days_ago = now - timedelta(days=3)
two_hours_later = now + timedelta(hours=2)

print(f"\n时间计算:")
print(f"  明天: {tomorrow.strftime('%Y-%m-%d')}")
print(f"  三天前: {three_days_ago.strftime('%Y-%m-%d')}")
print(f"  两小时后: {two_hours_later.strftime('%H:%M:%S')}")

# 计算日期差
national_day = datetime(2026, 10, 1)
days_left = (national_day - now).days
print(f"  距离国庆节(2026-10-01)还有 {days_left} 天")

# 时间戳
timestamp = time.time()
print(f"\n当前时间戳: {timestamp}")
print(f"从时间戳恢复: {datetime.fromtimestamp(timestamp)}")

# 性能计时演示
start = time.perf_counter()
# 模拟一段计算
sum(range(1000000))
end = time.perf_counter()
print(f"\n计算 sum(range(1000000)) 耗时: {(end - start) * 1000:.2f} 毫秒")


# =====================================================================
# 4. math — 数学运算
# =====================================================================
print("\n" + "=" * 60)
print("4. math — 数学运算")
print("=" * 60)

print(f"pi = {math.pi}")
print(f"e  = {math.e}")

print(f"\n取整:")
print(f"  ceil(4.3)  = {math.ceil(4.3)}     (向上取整)")
print(f"  ceil(-4.3) = {math.ceil(-4.3)}")
print(f"  floor(4.7) = {math.floor(4.7)}    (向下取整)")
print(f"  floor(-4.7)= {math.floor(-4.7)}")
print(f"  trunc(4.7) = {math.trunc(4.7)}    (截断)")
print(f"  trunc(-4.7)= {math.trunc(-4.7)}")

print(f"\n幂和根:")
print(f"  sqrt(144)   = {math.sqrt(144)}")
print(f"  pow(2, 10)  = {math.pow(2, 10)}")
print(f"  log2(1024)  = {math.log2(1024)}")

print(f"\n组合和阶乘:")
print(f"  factorial(6) = {math.factorial(6)}")
print(f"  comb(5, 2)   = {math.comb(5, 2)}   (C(5,2)组合)")
print(f"  gcd(48, 18)  = {math.gcd(48, 18)}   (最大公约数)")

print(f"\n浮点比较:")
print(f"  0.1 + 0.2 == 0.3? {0.1 + 0.2 == 0.3}         (直接比较不可靠)")
print(f"  isclose(0.1+0.2, 0.3)? {math.isclose(0.1 + 0.2, 0.3)}  (推荐方法)")


# =====================================================================
# 5. random — 随机数
# =====================================================================
print("\n" + "=" * 60)
print("5. random — 随机数")
print("=" * 60)

# 基本随机
print(f"random()          = {random.random():.4f}    (0~1 浮点数)")
print(f"uniform(1, 10)    = {random.uniform(1, 10):.2f}")
print(f"randint(1, 100)   = {random.randint(1, 100)}  (整数)")
print(f"randrange(0, 100, 5) = {random.randrange(0, 100, 5)}  (步长5)")

# 序列操作
colors = ['红', '橙', '黄', '绿', '蓝', '靛', '紫']
print(f"\n随机选择 1 个: {random.choice(colors)}")
print(f"随机选 3 个(可重复): {random.choices(colors, k=3)}")
print(f"随机选 3 个(不重复): {random.sample(colors, k=3)}")

# shuffle 洗牌
cards = list(range(1, 11))
random.shuffle(cards)
print(f"\n洗牌后的牌: {cards}")

# seed 种子：让随机可复现
random.seed(42)
val1 = random.randint(1, 100)
random.seed(42)
val2 = random.randint(1, 100)
print(f"\nrandom.seed(42) 后 randint(1,100): {val1} 和 {val2}")
print(f"相同种子 → 相同序列: {val1 == val2}")

# 实用示例：生成随机密码
import string
def generate_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choices(chars, k=length))

print(f"\n随机密码: {generate_password()}")


# =====================================================================
# 6. collections — 增强容器
# =====================================================================
print("\n" + "=" * 60)
print("6. collections — 增强容器")
print("=" * 60)

# ---- Counter ----
print("--- Counter 计数器 ---")
text = "abracadabra"
cnt = Counter(text)
print(f"  Counter('{text}') = {cnt}")
print(f"  最常见的3个: {cnt.most_common(3)}")
print(f"  'a' 的次数: {cnt['a']}")
print(f"  'z' 的次数(不存在): {cnt['z']}  (不报错，返回0)")

# ---- defaultdict ----
print("\n--- defaultdict 带默认值 ---")
# 按首字母分组
fruits = ['apple', 'banana', 'apricot', 'blueberry', 'cherry', 'coconut']
groups = defaultdict(list)
for fruit in fruits:
    groups[fruit[0]].append(fruit)
print("  按首字母分组:")
for letter, items in sorted(groups.items()):
    print(f"    {letter}: {items}")

# 计数器模式
dd_int = defaultdict(int)
for ch in "hello world":
    if ch != ' ':
        dd_int[ch] += 1  # 不用先判断 key 是否存在！
print(f"  字符计数: {dict(dd_int)}")

# ---- OrderedDict ----
print("\n--- OrderedDict 有序字典 ---")
od = OrderedDict()
od['c'] = 3
od['a'] = 1
od['b'] = 2
print(f"  插入顺序: {list(od.keys())}")  # ['c', 'a', 'b']
od.move_to_end('c')
print(f"  c移到最后: {list(od.keys())}")  # ['a', 'b', 'c']

# ---- namedtuple ----
print("\n--- namedtuple 具名元组 ---")
Point = namedtuple('Point', ['x', 'y'])
p1 = Point(10, 20)
p2 = Point(30, 40)
print(f"  p1 = {p1}")
print(f"  p1.x={p1.x}, p1.y={p1.y}")
print(f"  p1._asdict(): {p1._asdict()}")
print(f"  p2._replace(y=99): {p2._replace(y=99)}")

# ---- deque ----
print("\n--- deque 双端队列 ---")
dq = deque([1, 2, 3])
dq.appendleft(0)
dq.append(4)
print(f"  初始: deque([1,2,3])")
print(f"  左加0, 右加4: {dq}")

# maxlen 自动丢弃
dq2 = deque(maxlen=3)
dq2.extend([1, 2, 3, 4, 5])
print(f"  maxlen=3, extend 1~5: {dq2}  (自动丢弃1和2)")

dq3 = deque([1, 2, 3, 4, 5])
dq3.rotate(2)
print(f"  rotate(2): {dq3}")


# =====================================================================
# 7. itertools — 高效迭代器
# =====================================================================
print("\n" + "=" * 60)
print("7. itertools — 高效迭代器")
print("=" * 60)

# ---- 排列组合 ----
items = ['A', 'B', 'C']
print(f"--- 排列组合 (items={items}) ---")
print(f"  排列(2): {list(itertools.permutations(items, 2))}")
print(f"  组合(2): {list(itertools.combinations(items, 2))}")

# ---- product 笛卡尔积 ----
print(f"\n--- 笛卡尔积 ---")
ranks = ['A', 'K', 'Q']
suits = ['♠', '♥']
deck = list(itertools.product(ranks, suits))
print(f"  product({ranks}, {suits}) = {deck}")

# ---- chain 串联 ----
print(f"\n--- chain 串联 ---")
chained = list(itertools.chain([1, 2], (3, 4), {5, 6}))
print(f"  chain([1,2], (3,4), {{5,6}}) = {chained}")

# ---- accumulate 累积 ----
print(f"\n--- accumulate 累积 ---")
data = [1, 2, 3, 4, 5]
print(f"  数据: {data}")
print(f"  累加: {list(itertools.accumulate(data))}")
import operator
print(f"  累乘: {list(itertools.accumulate(data, operator.mul))}")

# ---- zip_longest ----
print(f"\n--- zip_longest 不等长配对 ---")
a = [1, 2, 3]
b = ['x', 'y']
print(f"  a={a}, b={b}")
print(f"  zip_longest(a, b): {list(itertools.zip_longest(a, b, fillvalue='-'))}")


# =====================================================================
# 8. functools — 高阶函数工具
# =====================================================================
print("\n" + "=" * 60)
print("8. functools — 高阶函数工具")
print("=" * 60)

# ---- partial 偏函数 ----
print("--- partial 偏函数 ---")
def power(base, exp):
    return base ** exp

square = partial(power, exp=2)
cube = partial(power, exp=3)
print(f"  square(5) = {square(5)}  (power(5, 2))")
print(f"  cube(3)   = {cube(3)}    (power(3, 3))")

# 实用：简化日志函数
def log(level, message):
    return f"[{level}] {message}"

info = partial(log, "INFO")
error = partial(log, "ERROR")
print(f"  {info('服务已启动')}")
print(f"  {error('磁盘空间不足')}")

# ---- lru_cache 缓存 ----
print("\n--- lru_cache 缓存 ---")
call_count = 0  # 用来追踪实际计算次数

@lru_cache(maxsize=128)
def expensive_computation(n):
    global call_count
    call_count += 1
    # 模拟耗时计算
    result = sum(i * i for i in range(n * 1000))
    return result

print(f"  第一次调用 expensive_computation(50): {expensive_computation(50)}")
print(f"  第二次调用 expensive_computation(50): {expensive_computation(50)}  (命中缓存)")
print(f"  实际计算次数: {call_count}  (只有1次!)")
print(f"  缓存信息: {expensive_computation.cache_info()}")

# ---- wraps 保持元信息 ----
print("\n--- wraps 保持函数元信息 ---")
def timing_decorator(func):
    @wraps(func)  # 保持 func 的名称和文档
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"  [{func.__name__}] 耗时: {elapsed * 1000:.2f}ms")
        return result
    return wrapper

@timing_decorator
def slow_add(a, b):
    """慢速加法函数"""
    time.sleep(0.01)
    return a + b

result = slow_add(3, 5)
print(f"  函数名(__name__): {slow_add.__name__!r}  (不用wraps会变成'wrapper')")
print(f"  文档(__doc__): {slow_add.__doc__!r}")

# ---- reduce 归约 ----
print("\n--- reduce 归约 ---")
numbers = [1, 2, 3, 4, 5]
sum_result = reduce(lambda x, y: x + y, numbers)
prod_result = reduce(lambda x, y: x * y, numbers)
print(f"  reduce(sum, [1,2,3,4,5])   = {sum_result}")
print(f"  reduce(mul, [1,2,3,4,5])   = {prod_result} (阶乘5!)")

# reduce 过程可视化
print(f"\n  reduce 执行过程:")
def show(acc, val):
    new_acc = acc + val
    print(f"    累积值 {acc} + {val} = {new_acc}")
    return new_acc
final = reduce(show, [10, 20, 30])
print(f"  最终结果: {final}")


# =====================================================================
print("\n" + "=" * 60)
print("Demo 3: 常用标准库演示完毕！")
print("=" * 60)
print(f"\n{'-' * 40}")
print("提示：以上演示了8个常用标准库的全部核心功能。")
print("每个模块都可以独立运行并查看输出。")
