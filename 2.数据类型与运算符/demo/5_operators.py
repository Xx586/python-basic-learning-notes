"""
Demo 5: 运算符
演示：算术/比较/逻辑/赋值/成员/身份/位运算符、三元表达式、链式比较、优先级

运行方式：python 5_operators.py
"""

# ========== 1. 算术运算符 ==========
print("=" * 50)
print("1. 算术运算符")
print("=" * 50)

print(f"10 + 3 = {10 + 3}")
print(f"10 - 3 = {10 - 3}")
print(f"10 * 3 = {10 * 3}")
print(f"10 / 3 = {10 / 3}  (结果总是 float)")
print(f"10 // 3 = {10 // 3}  (整除/地板除)")
print(f"-10 // 3 = {-10 // 3}  (向下取整，注意不是 -3！)")
print(f"10 % 3 = {10 % 3}  (取余)")
print(f"-10 % 3 = {-10 % 3}  (Python 保证 商*除数+余数=被除数)")
print(f"10 ** 3 = {10 ** 3}  (乘方)")

# 序列的算术运算
print(f"\n'hello' + ' world' = '{'hello' + ' world'}'  (拼接)")
print(f"'ha' * 3 = '{'ha' * 3}'  (重复)")
print(f"[1, 2] + [3, 4] = {[1, 2] + [3, 4]}")
print(f"[0] * 5 = {[0] * 5}")

# ========== 2. 比较运算符 ==========
print("\n" + "=" * 50)
print("2. 比较运算符")
print("=" * 50)

print(f"10 > 5 = {10 > 5}")
print(f"10 == 10 = {10 == 10}")
print(f"10 != 5 = {10 != 5}")
print(f"5 >= 5 = {5 >= 5}")
print(f"type(10 > 5) = {type(10 > 5)}  (比较结果总是 bool)")

# 字符串比较（字典序）
print(f"\n'abc' < 'abd' = {'abc' < 'abd'}")
print(f"'apple' < 'Banana' = {'apple' < 'Banana'}  (大写 < 小写)")

# 浮点数比较
print(f"\n0.1 + 0.2 == 0.3 ? {0.1 + 0.2 == 0.3}")
import math
print(f"math.isclose(0.1 + 0.2, 0.3) ? {math.isclose(0.1 + 0.2, 0.3)}")

# ========== 3. 逻辑运算符（短路求值） ==========
print("\n" + "=" * 50)
print("3. 逻辑运算符（短路求值）")
print("=" * 50)

# and — 全真才真，返回最后一个值（或第一个假值）
print("--- and ---")
print(f"1 and 2 and 3 = {1 and 2 and 3}  (返回最后一个)")
print(f"1 and 0 and 3 = {1 and 0 and 3}  (遇到假值就返回)")

# or — 一真即真，返回第一个真值（或最后一个假值）
print("\n--- or ---")
print(f"0 or '' or [] = {0 or '' or []}  (全假，返回最后一个)")
print(f"0 or 2 or 3 = {0 or 2 or 3}  (返回第一个真值)")

# not — 取反
print("\n--- not ---")
print(f"not True = {not True}")
print(f"not 0 = {not 0}")
print(f"not 'hello' = {not 'hello'}")

# 短路求值实战
print("\n--- 短路求值实战 ---")

# 1. 给变量赋默认值
data = None
items = data or []
print(f"data or [] = {items}  (None 为假，返回 [])")

# 2. 避免除零错误
count = 0
if count != 0 and 10 / count > 2:
    print("满足")
else:
    print(f"短路保护：count != 0 为假，右边不执行，避免 10/0 报错")

# ========== 4. 赋值运算符 ==========
print("\n" + "=" * 50)
print("4. 赋值运算符")
print("=" * 50)

x = 10
print(f"x = 10 -> {x}")

x += 5
print(f"x += 5 -> {x}")

x -= 3
print(f"x -= 3 -> {x}")

x *= 2
print(f"x *= 2 -> {x}")

x /= 4
print(f"x /= 4 -> {x}")

# 多重赋值
a = b = c = 0
print(f"\na = b = c = 0 -> a={a}, b={b}, c={c}")

x, y, z = 1, 2, 3
print(f"x, y, z = 1, 2, 3 -> x={x}, y={y}, z={z}")

# ========== 5. 成员运算符 ==========
print("\n" + "=" * 50)
print("5. 成员运算符 (in / not in)")
print("=" * 50)

# 字符串
print(f"'py' in 'python' = {'py' in 'python'}")
print(f"'z' not in 'python' = {'z' not in 'python'}")

# 列表
print(f"3 in [1, 2, 3, 4] = {3 in [1, 2, 3, 4]}")

# 字典（检查的是键！）
d = {"name": "张三", "age": 25}
print(f"\n字典 d = {d}")
print(f"'name' in d = {'name' in d}  (检查键)")
print(f"'张三' in d = {'张三' in d}  (不是键！)")
print(f"25 in d.values() = {25 in d.values()}  (检查值)")

# 集合
s = {1, 2, 3}
print(f"\n集合 s = {s}")
print(f"2 in s = {2 in s}")

# ========== 6. 身份运算符 ==========
print("\n" + "=" * 50)
print("6. 身份运算符 (is / is not)")
print("=" * 50)

# == 比较值，is 比较内存地址
lst1 = [1, 2, 3]
lst2 = [1, 2, 3]
print(f"lst1 == lst2: {lst1 == lst2}  (值相同)")
print(f"lst1 is lst2: {lst1 is lst2}  (不同对象)")

lst3 = lst1
print(f"\nlst3 = lst1")
print(f"lst1 is lst3: {lst1 is lst3}  (同一个对象)")

# 小整数缓存 (-5 ~ 256)
a = 256
b = 256
print(f"\n256 is 256: {a is b}  (缓存复用)")

a = 257
b = 257
print(f"257 is 257: {a is b}  (超出缓存)")

# None 必须用 is 判断
x = None
print(f"\n判断 None：")
print(f"x is None: {x is None}  (正确！)")
print(f"x == None: {x == None}  (也能用，但 PEP 8 不推荐)")

# ========== 7. 位运算符 ==========
print("\n" + "=" * 50)
print("7. 位运算符")
print("=" * 50)

a = 60    # 0011 1100
b = 13    # 0000 1101

print(f"a = {a} (二进制 {bin(a)})")
print(f"b = {b} (二进制 {bin(b)})")
print(f"a & b = {a & b}  (按位与)")
print(f"a | b = {a | b}  (按位或)")
print(f"a ^ b = {a ^ b}  (按位异或)")
print(f"~a = {~a}  (按位取反)")
print(f"a << 2 = {a << 2}  (左移，等于 a * 4)")
print(f"a >> 2 = {a >> 2}  (右移，等于 a // 4)")

# 实战：判断奇偶
def is_even(n):
    return (n & 1) == 0

print(f"\n位运算判断奇偶：")
print(f"is_even(10) = {is_even(10)}")
print(f"is_even(11) = {is_even(11)}")

# 实战：权限系统
print("\n位运算权限系统：")
READ = 4     # 100
WRITE = 2    # 010
EXECUTE = 1  # 001

perm = READ | WRITE
print(f"权限 = READ | WRITE = {perm}  (二进制 {bin(perm)})")

perm |= EXECUTE  # 添加执行权限
print(f"添加 EXECUTE 后: {perm} ({bin(perm)})")

check = (perm & WRITE) != 0
print(f"有写权限吗？ {check}")

perm &= ~WRITE   # 移除写权限
print(f"移除 WRITE 后: {perm} ({bin(perm)})")

# ========== 8. 三元表达式 ==========
print("\n" + "=" * 50)
print("8. 三元表达式")
print("=" * 50)

age = 20
status = "成年" if age >= 18 else "未成年"
print(f"{age} 岁: {status}")

score = 85
grade = "A" if score >= 90 else ("B" if score >= 80 else "C")
print(f"成绩 {score}: {grade}")

# 列表推导中使用三元
nums = [1, -2, 3, -4, 5]
result = [x if x > 0 else 0 for x in nums]
print(f"过滤负数: {result}")

# 默认值
name = None
print(f"用户: {name if name else '匿名'}")

# ========== 9. 链式比较 ==========
print("\n" + "=" * 50)
print("9. 链式比较")
print("=" * 50)

x = 5
print(f"x = {x}")
print(f"1 < x < 10: {1 < x < 10}")
print(f"1 <= x <= 5: {1 <= x <= 5}")

a = b = 10
print(f"\na = b = 10")
print(f"a == b == 10: {a == b == 10}")
print(f"0 < a <= b < 20: {0 < a <= b < 20}")

# ========== 10. 运算符优先级 ==========
print("\n" + "=" * 50)
print("10. 运算符优先级")
print("=" * 50)

print("优先级示例：")
print(f"2 + 3 * 4 = {2 + 3 * 4}  (先乘后加)")
print(f"(2 + 3) * 4 = {(2 + 3) * 4}  (括号优先)")
print(f"-3 ** 2 = {-3 ** 2}  (** 优先于 -)")
print(f"(-3) ** 2 = {(-3) ** 2}")
print(f"not True or False = {not True or False}  (not 优先于 or)")
print(f"True or True and False = {True or True and False}  (and 优先于 or)")

print("\n拿不准就加括号！")

print("\n✅ Demo 5 运行完毕！")
