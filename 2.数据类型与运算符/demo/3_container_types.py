"""
Demo 3: 四大容器类型
演示：列表、元组、字典、集合 的创建和常用操作

运行方式：python 3_container_types.py
"""

# ========== 1. 列表 list ==========
print("=" * 50)
print("1. 列表 (list) — 有序、可变的序列")
print("=" * 50)

# 创建
print("--- 创建 ---")
nums = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
range_list = list(range(5))
squares = [x ** 2 for x in range(5)]   # 列表推导式

print(f"nums = {nums}")
print(f"mixed = {mixed}")
print(f"range_list = {range_list}")
print(f"推导式 squares = {squares}")

# 增
print("\n--- 增 ---")
nums = [1, 2, 3]
print(f"原列表: {nums}")
nums.append(4)
print(f"append(4): {nums}")
nums.insert(0, 0)
print(f"insert(0, 0): {nums}")
nums.extend([5, 6])
print(f"extend([5, 6]): {nums}")

# 删
print("\n--- 删 ---")
nums = [1, 2, 3, 4, 5]
print(f"原列表: {nums}")
nums.remove(3)            # 删除第一个匹配值
print(f"remove(3): {nums}")
popped = nums.pop()       # 删除并返回末尾元素
print(f"pop() = {popped}, 列表: {nums}")
popped2 = nums.pop(1)     # 删除索引 1 的元素
print(f"pop(1) = {popped2}, 列表: {nums}")

# 改
print("\n--- 改 ---")
nums = [1, 2, 3]
print(f"原列表: {nums}")
nums[0] = 100
print(f"nums[0] = 100: {nums}")
nums[1:3] = [20, 30]
print(f"切片赋值 nums[1:3] = [20, 30]: {nums}")

# 切片
print("\n--- 切片 ---")
nums = [10, 20, 30, 40, 50]
print(f"nums = {nums}")
print(f"nums[1:4] = {nums[1:4]}")
print(f"nums[:3] = {nums[:3]}")
print(f"nums[::2] = {nums[::2]}")
print(f"nums[::-1] = {nums[::-1]}  (反转)")

# 排序
print("\n--- 排序 ---")
nums = [3, 1, 4, 1, 5, 9, 2]
print(f"原列表: {nums}")
print(f"sorted(nums): {sorted(nums)}")
print(f"sorted(nums, reverse=True): {sorted(nums, reverse=True)}")
nums.sort()
print(f"nums.sort() 后: {nums}")
nums.sort(reverse=True)
print(f"nums.sort(reverse=True) 后: {nums}")

# 按长度排序
words = ["apple", "banana", "kiwi", "pear"]
words.sort(key=len)
print(f"按长度排序: {words}")

# 常用方法
print("\n--- 其他方法 ---")
nums = [1, 2, 3, 2, 4, 2]
print(f"len(nums) = {len(nums)}")
print(f"nums.count(2) = {nums.count(2)}")
print(f"nums.index(3) = {nums.index(3)}")

# ========== 2. 元组 tuple ==========
print("\n" + "=" * 50)
print("2. 元组 (tuple) — 有序、不可变的序列")
print("=" * 50)

# 创建
t1 = (1, 2, 3)
t2 = tuple([1, 2, 3])
t3 = 1, 2, 3            # 括号可省略
single = (1,)            # 单元素元组必须有逗号！
not_tuple = (1)          # 这是 int，不是元组！

print(f"t1 = {t1}")
print(f"t2 = {t2}")
print(f"t3 = {t3}")
print(f"单元素元组 type((1,)) = {type(single)}")
print(f"不是元组 type((1)) = {type(not_tuple)}  ← 注意！")

# 解包
print("\n--- 解包 ---")
point = (10, 20)
x, y = point
print(f"point = {point}, x = {x}, y = {y}")

# 多变量交换
a, b = 1, 2
a, b = b, a
print(f"交换后: a = {a}, b = {b}")

# * 收集剩余
first, *rest = (1, 2, 3, 4)
print(f"first = {first}, rest = {rest}")
first, *middle, last = (1, 2, 3, 4, 5)
print(f"first = {first}, middle = {middle}, last = {last}")

# ========== 3. 字典 dict ==========
print("\n" + "=" * 50)
print("3. 字典 (dict) — 键值对映射")
print("=" * 50)

# 创建
print("--- 创建 ---")
person = {"name": "张三", "age": 25, "city": "北京"}
d1 = dict(name="李四", age=30)
d2 = dict([("a", 1), ("b", 2)])

print(f"person = {person}")
print(f"d1 = {d1}")
print(f"d2 = {d2}")

# 增 / 改
print("\n--- 增/改 ---")
person = {"name": "张三"}
print(f"原字典: {person}")
person["age"] = 25                # 新增
print(f"新增 age: {person}")
person["name"] = "李四"           # 修改
print(f"修改 name: {person}")
person.update({"city": "北京", "age": 30})
print(f"update: {person}")

# setdefault
score = person.setdefault("score", 0)  # 不存在，设为 0
print(f"setdefault('score', 0): score = {score}, person = {person}")

# 查
print("\n--- 查 ---")
person = {"name": "张三", "age": 25}
print(f"person['name'] = {person['name']}")
print(f"person.get('age') = {person.get('age')}")
print(f"person.get('city') = {person.get('city')}  (不存在返回 None)")
print(f"person.get('city', '未知') = {person.get('city', '未知')}  (自定义默认值)")

# 遍历
print("\n--- 遍历 ---")
for key in person:
    print(f"  {key} => {person[key]}")

print("\n使用 .items()：")
for key, value in person.items():
    print(f"  {key}: {value}")

# 常用操作
print("\n--- 常用操作 ---")
d = {"a": 1, "b": 2, "c": 3}
print(f"len(d) = {len(d)}")
print(f"'a' in d = {'a' in d}")
print(f"keys: {list(d.keys())}")
print(f"values: {list(d.values())}")

# ========== 4. 集合 set ==========
print("\n" + "=" * 50)
print("4. 集合 (set) — 无序、不重复")
print("=" * 50)

# 创建
print("--- 创建 ---")
empty_set = set()        # 空集合（{} 是空字典！）
s1 = {1, 2, 3, 4}
s2 = set([1, 2, 2, 3, 3, 4])   # 自动去重
s3 = set("hello")               # 字符去重

print(f"空集合: {empty_set}, type = {type(empty_set)}")
print(f"s1 = {s1}")
print(f"s2 = {s2}  (自动去重)")
print(f"s3 = {s3}  (字符去重)")

# 去重
print("\n--- 去重 ---")
nums = [1, 2, 2, 3, 3, 3, 4]
unique = list(set(nums))
print(f"list → set → list: {unique}")

# 增删
print("\n--- 增删 ---")
s = {1, 2, 3}
print(f"原集合: {s}")
s.add(4)
print(f"add(4): {s}")
s.add(2)                 # 重复不添加
print(f"add(2): {s}  (重复不添加)")
s.discard(2)
print(f"discard(2): {s}")
s.discard(99)            # 安全删除，不存在不报错
print(f"discard(99): {s}  (安全，不报错)")

# 集合运算
print("\n--- 集合运算 ---")
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(f"a = {a}")
print(f"b = {b}")
print(f"交集 a & b = {a & b}")
print(f"并集 a | b = {a | b}")
print(f"差集 a - b = {a - b}")
print(f"对称差 a ^ b = {a ^ b}")
print(f"a 是 b 的子集吗？ {a <= b}")
print(f"{{1, 2}} 是 a 的子集吗？ {{1, 2} <= a}")

# ========== 5. 容器对比总结 ==========
print("\n" + "=" * 50)
print("5. 容器对比总结")
print("=" * 50)

print("""
| 特性     | 列表 list | 元组 tuple | 字典 dict | 集合 set   |
|----------|----------|-----------|-----------|-----------|
| 写法     | []       | ()        | {k:v}     | {} / set()|
| 有序     | 是       | 是        | 是(3.7+)  | 否        |
| 可变     | 是       | 否        | 是        | 是        |
| 重复     | 允许     | 允许      | 键不允许  | 不允许    |
| 索引     | [0]      | [0]       | [key]     | 否        |
| 典型场景 | 有序集合 | 不变记录  | 键值映射  | 去重/运算 |
""")

print("✅ Demo 3 运行完毕！")
