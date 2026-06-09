"""
Demo 1: 文件读写操作
演示：读/写/追加、with 语句、文件模式、编码处理

运行方式：python 1_file_operations.py
"""

import os

# ========== 准备工作：清理旧文件 ==========
# 确保演示环境干净（忽略不存在的错误）
for f in ['demo_write.txt', 'demo_append.txt', 'demo_copy.txt', 'demo_binary.bin']:
    try:
        os.remove(f)
    except FileNotFoundError:
        pass

# ========== 1. 写入文件（'w' 模式） ==========
print("=" * 40)
print("1. 写入文件（'w' 模式）")
print("=" * 40)

# 'w' 模式：文件不存在则创建，存在则清空后写入
with open('demo_write.txt', 'w', encoding='utf-8') as f:
    f.write('第一行：你好，世界！\n')
    f.write('第二行：Python 文件操作\n')
    f.write('第三行：写入完毕\n')
print("已写入 demo_write.txt")

# ========== 2. 读取文件（多种方式） ==========
print("\n" + "=" * 40)
print("2. 读取文件（多种方式）")
print("=" * 40)

# 方式1：read() — 一次性读取全部内容
with open('demo_write.txt', 'r', encoding='utf-8') as f:
    content = f.read()
print(f"【read() 全部读取】:\n{content}")

# 方式2：readlines() — 返回列表，每行作为一个元素
with open('demo_write.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
print(f"【readlines() 逐行列表】: {lines}")

# 方式3：for line in f — 逐行迭代（推荐，省内存）
print("【for line in f 逐行迭代】:")
with open('demo_write.txt', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f, 1):
        print(f"  第{i}行: {line.rstrip()}")  # rstrip() 去掉末尾换行符

# ========== 3. 追加写入（'a' 模式） ==========
print("\n" + "=" * 40)
print("3. 追加写入（'a' 模式）")
print("=" * 40)

# 'a' 模式：文件不存在则创建，存在则在末尾追加，不清空
with open('demo_append.txt', 'w', encoding='utf-8') as f:
    f.write('原始内容\n')

with open('demo_append.txt', 'a', encoding='utf-8') as f:
    f.write('追加第一行\n')
    f.write('追加第二行\n')
print("已追加内容到 demo_append.txt")

# 验证追加结果
with open('demo_append.txt', 'r', encoding='utf-8') as f:
    print(f"追加后文件内容:\n{f.read()}")

# ========== 4. 'w' 和 'a' 模式的区别 ==========
print("=" * 40)
print("4. 'w' 模式 vs 'a' 模式")
print("=" * 40)

# 演示 'w' 清空特性
with open('demo_write.txt', 'r', encoding='utf-8') as f:
    before = f.read()

with open('demo_write.txt', 'w', encoding='utf-8') as f:
    f.write('覆盖后的新内容\n')

with open('demo_write.txt', 'r', encoding='utf-8') as f:
    after = f.read()

print(f"'w' 模式写入前: {repr(before[:30])}...")
print(f"'w' 模式写入后: {repr(after)}")
print(">>> 结论: 'w' 模式会清空原内容！")

# ========== 5. 二进制模式读写 ==========
print("\n" + "=" * 40)
print("5. 二进制模式（'rb' / 'wb'）")
print("=" * 40)

# 写入二进制数据
data = bytes([72, 101, 108, 108, 111, 32, 66, 105, 110, 97, 114, 121])
with open('demo_binary.bin', 'wb') as f:
    f.write(data)
print(f"已写入二进制文件 demo_binary.bin，内容: {data}")

# 读取二进制数据
with open('demo_binary.bin', 'rb') as f:
    binary_data = f.read()
print(f"读取二进制数据: {binary_data}")
print(f"解码为文本: {binary_data.decode('ascii')}")

# ========== 6. with 语句详解（上下文管理器） ==========
print("\n" + "=" * 40)
print("6. with 语句详解")
print("=" * 40)

# with 语句：离开代码块时自动关闭文件，即使发生异常也能正确关闭
print("使用 with 的代码结构：")
print("  with open('file', 'r') as f:")
print("      # 在这里操作文件")
print("  # 离开缩进后，文件自动关闭\n")

# 演示：with 内部的异常不会导致文件未关闭
try:
    with open('demo_write.txt', 'r', encoding='utf-8') as f:
        print(f"  文件已打开: {not f.closed}")
        raise RuntimeError("模拟 with 内部发生异常")
except RuntimeError:
    # 即使异常发生，f 已被自动关闭
    print("  RuntimeError 被捕获")
    # 注意：这里无法访问 f，因为它已经在 with 块外了

# ========== 7. 文件指针操作 ==========
print("\n" + "=" * 40)
print("7. 文件指针：seek() 和 tell()")
print("=" * 40)

with open('demo_write.txt', 'r', encoding='utf-8') as f:
    print(f"初始指针位置: {f.tell()}")          # 0
    f.read(3)                                    # 读取3个字符
    print(f"读取3个字符后指针: {f.tell()}")      # 指针前移
    f.seek(0)                                    # 回到开头
    print(f"seek(0) 后指针: {f.tell()}")         # 0
    print(f"重新读取全部: {f.read().strip()}")

# ========== 8. 文件模式对照表 ==========
print("\n" + "=" * 40)
print("8. 文件打开模式汇总")
print("=" * 40)

modes = {
    'r':  '只读，文件必须存在',
    'w':  '只写，存在则清空，不存在则创建',
    'a':  '追加写，存在则追加，不存在则创建',
    'x':  '排他创建，文件存在则报错',
    'r+': '读写，文件必须存在，指针在开头',
    'w+': '读写，存在则清空，不存在则创建',
    'a+': '读写，存在则追加，不存在则创建',
    'rb': '二进制只读',
    'wb': '二进制只写',
}
for mode, desc in modes.items():
    print(f"  '{mode}': {desc}")

print("\n文件读写操作演示完成！")
