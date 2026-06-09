"""
Demo 2: 字符串操作
演示：索引/切片、格式化、常用方法（split/join/strip/replace/find/大小写）

运行方式：python 2_string_operations.py
"""

# ========== 1. 索引与切片 ==========
print("=" * 50)
print("1. 索引与切片")
print("=" * 50)

s = "Hello World"

# 索引
print(f"字符串: '{s}'")
print(f"正向索引 s[0] = '{s[0]}'")
print(f"正向索引 s[6] = '{s[6]}'")
print(f"反向索引 s[-1] = '{s[-1]}'")
print(f"反向索引 s[-3] = '{s[-3]}'")

# 切片（start:end:step）
print(f"\n基本切片：")
print(f"  s[0:5] = '{s[0:5]}'     (索引 0~4)")
print(f"  s[6:11] = '{s[6:11]}'    (索引 6~10)")
print(f"  s[:5] = '{s[:5]}'       (省略 start，从 0 开始)")
print(f"  s[6:] = '{s[6:]}'       (省略 end，到末尾)")
print(f"  s[:] = '{s[:]}'         (全部)")

print(f"\n步长切片：")
print(f"  s[::2] = '{s[::2]}'     (每隔一个取一个)")
print(f"  s[1:8:2] = '{s[1:8:2]}' (从索引 1 到 7，步长为 2)")

# 反转字符串（经典技巧！）
print(f"\n反转字符串：")
print(f"  s[::-1] = '{s[::-1]}'   (反向遍历)")

# 切片不会越界
print(f"\n切片不会越界：")
print(f"  s[0:100] = '{s[0:100]}' (不报错，返回到末尾)")

# ========== 2. 字符串格式化 ==========
print("\n" + "=" * 50)
print("2. 字符串格式化")
print("=" * 50)

name = "小明"
age = 25
score = 95.5

# f-string（推荐！）
print("--- f-string ---")
print(f"我叫{name}，今年{age}岁")
print(f"明年我{age + 1}岁")
print(f"成绩{score}分，评级{'A' if score >= 90 else 'B'}")

# 格式化数字
price = 19.999
print(f"价格: {price:.2f}")       # 保留两位小数
num = 1234567
print(f"数量: {num:,}")            # 千位分隔符

# 对齐与填充
print(f"\n对齐与填充：")
print(f"{'左对齐':<10}|")
print(f"{'居中对齐':^10}|")
print(f"{'右对齐':>10}|")
print(f"{'填充':*^10}")

# .format() 方法
print("\n--- .format() ---")
print("我叫{}，今年{}岁".format("小明", 25))
print("{0}和{1}是好朋友".format("小明", "小红"))
print("我叫{name}，今年{age}岁".format(name="小明", age=25))

# % 格式化（老式）
print("\n--- % 格式化 ---")
print("我叫%s，今年%d岁" % ("小明", 25))
print("价格: %.2f" % 19.999)

# ========== 3. 常用方法 ==========
print("\n" + "=" * 50)
print("3. 常用字符串方法")
print("=" * 50)

# split() — 分割
print("--- split() ---")
s = "apple,banana,orange"
print(f"原字符串: '{s}'")
print(f"split(','): {s.split(',')}")
s2 = "hello world python"
print(f"split(): {s2.split()}  (默认按空白分割)")
print(f"split(' ', 1): {s2.split(' ', 1)}  (限制分割次数)")

# join() — 连接
print("\n--- join() ---")
words = ["apple", "banana", "orange"]
print(f"','.join(words): '{','.join(words)}'")
print(f"' - '.join(words): '{' - '.join(words)}'")

# strip() — 去除空白
print("\n--- strip() ---")
s = "  hello world  \n"
print(f"原字符串: {repr(s)}")
print(f"strip(): {repr(s.strip())}")
print(f"lstrip(): {repr(s.lstrip())}")
print(f"rstrip(): {repr(s.rstrip())}")
print(f"strip('#'): {repr('###hello###'.strip('#'))}")

# replace() — 替换
print("\n--- replace() ---")
s = "hello world"
new_s = s.replace("world", "Python")
print(f"原字符串: '{s}'")
print(f"replace 后: '{new_s}'")
print(f"原字符串没变: '{s}'  (不可变！)")
print(f"限制替换: '{'aaa'.replace('a', 'b', 2)}'")

# find() — 查找
print("\n--- find() ---")
s = "hello world"
print(f"find('o'): {s.find('o')}       (第一个 'o')")
print(f"rfind('o'): {s.rfind('o')}     (最后一个 'o')")
print(f"find('z'): {s.find('z')}        (找不到返回 -1)")

# startswith() / endswith()
print("\n--- startswith() / endswith() ---")
filename = "report.pdf"
print(f"endswith('.pdf'): {filename.endswith('.pdf')}")
print(f"startswith('rep'): {filename.startswith('rep')}")

# 大小写转换
print("\n--- 大小写转换 ---")
s = "Hello World"
print(f"upper(): '{s.upper()}'")
print(f"lower(): '{s.lower()}'")
print(f"title(): '{s.title()}'")
print(f"capitalize(): '{s.capitalize()}'")
print(f"swapcase(): '{s.swapcase()}'")

# count() — 计数
print("\n--- count() ---")
s = "banana"
print(f"'{s}'.count('a'): {s.count('a')}")
print(f"'{s}'.count('na'): {s.count('na')}")

# ========== 4. 字符串不可变性演示 ==========
print("\n" + "=" * 50)
print("4. 字符串不可变 — 重要！")
print("=" * 50)

s = "hello"
print(f"原字符串: '{s}'")
s.replace("h", "H")      # 返回值被丢弃了！
print(f"replace 后（没接收返回值）: '{s}'")   # 还是 "hello"！

# 正确做法
s = s.replace("h", "H")   # 接收返回值
print(f"正确做法后: '{s}'")

print("\n✅ Demo 2 运行完毕！")
