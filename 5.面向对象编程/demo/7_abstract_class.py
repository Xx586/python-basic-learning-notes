"""
Demo 7: 抽象类
演示：ABC、@abstractmethod、抽象属性、模板方法模式

运行方式：python 7_abstract_class.py
"""

from abc import ABC, abstractmethod


# ========== 1. 基本抽象类 ==========
print("=" * 40)
print("1. 基本抽象类")
print("=" * 40)


class Animal(ABC):
    """抽象基类：不能实例化"""

    @abstractmethod
    def speak(self) -> str:
        """子类必须实现 speak 方法"""
        pass


class Dog(Animal):
    def speak(self):
        return "汪汪！"


class Cat(Animal):
    def speak(self):
        return "喵喵！"


class Duck(Animal):
    def speak(self):
        return "嘎嘎！"


# animal = Animal()  # TypeError: 不能实例化抽象类

dog = Dog()
cat = Cat()
duck = Duck()
print(f"狗: {dog.speak()}")
print(f"猫: {cat.speak()}")
print(f"鸭子: {duck.speak()}")


# ========== 2. 抽象类 + 普通方法（模板方法模式） ==========
print("\n" + "=" * 40)
print("2. 模板方法模式")
print("=" * 40)


class DataExporter(ABC):
    """数据导出器：定义流程骨架，子类实现具体步骤"""

    @abstractmethod
    def format_data(self, data):
        """子类实现：如何格式化数据"""
        pass

    @abstractmethod
    def save(self, formatted, filename):
        """子类实现：如何保存文件"""
        pass

    # 模板方法：定义流程骨架（有自己的实现）
    def export(self, data, filename):
        print(f"开始导出到 {filename} ...")
        formatted = self.format_data(data)
        self.save(formatted, filename)
        print(f"导出完成！")


class TextExporter(DataExporter):
    def format_data(self, data):
        return "\n".join(f"{k}: {v}" for k, v in data.items())

    def save(self, formatted, filename):
        with open(filename, "w") as f:
            f.write(formatted)
        print(f"  已保存为文本文件")


class HTMLExporter(DataExporter):
    def format_data(self, data):
        rows = "".join(f"<tr><td>{k}</td><td>{v}</td></tr>"
                       for k, v in data.items())
        return f"<table>{rows}</table>"

    def save(self, formatted, filename):
        with open(filename, "w") as f:
            f.write(f"<html><body>{formatted}</body></html>")
        print(f"  已保存为HTML文件")


# 使用
data = {"姓名": "张三", "年龄": "25", "城市": "北京"}

text_exp = TextExporter()
text_exp.export(data, "demo_output.txt")

html_exp = HTMLExporter()
html_exp.export(data, "demo_output.html")


# ========== 3. 抽象属性 ==========
print("\n" + "=" * 40)
print("3. 抽象属性")
print("=" * 40)


class Vehicle(ABC):
    @property
    @abstractmethod
    def max_speed(self) -> int:
        """子类必须实现 max_speed 属性"""
        pass

    @property
    @abstractmethod
    def wheels(self) -> int:
        pass

    def info(self):
        print(f"{self.__class__.__name__}: {self.wheels}个轮子, 最高{self.max_speed}km/h")


class Car(Vehicle):
    @property
    def max_speed(self):
        return 200

    @property
    def wheels(self):
        return 4


class Bicycle(Vehicle):
    @property
    def max_speed(self):
        return 25

    @property
    def wheels(self):
        return 2


Car().info()
Bicycle().info()


# ========== 输出清理（可选） ==========
import os
for f in ["demo_output.txt", "demo_output.html"]:
    if os.path.exists(f):
        os.remove(f)
