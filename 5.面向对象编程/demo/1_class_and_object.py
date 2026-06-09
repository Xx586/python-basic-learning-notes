"""
Demo 1: 类和对象基础
演示：类的定义、实例化、self、实例属性 vs 类属性

运行方式：python 1_class_and_object.py
"""

# ========== 1. 最基本的类 ==========
class Dog:
    """狗类"""
    species = "犬科"  # 类属性：所有狗共享

    def __init__(self, name, age):
        """构造方法：创建对象时自动调用"""
        self.name = name  # 实例属性：每条狗有自己的名字
        self.age = age    # 实例属性：每条狗有自己的年龄

    def bark(self):
        """实例方法"""
        print(f"{self.name}（{self.age}岁）：汪汪！")

    def info(self):
        print(f"名字：{self.name}，年龄：{self.age}，种类：{self.species}")


# 创建对象
dog1 = Dog("旺财", 3)
dog2 = Dog("来福", 1)

print("=== 调用方法 ===")
dog1.bark()
dog2.bark()

print("\n=== 查看属性 ===")
print(f"{dog1.name} 的年龄：{dog1.age}")
print(f"{dog2.name} 的年龄：{dog2.age}")

print("\n=== 类属性是共享的 ===")
dog1.info()
dog2.info()

# 修改类属性 → 所有实例都受影响
Dog.species = "家犬"
print("\n修改类属性后：")
dog1.info()
dog2.info()


# ========== 2. 更多例子：学生类 ==========
print("\n" + "=" * 40)
print("学生类示例")
print("=" * 40)


class Student:
    school = "第一中学"

    def __init__(self, name, grade, score=0):
        self.name = name
        self.grade = grade
        self.score = score

    def is_pass(self):
        return "及格" if self.score >= 60 else "不及格"

    def report(self):
        print(f"{self.name} | {self.grade}年级 | {self.score}分 | {self.is_pass()}")


students = [
    Student("张三", 7, 85),
    Student("李四", 7, 55),
    Student("王五", 8, 92),
]

print(f"学校：{Student.school}")
for s in students:
    s.report()
