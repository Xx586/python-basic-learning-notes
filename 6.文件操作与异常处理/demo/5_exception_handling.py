"""
Demo 5: 异常处理
演示：try/except/else/finally、常见异常类型、raise 主动抛出、自定义异常、assert 断言

运行方式：python 5_exception_handling.py
"""

import traceback

# ========== 1. 基本 try/except ==========
print("=" * 40)
print("1. 基本 try/except")
print("=" * 40)

# 场景：用户输入可能不是数字
# 在这里直接模拟（避免需要在终端交互）
test_inputs = ["42", "abc", "100"]

for user_input in test_inputs:
    try:
        num = int(user_input)
        print(f"  '{user_input}' → {num} ✓")
    except ValueError:
        print(f"  '{user_input}' → ValueError：无法转为整数")

# ========== 2. 捕获多个异常 ==========
print("\n" + "=" * 40)
print("2. 捕获多个异常（多 except 分支）")
print("=" * 40)


def safe_operation(data, idx_a, idx_b):
    """演示：不同异常用不同分支处理"""
    try:
        a = data[idx_a]
        b = data[idx_b]
        result = a / b
    except IndexError:
        print(f"  IndexError: 索引越界！列表长度={len(data)}")
    except ZeroDivisionError:
        print(f"  ZeroDivisionError: 除数不能为 0")
    except TypeError as e:
        print(f"  TypeError: {e}")
    else:
        print(f"  ✓ {a} / {b} = {result}")
    finally:
        print(f"  [finally] 本次计算结束")


data = [10, 5, 0]

print("测试1: data[0]/data[1] → 10/5")
safe_operation(data, 0, 1)   # 10/5 → 正常

print("\n测试2: data[0]/data[2] → 10/0")
safe_operation(data, 0, 2)   # 10/0 → 除零错误

print("\n测试3: data[0]/data[10] → 索引越界")
safe_operation(data, 0, 10)  # 索引越界

# ========== 3. 常见异常类型一览 ==========
print("\n" + "=" * 40)
print("3. 常见异常类型演示")
print("=" * 40)

exceptions_demo = [
    ("ValueError",         lambda: int('abc')),
    ("TypeError",          lambda: 'hello' + 5),
    ("KeyError",           lambda: {}['missing_key']),
    ("IndexError",         lambda: [1, 2][10]),
    ("ZeroDivisionError",  lambda: 1 / 0),
    ("AttributeError",     lambda: 'abc'.not_a_method()),
    ("FileNotFoundError",  lambda: open('_no_such_file_42.txt')),
]

for name, func in exceptions_demo:
    try:
        func()
    except Exception as e:
        print(f"  {name:<20}: {e}")

# ========== 4. raise 主动抛出异常 ==========
print("\n" + "=" * 40)
print("4. raise 主动抛出异常")
print("=" * 40)


def set_age(age):
    """校验年龄，不合法时抛出异常"""
    if age < 0:
        raise ValueError(f"年龄不能为负数，传入: {age}")
    if age > 150:
        raise ValueError(f"年龄不能超过150，传入: {age}")
    return age


test_ages = [25, -5, 200]
for age in test_ages:
    try:
        result = set_age(age)
        print(f"  ✓ 年龄 {result} 合法")
    except ValueError as e:
        print(f"  ✗ {e}")

# ========== 5. 自定义异常类 ==========
print("\n" + "=" * 40)
print("5. 自定义异常类")
print("=" * 40)


# 定义异常层级
class PaymentError(Exception):
    """支付异常基类"""
    pass


class InsufficientBalanceError(PaymentError):
    """余额不足"""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.shortfall = amount - balance
        super().__init__(
            f"余额不足：余额 {balance} 元，需要 {amount} 元，差额 {self.shortfall} 元"
        )


class InvalidAmountError(PaymentError):
    """金额无效"""
    def __init__(self, amount):
        self.amount = amount
        super().__init__(f"金额无效: {amount}（必须大于0）")


def pay(balance, amount):
    """模拟支付"""
    if amount <= 0:
        raise InvalidAmountError(amount)
    if balance < amount:
        raise InsufficientBalanceError(balance, amount)
    balance -= amount
    print(f"  ✓ 支付成功！余额: {balance}")
    return balance


# 测试
test_cases = [
    ("正常支付", 1000, 300),
    ("金额无效", 1000, -50),
    ("余额不足", 100, 200),
]

for case_name, bal, amt in test_cases:
    print(f"\n{case_name}: balance={bal}, amount={amt}")
    try:
        pay(bal, amt)
    except InvalidAmountError as e:
        print(f"  ✗ InvalidAmountError: {e}")
    except InsufficientBalanceError as e:
        print(f"  ✗ InsufficientBalanceError: {e}")
        print(f"    余额: {e.balance}, 需要: {e.amount}, 差额: {e.shortfall}")
    except PaymentError as e:
        # 捕获其他支付相关异常
        print(f"  ✗ PaymentError: {e}")

# ========== 6. assert 断言 ==========
print("\n" + "=" * 40)
print("6. assert 断言")
print("=" * 40)


def calculate_average(scores):
    """计算平均分，要求列表不为空"""
    assert isinstance(scores, list), "scores 必须是列表类型"
    assert len(scores) > 0, "scores 列表不能为空"
    return sum(scores) / len(scores)


# 正常使用
try:
    avg = calculate_average([85, 92, 78, 90])
    print(f"  平均分: {avg:.1f} ✓")
except AssertionError as e:
    print(f"  ✗ AssertionError: {e}")

# 触发断言
try:
    calculate_average([])
except AssertionError as e:
    print(f"  ✗ AssertionError: {e}")

print("\n注意：assert 用于开发调试，生产环境可能被 -O 跳过")
print("业务校验应使用 if + raise，不依赖 assert")

# ========== 7. 异常链：raise ... from ... ==========
print("\n" + "=" * 40)
print("7. 异常链 raise ... from ...")
print("=" * 40)


def load_config(filepath):
    """加载配置文件，底层异常包装为业务异常"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError as e:
        # 把底层错误包装成更语义化的业务异常
        raise RuntimeError(f"配置加载失败: {filepath}") from e


try:
    load_config("不存在的配置文件.yaml")
except RuntimeError as e:
    print(f"  业务异常: {e}")
    print(f"  原因: {e.__cause__}")

# ========== 8. try/except/else/finally 完整流程 ==========
print("\n" + "=" * 40)
print("8. try/except/else/finally 完整流程")
print("=" * 40)


def demonstrate_full_try(should_fail=False):
    """演示 try/except/else/finally 的执行流程"""
    print(f"  should_fail = {should_fail}")
    try:
        print("  1. try 块开始")
        if should_fail:
            raise ValueError("模拟一个错误")
        result = 42
        print("  2. try 块完成（无异常）")
    except ValueError as e:
        print(f"  3. except 捕获: {e}")
        result = None
    else:
        print(f"  4. else 块执行（try 无异常才执行）")
    finally:
        print(f"  5. finally 块执行（无论如何都执行）")
    return result


print("\n场景A：无异常")
result = demonstrate_full_try(should_fail=False)
print(f"  最终结果: {result}")

print("\n场景B：有异常")
result = demonstrate_full_try(should_fail=True)
print(f"  最终结果: {result}")

# ========== 9. 不要空 except 吞异常 ==========
print("\n" + "=" * 40)
print("9. 反面教材：不要空 except")
print("=" * 40)

print("❌ 错误做法：")
print("  try:")
print("      do_something()")
print("  except:")
print("      pass  # 所有异常被静默吞掉，排查困难")
print()
print("✅ 正确做法：")
print("  try:")
print("      do_something()")
print("  except FileNotFoundError as e:")
print("      print(f'文件未找到: {e}')")
print("  except ValueError as e:")
print("      print(f'数据格式错误: {e}')")
print("  except Exception as e:")
print("      logging.exception('未预期错误')  # 至少要记录!")

# ========== 10. 实战：安全文件读取器 ==========
print("\n" + "=" * 40)
print("10. 实战：安全文件读取器")
print("=" * 40)


def safe_read_file(filepath, encodings=None):
    """
    安全读取文件：尝试多种编码，自动处理文件不存在等情况。
    返回 (content, encoding_used) 或 (None, None)。
    """
    if encodings is None:
        encodings = ['utf-8', 'utf-8-sig', 'gbk', 'gb2312', 'gb18030']

    for enc in encodings:
        try:
            with open(filepath, 'r', encoding=enc) as f:
                content = f.read()
            print(f"  ✓ 用 {enc} 编码读取成功")
            return content, enc
        except UnicodeDecodeError:
            continue
        except FileNotFoundError:
            print(f"  ✗ 文件不存在: {filepath}")
            return None, None
        except PermissionError:
            print(f"  ✗ 没有权限读取: {filepath}")
            return None, None

    print(f"  ✗ 所有编码都无法读取: {filepath}")
    return None, None


# 测试：正常读取
print("\n[测试1] 读取存在的文件:")
content, enc = safe_read_file('demo_basic.csv')
if content:
    print(f"  内容前50字符: {content[:50]}")

print("\n[测试2] 读取不存在的文件:")
content, enc = safe_read_file('不存在的文件.xyz')
print(f"  结果: content={content is None}")

# ========== 11. 异常处理最佳实践总结 ==========
print("\n" + "=" * 40)
print("11. 异常处理最佳实践")
print("=" * 40)

practices = [
    "捕获具体异常类型，不要用裸 except:",
    "try 块只包裹可能出错的代码，范围越小越好",
    "else 块放依赖 try 成功的代码，让逻辑更清晰",
    "finally 只做清理，不要写 return（会覆盖 try 的 return）",
    "自定义异常继承 Exception，不要继承 BaseException",
    "异常信息要记录完整（类型、消息、堆栈），方便排查",
    "业务校验用 if + raise，不要依赖 assert",
    "无法处理的异常要重新 raise，不要静默吞掉",
]
for i, tip in enumerate(practices, 1):
    print(f"  {i}. {tip}")

print("\n异常处理演示完成！")
