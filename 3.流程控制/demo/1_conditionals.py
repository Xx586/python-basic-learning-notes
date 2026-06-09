"""
Demo 1: 条件判断
演示：if/elif/else、三元表达式、match-case（Python 3.10+）、真值测试

运行方式：python 1_conditionals.py
"""

# ========== 1. if / elif / else ==========
print("=" * 50)
print("1. if / elif / else 基本用法")
print("=" * 50)

score = 85

if score >= 90:
    grade = "优秀"
elif score >= 80:
    grade = "良好"
elif score >= 70:
    grade = "中等"
elif score >= 60:
    grade = "及格"
else:
    grade = "不及格"

print(f"分数：{score} → 等级：{grade}")  # 分数：85 → 等级：良好


# ========== 2. 嵌套 if ==========
print("\n" + "=" * 50)
print("2. 嵌套 if 判断")
print("=" * 50)

has_ticket = True
age = 8

if has_ticket:
    print("有票，准备进场")
    if age < 12:
        price = "免费"
    elif age < 18:
        price = "半价"
    else:
        price = "全价"
    print(f"年龄 {age} 岁，票价：{price}")
else:
    print("请先购票")


# ========== 3. 三元表达式 ==========
print("\n" + "=" * 50)
print("3. 三元表达式（条件表达式）")
print("=" * 50)

# 基本用法
a, b = 10, 20
max_val = a if a > b else b
print(f"a={a}, b={b}，较大值是：{max_val}")  # 20

# 用于字符串
username = "admin"
status = "在线" if username else "游客"
print(f"用户状态：{status}")

# 与列表结合
nums = [1, 2, 3, 4, 5]
label = "偶数个" if len(nums) % 2 == 0 else "奇数个"
print(f"列表 {nums} 有 {label} 元素")


# ========== 4. match-case（Python 3.10+） ==========
print("\n" + "=" * 50)
print("4. match-case 结构模式匹配")
print("=" * 50)

# 4.1 匹配具体值
def handle_status(code):
    match code:
        case 200:
            return "请求成功"
        case 301 | 302:
            return "重定向"
        case 404:
            return "页面未找到"
        case 500:
            return "服务器内部错误"
        case _:
            return f"未知状态码：{code}"

print(f"200 → {handle_status(200)}")
print(f"301 → {handle_status(301)}")
print(f"404 → {handle_status(404)}")
print(f"999 → {handle_status(999)}")

# 4.2 匹配数据类型
print("\n--- 匹配数据类型 ---")

def describe(value):
    match value:
        case int():
            return f"整数：{value}"
        case str():
            return f"字符串：'{value}'（长度 {len(value)}）"
        case list():
            return f"列表，包含 {len(value)} 个元素"
        case dict():
            return f"字典，键：{list(value.keys())}"
        case _:
            return "未知类型"

print(describe(42))
print(describe("hello"))
print(describe([1, 2, 3]))
print(describe({"a": 1, "b": 2}))

# 4.3 解构匹配
print("\n--- 解构匹配坐标点 ---")

def locate(point):
    match point:
        case (0, 0):
            return "原点"
        case (0, y):
            return f"Y 轴上，y = {y}"
        case (x, 0):
            return f"X 轴上，x = {x}"
        case (x, y):
            return f"坐标点：({x}, {y})"

print(locate((0, 0)))   # 原点
print(locate((0, 5)))   # Y 轴上，y = 5
print(locate((3, 0)))   # X 轴上，x = 3
print(locate((3, 4)))   # 坐标点：(3, 4)


# ========== 5. 真值测试 ==========
print("\n" + "=" * 50)
print("5. 真值测试（Truthy / Falsy）")
print("=" * 50)

def check_truthy(value):
    """判断一个值的真假并打印"""
    if value:
        print(f"  {repr(value):20s} → True (真值)")
    else:
        print(f"  {repr(value):20s} → False (假值)")

print("常见假值：")
check_truthy(False)
check_truthy(None)
check_truthy(0)
check_truthy(0.0)
check_truthy("")         # 空字符串
check_truthy([])         # 空列表
check_truthy({})         # 空字典
check_truthy(set())      # 空集合

print("\n常见真值：")
check_truthy(True)
check_truthy(1)
check_truthy(-1)
check_truthy(" ")        # 含空格的字符串（非空）
check_truthy([0])        # 非空列表
check_truthy({"a": 0})   # 非空字典

# 实际应用：优雅检查非空
print("\n实际应用：")
items = []
if items:
    print("有数据")
else:
    print("列表为空")

username = ""
if not username:  # 利用 falsy 检查空输入
    print("用户名不能为空")


print("\n" + "=" * 50)
print("Demo 1 运行完毕")
print("=" * 50)
