"""
自定义数学工具模块 — 被其他文件导入使用

包含：基本运算函数、阶乘、斐波那契、Circle 类
"""

PI = 3.14159
E = 2.71828


def add(a, b):
    """加法"""
    return a + b


def subtract(a, b):
    """减法"""
    return a - b


def multiply(a, b):
    """乘法"""
    return a * b


def divide(a, b):
    """除法（含除零保护）"""
    if b == 0:
        raise ValueError("除数不能为0！")
    return a / b


def factorial(n):
    """计算 n 的阶乘（递归实现）"""
    if n < 0:
        raise ValueError("阶乘只接受非负整数")
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    """返回第 n 个斐波那契数（0-indexed）"""
    if n < 0:
        raise ValueError("n 必须 >= 0")
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b


def is_prime(n):
    """判断一个数是否为质数"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


class Circle:
    """圆类：演示被导入模块中的类"""

    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("半径必须大于0")
        self.radius = radius

    def area(self):
        """计算面积"""
        return PI * self.radius ** 2

    def circumference(self):
        """计算周长"""
        return 2 * PI * self.radius

    def __repr__(self):
        return f"Circle(radius={self.radius})"


# ========== 模块自测代码 ==========
# 只在直接运行本文件时执行，被 import 时不执行
if __name__ == '__main__':
    print("=== my_math 模块自测 ===\n")

    print(f"PI = {PI}")
    print(f"add(3, 5) = {add(3, 5)}")
    print(f"multiply(6, 7) = {multiply(6, 7)}")
    print(f"divide(10, 3) = {divide(10, 3):.2f}")
    print(f"factorial(5) = {factorial(5)}")
    print(f"fibonacci(10) = {fibonacci(10)}")
    print(f"is_prime(17) = {is_prime(17)}")
    print(f"is_prime(100) = {is_prime(100)}")

    c = Circle(5)
    print(f"\n{c}")
    print(f"面积: {c.area():.2f}")
    print(f"周长: {c.circumference():.2f}")
