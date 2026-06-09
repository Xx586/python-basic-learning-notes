"""
Demo 4: 类型转换与类型判断
演示：类型转换、type() vs isinstance()、安全转换、动态类型

运行方式：python 4_type_conversion.py
"""

# ========== 1. 常用类型转换 ==========
print("=" * 50)
print("1. 常用类型转换")
print("=" * 50)

# int()
print("--- int() ---")
print(f"int('42') = {int('42')}")
print(f"int('100', 2) = {int('100', 2)}  (二进制转十进制)")
print(f"int('FF', 16) = {int('FF', 16)}  (十六进制转十进制)")
print(f"int(3.14) = {int(3.14)}  (截断，不四舍五入)")
print(f"int(3.99) = {int(3.99)}  (仍然是 3！)")
print(f"int(True) = {int(True)}, int(False) = {int(False)}")

# float()
print("\n--- float() ---")
print(f"float('3.14') = {float('3.14')}")
print(f"float('1e-3') = {float('1e-3')}  (科学计数法)")
print(f"float(10) = {float(10)}")
print(f"float(True) = {float(True)}")

# str()
print("\n--- str() ---")
print(f"str(100) = '{str(100)}'")
print(f"str(3.14) = '{str(3.14)}'")
print(f"str(True) = '{str(True)}'")
print(f"str([1, 2, 3]) = '{str([1, 2, 3])}'")
print(f"str(None) = '{str(None)}'")

# bool()
print("\n--- bool() ---")
print(f"bool(0) = {bool(0)}")
print(f"bool(1) = {bool(1)}")
print(f"bool('') = {bool('')}")
print(f"bool(' ') = {bool(' ')}  (空格不是空字符串)")
print(f"bool([]) = {bool([])}")
print(f"bool([0]) = {bool([0])}  (非空列表)")
print(f"bool(None) = {bool(None)}")

# 容器转换
print("\n--- 容器转换 ---")
print(f"list('hello') = {list('hello')}")
print(f"list((1, 2, 3)) = {list((1, 2, 3))}")
print(f"tuple([1, 2, 3]) = {tuple([1, 2, 3])}")
print(f"set([1, 2, 2, 3]) = {set([1, 2, 2, 3])}  (自动去重)")
print(f"dict([('a', 1), ('b', 2)]) = {dict([('a', 1), ('b', 2)])}")
print(f"dict(a=1, b=2) = {dict(a=1, b=2)}")

# ========== 2. 隐式类型转换 ==========
print("\n" + "=" * 50)
print("2. 隐式类型转换")
print("=" * 50)

# 数值运算中的自动提升
result = 10 + 3.14        # int + float → float
print(f"10 + 3.14 = {result}, type = {type(result).__name__}")

result = 10 / 3
print(f"10 / 3 = {result}, type = {type(result).__name__}")

# 布尔值在数值运算中
print(f"True + 1 = {True + 1}")
print(f"False * 100 = {False * 100}")

# 布尔上下文
print("\n--- 布尔上下文 ---")
data = []
if not data:      # 空列表 → False
    print("[] 在 if 中为 False")
if "hello":       # 非空字符串 → True
    print("'hello' 在 if 中为 True")

# ========== 3. type() vs isinstance() ==========
print("\n" + "=" * 50)
print("3. type() vs isinstance()")
print("=" * 50)

# type() — 获取精确类型
print("--- type() ---")
print(f"type(10) = {type(10)}")
print(f"type(3.14) = {type(3.14)}")
print(f"type('hello') = {type('hello')}")
print(f"type([1, 2]) = {type([1, 2])}")

# type() 的局限：不支持继承
class MyInt(int):
    pass

n = MyInt()
print(f"\ntype(MyInt()) == int: {type(n) == int}  (只看最底层)")

# isinstance() — 支持继承
print("--- isinstance() ---")
print(f"isinstance(10, int) = {isinstance(10, int)}")
print(f"isinstance(3.14, float) = {isinstance(3.14, float)}")
print(f"isinstance(True, bool) = {isinstance(True, bool)}")
print(f"isinstance(True, int) = {isinstance(True, int)}  (bool 是 int 的子类)")
print(f"isinstance(MyInt(), int) = {isinstance(n, int)}  (支持子类!)")

# 检查多个类型
print(f"\nisinstance(10, (int, float)) = {isinstance(10, (int, float))}")
print(f"isinstance(3.14, (int, float)) = {isinstance(3.14, (int, float))}")
print(f"isinstance('hello', (int, float)) = {isinstance('hello', (int, float))}")

# ========== 4. 安全转换 ==========
print("\n" + "=" * 50)
print("4. 安全转换（处理转换失败）")
print("=" * 50)

def safe_int(s, default=0):
    """尝试转为 int，失败返回默认值"""
    try:
        return int(s)
    except (ValueError, TypeError):
        return default

print(f"safe_int('42') = {safe_int('42')}")
print(f"safe_int('abc') = {safe_int('abc')}  (失败返回 0)")
print(f"safe_int('3.14') = {safe_int('3.14')}  (不能直接 int)")

# 先 float 再 int 的技巧
print(f"\nint(float('3.14')) = {int(float('3.14'))}  (绕道转)")

# ========== 5. 动态类型特性 ==========
print("\n" + "=" * 50)
print("5. 动态类型特性")
print("=" * 50)

# 变量类型可以随时改变
x = 10
print(f"x = {x}, type = {type(x).__name__}")

x = "hello"
print(f"x = '{x}', type = {type(x).__name__}")

x = [1, 2, 3]
print(f"x = {x}, type = {type(x).__name__}")

# 根据类型做不同处理
def process(data):
    if isinstance(data, bool):         # 先检查 bool！
        return "这是一个布尔值"
    elif isinstance(data, int):
        return f"整数 * 2 = {data * 2}"
    elif isinstance(data, str):
        return f"字符串大写: {data.upper()}"
    elif isinstance(data, list):
        return f"列表长度: {len(data)}"
    else:
        return f"不支持的类型: {type(data).__name__}"

print(f"\nprocess(10) -> {process(10)}")
print(f"process('hello') -> {process('hello')}")
print(f"process([1, 2, 3]) -> {process([1, 2, 3])}")
print(f"process(True) -> {process(True)}")

print("\n✅ Demo 4 运行完毕！")
