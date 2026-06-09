"""
Demo 4: 封装
演示：公开/保护/私有属性、名称改写、@property 封装

运行方式：python 4_encapsulation.py
"""


# ========== 1. 三种访问级别 ==========
print("=" * 40)
print("1. 三种访问级别")
print("=" * 40)


class Demo:
    def __init__(self):
        self.public = "公开属性"     # 随便访问
        self._protected = "保护属性"  # 约定：不建议外部使用
        self.__private = "私有属性"   # 名称改写：_Demo__private

    def show(self):
        print(f"public: {self.public}")
        print(f"_protected: {self._protected}")
        print(f"__private: {self.__private}")


d = Demo()
d.show()

print("\n外部访问：")
print(f"d.public = {d.public}")
print(f"d._protected = {d._protected}（能访问，但不建议）")

# print(d.__private)  # 报错！AttributeError
print(f"d._Demo__private = {d._Demo__private}（名称改写后仍能访问）")


# ========== 2. @property 实现封装 ==========
print("\n" + "=" * 40)
print("2. @property 实现封装")
print("=" * 40)


class BankAccount:
    """银行账户：通过 @property 保护数据"""

    def __init__(self, owner, balance=0):
        self._owner = owner
        self._balance = balance

    @property
    def owner(self):
        """账户名（只读）"""
        return self._owner

    @property
    def balance(self):
        """余额（只读，不能直接改）"""
        return self._balance

    def deposit(self, amount):
        """存款（唯一改余额的方式）"""
        if amount <= 0:
            print(f"存款失败：金额必须大于0")
            return False
        self._balance += amount
        print(f"存入 {amount}元，当前余额 {self._balance}元")
        return True

    def withdraw(self, amount):
        """取款"""
        if amount <= 0:
            print(f"取款失败：金额必须大于0")
            return False
        if amount > self._balance:
            print(f"取款失败：余额不足（余额{self._balance}元）")
            return False
        self._balance -= amount
        print(f"取出 {amount}元，当前余额 {self._balance}元")
        return True


account = BankAccount("小明", 1000)
print(f"账户名：{account.owner}")
print(f"初始余额：{account.balance}")

# account.balance = 99999  # 报错！没有 setter，只读

account.deposit(500)
account.withdraw(200)
account.withdraw(2000)  # 余额不足


# ========== 3. 带校验的 @property ==========
print("\n" + "=" * 40)
print("3. 带校验的 @property")
print("=" * 40)


class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("名字不能为空")
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not 0 < value < 150:
            raise ValueError(f"年龄必须在1-149之间，收到: {value}")
        self._age = value

    def __repr__(self):
        return f"Person(name='{self._name}', age={self._age})"


p = Person("小明", 18)
print(p)

p.age = 20
print(f"修改年龄后: {p}")

try:
    p.age = -5
except ValueError as e:
    print(f"校验拦截: {e}")

try:
    p.name = ""
except ValueError as e:
    print(f"校验拦截: {e}")
