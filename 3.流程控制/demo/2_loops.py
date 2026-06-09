"""
Demo 2: 循环
演示：for 循环、while 循环、break/continue/pass、range()、嵌套循环、for-else

运行方式：python 2_loops.py
"""

# ========== 1. for 循环基础 ==========
print("=" * 50)
print("1. for 循环遍历各类可迭代对象")
print("=" * 50)

# 1.1 遍历列表
print("--- 遍历列表 ---")
fruits = ["苹果", "香蕉", "橘子", "葡萄"]
for fruit in fruits:
    print(f"  我喜欢吃{fruit}")

# 1.2 遍历字典
print("\n--- 遍历字典 ---")
student = {"name": "小明", "age": 18, "score": 95}

print("遍历键：", end=" ")
for key in student:
    print(key, end="  ")
print()

print("遍历值：", end=" ")
for value in student.values():
    print(value, end="  ")
print()

print("遍历键值对：")
for key, value in student.items():
    print(f"  {key}: {value}")

# 1.3 enumerate() 同时获取索引和值
print("\n--- enumerate() ---")
colors = ["红", "绿", "蓝"]
for index, color in enumerate(colors, start=1):  # 索引起始为 1
    print(f"  第{index}个颜色：{color}")

# 1.4 zip() 同时遍历多个序列
print("\n--- zip() ---")
names = ["小明", "小红", "小刚"]
scores = [95, 88, 76]
for name, score in zip(names, scores):
    print(f"  {name}：{score}分")


# ========== 2. while 循环 ==========
print("\n" + "=" * 50)
print("2. while 循环")
print("=" * 50)

# 基本用法
print("--- while 打印 1-5 ---")
count = 1
while count <= 5:
    print(f"  count = {count}")
    count += 1

# while True + break 模式
print("\n--- while True + break ---")
counter = 0
while True:
    counter += 1
    if counter > 3:
        break  # 出口条件
    print(f"  第 {counter} 次循环")


# ========== 3. break 和 continue ==========
print("\n" + "=" * 50)
print("3. break 和 continue")
print("=" * 50)

# break：找到目标后立即停止
print("--- break：找到 8 就停 ---")
numbers = [1, 3, 5, 7, 8, 9, 11]
for num in numbers:
    print(f"  检查：{num}")
    if num == 8:
        print(f"  找到目标 {num}，跳出循环！")
        break

# continue：跳过特定条件
print("\n--- continue：只打印奇数 ---")
for i in range(1, 11):
    if i % 2 == 0:
        continue  # 跳过偶数
    print(f"  {i}", end=" ")
print()


# ========== 4. pass 占位符 ==========
print("\n" + "=" * 50)
print("4. pass 占位符")
print("=" * 50)

# 函数占位
def future_function():
    pass  # TODO: 以后实现

# 条件分支占位
x = 10
if x > 5:
    pass  # 先不处理
else:
    print("x <= 5")

print("pass 什么都不做，仅占位——程序继续执行到这里")
print("注意：pass ≠ continue，continue 是跳过循环，pass 是啥也不干但继续往下")


# ========== 5. range() 用法 ==========
print("\n" + "=" * 50)
print("5. range() 的各种用法")
print("=" * 50)

print(f"range(5)       = {list(range(5))}")        # [0, 1, 2, 3, 4]
print(f"range(2, 6)    = {list(range(2, 6))}")     # [2, 3, 4, 5]
print(f"range(0, 10, 2)= {list(range(0, 10, 2))}") # [0, 2, 4, 6, 8]
print(f"range(10, 0, -1)= {list(range(10, 0, -1))}")  # 倒序

# range 的惰性特点
import sys
small_r = range(10)
big_r = range(1000000)
print(f"\nrange(10) 内存：{sys.getsizeof(small_r)} bytes")
print(f"range(1000000) 内存：{sys.getsizeof(big_r)} bytes")
print(f"list(range(1000000)) 内存：{sys.getsizeof(list(range(1000000)))} bytes（对比）")

# range 支持索引访问
r = range(10, 20)
print(f"\nrange(10, 20)[3] = {r[3]}")
print(f"5 in range(10, 20) = {5 in r}")
print(f"15 in range(10, 20) = {15 in r}")


# ========== 6. 嵌套循环 ==========
print("\n" + "=" * 50)
print("6. 嵌套循环（九九乘法表）")
print("=" * 50)

for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}×{i}={i*j:2d}", end="  ")
    print()  # 每行结束后换行

print("\n--- 遍历二维列表 ---")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for element in row:
        print(element, end=" ")
    print()


# ========== 7. for-else 和 while-else ==========
print("\n" + "=" * 50)
print("7. for-else 和 while-else")
print("=" * 50)

# for-else：找质数
print("--- for-else：判断质数 ---")
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print(f"  {n} 能被 {i} 整除，不是质数")
            break
    else:
        # 循环正常结束 = 没找到因子
        print(f"  {n} 是质数！")
        return True
    return False

is_prime(17)  # 质数
is_prime(15)  # 非质数

# for-else：未找到时的默认行为
print("\n--- for-else：搜索列表 ---")
items = ["苹果", "香蕉", "橘子"]
target = "西瓜"

for item in items:
    if item == target:
        print(f"找到 {target}！")
        break
else:
    print(f"列表中没找到 {target}")

target2 = "香蕉"
for item in items:
    if item == target2:
        print(f"找到 {target2}！")
        break
else:
    print(f"列表中没找到 {target2}")

# while-else：被 break 中断时 else 不执行
print("\n--- while-else：break 中断 ---")
count = 0
while count < 5:
    print(f"  count = {count}")
    if count == 2:
        print("  break 中断！")
        break
    count += 1
else:
    print("  这行不会执行（因为被 break 了）")


print("\n" + "=" * 50)
print("Demo 2 运行完毕")
print("=" * 50)
