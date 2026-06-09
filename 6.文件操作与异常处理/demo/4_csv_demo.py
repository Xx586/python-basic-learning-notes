"""
Demo 4: CSV 读写
演示：csv.reader/writer、csv.DictReader/DictWriter、编码处理（Excel的gbk）、delimiter参数

运行方式：python 4_csv_demo.py
"""

import csv
import os

# ========== 准备工作：清理旧文件 ==========
for f in ['demo_basic.csv', 'demo_dict.csv', 'demo_filter.csv', 'demo_gbk.csv',
          'demo_tsv.tsv', 'demo_quoted.csv']:
    try:
        os.remove(f)
    except FileNotFoundError:
        pass

# ========== 1. csv.reader 基本读取 ==========
print("=" * 40)
print("1. csv.reader 基本读取")
print("=" * 40)

# 先创建示例 CSV 文件
with open('demo_basic.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['姓名', '年龄', '城市', '分数'])
    writer.writerow(['张三', '25', '北京', '85'])
    writer.writerow(['李四', '30', '上海', '92'])
    writer.writerow(['王五', '28', '广州', '78'])
print("已创建 demo_basic.csv")

# 用 csv.reader 读取
with open('demo_basic.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    print("\n用 csv.reader 读取（每行是列表）：")
    for row in reader:
        print(f"  {row}")

# ========== 2. csv.writer 写入 ==========
print("\n" + "=" * 40)
print("2. csv.writer 写入")
print("=" * 40)

# writerow()：逐行写入
# writerows()：批量写入
data = [
    ['商品', '价格', '库存'],
    ['苹果', '5.5', '100'],
    ['香蕉', '3.0', '200'],
    ['橙子', '4.5', '150'],
]

with open('demo_basic.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)  # 批量写入
print("已用 writerows() 批量写入商品数据到 demo_basic.csv")

# ========== 3. csv.DictReader 字典方式读取（推荐） ==========
print("\n" + "=" * 40)
print("3. csv.DictReader 字典方式读取（推荐）")
print("=" * 40)

# 重新写一个带表头的 CSV 用于 DictReader 演示
with open('demo_basic.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['姓名', '年龄', '城市'])
    writer.writerow(['张三', '25', '北京'])
    writer.writerow(['李四', '30', '上海'])

# DictReader：自动用第一行做表头，每行返回字典
with open('demo_basic.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    print(f"自动检测的表头: {reader.fieldnames}")
    print("\n用 DictReader 读取（每行是字典）：")
    for row in reader:
        # 用字段名访问，比 row[0] 更可读
        print(f"  {row['姓名']} | {row['年龄']}岁 | 来自{row['城市']}")

# ========== 4. csv.DictWriter 字典方式写入（推荐） ==========
print("\n" + "=" * 40)
print("4. csv.DictWriter 字典方式写入（推荐）")
print("=" * 40)

# 定义表头
fieldnames = ['ID', '姓名', '分数', '等级']

students = [
    {'ID': '001', '姓名': '赵六', '分数': 88, '等级': 'B'},
    {'ID': '002', '姓名': '孙七', '分数': 95, '等级': 'A'},
    {'ID': '003', '姓名': '周八', '分数': 73, '等级': 'C'},
]

with open('demo_dict.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    # 必须先写表头！
    writer.writeheader()

    # 逐行写入
    for student in students:
        writer.writerow(student)

print("已用 DictWriter 写入 demo_dict.csv")

# 读回来验证
with open('demo_dict.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    print("验证读取：")
    for row in reader:
        print(f"  {row['ID']}: {row['姓名']} - {row['分数']}分 ({row['等级']})")

# ========== 5. writerow vs writerows 对比 ==========
print("\n" + "=" * 40)
print("5. writerow() vs writerows()")
print("=" * 40)

print("writerow(row):  写入一行（传单个 list/dict）")
print("writerows(rows): 批量写入多行（传 list 的 list/dict）")
print("\n示例：")
print("  writer.writerow(['a', 'b', 'c'])       # 写1行")
print("  writer.writerows([['a','b'], ['c','d']]) # 写2行")

# ========== 6. 编码问题：处理 Excel 的 gbk 编码 ==========
print("\n" + "=" * 40)
print("6. 编码问题：Excel 的 gbk 编码")
print("=" * 40)

# 模拟：用 gbk 编码写入（模拟 Excel 导出的文件）
with open('demo_gbk.csv', 'w', encoding='gbk', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['姓名', '部门', '工资'])
    writer.writerow(['张三', '技术部', '15000'])
    writer.writerow(['李四', '市场部', '12000'])
print("已用 gbk 编码写入 demo_gbk.csv（模拟 Excel 导出）")

# ❌ 如果用 utf-8 读 → 报错
print("\n尝试用 utf-8 读取 gbk 文件：")
try:
    with open('demo_gbk.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
except UnicodeDecodeError as e:
    print(f"  ✗ UnicodeDecodeError: {e}")

# ✅ 用 gbk 正确读取
print("\n用 gbk 编码正确读取：")
with open('demo_gbk.csv', 'r', encoding='gbk') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"  {row['姓名']} | {row['部门']} | {row['工资']}元")

# ✅ 推荐的写入方式：用 utf-8-sig（Excel 能正确识别中文）
print("\n推荐：写入时用 utf-8-sig 编码（兼容 Excel）：")
with open('demo_basic.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['名称', '数量'])
    writer.writerow(['苹果', '100'])
print("  用 utf-8-sig 写入，Excel 能直接打开不乱码")

# ========== 7. delimiter 自定义分隔符（TSV 等） ==========
print("\n" + "=" * 40)
print("7. delimiter 自定义分隔符")
print("=" * 40)

# TSV（Tab-Separated Values）用 Tab 作为分隔符
with open('demo_tsv.tsv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerow(['姓名', '年龄', '城市'])
    writer.writerow(['张三', '25', '北京'])

print("已写入 TSV 文件（Tab 分隔）：")
with open('demo_tsv.tsv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        print(f"  {row}")

# ========== 8. quotechar 和 quoting 参数 ==========
print("\n" + "=" * 40)
print("8. quotechar / quoting 处理含逗号字段")
print("=" * 40)

# 字段内容包含逗号时，需要用引号包裹
data_with_commas = [
    ['姓名', '简介'],
    ['张三', '喜欢读书，游泳，爬山'],     # 简介中有逗号
    ['公司A', '地址：北京，朝阳区'],      # 地址中有逗号
]

# QUOTE_MINIMAL（默认）：仅在需要时加引号
with open('demo_quoted.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    writer.writerows(data_with_commas)
print("QUOTE_MINIMAL（仅在需要时加引号）：")
with open('demo_quoted.csv', 'r', encoding='utf-8') as f:
    print(f.read())

# QUOTE_ALL：所有字段都加引号
with open('demo_quoted.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    writer.writerows(data_with_commas)
print("QUOTE_ALL（所有字段加引号）：")
with open('demo_quoted.csv', 'r', encoding='utf-8') as f:
    print(f.read())

# ========== 9. 实战：CSV 筛选过滤 ==========
print("=" * 40)
print("9. 实战：CSV 筛选过滤")
print("=" * 40)

# 创建测试数据
with open('demo_basic.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['姓名', '年龄', '城市'])
    writer.writerows([
        ['张三', '25', '北京'],
        ['小明', '12', '上海'],   # 未成年
        ['李四', '30', '广州'],
        ['小红', '16', '深圳'],   # 未成年
        ['王五', '28', '杭州'],
    ])

# 筛选成年人（年龄 >= 18）
adults = []
with open('demo_basic.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if int(row['年龄']) >= 18:
            adults.append(row)

# 写出筛选结果
with open('demo_filter.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['姓名', '年龄', '城市'])
    writer.writeheader()
    writer.writerows(adults)

print("原始数据 5 条记录")
print(f"筛选成年人（>=18岁）: {len(adults)} 条记录")
print("已写入 demo_filter.csv")
with open('demo_filter.csv', 'r', encoding='utf-8-sig') as f:
    print(f.read())

# ========== 10. CSV 读写要点总结 ==========
print("=" * 40)
print("10. CSV 读写要点总结")
print("=" * 40)
tips = [
    "open() 必须加 newline=''，否则 Windows 上多空行",
    "csv.reader 读取的字段全部是字符串，需手动转换 int/float",
    "DictWriter 必须先 writeheader() 再写数据",
    "Excel 导出的 CSV 可能是 gbk 编码，读时指定 encoding='gbk'",
    "写入让 Excel 打开的 CSV 用 encoding='utf-8-sig'",
    "字段含分隔符时会自动加引号包裹，正常现象",
]
for i, tip in enumerate(tips, 1):
    print(f"  {i}. {tip}")

print("\nCSV 读写演示完成！")
