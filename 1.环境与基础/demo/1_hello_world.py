# -*- coding: utf-8 -*-
"""
Demo 1: 第一个 Python 程序 —— Hello, World!

本 Demo 演示：
  1. 编写并运行第一个 Python 程序
  2. print() 函数的基本用法
  3. 验证 Python 环境是否正常工作
  4. 查看当前 Python 版本和系统信息

运行方式：
  python3 demo/1_hello_world.py

学习目标：
  确保你的 Python 环境安装正确，能成功执行 .py 文件
"""

import sys
import platform


# ============================================================
# Part 1: 最经典的 "Hello, World!"
# ============================================================
print("=" * 50)
print("Part 1: 你好，世界！")
print("=" * 50)

# print() 是 Python 最常用的输出函数，将内容打印到终端
print("Hello, World!")      # 输出字符串
print("你好，世界！")        # 中文也没问题
print(42)                   # 输出数字
print(3.14)                 # 输出浮点数
print(True)                 # 输出布尔值


# ============================================================
# Part 2: print() 的高级用法
# ============================================================
print("\n" + "=" * 50)
print("Part 2: print() 的各种用法")
print("=" * 50)

# sep 参数：指定多个参数之间的分隔符（默认是空格）
print("苹果", "香蕉", "橙子")               # 默认空格分隔
print("苹果", "香蕉", "橙子", sep=" | ")    # 自定义分隔符

# end 参数：指定打印结束后的字符（默认是换行符 \n）
print("第一句", end=" -> ")
print("第二句（紧跟在第一句后面）")

# f-string：格式化输出（Python 3.6+）
name = "小明"
age = 18
print(f"我叫{name}，今年{age}岁。")


# ============================================================
# Part 3: 验证 Python 环境
# ============================================================
print("\n" + "=" * 50)
print("Part 3: 验证 Python 环境")
print("=" * 50)

# 检查 Python 版本信息
print(f"Python 版本: {sys.version}")
print(f"版本号: {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
print(f"操作系统: {platform.system()} {platform.release()}")
print(f"CPU 架构: {platform.architecture()[0]}")
print(f"Python 路径: {sys.executable}")

# 检查 Python 版本是否满足最低要求 (>= 3.8)
if sys.version_info < (3, 8):
    print("\n[警告] 你的 Python 版本过低，建议升级到 3.11+")
else:
    print("\n[通过] Python 版本符合要求！")


# ============================================================
# Part 4: 简单的交互 —— input() 函数
# ============================================================
print("\n" + "=" * 50)
print("Part 4: 交互输入")
print("=" * 50)

# input() 函数等待用户输入，返回字符串
# 注意：在纯脚本环境中，这行会等待你输入
# 不想交互的话可以注释掉
# user_name = input("请输入你的名字: ")
# print(f"你好，{user_name}！欢迎来到 Python 的世界！")

# 模拟输入（不实际等待）
demo_name = "Python学习者"
print(f"（模拟输入）你好，{demo_name}！欢迎来到 Python 的世界！")


# ============================================================
# Part 5: 运行验证总结
# ============================================================
print("\n" + "=" * 50)
print("Part 5: 环境验证总结")
print("=" * 50)

# 简单计算验证
result = 1 + 2 * 3
print(f"简单计算测试: 1 + 2 * 3 = {result}（预期: 7）")

# 字符串操作验证
text = "Hello" + " " + "Python"
print(f"字符串拼接测试: {text}（预期: Hello Python）")

# 列表操作验证
numbers = [1, 2, 3, 4, 5]
print(f"列表操作测试: sum({numbers}) = {sum(numbers)}（预期: 15）")


print("\n" + "=" * 50)
print("恭喜！你的 Python 环境配置正确，一切正常！")
print("接下来可以继续学习下一个 Demo 了。")
print("=" * 50)
