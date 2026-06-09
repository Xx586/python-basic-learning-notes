"""
Demo 4: 递归函数
演示：阶乘、斐波那契、汉诺塔、二分查找、递归深度限制、递归vs迭代

运行方式：python 4_recursion.py
"""

import sys
import time
from functools import lru_cache

# ========== 1. 阶乘：最简单的递归 ==========
print("=" * 40)
print("1. 阶乘递归")
print("=" * 40)

def factorial(n):
    """递归计算阶乘: n! = n * (n-1)!"""
    if n <= 1:            # 终止条件
        return 1
    return n * factorial(n - 1)  # 递推关系

for n in range(0, 8):
    print(f"  {n}! = {factorial(n)}")
print()

# ========== 2. 斐波那契数列 ==========
print("=" * 40)
print("2. 斐波那契数列")
print("=" * 40)

def fibonacci(n):
    """返回第 n 个斐波那契数（n 从 0 开始）"""
    if n <= 1:            # F(0)=0, F(1)=1
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("前10个斐波那契数:")
for i in range(10):
    print(f"  F({i}) = {fibonacci(i)}")
print()

# ========== 3. 汉诺塔 ==========
print("=" * 40)
print("3. 汉诺塔（3个盘子）")
print("=" * 40)

def hanoi(n, source, auxiliary, target):
    """将 n 个盘子从 source 移到 target，借助 auxiliary"""
    if n == 1:
        print(f"  盘子 1: {source} → {target}")
        return
    hanoi(n - 1, source, target, auxiliary)   # n-1 个从 A→B
    print(f"  盘子 {n}: {source} → {target}")   # 最大的从 A→C
    hanoi(n - 1, auxiliary, source, target)    # n-1 个从 B→C

hanoi(3, "A", "B", "C")
print(f"  (共 {2**3 - 1} 步)")
print()

# ========== 4. 二分查找（递归版） ==========
print("=" * 40)
print("4. 二分查找（递归版）")
print("=" * 40)

def binary_search(arr, target, left, right):
    """递归二分查找，返回索引，找不到返回 -1"""
    if left > right:                    # 终止条件：没找到
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:              # 找到了
        return mid
    elif arr[mid] > target:             # 目标在左半边
        return binary_search(arr, target, left, mid - 1)
    else:                               # 目标在右半边
        return binary_search(arr, target, mid + 1, right)

nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(f"  列表: {nums}")
print(f"  查找 7, 索引: {binary_search(nums, 7, 0, len(nums) - 1)}")
print(f"  查找 13, 索引: {binary_search(nums, 13, 0, len(nums) - 1)}")
print(f"  查找 8 (不存在), 索引: {binary_search(nums, 8, 0, len(nums) - 1)}")
print()

# ========== 5. 递归深度限制 ==========
print("=" * 40)
print("5. 递归深度限制")
print("=" * 40)

print(f"  默认递归深度限制: {sys.getrecursionlimit()}")

def countdown(n):
    if n == 0:
        return "Done"
    return countdown(n - 1)

# 安全调用（深度小于限制）
print(f"  countdown(5): {countdown(5)}")

# 超深递归会报错：
# countdown(1500)  # RecursionError: maximum recursion depth exceeded
print("  (1500层会触发 RecursionError)")
print()

# ========== 6. 缓存优化：@lru_cache ==========
print("=" * 40)
print("6. 缓存优化：@lru_cache 优化斐波那契")
print("=" * 40)

@lru_cache(maxsize=None)
def fib_memo(n):
    """带缓存的递归斐波那契"""
    if n <= 1:
        return n
    return fib_memo(n - 1) + fib_memo(n - 2)

# 不缓存版本在 n=35 时就非常慢了
# 带缓存的版本 n=100 也是瞬间
result = fib_memo(100)
print(f"  fib_memo(100) = {result}")
print(f"  (共 {len(str(result))} 位数)")
print()

# ========== 7. 递归 vs 迭代：斐波那契性能对比 ==========
print("=" * 40)
print("7. 递归 vs 迭代：斐波那契性能对比")
print("=" * 40)

def fib_iterative(n):
    """迭代版斐波那契，O(n)"""
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# 计算 fib(35)，对比性能
n_test = 35

start = time.perf_counter()
fib_iterative(n_test)
time_iter = time.perf_counter() - start
print(f"  迭代版 fib({n_test}): {time_iter:.6f} 秒")

# 递归版（不含缓存）会非常慢，仅演示小数值
# start = time.perf_counter()
# fibonacci(n_test)  # 大约几秒到十几秒，建议跳过
# 改用 fib_memo 演示
start = time.perf_counter()
fib_memo.cache_clear()  # 清除之前练习5的缓存
fib_memo(n_test)
time_memo = time.perf_counter() - start
print(f"  缓存递归 fib({n_test}): {time_memo:.6f} 秒")
print()

# ========== 8. 综合示例：目录树遍历 ==========
print("=" * 40)
print("8. 综合示例：递归遍历目录树")
print("=" * 40)

# 模拟一个目录树结构
file_system = [
    "README.md",
    ["src", ["main.py", "utils.py", ["tests", ["test_main.py"]]]],
    ["docs", ["index.html"]],
    "config.json",
]

def count_files(tree, indent=0):
    """递归统计文件数量并打印结构"""
    count = 0
    for item in tree:
        if isinstance(item, str):
            print("  " * indent + f"  📄 {item}")
            count += 1
        elif isinstance(item, list):
            folder_name = item[0]
            files = item[1:]
            print("  " * indent + f"  📁 {folder_name}/")
            count += count_files(files, indent + 1)
    return count

total = count_files(file_system)
print(f"\n  文件总数: {total}")
