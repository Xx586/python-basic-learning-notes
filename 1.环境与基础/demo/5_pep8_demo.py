# -*- coding: utf-8 -*-
"""
Demo 5: PEP 8 编码规范演示

本 Demo 演示：
  1. PEP 8 核心规则的正确写法（缩进、命名、空格、空行）
  2. 常见违规写法和正确写法的对比
  3. 各命名风格（snake_case、PascalCase、UPPER_CASE）的使用场景
  4. 导入语句的正确排序方式

运行方式：
  python3 demo/5_pep8_demo.py

学习建议：
  边读代码边观察规范细节，培养"代码洁癖"。
"""

import math
import os
import sys
from datetime import datetime


# ============================================================
# Part 1: 缩进规范 —— 4 个空格
# ============================================================
print("=" * 55)
print("Part 1: 缩进规范 — 使用 4 个空格")
print("=" * 55)


def demonstrate_indentation():
    """演示正确的缩进方式。"""
    print("正确的缩进示例：")

    # 每个缩进层级 = 4 个空格
    for i in range(3):
        if i % 2 == 0:
            print(f"  层级 2 缩进 (8 空格): i = {i}")
        else:
            print(f"  层级 2 缩进 (8 空格): i = {i} 是奇数")

    print("\n规则：")
    print("  - 永远使用 4 个空格缩进")
    print("  - 不要混用 Tab 和空格（Python 3 会报错）")
    print("  - IDE 设置: 按 Tab 键时插入 4 个空格")


demonstrate_indentation()

# ---- 违规 vs 正确对比 ----
print("\n违规示例（不要这样写）：")
print("""
# 2 个空格缩进（错误，某些语言允许但 PEP 8 不允许）
if True:
  print("2 空格缩进")  # 不规范
""")

print("正确示例：")
print("""
# 4 个空格缩进（正确）
if True:
    print("4 空格缩进")  # 规范
""")


# ============================================================
# Part 2: 命名规范
# ============================================================
print("=" * 55)
print("Part 2: 命名规范")
print("=" * 55)


# ---- 常量: UPPER_SNAKE_CASE ----
MAX_CONNECTIONS = 100
DEFAULT_TIMEOUT = 30  # 秒
DATABASE_URL = "localhost:5432"
PI = math.pi

print("常量命名 (UPPER_SNAKE_CASE):")
print(f"  MAX_CONNECTIONS = {MAX_CONNECTIONS}")
print(f"  DEFAULT_TIMEOUT = {DEFAULT_TIMEOUT}")
print(f"  PI = {PI:.5f}")


# ---- 变量和函数: snake_case ----
def get_user_full_name(first_name, last_name):
    """
    拼接用户全名。

    Args:
        first_name: 名
        last_name: 姓

    Returns:
        全名字符串
    """
    return f"{last_name}{first_name}"


def calculate_average_score(scores):
    """计算平均分。"""
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


user_name = "小明"
user_age = 25
total_students = 42
average_score = 86.5

print(f"\n变量/函数命名 (snake_case):")
print(f"  user_name = '{user_name}'")
print(f"  user_age = {user_age}")
print(f"  get_user_full_name('三', '张') = '{get_user_full_name('三', '张')}'")
print(f"  calculate_average_score([80,90,85]) = {calculate_average_score([80, 90, 85])}")


# ---- 类名: PascalCase ----
class StudentRecord:
    """学生档案类。"""
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


class HttpRequestHandler:
    """HTTP 请求处理类。"""
    pass


class XMLParser:
    """XML 解析类。"""
    pass


print(f"\n类命名 (PascalCase):")
print(f"  StudentRecord")
print(f"  HttpRequestHandler")
print(f"  XMLParser")

student = StudentRecord("小红", "三年级")
print(f"  实例化: StudentRecord('小红', '三年级') -> name={student.name}")


# ---- 私有属性: _单下划线前缀 ----
class BankAccount:
    """银行账户类 —— 演示命名约定。"""

    def __init__(self, owner, balance):
        self.owner = owner              # 公开属性
        self._balance = balance         # 受保护属性（约定：外部不要直接访问）
        self.__pin = "1234"             # 私有属性（名称改写为 _BankAccount__pin）

    def get_balance(self):
        """公开方法：获取余额。"""
        return self._balance

    def _validate_amount(self, amount):
        """内部方法：校验金额是否合法（外部不应调用）。"""
        return amount > 0


account = BankAccount("张三", 1000.00)
print(f"\n访问控制演示:")
print(f"  公开属性: account.owner = '{account.owner}'")
print(f"  受保护属性: account._balance = {account._balance} (约定不直接访问)")
print(f"  公开方法: account.get_balance() = {account.get_balance()}")


# ============================================================
# Part 3: 空行规范
# ============================================================
print("\n" + "=" * 55)
print("Part 3: 空行规范")
print("=" * 55)

print("""
PEP 8 空行规则（请阅读源码验证）：

  顶层函数和类定义之间: 2 个空行
  类内部方法之间:       1 个空行
  函数内部逻辑分组之间:  1 个空行

  具体示例：观察本文件中的空行数量。
  - 每个顶层 def 之间都是 2 个空行
  - 类内部的 def 之间是 1 个空行
""")


def top_level_function_one():
    """顶层函数一。（和 top_level_function_two 之间有 2 个空行）"""
    pass


def top_level_function_two():
    """顶层函数二。"""
    pass


class ExampleClass:

    def method_one(self):
        """方法一。（和 method_two 之间有 1 个空行）"""
        pass

    def method_two(self):
        """方法二。"""
        pass


# ============================================================
# Part 4: 空格规范
# ============================================================
print("=" * 55)
print("Part 4: 运算符和逗号周围的空格")
print("=" * 55)

# ---- 运算符两侧各一个空格 ----
a, b, c = 10, 20, 30
result = a + b * c          # 正确：运算符两侧有空格
print(f"运算符空格: {a} + {b} * {c} = {result}")

# ---- 逗号后面加空格 ----
fruits = ["苹果", "香蕉", "橙子"]          # 正确
coordinates = {"x": 100, "y": 200}         # 正确
print(f"水果列表: {fruits}")
print(f"坐标: {coordinates}")

# ---- 函数默认参数：等号不加空格 ----
def greet(name, greeting="你好"):
    return f"{greeting}, {name}!"

print(f"函数参数空格: greet('小明') = '{greet('小明')}'")

# ---- 切片：冒号两侧不留多余空格 ----
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"切片: numbers[2:5] = {numbers[2:5]}")


# ---- 违规 vs 正确对比 ----
print("\n--- 空格违规 vs 正确对比 ---")
print("""
违规写法                    正确写法
─────────────────────────   ─────────────────────────
result=a+b*c                result = a + b * c
names=["张三","李四"]       names = ["张三", "李四"]
def func(param = 1):        def func(param=1):
spam( ham[ 1 ], { eg:2 })   spam(ham[1], {eg: 2})
x             = 1           x = 1
""")


# ============================================================
# Part 5: 导入规范
# ============================================================
print("=" * 55)
print("Part 5: 导入语句规范")
print("=" * 55)

print("""
导入语句应放在文件顶部，按以下顺序分组：

  1. 标准库导入（Python 自带）
  2. 第三方库导入（pip 安装的）
  3. 本地模块导入（你自己写的）

每组之间空一行，组内按字母顺序排序。

本文件的导入就是正确示例（请查看文件头部）：

  import math          # 标准库
  import os            # 标准库
  import sys           # 标准库
  from datetime import datetime  # 标准库

  # 第三方库（如果有）放在这里

  # 本地模块（如果有）放在这里
""")


# ============================================================
# Part 6: 行长度和换行
# ============================================================
print("=" * 55)
print("Part 6: 行长度和换行")
print("=" * 55)

print("""
PEP 8 建议每行不超过 79 个字符。

长代码的换行方式：

1. 使用括号（推荐）：
   long_result = (
       some_function(param1, param2, param3)
       + another_function(param4)
   )

2. 字符串拼接换行：
   message = (
       "这是一个很长的消息，"
       "用小括号拼接比用反斜杠更优雅，"
       "Python 会自动合并相邻的字符串字面量。"
   )

3. 函数参数过长时的换行：
   def function_with_many_params(
       parameter_one,
       parameter_two,
       parameter_three,
       parameter_four,
   ):
       pass
""")


# ============================================================
# Part 7: 综合演示 —— 一个符合 PEP 8 的完整类
# ============================================================
print("=" * 55)
print("Part 7: 综合演示 — 符合 PEP 8 的完整类")
print("=" * 55)


class BookInventory:
    """
    图书库存管理类 —— PEP 8 规范的完整演示。

    这个类展示了正确的命名、缩进、空行、docstring 和空格用法。

    Attributes:
        books (dict): 图书信息，键为书名，值为 (作者, 库存量) 元组
    """

    MAX_BOOKS_PER_TYPE = 999  # 常量：UPPER_SNAKE_CASE

    def __init__(self):
        """初始化一个空的图书库存。"""
        self.books = {}
        self._total_sold = 0  # 受保护属性：单下划线

    def add_book(self, title, author, quantity):
        """
        添加书籍到库存。

        Args:
            title (str): 书名
            author (str): 作者
            quantity (int): 入库数量
        """
        if title in self.books:
            _, current_qty = self.books[title]
            self.books[title] = (author, current_qty + quantity)
        else:
            self.books[title] = (author, quantity)

    def sell_book(self, title, quantity):
        """
        售出图书。

        Args:
            title (str): 书名
            quantity (int): 售出数量

        Returns:
            bool: 交易是否成功

        Raises:
            ValueError: 库存不足时抛出
        """
        if title not in self.books:
            raise ValueError(f"书籍 '{title}' 不在库存中")

        author, stock = self.books[title]
        if stock < quantity:
            raise ValueError(f"库存不足: 需要 {quantity} 本, 仅有 {stock} 本")

        self.books[title] = (author, stock - quantity)
        self._total_sold += quantity
        return True

    def get_total_stock(self):
        """
        获取总库存量。

        Returns:
            int: 所有图书的库存数量之和
        """
        return sum(stock for _, stock in self.books.values())


# --- 使用演示 ---
inventory = BookInventory()
inventory.add_book("Python 编程", "Guido", 50)
inventory.add_book("算法导论", "CLRS", 30)
inventory.add_book("Python 编程", "Guido", 20)  # 补充库存

print(f"当前库存: {inventory.books}")
print(f"总库存量: {inventory.get_total_stock()} 本")

try:
    inventory.sell_book("Python 编程", 5)
    print(f"售出 5 本 'Python 编程'，剩余库存: {inventory.get_total_stock()} 本")
except ValueError as e:
    print(f"交易失败: {e}")


# ============================================================
# Part 8: 常见违规总结
# ============================================================
print("\n" + "=" * 55)
print("Part 8: 常见 PEP 8 违规清单")
print("=" * 55)

print("""
新手最常犯的 5 个 PEP 8 违规：

1. 混用 Tab 和空格缩进
   -> 设置 IDE: Tab 键 = 4 个空格

2. 变量名用 PascalCase 或拼音
   -> 变量/函数: snake_case, 类: PascalCase, 常量: UPPER_CASE

3. 运算符周围没有空格
   -> x = a + b 而不是 x=a+b

4. 导入语句混乱
   -> 标准库 -> 第三方库 -> 本地模块, 组间空一行

5. 行太长不换行
   -> 每行不超过 79 字符, 用括号优雅换行

工具推荐:
  - flake8: 静态检查 PEP 8 违规
  - black: 自动格式化为标准风格
  - isort: 自动排序导入语句
""")


print("=" * 55)
print("Demo 5 演示完成！")
print("你已经掌握了 Python 环境配置和编码规范的基础知识。")
print("接下来可以进入第 2 阶段: 数据类型与运算符。")
print("=" * 55)
