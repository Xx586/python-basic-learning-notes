# -*- coding: utf-8 -*-
"""
Demo 4: 代码注释风格演示

本 Demo 演示：
  1. 单行注释的正确用法
  2. 多行注释（三个引号）的使用场景
  3. 文档字符串（docstring）为模块、类、函数写说明
  4. TODO / FIXME / HACK 标记的用法
  5. 好注释 vs 坏注释的对比

运行方式：
  python3 demo/4_comment_style.py
"""

# ============================================================
# Part 1: 单行注释
# ============================================================
print("=" * 55)
print("Part 1: 单行注释（# 开头）")
print("=" * 55)

# 这是标准的单行注释：解释"为什么"要这样设置
# 这里的 0.08 是公司的标准税率，2024 年 1 月起调整为 0.1
TAX_RATE = 0.1
print(f"当前税率: {TAX_RATE * 100}%")

# TODO: 2024 Q3 需要对接新的税务系统 API
# FIXME: 当金额超过 1 亿时精度丢失，需要用 Decimal 类型
# HACK: 临时方案，等后端金额校验接口就绪后替换
amount = 150000.50
tax = amount * TAX_RATE
print(f"金额: {amount:.2f}, 税额: {tax:.2f}")

# 行内注释：放在代码右侧
user_name = "张三"  # 从数据库中查询的用户名
print(f"当前用户: {user_name}")


# ============================================================
# Part 2: 多行注释（用三个引号）
# ============================================================
print("\n" + "=" * 55)
print("Part 2: 多行注释 / 文档字符串")
print("=" * 55)

"""
这是多行注释（严格来说是未被引用的多行字符串）。
Python 解释器会忽略不被赋值的字符串字面量。

适用场景：
  - 文件/模块开头的概述说明
  - 临时代码块说明
  - 大段的功能描述

注意：如果放在函数/类的第一行，它就是 docstring，
      可通过 help() 查看，而不是简单的注释。
"""


# ---- 2.1 模块级 docstring ----
# 本文件开头的 """ ... """ 就是模块级 docstring
# 可以通过 __doc__ 属性访问
print("模块 docstring 预览（前 80 字符）：")
print(__doc__[:80] + "...")


# ---- 2.2 函数 docstring ----
def calculate_discount(price, discount_rate):
    """
    计算折扣后的价格。

    这个函数用于电商平台的优惠计算。
    支持百分比折扣，折扣率范围 [0, 1]。

    Args:
        price (float): 原价（单位：元）
        discount_rate (float): 折扣率，如 0.2 表示打 8 折

    Returns:
        float: 折扣后的价格，保留 2 位小数

    Raises:
        ValueError: 折扣率不在 [0, 1] 范围内

    Example:
        >>> calculate_discount(100, 0.2)
        80.0
        >>> calculate_discount(50, 0.15)
        42.5
    """
    if not 0 <= discount_rate <= 1:
        raise ValueError("折扣率必须在 0 到 1 之间")
    final_price = price * (1 - discount_rate)
    return round(final_price, 2)


# 测试折扣计算
original_price = 299.99
discount = 0.3  # 7 折
final = calculate_discount(original_price, discount)
print(f"\n折扣计算: 原价 {original_price} 元, 打 {(1 - discount) * 10:.0f} 折 -> {final} 元")


# ---- 2.3 类 docstring ----
class ShoppingCart:
    """
    购物车类 —— 管理用户的购物车。

    支持添加商品、移除商品、计算总价。
    所有价格单位为人民币（元）。

    Attributes:
        items (list): 商品列表，每个元素为 (商品名, 单价, 数量) 元组
        created_at (str): 购物车创建时间
    """

    def __init__(self):
        """初始化一个空的购物车。"""
        from datetime import datetime
        self.items = []
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"  购物车已创建，时间: {self.created_at}")

    def add_item(self, name, price, quantity=1):
        """
        向购物车中添加商品。

        Args:
            name (str): 商品名称
            price (float): 商品单价
            quantity (int): 购买数量，默认 1
        """
        self.items.append((name, price, quantity))
        print(f"  已添加: {name} x{quantity} (单价: {price} 元)")

    def get_total(self):
        """
        计算购物车中所有商品的总价。

        Returns:
            float: 总价（元）
        """
        total = sum(price * qty for _, price, qty in self.items)
        return round(total, 2)


# 使用购物车
print("\n购物车演示：")
cart = ShoppingCart()
cart.add_item("Python 编程书", 79.00, 1)
cart.add_item("机械键盘", 349.00, 1)
cart.add_item("鼠标垫", 29.90, 2)
print(f"  购物车总价: {cart.get_total()} 元")


# ============================================================
# Part 3: 好注释 vs 坏注释
# ============================================================
print("\n" + "=" * 55)
print("Part 3: 好注释 vs 坏注释")
print("=" * 55)


# ---- 坏注释示例 ----
# 这些注释是"废话"——重复了代码本身已经表达的内容
print("\n--- 坏注释示例 ---")

# 设置 x 为 10
x = 10
# 循环 5 次
for i in range(5):
    # 把 x 加上 i
    x += i
# 打印 x
print(f"  x 的最终值: {x}")


# ---- 好注释示例 ----
# 解释"为什么"，而不是"做了什么"
print("\n--- 好注释示例 ---")

# 从配置中心读取的缓冲池大小，过小会导致频繁重组，过大会浪费内存
BUFFER_POOL_SIZE = 10

# 模拟接受到的数据包，最后一个元素是校验和，不参与计算
data_packets = [1.5, 2.3, 4.1, 0]

# 只累加有效数据（排除校验位）
# 验证条件：需求文档 v3.2 规定校验位固定为 0
valid_data = data_packets[:-1]  # 排除最后一个元素
total = sum(valid_data)
print(f"  有效数据包: {valid_data}, 总和: {total}")

# 输出时做阈值判断 —— 产品要求超过缓冲池 80% 时发告警
if total > BUFFER_POOL_SIZE * 0.8:
    print(f"  [告警] 数据量接近缓冲池上限 ({(total / BUFFER_POOL_SIZE) * 100:.0f}%)")


# ============================================================
# Part 4: TODO / FIXME / HACK 标记
# ============================================================
print("\n" + "=" * 55)
print("Part 4: 注释标记（TODO / FIXME / HACK）")
print("=" * 55)

print("""
常用注释标记及其含义：

  TODO:   计划未来做的事情
  FIXME:  已知有 bug，需要修复
  HACK:   临时方案，不够优雅，需要重构
  NOTE:   重要说明，提醒读者注意
  XXX:    有问题的代码，需要关注
  OPTIMIZE: 性能优化点

IDE（如 PyCharm、VS Code）会自动识别这些标记，
并在专门的窗口中列出所有标记，方便跟踪。
""")

# 模拟一个有待改进的函数
def process_user_data(raw_data):
    """
    处理用户原始数据并返回清洗后的结果。
    """
    # TODO: 添加数据格式校验（支持 JSON 和 XML）
    # FIXME: 当 raw_data 为 None 时会崩溃，需要加上空值检查
    # HACK: 暂时用 str() 转换，之后应该用专门的序列化库

    if raw_data is None:
        print("  [处理] 收到空数据，跳过处理")
        return None

    print(f"  [处理] 正在处理: {raw_data}")

    # NOTE: 生产环境中应该记录日志而不是用 print
    # OPTIMIZE: 大量数据时这里可能需要异步处理
    result = str(raw_data).strip().upper()
    print(f"  [处理] 结果: {result}")
    return result


# 测试
process_user_data("  hello, world  ")
process_user_data(None)


# ============================================================
# Part 5: 查看 docstring
# ============================================================
print("\n" + "=" * 55)
print("Part 5: 如何查看 docstring")
print("=" * 55)

print("""
有 3 种方式可以查看函数/类的 docstring：

方法 1: 使用 help() 函数（在终端中会进入交互模式）
  >>> help(calculate_discount)

方法 2: 使用 .__doc__ 属性
  >>> print(calculate_discount.__doc__)

方法 3: 在 IDE 中将鼠标悬停在函数名上
  （PyCharm 和 VS Code 都支持悬停查看文档）

下面演示方法 2：
""")

print("calculate_discount 函数的 docstring：")
print(calculate_discount.__doc__)


print("\n" + "=" * 55)
print("Demo 4 演示完成！")
print("接下来请学习 Demo 5: PEP 8 编码规范")
print("=" * 55)
