"""
Demo 1: 基本数据类型
演示：int、float、bool、str、NoneType 的创建和基本操作

运行方式：python 1_basic_types.py
"""

# ========== 1. 整数 int ==========
print("=" * 50)
print("1. 整数 (int)")
print("=" * 50)

a = 10
b = int(3.14)          # 截断小数，结果为 3
c = 0xFF               # 十六进制，值为 255
d = 0b1010             # 二进制，值为 10
e = 1_000_000          # 下划线增强可读性，值为 1000000

print(f"a = {a}, b = {b}, c = {c}, d = {d}, e = {e}")

# 整数运算
x = 10
print(f"10 + 3 = {10 + 3}")
print(f"10 - 3 = {10 - 3}")
print(f"10 * 3 = {10 * 3}")
print(f"10 / 3 = {10 / 3}  (除法结果总是 float)")
print(f"10 // 3 = {10 // 3}  (整除/地板除)")
print(f"10 % 3 = {10 % 3}  (取余)")
print(f"10 ** 3 = {10 ** 3}  (乘方)")

# 内置函数
print(f"abs(-5) = {abs(-5)}")
print(f"pow(2, 3) = {pow(2, 3)}")
print(f"divmod(10, 3) = {divmod(10, 3)}  (商和余数)")
print(f"round(3.6) = {round(3.6)}")

# ========== 2. 浮点数 float ==========
print("\n" + "=" * 50)
print("2. 浮点数 (float)")
print("=" * 50)

a = 3.14
b = float(10)          # 10.0
c = 1.5e3              # 科学计数法，1500.0
d = 2.5e-2             # 0.025

print(f"a = {a}, b = {b}, c = {c}, d = {d}")

# 浮点数精度陷阱（重要！！！）
print("\n⚠️  浮点数精度陷阱：")
print(f"0.1 + 0.2 = {0.1 + 0.2}")                 # 0.30000000000000004
print(f"0.1 + 0.2 == 0.3 ? {0.1 + 0.2 == 0.3}")    # False!

# 解决方案
import math
from decimal import Decimal

print(f"\n使用 Decimal: {Decimal('0.1') + Decimal('0.2')}")
print(f"使用 isclose: {math.isclose(0.1 + 0.2, 0.3)}")

# ========== 3. 布尔值 bool ==========
print("\n" + "=" * 50)
print("3. 布尔值 (bool)")
print("=" * 50)

a = True
b = False
c = bool(1)            # True
d = bool(0)            # False
e = bool("hello")      # True（非空字符串为 True）
f = bool("")           # False（空字符串为 False）
g = 10 > 5             # True（比较运算的结果）

print(f"True = {a}, False = {b}")
print(f"bool(1) = {c}, bool(0) = {d}")
print(f"bool('hello') = {e}, bool('') = {f}")
print(f"10 > 5 = {g}")

# True 是 int 的子类
print(f"\nTrue == 1: {True == 1}")
print(f"True + 1 = {True + 1}")
print(f"isinstance(True, int): {isinstance(True, int)}")

# 哪些值被视为 False？
print("\n哪些值是 False？")
for val in [0, 0.0, "", [], {}, (), set(), None]:
    print(f"  bool({repr(val)}) = {bool(val)}")

# ========== 4. 字符串 str ==========
print("\n" + "=" * 50)
print("4. 字符串 (str)")
print("=" * 50)

s1 = 'hello'
s2 = "world"
s3 = str(123)          # "123"
s4 = "He said, \"Hello!\""   # 转义引号
s5 = r"C:\Users\name" # 原始字符串，\ 不转义

print(f's1 = {s1}')
print(f's2 = {s2}')
print(f's3 = {s3}')
print(f's4 = {s4}')
print(f's5 = {s5}')

# 字符串拼接和重复
print(f'"hello" + " world" = {"hello" + " world"}')
print(f'"ha" * 3 = {"ha" * 3}')

# ========== 5. 空值 None ==========
print("\n" + "=" * 50)
print("5. 空值 (NoneType)")
print("=" * 50)

result = None          # 初始化一个暂时还没有值的变量
print(f"result = {result}")
print(f"type(None) = {type(None)}")
print(f"bool(None) = {bool(None)}")

# 正确判断方式：用 is
if result is None:
    print("变量为 None（使用 is 判断）")

# 错误方式：用 ==（PEP 8 不推荐）
# if result == None:   # 不推荐！
#     pass

# ========== 6. 动态类型 ==========
print("\n" + "=" * 50)
print("6. 动态类型演示")
print("=" * 50)

x = 10
print(f"x = {x}, type = {type(x).__name__}")

x = 3.14
print(f"x = {x}, type = {type(x).__name__}")

x = "Python"
print(f"x = {x}, type = {type(x).__name__}")

x = [1, 2, 3]
print(f"x = {x}, type = {type(x).__name__}")

print("\n✅ Demo 1 运行完毕！")
