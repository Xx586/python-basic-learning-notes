"""
Demo 6: 装饰器
演示：函数一等公民、@语法糖、无参/有参装饰器、functools.wraps、多装饰器顺序、实战应用

运行方式：python 6_decorator.py
"""

import time
from functools import wraps

# ========== 1. 函数是一等公民 ==========
print("=" * 40)
print("1. 函数是一等公民")
print("=" * 40)

def greet(name):
    return f"Hello, {name}!"

# 赋值给变量
say_hello = greet
print(f"  变量调用: {say_hello('World')}")

# 作为参数传递
def execute(func, arg):
    return func(arg)

print(f"  作为参数: {execute(greet, 'Python')}")

# 作为返回值
def make_func():
    def inner():
        return "I'm inner"
    return inner

f = make_func()
print(f"  作为返回值: {f()}")
print()

# ========== 2. 装饰器基本原理（不用 @） ==========
print("=" * 40)
print("2. 装饰器基本原理")
print("=" * 40)

def simple_decorator(func):
    """最简单的装饰器"""
    def wrapper(*args, **kwargs):
        print("  函数调用前...")
        result = func(*args, **kwargs)
        print("  函数调用后...")
        return result
    return wrapper

def say_hi():
    print("  Hi!")

# 手动装饰（不用 @）
say_hi = simple_decorator(say_hi)
say_hi()
print()

# ========== 3. @ 语法糖 ==========
print("=" * 40)
print("3. @ 语法糖")
print("=" * 40)

@simple_decorator  # 等价于 add = simple_decorator(add)
def add(a, b):
    return a + b

result = add(3, 5)
print(f"  add(3, 5) = {result}")
print()

# ========== 4. 无参数装饰器（计时器） ==========
print("=" * 40)
print("4. 无参数装饰器 —— 计时器")
print("=" * 40)

def timer(func):
    """计时器装饰器"""
    @wraps(func)  # 保留原函数的元数据
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"  ⏱ {func.__name__} 运行时间: {elapsed:.6f} 秒")
        return result
    return wrapper

@timer
def slow_function():
    """模拟耗时操作"""
    total = 0
    for i in range(5_000_000):
        total += i
    return total

print(f"  结果: {slow_function()}")
print(f"  函数名: {slow_function.__name__}")  # 有了 @wraps，名字是对的
print(f"  文档: {slow_function.__doc__}")
print()

# ========== 5. 有参数装饰器（三层） ==========
print("=" * 40)
print("5. 有参数装饰器 —— @repeat(n)")
print("=" * 40)

def repeat(times):
    """重复执行装饰器"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for i in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hello(name):
    print(f"    Hello, {name}!")

say_hello("World")
print()

# ========== 6. 多装饰器叠加顺序 ==========
print("=" * 40)
print("6. 多装饰器叠加 —— 洋葱模型")
print("=" * 40)

def decorator_a(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("  [A 开始]")
        result = func(*args, **kwargs)
        print("  [A 结束]")
        return result
    return wrapper

def decorator_b(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("  [B 开始]")
        result = func(*args, **kwargs)
        print("  [B 结束]")
        return result
    return wrapper

@decorator_a   # 外层
@decorator_b   # 内层
def hello():
    print("    Hello!")

hello()
# 输出顺序: A开始 → B开始 → Hello! → B结束 → A结束
print()

# ========== 7. 实战应用 ==========
print("=" * 40)
print("7. 实战应用")
print("=" * 40)

# 7.1 日志装饰器
print("\n--- 日志装饰器 ---")

def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"  [LOG] 调用 {func.__name__}({args}, {kwargs})")
        result = func(*args, **kwargs)
        print(f"  [LOG] {func.__name__} 返回 {result}")
        return result
    return wrapper

@log
def multiply(a, b):
    return a * b

multiply(6, 7)
print()

# 7.2 权限校验装饰器
print("--- 权限校验装饰器 ---")

def require_role(role):
    """带参数装饰器：检查用户角色"""
    def decorator(func):
        @wraps(func)
        def wrapper(user, *args, **kwargs):
            if user.get("role") != role:
                print(f"  ❌ 用户 {user['name']} 无 {role} 权限")
                return None
            print(f"  ✅ 用户 {user['name']} 权限验证通过")
            return func(user, *args, **kwargs)
        return wrapper
    return decorator

@require_role("admin")
def delete_user(operator, target_id):
    print(f"    管理员 {operator['name']} 删除了用户 {target_id}")

admin = {"name": "Alice", "role": "admin"}
normal = {"name": "Bob", "role": "user"}

delete_user(admin, 123)
delete_user(normal, 456)
print()

# 7.3 缓存装饰器
print("--- 缓存装饰器 ---")

def memoize(func):
    """简单的缓存装饰器"""
    cache = {}
    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        else:
            print(f"    [缓存命中] {args}")
        return cache[args]
    return wrapper

@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(f"  fibonacci(10) = {fibonacci(10)}")
print(f"  fibonacci(10) = {fibonacci(10)}")  # 缓存命中
print()

# 7.4 类型检查装饰器
print("--- 类型检查装饰器 ---")

def validate_type(expected_type, index=0):
    """检查第 index 个参数的类型"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not isinstance(args[index], expected_type):
                raise TypeError(
                    f"参数应为 {expected_type.__name__}，"
                    f"实际为 {type(args[index]).__name__}"
                )
            return func(*args, **kwargs)
        return wrapper
    return decorator

@validate_type(int, index=0)
def square(n):
    return n * n

print(f"  square(5) = {square(5)}")
try:
    square("5")
except TypeError as e:
    print(f"  TypeError: {e}")
