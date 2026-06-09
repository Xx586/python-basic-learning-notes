"""
Demo 1: 函数定义与调用
演示：def定义、参数类型（必选/默认/*args/**kwargs）、return返回值、docstring

运行方式：python 1_function_basics.py
"""

# ========== 1. 最基础的函数定义与调用 ==========
def greet(name):
    """打印一句问候语"""
    print(f"Hello, {name}!")

greet("Python")
print()

# ========== 2. 带返回值的函数 ==========
def add(a, b):
    """返回两个数的和"""
    return a + b

result = add(3, 5)
print(f"add(3, 5) = {result}")
print()

# ========== 3. 参数类型演示 ==========
# 3.1 位置参数 —— 必须按顺序传入
def introduce(name, age):
    print(f"我叫{name}，今年{age}岁")

introduce("小明", 18)

# 3.2 关键字传参 —— 可以打乱顺序
introduce(age=20, name="小红")

# 3.3 默认参数 —— 调用时可以不传
def greet_with_prefix(name, greeting="你好"):
    print(f"{greeting}，{name}！")

greet_with_prefix("小明")                  # 使用默认值
greet_with_prefix("Alice", greeting="Hi")  # 覆盖默认值
print()

# 3.4 *args —— 可变位置参数，打包成元组
def my_sum(*args):
    """计算任意数量数字的和"""
    print(f"传入的参数: {args}, 类型: {type(args).__name__}")
    return sum(args)

print(f"my_sum(1, 2, 3) = {my_sum(1, 2, 3)}")
print(f"my_sum(1, 2, 3, 4, 5) = {my_sum(1, 2, 3, 4, 5)}")
print(f"my_sum() = {my_sum()}")  # 不传参数也OK
print()

# 3.5 **kwargs —— 可变关键字参数，打包成字典
def print_info(**kwargs):
    """打印任意关键字参数"""
    print(f"传入的参数: {kwargs}, 类型: {type(kwargs).__name__}")
    for key, value in kwargs.items():
        print(f"  {key} = {value}")

print_info(name="张三", age=18, city="北京")
print()

# ========== 4. 四种参数混用 ==========
def full_demo(required, default="默认值", *args, **kwargs):
    """
    完整参数演示
    参数顺序: 必选 → 默认 → *args → **kwargs
    """
    print(f"必选参数 required: {required}")
    print(f"默认参数 default: {default}")
    print(f"*args: {args}")
    print(f"**kwargs: {kwargs}")

full_demo("必须传", "覆盖默认", 1, 2, 3, name="张三", age=18)
print()

# ========== 5. 多值返回（本质是返回元组） ==========
def divide_and_remainder(a, b):
    """返回商和余数"""
    return a // b, a % b

result = divide_and_remainder(10, 3)
print(f"返回结果: {result}, 类型: {type(result).__name__}")

# 元组解包
quotient, remainder = divide_and_remainder(10, 3)
print(f"商: {quotient}, 余数: {remainder}")
print()

# ========== 6. 文档字符串 docstring ==========
def calculate_bmi(weight, height):
    """
    计算身体质量指数 (BMI)

    参数:
        weight: 体重（千克）
        height: 身高（米）

    返回值:
        BMI 数值
    """
    return weight / (height ** 2)

# 通过 help() 查看文档
print("函数文档：")
print(calculate_bmi.__doc__)
print(f"BMI 计算: {calculate_bmi(70, 1.75):.1f}")
print()

# ========== 7. 参数传递的本质 ==========
print("=" * 40)
print("参数传递演示：不可变对象 vs 可变对象")
print("=" * 40)

# 不可变对象（int）—— 函数内修改不影响外部
def modify_num(n):
    n = n + 1
    print(f"  函数内 n = {n}")

x = 10
modify_num(x)
print(f"  函数外 x = {x}")  # 不变

# 可变对象（list）—— 函数内修改会影响外部
def modify_list(lst):
    lst.append(4)
    print(f"  函数内 lst = {lst}")

my_list = [1, 2, 3]
modify_list(my_list)
print(f"  函数外 my_list = {my_list}")  # 被改变了
print()

# ========== 8. 可变默认参数的坑 ==========
print("=" * 40)
print("踩坑演示：可变默认参数")
print("=" * 40)

# 错误写法
def add_item_bad(item, items=[]):
    items.append(item)
    return items

print(f"add_item_bad(1) = {add_item_bad(1)}")
print(f"add_item_bad(2) = {add_item_bad(2)}")  # [1, 2] ← 1还在！
print(f"add_item_bad(3) = {add_item_bad(3)}")  # [1, 2, 3]

# 正确写法
def add_item_good(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print(f"add_item_good(1) = {add_item_good(1)}")
print(f"add_item_good(2) = {add_item_good(2)}")
print(f"add_item_good(3) = {add_item_good(3)}")
