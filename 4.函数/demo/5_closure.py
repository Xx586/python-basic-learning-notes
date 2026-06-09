"""
Demo 5: 闭包
演示：外层函数返回内层函数、内层引用外层变量、工厂函数、回调函数、循环中闭包延迟绑定

运行方式：python 5_closure.py
"""

# ========== 1. 闭包基础 —— 记住环境变量 ==========
print("=" * 40)
print("1. 闭包基础")
print("=" * 40)

def outer():
    msg = "Hello"  # 外层函数的变量

    def inner():   # 内层函数
        print(msg)  # 引用了外层的 msg

    return inner   # 返回内层函数

f = outer()  # outer() 执行完毕，msg 本该销毁
f()          # 但 inner 仍然记得 msg = "Hello"
print()

# ========== 2. 工厂函数 —— 生产定制化的函数 ==========
print("=" * 40)
print("2. 工厂函数")
print("=" * 40)

def make_multiplier(factor):
    """返回一个乘以 factor 的函数"""
    def multiply(x):
        return x * factor  # factor 被"记住"了
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(f"  double(5)  = {double(5)}")   # 10 (factor=2)
print(f"  triple(5)  = {triple(5)}")   # 15 (factor=3)
print(f"  double(10) = {double(10)}")  # 20
print(f"  triple(10) = {triple(10)}")  # 30

# double 和 triple 是独立的闭包
print(f"  double 的 factor: {double.__closure__[0].cell_contents}")
print(f"  triple 的 factor: {triple.__closure__[0].cell_contents}")
print()

# ========== 3. 带状态的函数 —— 闭包版计数器 ==========
print("=" * 40)
print("3. 带状态的函数（计数器）")
print("=" * 40)

def make_counter(start=0):
    """创建一个计数器，从 start 开始"""
    count = start

    def counter():
        nonlocal count  # 修改外层变量
        count += 1
        return count

    return counter

counter_a = make_counter(0)
counter_b = make_counter(100)

print(f"  counter_a: {counter_a()}, {counter_a()}, {counter_a()}")
print(f"  counter_b: {counter_b()}, {counter_b()}")
print()

# ========== 4. 回调函数 —— 传入上下文 ==========
print("=" * 40)
print("4. 回调函数")
print("=" * 40)

def make_logger(prefix):
    """创建一个带前缀的日志函数"""
    def logger(message):
        print(f"  [{prefix}] {message}")
    return logger

info_log = make_logger("INFO")
error_log = make_logger("ERROR")
debug_log = make_logger("DEBUG")

info_log("服务器启动")
error_log("数据库连接失败")
debug_log("变量 x = 42")
print()

# ========== 5. 预计算（缓存） ==========
print("=" * 40)
print("5. 预计算（缓存）")
print("=" * 40)

def make_power_table(base):
    """预计算 base 的 1~5 次方"""
    table = {i: base ** i for i in range(1, 6)}

    def power(exponent):
        if exponent in table:
            print(f"    [缓存命中] {base}^{exponent}")
        return table.get(exponent, base ** exponent)

    return power

power_of_2 = make_power_table(2)
print(f"  2^3 = {power_of_2(3)}")  # 缓存命中
print(f"  2^5 = {power_of_2(5)}")  # 缓存命中
print(f"  2^10 = {power_of_2(10)}")  # 不在缓存，现场计算
print()

# ========== 6. 循环中闭包的延迟绑定（重要踩坑） ==========
print("=" * 40)
print("6. 循环中闭包的延迟绑定（重要！）")
print("=" * 40)

# ❌ 错误写法
print("  错误写法:")
funcs_wrong = []
for i in range(5):
    funcs_wrong.append(lambda: i)  # 所有闭包共享同一个 i

print(f"    结果: {[f() for f in funcs_wrong]}")  # [4, 4, 4, 4, 4]

# ✅ 修复1：默认参数冻结值
print("  修复1（默认参数）:")
funcs_fix1 = []
for i in range(5):
    funcs_fix1.append(lambda x=i: x)

print(f"    结果: {[f() for f in funcs_fix1]}")

# ✅ 修复2：工厂函数
print("  修复2（工厂函数）:")
def make_func(n):
    return lambda: n

funcs_fix2 = list(map(make_func, range(5)))
print(f"    结果: {[f() for f in funcs_fix2]}")
print()

# ========== 7. 查看闭包内容 __closure__ ==========
print("=" * 40)
print("7. 查看 __closure__")
print("=" * 40)

def outer_with_params(x, y, z):
    def inner():
        return x + y + z  # 引用 x, y；z 未引用
    return inner

f = outer_with_params(10, 20, 30)
print(f"  闭包变量数量: {len(f.__closure__)}")  # 3（x, y, z）
print(f"  变量值: {[cell.cell_contents for cell in f.__closure__]}")
print()

# ========== 8. 综合示例：平均值计算器 ==========
print("=" * 40)
print("8. 综合示例：平均值计算器")
print("=" * 40)

def make_averager():
    """返回一个函数，每次传入数字，返回当前平均值"""
    total = 0
    count = 0

    def averager(value):
        nonlocal total, count
        total += value
        count += 1
        return total / count

    return averager

avg = make_averager()
print(f"  传入 10 → 平均: {avg(10)}")
print(f"  传入 20 → 平均: {avg(20)}")
print(f"  传入 30 → 平均: {avg(30)}")
print(f"  传入 40 → 平均: {avg(40)}")
