"""
Demo 6: dataclass
演示：@dataclass、field()、__post_init__、frozen、asdict/astuple

运行方式：python 6_dataclass.py
"""

from dataclasses import dataclass, field, asdict, astuple
from typing import List


# ========== 1. 基本 dataclass ==========
print("=" * 40)
print("1. 基本 dataclass")
print("=" * 40)


@dataclass
class Point:
    x: float
    y: float


p1 = Point(1.0, 2.0)
p2 = Point(1.0, 2.0)
p3 = Point(3.0, 4.0)

print(f"p1 = {p1}")         # 自动 __repr__
print(f"p1 == p2: {p1 == p2}")  # 自动 __eq__
print(f"p1 == p3: {p1 == p3}")


# ========== 2. 默认值与 field() ==========
print("\n" + "=" * 40)
print("2. 默认值与 field()")
print("=" * 40)


@dataclass
class Student:
    name: str
    age: int = 18                     # 简单默认值
    scores: List[int] = field(default_factory=list)  # 可变默认值
    grade: str = field(init=False, default="一年级")  # 非 __init__ 参数

    def add_score(self, value):
        self.scores.append(value)

    def average(self):
        return sum(self.scores) / len(self.scores) if self.scores else 0


s1 = Student("小明")
s2 = Student("小红", 20)

s1.add_score(85)
s1.add_score(90)
s2.add_score(78)

# 关键：每个实例的 scores 是独立的
print(f"{s1.name}: scores={s1.scores}, avg={s1.average()}")
print(f"{s2.name}: scores={s2.scores}, avg={s2.average()}")
print(f"s1.grade = {s1.grade}")


# ========== 3. __post_init__ ==========
print("\n" + "=" * 40)
print("3. __post_init__ 后处理")
print("=" * 40)


@dataclass
class Rectangle:
    width: float
    height: float
    area: float = field(init=False)

    def __post_init__(self):
        self.area = self.width * self.height


r = Rectangle(5, 3)
print(f"矩形: {r.width} x {r.height}, 面积 = {r.area}")


# ========== 4. 不可变 dataclass ==========
print("\n" + "=" * 40)
print("4. frozen=True 不可变")
print("=" * 40)


@dataclass(frozen=True)
class Config:
    host: str
    port: int
    debug: bool = False


c = Config("localhost", 8080)
print(f"Config: {c}")
# c.port = 9090  # 报错！FrozenInstanceError
print("（frozen 的 dataclass 实例创建后不能修改）")


# ========== 5. asdict / astuple ==========
print("\n" + "=" * 40)
print("5. asdict / astuple")
print("=" * 40)


@dataclass
class Person:
    name: str
    age: int
    city: str = "北京"


p = Person("小明", 18)
print(f"asdict:  {asdict(p)}")
print(f"astuple: {astuple(p)}")
