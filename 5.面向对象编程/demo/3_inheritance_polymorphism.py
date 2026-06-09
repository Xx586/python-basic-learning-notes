"""
Demo 3: 继承与多态
演示：单继承、super()、多继承MRO、方法重写、多态

运行方式：python 3_inheritance_polymorphism.py
"""


# ========== 1. 单继承 + super() ==========
print("=" * 40)
print("1. 单继承 + super()")
print("=" * 40)


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return f"{self.name} 发出声音"


class Dog(Animal):
    """Dog 继承 Animal"""

    def __init__(self, name, age, breed):
        super().__init__(name, age)  # 调用父类 __init__
        self.breed = breed

    def speak(self):
        """重写父类方法"""
        return f"{self.name}（{self.breed}）：汪汪！"

    def wag_tail(self):
        """子类新增方法"""
        return f"{self.name} 摇尾巴"


class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        return f"{self.name}（{self.color}猫）：喵喵！"


dog = Dog("旺财", 3, "金毛")
cat = Cat("咪咪", 1, "白")

print(dog.speak())
print(cat.speak())
print(dog.wag_tail())


# ========== 2. 多继承与 MRO ==========
print("\n" + "=" * 40)
print("2. 多继承与 MRO")
print("=" * 40)


class Flyable:
    def move(self):
        return "我在飞"


class Swimmable:
    def move(self):
        return "我在游"


class Duck(Flyable, Swimmable):
    """多继承：按 MRO 顺序查找方法"""

    def speak(self):
        return "嘎嘎"


d = Duck()
print(f"鸭子叫：{d.speak()}")
print(f"鸭子移动：{d.move()}")  # Flyable.move（先继承的优先）
print(f"MRO 顺序：{[c.__name__ for c in Duck.__mro__]}")


# ========== 3. 多态 ==========
print("\n" + "=" * 40)
print("3. 多态（鸭子类型）")
print("=" * 40)


class DuckType:
    def speak(self):
        return "嘎嘎嘎"


class ChickenType:
    def speak(self):
        return "咯咯咯"


class Person:
    def speak(self):
        return "你好！"


# 核心：同一个函数，不关心类型，只关心有没有 speak 方法
def chorus(things):
    """对所有有 speak 方法的对象统一调用"""
    for t in things:
        print(f"  {t.__class__.__name__}: {t.speak()}")


print("大合唱：")
chorus([Dog("旺财", 3, "金毛"), Cat("咪咪", 1, "白"), DuckType(), ChickenType(), Person()])


# ========== 4. isinstance / issubclass ==========
print("\n" + "=" * 40)
print("4. isinstance / issubclass")
print("=" * 40)

print(f"dog 是 Dog 的实例？{isinstance(dog, Dog)}")
print(f"dog 是 Animal 的实例？{isinstance(dog, Animal)}")
print(f"dog 是 object 的实例？{isinstance(dog, object)}")
print(f"Dog 是 Animal 的子类？{issubclass(Dog, Animal)}")
print(f"Animal 是 Dog 的子类？{issubclass(Animal, Dog)}")
