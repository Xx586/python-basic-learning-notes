"""
Demo 7: 类型注解
演示：参数/返回值标注、typing模块、3.10+新语法、mypy使用、不影响运行

运行方式：python 7_type_hints.py
"""

from typing import List, Dict, Tuple, Optional, Union, Callable, Any, Set

# ========== 1. 基础类型注解 ==========
print("=" * 40)
print("1. 基础类型注解")
print("=" * 40)

# 变量注解
name: str = "张三"
age: int = 18
score: float = 95.5
is_pass: bool = True

print(f"  name: {name} (type: {type(name).__name__})")
print(f"  age: {age} (type: {type(age).__name__})")
print(f"  score: {score} (type: {type(score).__name__})")

# 函数注解 —— 类型注解不影响运行！
def add(a: int, b: int) -> int:
    return a + b

print(f"  add(3, 5) = {add(3, 5)}")
# 类型注解不校验！传入字符串也能运行
print(f"  add('hello', 'world') = {add('hello', 'world')}  ← 不会报错")
print()

# ========== 2. typing 模块 —— 复合类型 ==========
print("=" * 40)
print("2. typing 模块")
print("=" * 40)

# List
def double_all(numbers: List[int]) -> List[int]:
    """列表中的每个数翻倍"""
    return [n * 2 for n in numbers]

print(f"  double_all([1, 2, 3]) = {double_all([1, 2, 3])}")

# Dict
def get_names(students: List[Dict[str, int]]) -> Dict[str, int]:
    """提取学生名字和分数"""
    return {s["name"]: s["score"] for s in students}  # type: ignore[index]

students = [{"name": "张三", "score": 85}, {"name": "李四", "score": 92}]
# print(f"  get_names: {get_names(students)}")  # 略，和上面冲突的类型注解演示

# Tuple
def get_position() -> Tuple[float, float]:
    """返回坐标元组"""
    return (3.5, 7.2)

pos = get_position()
print(f"  坐标: {pos}, 类型: {type(pos).__name__}")

# Set
def get_unique_chars(text: str) -> Set[str]:
    """返回字符串中的唯一字符"""
    return set(text)

print(f"  唯一字符: {get_unique_chars('hello world')}")
print()

# ========== 3. Optional 和 Union ==========
print("=" * 40)
print("3. Optional 和 Union")
print("=" * 40)

# Optional[str] = Union[str, None]
def find_user(user_id: int) -> Optional[str]:
    """查找用户名，可能返回 None"""
    users = {1: "张三", 2: "李四", 3: "王五"}
    return users.get(user_id)

print(f"  找到: {find_user(2)}")
print(f"  未找到: {find_user(999)}")

# Union —— 多种类型之一
def process(value: Union[int, str]) -> str:
    """可以接收 int 或 str"""
    if isinstance(value, int):
        return f"数字: {value}"
    else:
        return f"字符串: {value}"

print(f"  process(42) = {process(42)}")
print(f"  process('hello') = {process('hello')}")
print()

# ========== 4. Callable ==========
print("=" * 40)
print("4. Callable —— 函数类型")
print("=" * 40)

def apply(a: int, b: int, op: Callable[[int, int], int]) -> int:
    """对两个数应用操作"""
    return op(a, b)

def multiply(x: int, y: int) -> int:
    return x * y

print(f"  apply(3, 5, multiply) = {apply(3, 5, multiply)}")
print(f"  apply(3, 5, lambda x, y: x ** y) = {apply(3, 5, lambda x, y: x ** y)}")
print()

# ========== 5. Any ==========
print("=" * 40)
print("5. Any —— 任意类型")
print("=" * 40)

def debug_print(value: Any) -> None:
    """打印任意类型的值"""
    print(f"  [DEBUG] {value} ({type(value).__name__})")

debug_print(42)
debug_print("hello")
debug_print([1, 2, 3])
print()

# ========== 6. Python 3.10+ 新语法 ==========
print("=" * 40)
print("6. Python 3.10+ 新语法（仅展示）")
print("=" * 40)

# 新语法（需要 Python 3.10+）
# def new_style(names: list[str]) -> dict[str, int]: ...
# def new_optional(name: str | None) -> None: ...
# def new_union(value: int | str) -> str: ...

print("  旧: Optional[str]        新: str | None")
print("  旧: Union[int, str]      新: int | str")
print("  旧: List[int]            新: list[int]")
print("  旧: Dict[str, int]       新: dict[str, int]")
print("  旧: Tuple[int, str]      新: tuple[int, str]")
print()

# ========== 7. 类型别名 ==========
print("=" * 40)
print("7. 类型别名")
print("=" * 40)

# 简化复杂类型
UserId = int
StudentRecord = Tuple[str, int, float]  # (name, age, score)
ScoreMap = Dict[str, List[int]]         # {科目: [成绩列表]}

def get_student() -> StudentRecord:
    return ("张三", 18, 95.5)

def get_scores() -> ScoreMap:
    return {
        "数学": [85, 90, 78],
        "语文": [92, 88, 95],
    }

print(f"  get_student() = {get_student()}")
print(f"  get_scores() = {get_scores()}")
print()

# ========== 8. __annotations__ 查看注解 ==========
print("=" * 40)
print("8. 查看 __annotations__")
print("=" * 40)

def greet(name: str, times: int = 1) -> str:
    """打招呼"""
    return f"Hello, {name}! " * times

print(f"  函数注解: {greet.__annotations__}")
# {'name': <class 'str'>, 'times': <class 'int'>, 'return': <class 'str'>}
print()

# ========== 9. 类型注解不影响运行 ==========
print("=" * 40)
print("9. 类型注解不影响运行（重要！）")
print("=" * 40)

def add_typed(a: int, b: int) -> int:
    return a + b

# 即使传入字符串也能运行
result = add_typed("Hello, ", "World!")
print(f"  add_typed('Hello, ', 'World!') = {result}")
print("  (类型注解仅用于静态检查，如 mypy，不影响运行时)")

# mypy 使用提示：
# $ pip install mypy
# $ mypy 7_type_hints.py  # 会检测出上面的类型不匹配
