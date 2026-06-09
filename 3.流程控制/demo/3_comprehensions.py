"""
Demo 3: 推导式与生成器表达式
演示：列表推导式、字典推导式、集合推导式、生成器表达式、嵌套推导式

运行方式：python 3_comprehensions.py
"""

import sys

# ========== 1. 列表推导式 ==========
print("=" * 50)
print("1. 列表推导式（List Comprehension）")
print("=" * 50)

# 1.1 基本用法
print("--- 基本变换 ---")
squares = [x ** 2 for x in range(1, 11)]
print(f"1-10 的平方：{squares}")

# 1.2 带过滤条件
print("\n--- 带过滤条件 ---")
evens = [x for x in range(1, 21) if x % 2 == 0]
print(f"1-20 的偶数：{evens}")

# 1.3 带 if-else 的变换
print("\n--- 带 if-else 变换 ---")
nums = [1, 2, 3, 4, 5, 6]
transformed = [x * 10 if x % 2 == 0 else x for x in nums]
print(f"偶数×10，奇数不变：{transformed}")  # [1, 20, 3, 40, 5, 60]

# 1.4 与传统 for 循环对比
print("\n--- 推导式 vs 传统 for ---")
# 传统方式
traditional = []
for x in range(10):
    if x > 3:
        traditional.append(x * 2)
print(f"传统方式：{traditional}")

# 推导式
comprehension = [x * 2 for x in range(10) if x > 3]
print(f"推导式：  {comprehension}")
print(f"结果一致：{traditional == comprehension}")


# ========== 2. 字典推导式 ==========
print("\n" + "=" * 50)
print("2. 字典推导式（Dict Comprehension）")
print("=" * 50)

# 2.1 从列表构建
print("--- 从列表构建字典 ---")
words = ["apple", "banana", "cherry"]
word_len = {w: len(w) for w in words}
print(f"单词长度：{word_len}")

# 2.2 从已有字典筛选/变换
print("\n--- 从已有字典筛选 ---")
scores = {"张三": 85, "李四": 55, "王五": 92, "赵六": 48}
passed = {name: score for name, score in scores.items() if score >= 60}
print(f"及格学生：{passed}")

# 键值对调
print("\n--- 键值对调 ---")
inverted = {v: k for k, v in scores.items()}
print(f"对调后：{inverted}")

# 2.3 条件变换
print("\n--- 分数等级映射 ---")
grades = {
    name: "及格" if score >= 60 else "不及格"
    for name, score in scores.items()
}
print(f"等级：{grades}")


# ========== 3. 集合推导式 ==========
print("\n" + "=" * 50)
print("3. 集合推导式（Set Comprehension）")
print("=" * 50)

# 去重
nums = [1, -1, 2, -2, 3, -3, 2, 1]
abs_set = {abs(x) for x in nums}
print(f"绝对值去重：{abs_set}")  # {1, 2, 3}

# 提取不重复字母
text = "hello world"
unique_chars = {c for c in text if c != " "}
print(f"不同字母：{sorted(unique_chars)}")

# 对比列表推导式（不去重）
unique_list = [c for c in text if c != " "]
print(f"列表推导（保留重复）：{unique_list}")


# ========== 4. 生成器表达式 ==========
print("\n" + "=" * 50)
print("4. 生成器表达式（Generator Expression）")
print("=" * 50)

# 4.1 基本用法
print("--- 创建生成器 ---")
gen = (x ** 2 for x in range(10))
print(f"类型：{type(gen)}")
print(f"对象：{gen}")

# 逐个取值
print("逐个取值：", end=" ")
print(next(gen), end=" ")
print(next(gen), end=" ")
print(next(gen), end=" ")
print()

# 4.2 遍历生成器
print("\n--- for 循环遍历 ---")
gen2 = (x ** 2 for x in range(5))
for val in gen2:
    print(val, end=" ")
print()

# 4.3 生成器只能遍历一次！
print("\n--- 重要：生成器只能遍历一次！---")
gen3 = (x ** 2 for x in range(5))
print(f"第一次 list()：{list(gen3)}")
print(f"第二次 list()：{list(gen3)}  ← 空的！已耗尽")

# 4.4 作为函数参数（省略外层括号）
print("\n--- 作为函数参数使用 ---")
# 生成器表达式是函数唯一参数时，可以省略外层括号
total = sum(x ** 2 for x in range(1, 6))
print(f"sum(x**2 for x in range(1,6)) = {total}")

max_val = max(len(w) for w in ["a", "bc", "def", "python"])
print(f"最长单词长度：{max_val}")

# 4.5 内存对比
print("\n--- 内存对比：列表 vs 生成器 ---")
n = 1000000
list_comp = [x * 2 for x in range(n)]
gen_expr = (x * 2 for x in range(n))
list_n = 1000
small_list = [x * 2 for x in range(list_n)]
small_gen = (x * 2 for x in range(list_n))

print(f"列表推导（{n} 个元素）内存：{sys.getsizeof(list_comp):,} bytes")
print(f"列表推导（{list_n} 个元素）内存：{sys.getsizeof(small_list):,} bytes")
print(f"生成器表达式内存：       {sys.getsizeof(gen_expr):,} bytes")
print(f"生成器表达式内存：       {sys.getsizeof(small_gen):,} bytes")
print("→ 生成器表达式无论数据量多大，内存占用都极小")


# ========== 5. 嵌套推导式 ==========
print("\n" + "=" * 50)
print("5. 嵌套推导式")
print("=" * 50)

# 5.1 展平二维列表
print("--- 展平二维列表 ---")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(f"展平结果：{flattened}")

# 5.2 生成二维列表
print("\n--- 生成乘法表矩阵 ---")
table = [[i * j for j in range(1, 5)] for i in range(1, 4)]
print("3×4 乘法表：")
for row in table:
    print(f"  {row}")

# 5.3 笛卡尔积
print("\n--- 生成坐标对 ---")
xs = [1, 2, 3]
ys = [10, 20]
points = [(x, y) for x in xs for y in ys]
print(f"坐标对：{points}")

# 5.4 嵌套字典推导式
print("\n--- 嵌套字典推导 ---")
students = {
    "张三": {"语文": 85, "数学": 92, "英语": 78},
    "李四": {"语文": 65, "数学": 70, "英语": 80},
    "王五": {"语文": 90, "数学": 88, "英语": 95},
}
totals = {name: sum(scores.values()) for name, scores in students.items()}
print(f"每人总分：{totals}")

# 统计全班各科平均分
subjects = ["语文", "数学", "英语"]
avgs = {
    sub: sum(students[name][sub] for name in students) / len(students)
    for sub in subjects
}
print(f"各科平均分：{avgs}")


# ========== 6. 可读性 vs 简洁 ==========
print("\n" + "=" * 50)
print("6. 可读性优先——什么时候不该用推导式")
print("=" * 50)

print("反例：逻辑过于复杂，不适合写推导式")
# 假设有这样一段逻辑（虽然没有实际运行）
print("""
# 不推荐（难以阅读）：
# result = [process(x) if validate(x) else fallback(x)
#           for x in data if check(x) and not skip(x)]

# 推荐（拆成 for 循环）：
# result = []
# for x in data:
#     if check(x) and not skip(x):
#         if validate(x):
#             result.append(process(x))
#         else:
#             result.append(fallback(x))
""")

print("规则：超过 2 层嵌套或包含复杂逻辑 → 用传统 for 循环")


print("\n" + "=" * 50)
print("Demo 3 运行完毕")
print("=" * 50)
