"""
Demo 1: 可迭代对象和迭代器
演示：自定义迭代器、for循环原理、iter/next/StopIteration

运行方式：python 1_iterator.py
"""


# ========== 1. 可迭代对象 vs 迭代器 ==========
print("=" * 50)
print("1. 判断可迭代对象和迭代器")
print("=" * 50)

from collections.abc import Iterable, Iterator

# 列表是可迭代对象，但不是迭代器
nums = [1, 2, 3]
print(f"列表是可迭代对象？{isinstance(nums, Iterable)}")  # True
print(f"列表是迭代器？{isinstance(nums, Iterator)}")        # False

# iter() 返回的对象才是迭代器
it = iter(nums)
print(f"iter(列表)是可迭代对象？{isinstance(it, Iterable)}")  # True
print(f"iter(列表)是迭代器？{isinstance(it, Iterator)}")      # True


# ========== 2. 手动使用 iter() 和 next() ==========
print("\n" + "=" * 50)
print("2. iter() 和 next() 基础用法")
print("=" * 50)

it = iter([10, 20, 30])
print(f"第一个元素：{next(it)}")  # 10
print(f"第二个元素：{next(it)}")  # 20
print(f"第三个元素：{next(it)}")  # 30

# 取完后再调用 next() 会抛出 StopIteration
try:
    print(next(it))
except StopIteration:
    print("StopIteration —— 迭代器已耗尽！")


# ========== 3. for 循环的本质（手动模拟） ==========
print("\n" + "=" * 50)
print("3. 手动模拟 for 循环")
print("=" * 50)

data = ["苹果", "香蕉", "橘子"]
print("=== 原生 for 循环 ===")
for fruit in data:
    print(f"  {fruit}")

print("\n=== 手动模拟（while + iter + next）===")
iterator = iter(data)
while True:
    try:
        fruit = next(iterator)
        print(f"  {fruit}")
    except StopIteration:
        print("  遍历结束！")
        break


# ========== 4. 自定义迭代器：倒计时 ==========
print("\n" + "=" * 50)
print("4. 自定义迭代器：倒计时")
print("=" * 50)


class Countdown:
    """倒计时迭代器：从 start 倒数到 1"""

    def __init__(self, start):
        self.current = start

    def __iter__(self):
        # 迭代器的 __iter__ 返回自身
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration  # 到头了，发出"取完了"的信号
        value = self.current
        self.current -= 1
        return value


print("倒计时：", end=" ")
for num in Countdown(5):
    print(num, end=" ")  # 5 4 3 2 1
print()


# ========== 5. 自定义迭代器：斐波那契数列 ==========
print("\n" + "=" * 50)
print("5. 自定义迭代器：前 N 个斐波那契数")
print("=" * 50)


class Fibonacci:
    """生成前 n 个斐波那契数的迭代器"""

    def __init__(self, n):
        self.n = n           # 要生成多少个数
        self.a, self.b = 0, 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        if self.count == 0:
            self.count += 1
            return 0
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return self.a


print("前 10 个斐波那契数：", end=" ")
for num in Fibonacci(10):
    print(num, end=" ")
print()


# ========== 6. 自定义迭代器：偶数生成器 ==========
print("\n" + "=" * 50)
print("6. 自定义迭代器：生成 0 到 limit 之间的偶数")
print("=" * 50)


class EvenNumber:
    """生成 0 到 limit 之间所有偶数的迭代器"""

    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.limit:
            raise StopIteration
        value = self.current
        self.current += 2
        return value


print("0~20 的偶数：", end=" ")
for num in EvenNumber(20):
    print(num, end=" ")  # 0 2 4 6 8 10 12 14 16 18 20
print()


# ========== 7. 迭代器的三大特性 ==========
print("\n" + "=" * 50)
print("7. 迭代器特性演示")
print("=" * 50)

# 特性 1：一次性消费
print("--- 一次性消费 ---")
it = iter([1, 2, 3])
print(f"第一次转列表：{list(it)}")  # [1, 2, 3]
print(f"第二次转列表：{list(it)}")  # [] —— 已空！

# 特性 2：惰性求值
print("\n--- 惰性求值 ---")
big_range = range(10_000_000)  # 不会在内存中创建 1000 万个整数
print(f"range(10_000_000) 取第 5000 个值：{big_range[5000]}")  # 立刻算出来
print(f"range(10_000_000) 占用内存：{big_range.__sizeof__()} 字节")

# 特性 3：节省内存
print("\n--- 节省内存 ---")
import sys

list_1m = [x for x in range(1_000_000)]
iter_1m = iter(range(1_000_000))
print(f"列表 100 万元素占用：{sys.getsizeof(list_1m):,} 字节")
print(f"迭代器 100 万元素占用：{sys.getsizeof(iter_1m):,} 字节")
print(f"内存差距约：{sys.getsizeof(list_1m) / sys.getsizeof(iter_1m):.0f} 倍")


# ========== 8. 可迭代对象 vs 迭代器：多次遍历对比 ==========
print("\n" + "=" * 50)
print("8. 可迭代对象 vs 迭代器：多次遍历")
print("=" * 50)

# 可迭代对象（列表）—— 可以多次遍历
print("--- 可迭代对象（列表）---")
book = [1, 2, 3]
print("第一次遍历：", end=" ")
for x in book:
    print(x, end=" ")
print()
print("第二次遍历：", end=" ")
for x in book:
    print(x, end=" ")
print("\n（两次都有输出，列表可以重复遍历）")

# 迭代器 —— 只能遍历一次
print("\n--- 迭代器 ---")
bookmark = iter(book)
print("第一次遍历：", end=" ")
for x in bookmark:
    print(x, end=" ")
print()
print("第二次遍历：", end=" ")
for x in bookmark:
    print(x, end=" ")
print("\n（第二次是空的，迭代器已消耗完毕）")


# ========== 9. 常见踩坑：in 检查消耗迭代器 ==========
print("\n" + "=" * 50)
print("9. 踩坑演示：in 会消耗迭代器元素")
print("=" * 50)

it = iter([1, 2, 3, 4, 5])
print(f"检查 3 是否在迭代器中：{3 in it}")  # True —— 但内部调用了 next() 直到找到 3
print(f"剩余元素：{list(it)}")                # [4, 5] —— 1, 2, 3 已经被消耗了！
print("注意：第一次遍历时 1 和 2 已经被跳过，3 被找到但也消耗了")


print("\n" + "=" * 50)
print("所有演示完成！")
print("=" * 50)
