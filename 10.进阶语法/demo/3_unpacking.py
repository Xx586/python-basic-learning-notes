"""
演示各种解包操作

本文件展示 Python 解包操作的多种应用：
- 序列解包：列表/元组/字符串
- 星号解包：* 在赋值、函数调用、字面量中
- 字典解包：** 合并和覆盖
- 函数参数：*args / **kwargs
- 实际场景：交换变量、拆分路径、配置合并

可以独立运行，用 = 分隔线和 print 明确展示输出。
"""


# ============================================================================
# 一、序列解包基础
# ============================================================================
print("=" * 60)
print("一、序列解包基础")
print("=" * 60)

# 列表解包
a, b, c = [1, 2, 3]
print(f"列表解包: a={a}, b={b}, c={c}")

# 元组解包（括号可省略）
x, y = (10, 20)
p, q = 30, 40  # 等价
print(f"元组解包: x={x}, y={y}")
print(f"省略括号: p={p}, q={q}")

# 字符串解包
ch1, ch2, ch3 = "ABC"
print(f"字符串解包: ch1='{ch1}', ch2='{ch2}', ch3='{ch3}'")

# 变量的数量必须匹配序列长度
# a, b = [1, 2, 3]  # ValueError: too many values to unpack

# 迭代中的解包
print("\n[enumerate 解包]:")
for i, val in enumerate(["apple", "banana", "cherry"]):
    print(f"  [{i}] {val}")

# 字典迭代解包
print("\n[字典 items() 解包]:")
d = {"name": "Alice", "age": 25, "city": "NY"}
for key, value in d.items():
    print(f"  {key} = {value}")


# ============================================================================
# 二、交换变量（一行搞定，无需临时变量）
# ============================================================================
print("\n" + "=" * 60)
print("二、交换变量（一行搞定）")
print("=" * 60)

a, b = 10, 20
print(f"交换前: a={a}, b={b}")

a, b = b, a  # Python 一行交换
print(f"交换后: a={a}, b={b}")

# 原理：右侧先打包成元组 (20, 10)，再解包赋值给左侧
# 等价于: temp = (b, a); a, b = temp


# ============================================================================
# 三、星号解包 *（核心功能）
# ============================================================================
print("\n" + "=" * 60)
print("三、星号解包 *")
print("=" * 60)

numbers = [1, 2, 3, 4, 5]

# 在开头：吸收后面的元素
first, *rest = numbers
print(f"在开头: first={first}, rest={rest}")

# 在结尾（最常用）：吸收前面的元素
*head, last = numbers
print(f"在结尾: head={head}, last={last}")

# 在中间
first, *middle, last = numbers
print(f"在中间: first={first}, middle={middle}, last={last}")

# 丢弃不需要的值（约定用 _ 或 *_）
a, *_ = numbers
print(f"\n丢弃剩余: a={a}, _={_}")  # a=1, _=[2, 3, 4, 5]

first, *_, last = numbers
print(f"取首尾: first={first}, last={last}")  # first=1, last=5

# 吸收不到元素时返回空列表
single = [42]
first, *rest = single
print(f"\n单元素解包: first={first}, rest={rest}")  # first=42, rest=[]

# 必须确保非星号变量有值可取
# a, *b, c = [1]  # ValueError: not enough values to unpack


# ============================================================================
# 四、字典解包 **
# ============================================================================
print("\n" + "=" * 60)
print("四、字典解包 **")
print("=" * 60)

d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}
d3 = {"b": 999, "e": 5}  # b 和 d1 重复

# 合并字典
merged = {**d1, **d2}
print(f"合并 d1 + d2: {merged}")  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# 后者覆盖前者（b 被覆盖）
merged_override = {**d1, **d3}
print(f"覆盖 (d1 + d3): {merged_override}")  # {'a': 1, 'b': 999, 'e': 5}

# 添加/覆盖单个键（非常实用的模式）
config = {"host": "localhost", "port": 8080}
new_config = {**config, "port": 9090, "debug": True}
print(f"添加/覆盖键: {new_config}")

# ** 只能用于 mapping 类型
# {**[(1, 2)]}  # TypeError!


# ============================================================================
# 五、函数参数中的解包
# ============================================================================
print("\n" + "=" * 60)
print("五、函数参数中的解包")
print("=" * 60)

# --- 定义时打包 ---
print("\n[5.1] 定义时打包（*args, **kwargs）:")

def show_args(*args):
    """接收任意数量位置参数，打包成元组"""
    print(f"  *args 类型: {type(args)}, 内容: {args}")

show_args(1, 2, 3)  # args = (1, 2, 3)
show_args("a", "b")  # args = ('a', 'b')

def show_kwargs(**kwargs):
    """接收任意数量关键字参数，打包成字典"""
    print(f"  **kwargs 类型: {type(kwargs)}, 内容: {kwargs}")

show_kwargs(name="Alice", age=25)  # kwargs = {'name': 'Alice', 'age': 25}

# 组合使用
def full_demo(a, b, *args, **kwargs):
    print(f"  必选: a={a}, b={b}")
    print(f"  多余位置: args={args}")
    print(f"  多余关键字: kwargs={kwargs}")

print("\n[5.2] 组合 *args 和 **kwargs:")
full_demo(1, 2, 3, 4, 5, x=10, y=20)
# a=1, b=2, args=(3, 4, 5), kwargs={'x':10, 'y':20}

# --- 调用时解包 ---
print("\n[5.3] 调用时解包:")

def add_three(a, b, c):
    return a + b + c

nums = [1, 2, 3]
result = add_three(*nums)  # 展开列表成位置参数
print(f"  add_three(*{nums}) = {result}")  # 6

params = {"a": 10, "b": 20, "c": 30}
result2 = add_three(**params)  # 展开字典成关键字参数
print(f"  add_three(**{params}) = {result2}")  # 60

# 函数调用转发模式
def wrapper(*args, **kwargs):
    """通用转发器"""
    print(f"  转发: args={args}, kwargs={kwargs}")
    return add_three(*args, **kwargs)

result3 = wrapper(5, 5, 5)
print(f"  wrapper 结果: {result3}")


# ============================================================================
# 六、字面量中的解包
# ============================================================================
print("\n" + "=" * 60)
print("六、字面量中的解包（Python 3.5+）")
print("=" * 60)

# 列表字面量中解包
list1 = [1, 2]
list2 = [3, 4]
combined_list = [*list1, *list2, 5, 6]
print(f"列表合并: [*{list1}, *{list2}, 5, 6] = {combined_list}")

# 元组字面量中解包
t1 = (1, 2)
t2 = (3, 4)
combined_tuple = (*t1, *t2, 5)
print(f"元组合并: (*{t1}, *{t2}, 5) = {combined_tuple}")

# 集合字面量中解包
s1 = {1, 2, 3}
s2 = {3, 4, 5}  # 3 是重复的
combined_set = {*s1, *s2}
print(f"集合并集: {{*{s1}, *{s2}}} = {combined_set}")  # {1, 2, 3, 4, 5}（去重）


# ============================================================================
# 七、实际场景
# ============================================================================
print("\n" + "=" * 60)
print("七、实际应用场景")
print("=" * 60)

# 场景1：拆分路径
print("\n[场景1] 拆分路径:")
path = "/home/user/projects/python/main.py"
*dirs, filename = path.split("/")
print(f"  目录部分: {dirs}")
print(f"  文件名:   {filename}")

# 场景2：配置合并（多优先级）
print("\n[场景2] 配置合并（多优先级）:")
defaults = {"host": "0.0.0.0", "port": 80, "debug": False, "cache": True}
env_config = {"port": 8080, "debug": True}
user_config = {"host": "myapp.com"}

# 优先级: user_config > env_config > defaults
final = {**defaults, **env_config, **user_config}
print(f"  最终配置: {final}")

# 场景3：函数参数转发
print("\n[场景3] 函数参数转发:")
def original(a, b, c):
    return f"{a}-{b}-{c}"

def log_and_call(func):
    """装饰器：打印参数并转发调用"""
    def wrapper(*args, **kwargs):
        print(f"  调用 {func.__name__}, args={args}, kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper

logged = log_and_call(original)
print(f"  结果: {logged(1, 2, 3)}")

# 场景4：数据分离
print("\n[场景4] CSV 数据处理:")
records = [
    "Alice,25,Engineer",
    "Bob,30,Designer",
    "Charlie,35,Manager",
]
for record in records:
    name, age, job = record.split(",")
    print(f"  姓名: {name:<8} 年龄: {age:<3} 职业: {job}")

# 场景5：多个列表的笛卡尔积辅助
print("\n[场景5] 列表展平收集:")
# 收集多个来源的元素
source_a = [1, 2, 3]
source_b = [4, 5]
source_c = [6, 7, 8, 9]
all_items = [*source_a, *source_b, *source_c]
print(f"  展平合并: {all_items}")


# ============================================================================
# 八、踩坑演示
# ============================================================================
print("\n" + "=" * 60)
print("八、常见踩坑演示")
print("=" * 60)

# 坑1：** 解包非 dict 对象
print("\n[坑1] ** 只能解包 mapping:")
try:
    lst = [("a", 1), ("b", 2)]
    # {**lst}  # TypeError!
    # 正确做法：
    result = {**dict(lst)}
    print(f"  正确: dict() 转后解包: {result}")
except Exception as e:
    print(f"  错误: {e}")

# 坑2：函数参数顺序
print("\n[坑2] 参数定义顺序:")
# 正确顺序: 必选参数, *args, 关键字参数, **kwargs
def correct_order(a, b, *args, c=10, **kwargs):
    print(f"  a={a}, b={b}, args={args}, c={c}, kwargs={kwargs}")

correct_order(1, 2, 3, 4, c=99, x=100)
# a=1, b=2, args=(3, 4), c=99, kwargs={'x': 100}

# 坑3：字典解包是浅合并
print("\n[坑3] 字典解包是浅合并:")
d1 = {"db": {"host": "old", "port": 1}}
d2 = {"db": {"port": 2}}
merged = {**d1, **d2}
print(f"  浅合并结果: {merged}")
print(f"  注意: host 丢失了！深合并需要手动处理")


print("\n" + "=" * 60)
print("全部演示完成！")
print("=" * 60)
