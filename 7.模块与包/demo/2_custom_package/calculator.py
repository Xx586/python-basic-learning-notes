"""
自定义包内的计算器模块

定义基本的数学运算函数和科学计算函数。
"""

import math


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
        raise ValueError("除数不能为0")
    return a / b


def power(base, exp):
    """幂运算"""
    return base ** exp


def square_root(x):
    """平方根"""
    if x < 0:
        raise ValueError("不能对负数开平方根")
    return math.sqrt(x)


def percentage(value, total):
    """计算百分比"""
    if total == 0:
        raise ValueError("总数不能为0")
    return round((value / total) * 100, 2)


class Calculator:
    """计算器类：演示包内模块中的类"""

    def __init__(self, initial=0):
        self._result = initial
        self._history = []

    @property
    def result(self):
        return self._result

    def add(self, value):
        self._history.append(f"{self._result} + {value} = {self._result + value}")
        self._result += value
        return self

    def subtract(self, value):
        self._history.append(f"{self._result} - {value} = {self._result - value}")
        self._result -= value
        return self

    def multiply(self, value):
        self._history.append(f"{self._result} * {value} = {self._result * value}")
        self._result *= value
        return self

    def divide(self, value):
        if value == 0:
            raise ValueError("除数不能为0")
        self._history.append(f"{self._result} / {value} = {self._result / value}")
        self._result /= value
        return self

    def reset(self):
        """重置计算器"""
        self._history.append(f"--- 重置 ---")
        self._result = 0
        return self

    def show_history(self):
        """显示计算历史"""
        print("计算历史:")
        for record in self._history:
            print(f"  {record}")

    def __repr__(self):
        return f"Calculator(result={self._result})"


# 模块自测
if __name__ == '__main__':
    print("=== calculator 模块自测 ===\n")

    print(f"add(10, 5) = {add(10, 5)}")
    print(f"multiply(6, 7) = {multiply(6, 7)}")
    print(f"power(2, 10) = {power(2, 10)}")
    print(f"square_root(144) = {square_root(144)}")
    print(f"percentage(45, 200) = {percentage(45, 200)}%\n")

    calc = Calculator()
    calc.add(10).multiply(3).subtract(5).divide(5)
    print(f"计算器最终结果: {calc.result}")
    calc.show_history()
