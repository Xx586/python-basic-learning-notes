"""
Demo 3: lambda 匿名函数
演示：lambda语法、配合sorted/map/filter、vs def选择、延迟绑定陷阱

运行方式：python 3_lambda.py
"""

# ========== 1. lambda 基础语法 ==========
print("=" * 40)
print("1. lambda 基础语法")
print("=" * 40)

# def 写法
def add_def(x, y):
    return x + y

# lambda 写法
add_lambda = lambda x, y: x + y

print(f"def: add_def(3, 5) = {add_def(3, 5)}")
print(f"lambda: add_lambda(3, 5) = {add_lambda(3, 5)}")

# 多个参数
multiply = lambda a, b, c: a * b * c
print(f"multiply(2, 3, 4) = {multiply(2, 3, 4)}")

# 无参数
say_hi = lambda: "Hello, World!"
print(f"say_hi() = {say_hi()}")
print()

# ========== 2. lambda + sorted() —— 自定义排序 ==========
print("=" * 40)
print("2. lambda + sorted()")
print("=" * 40)

students = [
    {"name": "张三", "score": 85},
    {"name": "李四", "score": 92},
    {"name": "王五", "score": 78},
]

# 按分数升序
sorted_by_score = sorted(students, key=lambda s: s["score"])
print(f"按分数升序: {sorted_by_score}")

# 按分数降序
sorted_desc = sorted(students, key=lambda s: s["score"], reverse=True)
print(f"按分数降序: {sorted_desc}")

# 多级排序：先按年级，再按分数降序
students2 = [
    {"name": "A", "grade": 1, "score": 85},
    {"name": "B", "grade": 2, "score": 90},
    {"name": "C", "grade": 1, "score": 90},
]
sorted_multi = sorted(students2, key=lambda s: (s["grade"], -s["score"]))
print(f"多级排序: {sorted_multi}")
print()

# ========== 3. lambda + map() —— 批量映射 ==========
print("=" * 40)
print("3. lambda + map()")
print("=" * 40)

nums = [1, 2, 3, 4, 5]

# 平方
squares = list(map(lambda x: x ** 2, nums))
print(f"平方: {squares}")

# 摄氏度 → 华氏度
celsius = [0, 10, 20, 30, 40]
fahrenheit = list(map(lambda c: c * 9 / 5 + 32, celsius))
print(f"华氏度: {fahrenheit}")

# 对比：list comprehension 也是好选择
squares_lc = [x ** 2 for x in nums]
print(f"列表推导式平方: {squares_lc}")
print()

# ========== 4. lambda + filter() —— 条件筛选 ==========
print("=" * 40)
print("4. lambda + filter()")
print("=" * 40)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 筛选偶数
evens = list(filter(lambda x: x % 2 == 0, nums))
print(f"偶数: {evens}")

# 筛选大于 5 的数
big_nums = list(filter(lambda x: x > 5, nums))
print(f">5: {big_nums}")

# 筛选长度 >= 5 的单词
words = ["a", "ab", "abc", "abcd", "abcde", "abcdef"]
long_words = list(filter(lambda w: len(w) >= 5, words))
print(f"长度>=5: {long_words}")
print()

# ========== 5. lambda + max()/min() ==========
print("=" * 40)
print("5. lambda + max()/min()")
print("=" * 40)

# 找分数最高的学生
best_student = max(students, key=lambda s: s["score"])
print(f"最高分学生: {best_student}")

# 找最长的单词
longest_word = max(words, key=lambda w: len(w))
print(f"最长单词: {longest_word}")
print()

# ========== 6. lambda 中的条件表达式 ==========
print("=" * 40)
print("6. lambda 中的条件表达式（三元运算符）")
print("=" * 40)

# 取绝对值
my_abs = lambda x: x if x >= 0 else -x
print(f"my_abs(-5) = {my_abs(-5)}")
print(f"my_abs(3) = {my_abs(3)}")

# 判断奇偶
check = lambda x: "偶数" if x % 2 == 0 else "奇数"
print(f"5 是 {check(5)}, 8 是 {check(8)}")
print()

# ========== 7. 踩坑：循环中 lambda 延迟绑定 ==========
print("=" * 40)
print("7. 踩坑：循环中 lambda 延迟绑定")
print("=" * 40)

# ❌ 错误写法
funcs_wrong = []
for i in range(5):
    funcs_wrong.append(lambda: i)

print(f"错误结果: {[f() for f in funcs_wrong]}")  # [4, 4, 4, 4, 4]

# ✅ 修复方法1：默认参数冻结值
funcs_fix1 = []
for i in range(5):
    funcs_fix1.append(lambda x=i: x)

print(f"修复1(默认参数): {[f() for f in funcs_fix1]}")

# ✅ 修复方法2：工厂函数
def make_func(n):
    return lambda: n

funcs_fix2 = [make_func(i) for i in range(5)]
print(f"修复2(工厂函数): {[f() for f in funcs_fix2]}")
print()

# ========== 8. lambda vs def 选择 ==========
print("=" * 40)
print("8. lambda vs def —— 什么时候用哪个？")
print("=" * 40)

# 适合 lambda 的场景：一行表达式、一次性使用
data = [("张三", 85), ("李四", 92), ("王五", 78)]
# 按分数排序，lambda 清晰简洁
data_sorted = sorted(data, key=lambda x: x[1])
print(f"lambda 排序: {data_sorted}")

# 不适合 lambda 的场景：多行逻辑
def calculate_grade(score):
    """计算等级 —— 多行逻辑必须用 def"""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

grades = list(map(calculate_grade, [95, 82, 73, 55]))
print(f"def 计算等级: {grades}")
