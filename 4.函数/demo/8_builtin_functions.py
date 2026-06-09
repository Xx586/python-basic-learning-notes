"""
Demo 8: 常用内置函数
演示：len/max/min/sum/abs/round/pow、zip/map/filter/enumerate、sorted、reversed、
      any/all、isinstance/type、chr/ord

运行方式：python 8_builtin_functions.py
"""

# ========== 1. 数学相关 ==========
print("=" * 40)
print("1. 数学相关: len/max/min/sum/abs/round/pow")
print("=" * 40)

nums = [3, 1, 4, 1, 5, 9, 2, 6]

print(f"  len(nums) = {len(nums)}")
print(f"  max(nums) = {max(nums)}")
print(f"  min(nums) = {min(nums)}")
print(f"  sum(nums) = {sum(nums)}")
print(f"  abs(-5) = {abs(-5)}")

# round() 注意银行家舍入
print(f"  round(3.14159, 2) = {round(3.14159, 2)}")
print(f"  round(2.5) = {round(2.5)}  ← 银行家舍入（向偶数靠拢）")
print(f"  round(3.5) = {round(3.5)}")

# pow(x, y, mod) 带模运算
print(f"  pow(2, 3) = {pow(2, 3)}")
print(f"  pow(2, 10, 100) = {pow(2, 10, 100)}  ← (2^10) % 100")
print()

# ========== 2. zip —— 并行迭代 ==========
print("=" * 40)
print("2. zip —— 并行迭代")
print("=" * 40)

names = ["张三", "李四", "王五"]
scores = [85, 92, 78]

# 并行遍历
print("  遍历:")
for name, score in zip(names, scores):
    print(f"    {name}: {score} 分")

# 转为列表/字典
pairs = list(zip(names, scores))
print(f"  zip → list: {pairs}")
print(f"  zip → dict: {dict(pairs)}")

# 长度不同时以最短的为准
a = [1, 2, 3]
b = ["a", "b"]
print(f"  不等长 zip: {list(zip(a, b))}  ← 3 被丢弃")

# 解压缩
zipped = [(1, 'a'), (2, 'b'), (3, 'c')]
nums_out, letters_out = zip(*zipped)
print(f"  解压缩: nums={nums_out}, letters={letters_out}")
print()

# ========== 3. map —— 批量映射 ==========
print("=" * 40)
print("3. map —— 批量映射")
print("=" * 40)

nums = [1, 2, 3, 4, 5]

# 平方
squares = list(map(lambda x: x ** 2, nums))
print(f"  平方: {squares}")

# 多参数 map
a_list = [1, 2, 3]
b_list = [10, 20, 30]
sums = list(map(lambda x, y: x + y, a_list, b_list))
print(f"  相加: {a_list} + {b_list} = {sums}")

# map 返回迭代器，不转 list 不会执行
map_obj = map(str, nums)
print(f"  map 对象: {map_obj}  (需要 list() 才能看到结果)")
print()

# ========== 4. filter —— 条件筛选 ==========
print("=" * 40)
print("4. filter —— 条件筛选")
print("=" * 40)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 筛选偶数
evens = list(filter(lambda x: x % 2 == 0, nums))
print(f"  偶数: {evens}")

# 筛选大于 5
big = list(filter(lambda x: x > 5, nums))
print(f"  >5: {big}")

# 筛选非空字符串
words = ["hello", "", "world", "", "python"]
non_empty = list(filter(lambda w: len(w) > 0, words))
print(f"  非空: {non_empty}")
print()

# ========== 5. enumerate —— 带索引迭代 ==========
print("=" * 40)
print("5. enumerate —— 带索引迭代")
print("=" * 40)

fruits = ["苹果", "香蕉", "橘子"]

# 从 0 开始
for idx, fruit in enumerate(fruits):
    print(f"  {idx}: {fruit}")

# 从 1 开始
print("  (start=1):")
for idx, fruit in enumerate(fruits, start=1):
    print(f"  第{idx}个: {fruit}")

# 同时获取索引和值的经典用法
print("  枚举字符串:")
for i, ch in enumerate("ABC", 1):
    print(f"    字母{i}: {ch}")
print()

# ========== 6. sorted —— 排序（key 参数详解） ==========
print("=" * 40)
print("6. sorted —— 排序（key 参数详解）")
print("=" * 40)

nums = [3, 1, 4, 1, 5, 9, 2]
print(f"  升序: {sorted(nums)}")
print(f"  降序: {sorted(nums, reverse=True)}")

# key 参数 —— 最强大的特性
words = ["apple", "Banana", "kiwi", "Grape"]
print(f"  按长度: {sorted(words, key=len)}")
print(f"  忽略大小写: {sorted(words, key=str.lower)}")

# 多级排序经典案例
students = [
    {"name": "张三", "grade": 2, "score": 85},
    {"name": "李四", "grade": 1, "score": 92},
    {"name": "王五", "grade": 2, "score": 92},
    {"name": "赵六", "grade": 1, "score": 85},
]
# 先按年级升序，年级相同按分数降序
result = sorted(students, key=lambda s: (s["grade"], -s["score"]))
print(f"  多级排序:")
for s in result:
    print(f"    {s['name']}: 年级{s['grade']}, 分数{s['score']}")
print()

# ========== 7. reversed —— 反转 ==========
print("=" * 40)
print("7. reversed —— 反转")
print("=" * 40)

nums = [1, 2, 3, 4, 5]
print(f"  反转列表: {list(reversed(nums))}")
print(f"  反转字符串: {''.join(reversed('hello'))}")
print()

# ========== 8. any/all —— 逻辑判断 ==========
print("=" * 40)
print("8. any() / all() —— 逻辑判断")
print("=" * 40)

# all: 全部为 True
print(f"  all([True, True, True]) = {all([True, True, True])}")
print(f"  all([True, False, True]) = {all([True, False, True])}")

# any: 至少一个为 True
print(f"  any([False, False, True]) = {any([False, False, True])}")
print(f"  any([False, False, False]) = {any([False, False, False])}")

# 实际应用
scores = [85, 92, 55, 78]
print(f"  成绩: {scores}")
print(f"  全及格? {all(s >= 60 for s in scores)}")
print(f"  有人上90? {any(s >= 90 for s in scores)}")
print()

# ========== 9. isinstance / type ==========
print("=" * 40)
print("9. isinstance() vs type()")
print("=" * 40)

print(f"  isinstance(42, int) = {isinstance(42, int)}")
print(f"  isinstance(3.14, float) = {isinstance(3.14, float)}")
print(f"  isinstance('hello', (int, str)) = {isinstance('hello', (int, str))}")

# isinstance vs type 的区别
print(f"  isinstance(True, int) = {isinstance(True, int)}  ← bool 是 int 子类")
print(f"  type(True) == int = {type(True) == int}  ← type 不考虑继承")

# 推荐用 isinstance
def process_value(value):
    if isinstance(value, int):
        print(f"    整数: {value}")
    elif isinstance(value, str):
        print(f"    字符串: {value}")
    else:
        print(f"    其他类型: {type(value).__name__}")

process_value(42)
process_value("hello")
process_value([1, 2, 3])
print()

# ========== 10. chr / ord —— 字符编码 ==========
print("=" * 40)
print("10. chr() / ord() —— 字符与编码互转")
print("=" * 40)

print(f"  chr(65) = '{chr(65)}'")
print(f"  chr(97) = '{chr(97)}'")
print(f"  ord('A') = {ord('A')}")
print(f"  ord('a') = {ord('a')}")

# 生成字母表
uppercase = [chr(i) for i in range(65, 91)]
lowercase = [chr(i) for i in range(97, 123)]
print(f"  大写: {''.join(uppercase)}")
print(f"  小写: {''.join(lowercase)}")

# 简单凯撒密码
def caesar(text: str, shift: int = 3) -> str:
    """凯撒密码加密"""
    result = []
    for ch in text:
        if 'a' <= ch <= 'z':
            new_code = (ord(ch) - ord('a') + shift) % 26 + ord('a')
            result.append(chr(new_code))
        elif 'A' <= ch <= 'Z':
            new_code = (ord(ch) - ord('A') + shift) % 26 + ord('A')
            result.append(chr(new_code))
        else:
            result.append(ch)
    return "".join(result)

print(f"  caesar('Hello') = '{caesar('Hello')}'")
print(f"  caesar('abc', 3) = '{caesar('abc', 3)}'")
print(f"  caesar('xyz', 3) = '{caesar('xyz', 3)}'  ← 循环回绕")

# ========== 11. range / bin / oct / hex ==========
print()
print("=" * 40)
print("11. range / 进制转换")
print("=" * 40)

print(f"  list(range(5)) = {list(range(5))}")
print(f"  list(range(2, 8, 2)) = {list(range(2, 8, 2))}")
print(f"  list(range(5, 0, -1)) = {list(range(5, 0, -1))}")

print(f"  bin(42) = {bin(42)}")
print(f"  oct(42) = {oct(42)}")
print(f"  hex(42) = {hex(42)}")
