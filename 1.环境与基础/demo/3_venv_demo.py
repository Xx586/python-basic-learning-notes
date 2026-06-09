# -*- coding: utf-8 -*-
"""
Demo 3: 虚拟环境演示

本 Demo 演示：
  1. 如何在代码中检测当前是否在虚拟环境中运行
  2. 虚拟环境和系统 Python 的区别
  3. 以注释形式展示虚拟环境的完整操作流程
  4. 各操作系统（macOS / Linux / Windows）的激活方式对比

运行方式：
  python3 demo/3_venv_demo.py

建议操作：
  先在终端中创建并激活一个虚拟环境，再运行本脚本观察输出差异
"""

import sys
import os
import site


# ============================================================
# Part 1: 检测当前是否在虚拟环境中
# ============================================================
print("=" * 55)
print("Part 1: 虚拟环境检测")
print("=" * 55)

# 方法 1: 比较 sys.prefix 和 sys.base_prefix
# 在虚拟环境中，这两个值不同
# 在系统 Python 中，这两个值完全相同
is_in_venv = sys.prefix != sys.base_prefix

# 方法 2: 检查 VIRTUAL_ENV 环境变量
# 激活虚拟环境后，操作系统会设置这个环境变量
venv_env = os.environ.get("VIRTUAL_ENV", None)

# 方法 3: 检查 sys.real_prefix（某些旧版本虚拟环境）
real_prefix = getattr(sys, "real_prefix", None)

print(f"Python 可执行文件路径: {sys.executable}")
print(f"sys.prefix:            {sys.prefix}")
print(f"sys.base_prefix:       {sys.base_prefix}")
print(f"VIRTUAL_ENV 环境变量:  {venv_env or '(未设置 — 未激活虚拟环境)'}")

if is_in_venv:
    print("\n>>> 检测结果: 你正在 【虚拟环境】 中运行 Python")
    print(f"    虚拟环境路径: {venv_env}")
    print("    在此环境中 pip install 的包不会影响系统 Python。")
else:
    print("\n>>> 检测结果: 你正在 【系统 Python】 中运行 Python")
    print("    推荐为每个项目创建独立的虚拟环境。")


# ============================================================
# Part 2: 查看包的安装位置
# ============================================================
print("\n" + "=" * 55)
print("Part 2: 包安装位置对比")
print("=" * 55)

# 显示当前环境的包搜索路径（site-packages）
print("当前 Python 的包搜索路径（site-packages）：")
for path in site.getsitepackages():
    print(f"  - {path}")

if is_in_venv:
    print("\n说明：以上路径在虚拟环境目录下，与系统 Python 隔离。")
else:
    print("\n说明：以上路径在系统 Python 目录下，所有项目共享。")
    print("      这就是为什么需要虚拟环境 —— 避免不同项目的包互相冲突。")


# ============================================================
# Part 3: 虚拟环境标准操作流程（注释展示）
# ============================================================
print("\n" + "=" * 55)
print("Part 3: 虚拟环境完整操作流程")
print("=" * 55)

print("""
下面以终端命令形式展示虚拟环境的完整使用流程。
请在终端中跟着操作一遍！

--- 步骤 1: 创建项目目录 ---
$ mkdir ~/my_python_project
$ cd ~/my_python_project

--- 步骤 2: 创建虚拟环境 ---
$ python3 -m venv venv

执行后，当前目录会出现一个 venv/ 文件夹，包含：
  venv/
    bin/          (Windows: Scripts/)
      python      -> Python 解释器
      pip         -> pip 包管理器
      activate    -> 激活脚本
    lib/          (Windows: Lib/)
      python3.12/
        site-packages/  -> 第三方包安装位置
    pyvenv.cfg    -> 配置文件

--- 步骤 3: 激活虚拟环境 ---
各系统激活命令不同：

  macOS / Linux:
    $ source venv/bin/activate

  Windows CMD:
    > venv\\Scripts\\activate

  Windows PowerShell:
    > venv\\Scripts\\Activate.ps1

激活后，终端提示符变为：
  (venv) $

--- 步骤 4: 验证是否成功激活 ---
(venv) $ which python3
/Users/xxx/my_python_project/venv/bin/python3
# 路径在 venv 下，说明激活成功！

(venv) $ pip list
Package    Version
---------- -------
pip        24.0
setuptools 69.0.3
# 只有基础包，证明这是干净的环境

--- 步骤 5: 在虚拟环境中安装包 ---
(venv) $ pip install requests

收集 requests... -> 下载 -> 安装到 venv/lib/.../site-packages/

--- 步骤 6: 导出依赖清单 ---
(venv) $ pip freeze > requirements.txt

--- 步骤 7: 退出虚拟环境 ---
(venv) $ deactivate

退出后终端提示符恢复为普通的 $，不再显示 (venv)。
""")


# ============================================================
# Part 4: 各系统激活方式对比速查
# ============================================================
print("=" * 55)
print("Part 4: 各操作系统激活方式速查表")
print("=" * 55)

print("""
┌──────────────────┬──────────────────────────────────┐
│  操作系统        │  激活命令                         │
├──────────────────┼──────────────────────────────────┤
│  macOS           │  source venv/bin/activate         │
│  Linux           │  source venv/bin/activate         │
│  Windows CMD     │  venv\\Scripts\\activate           │
│  Windows PS      │  venv\\Scripts\\Activate.ps1       │
├──────────────────┼──────────────────────────────────┤
│  退出（所有系统）│  deactivate                       │
└──────────────────┴──────────────────────────────────┘
""")


# ============================================================
# Part 5: .gitignore 配置提醒
# ============================================================
print("=" * 55)
print("Part 5: 版本管理提醒 — .gitignore")
print("=" * 55)

print("""
虚拟环境目录（venv/）不应该提交到 Git 仓库：

原因 1: 体积大（几十 MB 到几百 MB），push / pull 慢
原因 2: 包含本地绝对路径，在别人电脑上无法使用
原因 3: 通过 requirements.txt 完全可以重建

在项目根目录创建 .gitignore，添加以下内容：

  # Python 虚拟环境
  venv/
  .venv/
  env/
  .env/

  # Python 字节码缓存
  __pycache__/
  *.py[cod]

  # IDE 配置
  .vscode/
  .idea/

  # 系统文件
  .DS_Store
  Thumbs.db
""")


# ============================================================
# Part 6: Poetry / PDM 简介
# ============================================================
print("=" * 55)
print("Part 6: 现代包管理工具简介")
print("=" * 55)

print("""
除了 Python 内置的 venv + pip，还有更强大的工具：

1. Poetry
   - 自动解析依赖冲突
   - 使用 pyproject.toml + poetry.lock 管理依赖
   - 自动创建和管理虚拟环境
   - 适合需要发布到 PyPI 的项目

   安装: curl -sSL https://install.python-poetry.org | python3 -
   创建项目: poetry new my_project
   添加依赖: poetry add requests

2. PDM (Python Development Master)
   - 遵循 PEP 582，不需要传统虚拟环境
   - 使用本地 __pypackages__/ 目录存放依赖
   - 依赖解析速度快

   安装: pip install pdm
   初始化: pdm init
   添加依赖: pdm add requests

建议学习路径:
  初学者 → 先精通 venv + pip（基础且够用）
  进阶   → 再学习 Poetry（工业标准）
""")


# ============================================================
# Part 7: 动手实践引导
# ============================================================
print("=" * 55)
print("Part 7: 动手实践")
print("=" * 55)

print("""
请按照以下步骤动手体验虚拟环境：

步骤 1: 创建虚拟环境
  $ cd /path/to/your/practice/folder
  $ python3 -m venv my_first_venv

步骤 2: 激活虚拟环境
  $ source my_first_venv/bin/activate     (macOS/Linux)
  > my_first_venv\\Scripts\\activate       (Windows)

步骤 3: 在虚拟环境中重新运行本脚本
  (my_first_venv) $ python3 demo/3_venv_demo.py

  对比激活前和激活后 Part 1 的输出有何不同！

步骤 4: 在虚拟环境中安装一个包并测试
  (my_first_venv) $ pip install requests
  (my_first_venv) $ python3 -c "import requests; print(requests.__version__)"

步骤 5: 退出虚拟环境
  (my_first_venv) $ deactivate

步骤 6: （可选）删除虚拟环境（虚拟环境就是文件夹，删除即可）
  $ rm -rf my_first_venv
""")


print("=" * 55)
print("Demo 3 演示完成！")
print("接下来请学习 Demo 4: 代码注释风格")
print("=" * 55)
