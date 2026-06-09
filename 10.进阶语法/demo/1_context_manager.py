"""
演示 with 语句 / 自定义上下文管理器（类方式 + 生成器方式）/ 计时器

本文件展示上下文管理器的多种实现方式：
- 类方式：__enter__ / __exit__
- 生成器方式：@contextmanager 装饰器
- 实际应用：计时器、异常处理

可以独立运行，用 = 分隔线和 print 明确展示输出。
"""

import time
from contextlib import contextmanager, closing


# ============================================================================
# 一、with 语句基础（内置上下文管理器）
# ============================================================================
print("=" * 60)
print("一、with 语句基础：文件操作")
print("=" * 60)

# 传统方式 vs with 方式
# with 自动调用 close()，无论是否发生异常
with open("/tmp/test_cm.txt", "w") as f:
    f.write("Hello Context Manager!")
    print(f"[写入] 文件名: {f.name}")

# 离开 with 块后文件自动关闭
print("[验证] 文件已自动关闭:", f.closed)


# ============================================================================
# 二、类方式自定义上下文管理器
# ============================================================================
print("\n" + "=" * 60)
print("二、类方式自定义上下文管理器")
print("=" * 60)

class DatabaseConnection:
    """
    模拟数据库连接的上下文管理器
    __enter__: 建立连接，返回连接对象
    __exit__:  关闭连接，处理异常
    """

    def __init__(self, db_url: str):
        self.db_url = db_url
        self.connected = False

    def __enter__(self):
        """进入 with 块：建立连接"""
        print(f"  [__enter__] 正在连接 {self.db_url} ...")
        time.sleep(0.3)  # 模拟连接耗时
        self.connected = True
        print(f"  [__enter__] 连接成功！")
        # 返回值赋给 as 后面的变量
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        离开 with 块：关闭连接
        参数说明：
          exc_type:  异常类型，无异常时为 None
          exc_val:   异常值，无异常时为 None
          exc_tb:    异常 traceback，无异常时为 None
        返回 True 可吞掉异常，返回 False 则异常继续向上传播
        """
        if exc_type is not None:
            print(f"  [__exit__] 发生异常: {exc_type.__name__}: {exc_val}")
        print(f"  [__exit__] 断开连接 {self.db_url}")
        self.connected = False
        # 返回 False → 异常继续抛出（默认行为）
        return False

    def query(self, sql: str) -> str:
        """模拟执行查询"""
        if not self.connected:
            raise RuntimeError("未连接！")
        print(f"  [查询] 执行 SQL: {sql}")
        return f"结果_{sql}"

# 正常使用
print("\n[场景1] 正常执行:")
with DatabaseConnection("mysql://localhost/mydb") as conn:
    result = conn.query("SELECT * FROM users")
    print(f"  查询结果: {result}")
print(f"  [外部] 连接状态: {conn.connected}")

# 异常处理
print("\n[场景2] with 块内发生异常:")
try:
    with DatabaseConnection("mysql://localhost/mydb") as conn:
        conn.query("SELECT *")
        raise ValueError("模拟业务异常")
except ValueError as e:
    print(f"  [外部] 捕获到异常: {e}")


# ============================================================================
# 三、__exit__ 返回 True 吞掉异常
# ============================================================================
print("\n" + "=" * 60)
print("三、__exit__ 返回 True 吞掉异常")
print("=" * 60)

class SuppressValueError:
    """只吞掉 ValueError，其他异常正常抛出"""

    def __enter__(self):
        print("  [进入] SuppressValueError")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print("  [退出] 无异常")
        elif exc_type is ValueError:
            print(f"  [退出] 吞掉 ValueError: {exc_val}")
            return True  # 吞掉异常
        else:
            print(f"  [退出] {exc_type.__name__} 继续抛出")
            return False  # 异常继续传播

print("\n[场景1] 抛 ValueError（被吞掉）:")
with SuppressValueError():
    raise ValueError("这个异常被吞掉了")
print("  [外部] 程序继续执行！")  # 会执行

print("\n[场景2] 抛 TypeError（不被吞掉）:")
try:
    with SuppressValueError():
        raise TypeError("这个异常会抛出")
except TypeError as e:
    print(f"  [外部] 捕获到 TypeError: {e}")


# ============================================================================
# 四、@contextmanager 装饰器（生成器方式）
# ============================================================================
print("\n" + "=" * 60)
print("四、@contextmanager 生成器方式")
print("=" * 60)

@contextmanager
def timer(task_name: str):
    """
    计时器上下文管理器（生成器实现）
    yield 之前 → 相当于 __enter__
    yield 之后 → 相当于 __exit__（写在 finally 中确保执行）
    """
    start = time.time()
    print(f"  [计时开始] {task_name}")
    try:
        yield  # 在此执行 with 块内的代码
    finally:
        # finally 确保即使 with 块发生异常也会执行清理
        elapsed = time.time() - start
        print(f"  [计时结束] {task_name} 耗时: {elapsed:.2f} 秒")

with timer("数据处理任务"):
    time.sleep(0.5)
    print("  处理中...")
    time.sleep(0.3)

# 验证 finally 的效果：with 块中抛出异常仍会执行清理
print("\n[验证] finally 保证清理:")
try:
    with timer("会失败的任务"):
        time.sleep(0.2)
        raise RuntimeError("任务中途失败")
except RuntimeError:
    print("  [外部] 异常被捕获，但计时器仍然打印了结束信息")


# ============================================================================
# 五、嵌套 with：同时管理多个资源
# ============================================================================
print("\n" + "=" * 60)
print("五、嵌套 with（多资源管理）")
print("=" * 60)

class Tracker:
    """用于追踪进入/退出顺序的简单上下文管理器"""
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f"  --> 进入 {self.name}")
        return self

    def __exit__(self, *args):
        print(f"  <-- 退出 {self.name}")
        return False

# 逗号并列写法（进入顺序：A→B→C，退出顺序：C→B→A，类似栈）
print("\n[执行顺序]:")
with Tracker("A"), Tracker("B"), Tracker("C"):
    print("  *** 在 with 块中 ***")

# 等价于：
# with Tracker("A"):
#     with Tracker("B"):
#         with Tracker("C"):
#             print("在 with 块中")


# ============================================================================
# 六、closing 包装器
# ============================================================================
print("\n" + "=" * 60)
print("六、contextlib.closing 包装器")
print("=" * 60)

# closing 将只有 close() 方法的对象包装成上下文管理器
class SimpleResource:
    """只有 close 方法的简单资源类"""
    def __init__(self, name):
        self.name = name
        self.closed = False

    def close(self):
        self.closed = True
        print(f"  [关闭] {self.name} 已关闭")

    def use(self):
        print(f"  [使用] {self.name}")

# 使用 closing 包装
with closing(SimpleResource("数据源")) as resource:
    resource.use()
print(f"  [外部] resource.closed = {resource.closed}")


# ============================================================================
# 七、自定义 contextmanager 实现临时目录操作
# ============================================================================
print("\n" + "=" * 60)
print("七、实际场景：临时工作目录切换")
print("=" * 60)

import os

# 保存当前目录以便演示
ORIGINAL_DIR = os.getcwd()

@contextmanager
def change_dir(path: str):
    """进入时切换目录，退出时回到原目录"""
    old_dir = os.getcwd()
    os.chdir(path)
    print(f"  [切换] 进入 {path}")
    try:
        yield
    finally:
        os.chdir(old_dir)
        print(f"  [恢复] 回到 {old_dir}")

print(f"  原始目录: {ORIGINAL_DIR}")
with change_dir("/tmp"):
    print(f"  当前目录: {os.getcwd()}")
print(f"  恢复目录: {os.getcwd()}")


# ============================================================================
# 八、异常安全验证：生成器方式无 try/finally 陷阱
# ============================================================================
print("\n" + "=" * 60)
print("八、踩坑演示：生成器方式须用 try/finally")
print("=" * 60)

@contextmanager
def bad_manager(name):
    """错误示范：没有 try/finally，异常时清理代码不执行"""
    print(f"  [BAD] {name} 开始")
    yield
    print(f"  [BAD] {name} 清理")  # 如果 with 块异常，这行不执行！

@contextmanager
def good_manager(name):
    """正确示范：try/finally 包裹"""
    print(f"  [GOOD] {name} 开始")
    try:
        yield
    finally:
        print(f"  [GOOD] {name} 清理")  # 始终执行！

print("\n[BAD 版本]:")
try:
    with bad_manager("测试"):
        raise ValueError("异常")
except ValueError:
    print("  [外部] 异常被捕获，但清理代码没执行")

print("\n[GOOD 版本]:")
try:
    with good_manager("测试"):
        raise ValueError("异常")
except ValueError:
    print("  [外部] 异常被捕获，清理代码仍然执行了")


print("\n" + "=" * 60)
print("全部演示完成！")
print("=" * 60)
