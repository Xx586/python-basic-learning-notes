"""
Demo 2: 演示导入和使用自定义包 2_custom_package

演示：
  1. importlib.import_module() 导入目录名以数字开头的包
  2. 使用包内模块的类和函数
  3. __name__ 和 __init__.py 的执行时机
  4. python -m 方式运行包内模块

注意：Python 模块/包名不能以数字开头。
如果目录名以数字开头（如 2_custom_package），
需要用 importlib.import_module() 来导入。

运行方式：在 demo/ 目录下执行 python 2_use_custom_package.py
"""

import importlib

print("=" * 60)
print("Demo 2: 使用自定义包 2_custom_package")
print("=" * 60)

# ========== 知识点：Python 包名不能以数字开头 ==========
print("\n--- 知识点：包名不能以数字开头 ---")
print("Python 语法规则：标识符不能以数字开头。")
print("因此不能写: import 2_custom_package  (SyntaxError)")
print("解决方案：使用 importlib.import_module()\n")

# ========== 用 importlib 导入包 ==========
pkg = importlib.import_module('2_custom_package')
calculator = importlib.import_module('2_custom_package.calculator')
formatter = importlib.import_module('2_custom_package.formatter')

# 给模块起短别名方便使用
calc = calculator
fmt = formatter


# ========== 基本运算演示 ==========
print("--- 基本运算 ---")
print(f"calc.add(10, 25)          = {calc.add(10, 25)}")
print(f"calc.subtract(50, 18)     = {calc.subtract(50, 18)}")
print(f"calc.multiply(7, 8)       = {calc.multiply(7, 8)}")
print(f"calc.divide(100, 6)       = {calc.divide(100, 6):.2f}")
print(f"calc.power(2, 10)         = {calc.power(2, 10)}")
print(f"calc.square_root(256)     = {calc.square_root(256)}")
print(f"calc.percentage(45, 200)  = {calc.percentage(45, 200)}%")


# ========== 使用 Calculator 类 ==========
print(f"\n--- Calculator 类（链式调用）---")
c = calc.Calculator(100)
c.add(50).multiply(2).subtract(30).divide(3)
print(f"初始100, +50, *2, -30, /3 = {c.result:.2f}")
print(f"计算历史:")
c.show_history()


# ========== 格式化功能演示 ==========
print(f"\n--- 格式化工具 ---")
print(f"货币格式化:  {fmt.format_currency(1234567.89)}")
print(f"美元格式化:  {fmt.format_currency(9999.99, '$')}")
print(f"百分比:      {fmt.format_percentage(45, 200)}")
print(f"当前时间:    {fmt.format_timestamp()}")
print(f"文件大小:    {fmt.format_file_size(2048000)}")
print(f"1GB:         {fmt.format_file_size(1073741824)}")


# ========== 使用 TableFormatter 类 ==========
print(f"\n--- TableFormatter 类 ---")
tf = fmt.TableFormatter()
tf.set_headers("操作", "输入", "结果")
tf.add_row("加法", "10 + 25", str(calc.add(10, 25)))
tf.add_row("平方根", "sqrt(144)", str(calc.square_root(144)))
tf.add_row("百分比", "45/200", fmt.format_percentage(45, 200))
tf.add_row("幂运算", "2^16", str(calc.power(2, 16)))
tf.add_row("货币", "1234.5元", fmt.format_currency(1234.5))
print(tf.build())


# ========== 查看包信息 ==========
print(f"\n--- 包信息 ---")
print(f"包的 __name__: {pkg.__name__!r}")
print(f"包的 __file__: {pkg.__file__!r}")
print(f"包的 __doc__ 摘要: {pkg.__doc__[:60]!r}...")


# ========== 提示：python -m 运行 ==========
print("\n" + "=" * 60)
print("--- 提示：如何单独测试包内模块 ---")
print("在 demo/ 目录下执行:")
print("  python -m 2_custom_package.calculator")
print("  python -m 2_custom_package.formatter")
print()
print("python -m 将模块作为包成员运行，")
print("此时 __name__ 为 '2_custom_package.calculator'，")
print("包内相对导入 (from . import xxx) 可以正常工作。")

print("\n" + "=" * 60)
print("Demo 2 演示完毕！")
print("=" * 60)
