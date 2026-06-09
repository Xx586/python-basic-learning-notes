"""
Demo 2: 路径操作
演示：os.path 和 pathlib 路径操作、路径拼接、文件遍历、目录创建

运行方式：python 2_path_operations.py
"""

import os
from pathlib import Path

# ========== 1. os.path 基本操作 ==========
print("=" * 40)
print("1. os.path 基本操作")
print("=" * 40)

# 获取当前工作目录和脚本路径
cwd = os.getcwd()
script_path = os.path.abspath(__file__)
print(f"当前工作目录: {cwd}")
print(f"当前脚本路径: {script_path}")

# 路径拼接（自动处理分隔符）
data_path = os.path.join(cwd, 'data', 'files')
print(f"拼接的路径: {data_path}")

# 路径拆分
file_path = '/home/user/project/data.csv'
print(f"\n原始路径: {file_path}")
print(f"  basename: {os.path.basename(file_path)}")    # data.csv
print(f"  dirname:  {os.path.dirname(file_path)}")     # /home/user/project
print(f"  splitext: {os.path.splitext(file_path)}")    # ('.../data', '.csv')

# 判断文件/目录
print(f"\n当前工作目录是否存在: {os.path.exists(cwd)}")
print(f"当前脚本是否是文件: {os.path.isfile(script_path)}")
print(f"当前工作目录是否是目录: {os.path.isdir(cwd)}")

# ========== 2. pathlib 基本操作 ==========
print("\n" + "=" * 40)
print("2. pathlib 基本操作（推荐）")
print("=" * 40)

# 创建 Path 对象
home = Path.home()      # 用户主目录
current = Path.cwd()    # 当前工作目录
script = Path(__file__) # 当前脚本

print(f"用户主目录: {home}")
print(f"当前工作目录: {current}")
print(f"当前脚本: {script}")

# 用 / 运算符拼接路径（pathlib 的核心特性）
project = Path.home() / 'my_project' / 'data'
print(f"\n/ 运算符拼接: {project}")

# Path 对象的常用属性
p = Path('/Users/name/project/data.csv')
print(f"\n路径: {p}")
print(f"  .name:    {p.name}")      # data.csv
print(f"  .stem:    {p.stem}")      # data
print(f"  .suffix:  {p.suffix}")    # .csv
print(f"  .parent:  {p.parent}")    # /Users/name/project
print(f"  .parents: {[str(x) for x in p.parents]}")
# parents[0] = /Users/name/project
# parents[1] = /Users/name
# parents[2] = /Users
# parents[3] = /

# ========== 3. os.path vs pathlib 对比 ==========
print("\n" + "=" * 40)
print("3. os.path vs pathlib 对比")
print("=" * 40)

# 对比表
comparisons = [
    ("路径拼接", 'os.path.join("a", "b")', 'Path("a") / "b"'),
    ("判断存在", 'os.path.exists("a")', 'Path("a").exists()'),
    ("文件名",   'os.path.basename(p)', 'Path(p).name'),
    ("扩展名",   'os.path.splitext(p)[1]', 'Path(p).suffix'),
    ("遍历目录", 'os.listdir(".")', 'Path(".").iterdir()'),
    ("递归搜索", 'glob.glob("**/*.py")', 'Path(".").rglob("*.py")'),
]
print(f"{'功能':<10} {'os.path':<30} {'pathlib':<30}")
print("-" * 70)
for func, os_way, pl_way in comparisons:
    print(f"{func:<10} {os_way:<30} {pl_way:<30}")

# ========== 4. 创建和删除目录 ==========
print("\n" + "=" * 40)
print("4. 创建和删除目录")
print("=" * 40)

# 创建一个临时目录做演示
demo_dir = Path('demo_directory')
sub_dir = demo_dir / 'sub1' / 'sub2'

# mkdir(parents=True) 递归创建；exist_ok=True 已存在不报错
sub_dir.mkdir(parents=True, exist_ok=True)
print(f"已创建目录: {sub_dir}")

# 在目录中创建文件
note = sub_dir / '笔记.txt'
note.write_text('这是 pathlib 创建的笔记\n', encoding='utf-8')
print(f"已创建文件: {note}")

# 读取文件内容
content = note.read_text(encoding='utf-8')
print(f"文件内容: {content.strip()}")

# 清理临时目录（递归删除）
import shutil
shutil.rmtree(demo_dir)
print(f"已删除临时目录: {demo_dir}")

# ========== 5. 遍历目录 ==========
print("\n" + "=" * 40)
print("5. 遍历目录")
print("=" * 40)

# 先创建一些测试文件和目录
test_dir = Path('traverse_demo')
test_dir.mkdir(exist_ok=True)
(test_dir / 'a.py').write_text('', encoding='utf-8')
(test_dir / 'b.txt').write_text('', encoding='utf-8')
(test_dir / 'c.py').write_text('', encoding='utf-8')
sub = test_dir / 'subdir'
sub.mkdir(exist_ok=True)
(sub / 'd.py').write_text('', encoding='utf-8')
(sub / 'e.csv').write_text('', encoding='utf-8')

# iterdir()：列出当前目录（不递归）
print(f"\n{test_dir}/ 下的内容（不递归）:")
for item in test_dir.iterdir():
    type_label = '📁' if item.is_dir() else '📄'
    print(f"  {type_label} {item.name}")

# glob()：模式匹配（不递归）
print(f"\n{test_dir}/ 下的 .py 文件（不递归）:")
for py_file in test_dir.glob('*.py'):
    print(f"  {py_file.name}")

# rglob()：递归模式匹配
print(f"\n{test_dir}/ 下的 .py 文件（递归）:")
for py_file in test_dir.rglob('*.py'):
    print(f"  {py_file}")

# 清理
shutil.rmtree(test_dir)

# ========== 6. 获取脚本所在目录（重要！） ==========
print("\n" + "=" * 40)
print("6. 获取脚本所在目录")
print("=" * 40)

# 场景：脚本运行时，当前工作目录 != 脚本所在目录
# 用 __file__ 获取脚本本身的路径
script_dir = Path(__file__).parent
print(f"当前工作目录 (cwd):      {Path.cwd()}")
print(f"脚本所在目录 (__file__):  {script_dir}")

# 正确做法：基于脚本目录构建数据文件路径
data_file = script_dir / 'data.txt'
print(f"基于脚本目录的数据路径: {data_file}")
print(">>> 这样无论在哪执行脚本，都能找到数据文件")

# ========== 7. 文件信息与批量操作 ==========
print("\n" + "=" * 40)
print("7. 文件信息与批量操作")
print("=" * 40)

# 创建一个文件来获取信息
demo_file = Path('path_demo_file.txt')
demo_file.write_text('Python 路径操作演示\n' * 10, encoding='utf-8')

stat = demo_file.stat()
print(f"文件: {demo_file}")
print(f"  大小: {stat.st_size} 字节")
print(f"  创建时间: {stat.st_ctime}")
print(f"  修改时间: {stat.st_mtime}")

# 用 with_suffix() 改扩展名
renamed = demo_file.with_suffix('.md')
print(f"\n改扩展名: {demo_file} -> {renamed}")

# 用 with_name() 改名
print(f"改名: {demo_file.with_name('new_name.txt')}")

# 清理
demo_file.unlink()

print("\n路径操作演示完成！")
