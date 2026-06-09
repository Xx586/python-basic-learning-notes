"""
Demo 2: 作用域
演示：LEGB规则、global/nonlocal、可变对象无需global

运行方式：python 2_scope.py
"""

# ========== 1. 局部变量 vs 全局变量 ==========
global_var = "我是全局变量"

def demo_local_global():
    local_var = "我是局部变量"
    print(f"  函数内 - 局部变量: {local_var}")
    print(f"  函数内 - 全局变量: {global_var}")  # 可以读取

demo_local_global()
print(f"  函数外 - 全局变量: {global_var}")
# print(local_var)  # ❌ NameError: 局部变量在函数外不可见
print()

# ========== 2. LEGB 规则演示 ==========
print("=" * 40)
print("LEGB 规则演示")
print("=" * 40)

x = "G: 全局变量"

def outer():
    x = "E: 外层函数变量"

    def inner():
        x = "L: 内层函数变量"
        print(f"  inner 中的 x: {x}")  # L 优先

    inner()
    print(f"  outer 中的 x: {x}")

outer()
print(f"  全局中的 x: {x}")
print()

# ========== 3. global 关键字 ==========
print("=" * 40)
print("global 关键字")
print("=" * 40)

counter = 0

def increment():
    global counter  # 声明要修改全局变量
    counter += 1
    print(f"  计数器: {counter}")

increment()
increment()
increment()
print(f"  最终计数: {counter}")
print()

# ========== 4. nonlocal 关键字 ==========
print("=" * 40)
print("nonlocal 关键字")
print("=" * 40)

def make_counter():
    count = 0  # 外层函数的局部变量

    def inner():
        nonlocal count  # 声明要修改外层变量
        count += 1
        return count

    return inner

counter_a = make_counter()
counter_b = make_counter()

print(f"  counter_a: {counter_a()}, {counter_a()}, {counter_a()}")
print(f"  counter_b: {counter_b()}, {counter_b()}")  # 独立的
print()

# ========== 5. 可变对象不需要 global ==========
print("=" * 40)
print("可变对象无需 global")
print("=" * 40)

scores = [90, 85, 78]

def add_score(score):
    # 修改列表内容，不是重新赋值变量，所以不需要 global
    scores.append(score)
    print(f"  添加 {score} 后: {scores}")

add_score(95)
add_score(100)
print(f"  最终 scores: {scores}")

# 但是重新赋值整个变量就需要 global
def reset_scores():
    global scores
    scores = []
    print(f"  重置后: {scores}")

reset_scores()
print(f"  全局 scores: {scores}")
print()

# ========== 6. 踩坑：函数内先读后写 ==========
print("=" * 40)
print("踩坑：先读后写全局变量")
print("=" * 40)

name = "张三"

def read_name():
    # 只读取，没问题
    print(f"  读取 name: {name}")

read_name()

def try_change():
    global name  # 必须有这行，否则下一行会报 UnboundLocalError
    print(f"  修改前 name: {name}")
    name = "李四"
    print(f"  修改后 name: {name}")

try_change()
print(f"  全局 name: {name}")
