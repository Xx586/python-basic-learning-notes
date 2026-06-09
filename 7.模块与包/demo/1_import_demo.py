"""
Demo 1: 演示各种模块导入方式

演示：import 模块、from...import、as 别名、
      from...import *、__name__ 检测、sys.path

运行方式：在 demo/ 目录下执行 python 1_import_demo.py
"""

import sys
import os

print("=" * 60)
print("Demo 1: 模块导入方式演示")
print("=" * 60)

# ========== 1. import 模块名 ==========
print("\n--- 1. import 模块名 ---")
import my_math
import my_string

# 使用时必须加模块名前缀
print(f"my_math.PI = {my_math.PI}")
print(f"my_math.add(10, 20) = {my_math.add(10, 20)}")
print(f"my_math.fibonacci(8) = {my_math.fibonacci(8)}")
print(f"my_math.is_prime(29) = {my_math.is_prime(29)}")

# 使用 Circle 类
c = my_math.Circle(3)
print(f"{c} → 面积: {c.area():.2f}, 周长: {c.circumference():.2f}")

# my_string 模块
print(f"\nmy_string.reverse_string('abcdef') = {my_string.reverse_string('abcdef')}")
print(f"my_string.is_palindrome('racecar') = {my_string.is_palindrome('racecar')}")
print(f"my_string.count_words('Python is great') = {my_string.count_words('Python is great')}")


# ========== 2. from...import 具体内容 ==========
print("\n" + "=" * 60)
print("--- 2. from...import 导入具体内容 ---")
from my_math import add, subtract, multiply, divide, PI
from my_string import reverse_string, is_palindrome, mask_string

# 直接使用，不需要模块名前缀
print(f"PI = {PI}")
print(f"add(3, 7) = {add(3, 7)}")
print(f"subtract(10, 4) = {subtract(10, 4)}")
print(f"multiply(5, 8) = {multiply(5, 8)}")
print(f"divide(100, 4) = {divide(100, 4)}")

# from...import 的坑：可能与本地变量冲突
# PI = 100          # 这会覆盖上面导入的 PI
# from my_math import PI  # 又覆盖了你的 PI = 100
print(f"\nreverse_string('hello') = {reverse_string('hello')}")
print(f"is_palindrome('madam') = {is_palindrome('madam')}")
print(f"mask_string('13812345678', start=3, end=4) = {mask_string('13812345678', start=3, end=4)}")


# ========== 3. as 别名 ==========
print("\n" + "=" * 60)
print("--- 3. as 起别名 ---")
import my_math as mm       # 给模块起短别名
import my_string as ms

print(f"mm.factorial(5) = {mm.factorial(5)}")
print(f"mm.is_prime(97) = {mm.is_prime(97)}")
print(f"ms.truncate('很长的文本内容需要截断', 8, '~') = {ms.truncate('很长的文本内容需要截断', 8, '~')}")
print(f"ms.capitalize_words('hello world from python') = {ms.capitalize_words('hello world from python')}")

# from...import 也能 as
from my_math import fibonacci as fib, is_prime as prime_check
print(f"\nfib(15) [fibonacci alias] = {fib(15)}")
print(f"prime_check(53) [is_prime alias] = {prime_check(53)}")


# ========== 4. from...import * (不推荐!) ==========
print("\n" + "=" * 60)
print("--- 4. from...import * (仅演示，不推荐!) ---")
from my_string import *

# 所有公开名称（不以下划线开头）都被导入
print(f"StringWrapper (通过 * 导入):")
sw = StringWrapper("import star test")
print(f"  {sw}")
print(f"  upper: {sw.upper()}")

# 说明：from...import * 会导致命名空间污染，不知道某个函数来自哪个模块
# 强烈建议避免在生产代码中使用此方式


# ========== 5. __name__ 检测 ==========
print("\n" + "=" * 60)
print("--- 5. __name__ 属性演示 ---")
print(f"当前文件的 __name__ = {__name__!r}")

# 验证被导入模块的 __name__
print(f"my_math 模块的 __name__ = {my_math.__name__!r}")
print(f"my_string 模块的 __name__ = {my_string.__name__!r}")


# ========== 6. 显示模块搜索路径 ==========
print("\n" + "=" * 60)
print("--- 6. sys.path (前5条) ---")
for i, path in enumerate(sys.path[:5]):
    print(f"  [{i}] {path}")
print(f"  (共 {len(sys.path)} 条路径)")


# ========== 7. 附加演示：my_math 内模块自测不会被触发 ==========
print("\n" + "=" * 60)
print("--- 7. 验证被导入模块的自测代码不执行 ---")
print("如果需要单独测试 my_math.py，用以下命令直接运行:")
print("  python my_math.py")
print("被 import 时，my_math 和 my_string 中的 if __name__ == '__main__' 代码块不会执行。")

print("\n" + "=" * 60)
print("Demo 1 演示完毕！")
print("=" * 60)
