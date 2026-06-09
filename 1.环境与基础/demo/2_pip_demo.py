# -*- coding: utf-8 -*-
"""
Demo 2: pip 包管理演示

本 Demo 演示：
  1. 在 Python 代码中检查包是否已安装
  2. 尝试导入常用第三方库并获取版本信息
  3. 以注释形式展示常用 pip 命令及输出示例
  4. 如何导出和查看依赖清单

运行方式：
  python3 demo/2_pip_demo.py

注意：
  本 Demo 部分依赖（如 requests、numpy）可能未安装，
  这是正常的——这正是 pip 存在的意义。
  看完本 Demo 后，请在终端中尝试用 pip 安装它们。
"""

import sys
import importlib
import subprocess


# ============================================================
# Part 1: 检查第三方包是否已安装
# ============================================================
print("=" * 55)
print("Part 1: 检查常用第三方包安装状态")
print("=" * 55)

# 列出需要检查的包：(包名, 用途简介)
packages_to_check = [
    ("requests", "HTTP 请求库 —— 发送网络请求"),
    ("numpy", "数值计算库 —— 高效数组和矩阵运算"),
    ("pandas", "数据分析库 —— 表格数据处理"),
    ("flask", "Web 框架 —— 快速搭建网站后端"),
    ("pytest", "测试框架 —— 编写和运行自动化测试"),
]

installed_count = 0
for pkg_name, description in packages_to_check:
    try:
        module = importlib.import_module(pkg_name)
        version = getattr(module, "__version__", "未知版本")
        print(f"  [已安装] {pkg_name:12s} | {description:30s} | 版本: {version}")
        installed_count += 1
    except ImportError:
        print(f"  [未安装] {pkg_name:12s} | {description:30s}")

print(f"\n安装情况: {installed_count}/{len(packages_to_check)} 个包已安装")


# ============================================================
# Part 2: 演示 pip 命令（注释展示，含模拟输出）
# ============================================================
print("\n" + "=" * 55)
print("Part 2: 常用 pip 命令速查")
print("=" * 55)
print("以下是在终端中执行的 pip 命令及预期输出：")
print("-" * 55)

# --- 2.1 查看 pip 版本 ---
print("""
# --- 查看 pip 版本 ---
$ pip3 --version

输出示例:
pip 24.0 from /usr/local/lib/python3.12/site-packages/pip (python 3.12)
""")

# --- 2.2 列出已安装的包 ---
print("""
# --- 列出所有已安装的包 ---
$ pip3 list

输出示例:
Package    Version
---------- -------
pip         24.0
setuptools  69.0.3
wheel       0.42.0
""")

# --- 2.3 安装包 ---
print("""
# --- 安装第三方包 ---
$ pip3 install requests

输出示例:
Collecting requests
  Downloading requests-2.31.0-py3-none-any.whl (62 kB)
     ━━━━━━━━━━━━━━━━━━━━ 62.1/62.1 kB 1.2 MB/s
Collecting urllib3<3,>=1.21.1
  Downloading urllib3-2.2.1-py3-none-any.whl (121 kB)
     ━━━━━━━━━━━━━━━━━━━━ 121.3/121.3 kB 3.4 MB/s
Successfully installed requests-2.31.0 urllib3-2.2.1
""")

# --- 2.4 安装指定版本 ---
print("""
# --- 安装指定版本的包 ---
$ pip3 install numpy==1.24.3

需要精确控制版本时使用 "==" 语法。
这在团队协作和部署时非常重要。
""")

# --- 2.5 查看包详细信息 ---
print("""
# --- 查看包的详细信息 ---
$ pip3 show requests

输出示例:
Name: requests
Version: 2.31.0
Summary: Python HTTP for Humans.
Home-page: https://requests.readthedocs.io
Author: Kenneth Reitz
License: Apache 2.0
Location: /usr/local/lib/python3.12/site-packages
Requires: certifi, charset-normalizer, idna, urllib3
""")

# --- 2.6 升级包 ---
print("""
# --- 升级已安装的包 ---
$ pip3 install --upgrade requests

# --- 升级 pip 自身 ---
$ pip3 install --upgrade pip
""")

# --- 2.7 导出依赖 ---
print("""
# --- 导出当前环境所有依赖到文件 ---
$ pip3 freeze > requirements.txt

# 查看生成的文件内容
$ cat requirements.txt

输出示例:
certifi==2024.2.2
charset-normalizer==3.3.2
idna==3.6
requests==2.31.0
urllib3==2.2.1
""")

# --- 2.8 从文件批量安装 ---
print("""
# --- 从 requirements.txt 批量安装 ---
$ pip3 install -r requirements.txt

这在拿到新项目代码后非常有用：一行命令还原所有依赖！
""")


# ============================================================
# Part 3: 国内换源加速
# ============================================================
print("=" * 55)
print("Part 3: 国内镜像源 — 下载加速")
print("=" * 55)

print("""
为什么需要换源？
  PyPI 官方源位于海外，国内下载速度可能非常慢（几十 KB/s）。
  切换到国内镜像源后，速度可达数 MB/s。

常用国内镜像源：
  清华:   https://pypi.tuna.tsinghua.edu.cn/simple
  阿里云: https://mirrors.aliyun.com/pypi/simple
  中科大: https://pypi.mirrors.ustc.edu.cn/simple
  豆瓣:   https://pypi.douban.com/simple

临时换源（单次安装）：
  $ pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple requests

永久换源（一劳永逸）：
  $ pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
  $ pip3 config set global.trusted-host pypi.tuna.tsinghua.edu.cn

验证配置：
  $ pip3 config list
""")


# ============================================================
# Part 4: pip 相关安全提醒
# ============================================================
print("=" * 55)
print("Part 4: 安全提醒")
print("=" * 55)

print("""
重要注意事项：

1. 永远不要使用 sudo pip install
   - sudo 会以 root 身份安装包到系统目录
   - 可能覆盖操作系统依赖，导致系统工具故障
   - 正确做法：使用虚拟环境（参见 Demo 3）

2. 使用 pip freeze 时要谨慎
   - 它会导出当前环境的所有包（包括依赖的依赖）
   - 在虚拟环境中使用才能得到精确清单
   - 记得将 requirements.txt 纳入版本管理

3. 安装前确认包名
   - 有些恶意包会取和流行包相似的名字（typo-squatting）
   - 始终从官方文档确认正确的包名
   - 优先选择下载量大、维护活跃的包

4. 避免安装到系统 Python
   - 推荐每个项目使用独立的虚拟环境
   - 这样即使环境出问题，也不会影响其他项目
""")


# ============================================================
# Part 5: 动手实践引导
# ============================================================
print("=" * 55)
print("Part 5: 动手实践")
print("=" * 55)

print("""
请按照以下步骤动手体验 pip：

步骤 1: 打开终端，执行以下命令查看当前环境
  $ pip3 list
  $ pip3 --version

步骤 2: 安装一个简单的包试试
  $ pip3 install requests

步骤 3: 在 Python 中导入使用
  $ python3 -c "import requests; print(requests.__version__)"

步骤 4: 尝试导出依赖（创建虚拟环境后效果更佳 — 参见 Demo 3）
  $ pip3 freeze > my_requirements.txt
  $ cat my_requirements.txt

步骤 5: 如果觉得慢，配置国内镜像源
  $ pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
""")


print("=" * 55)
print("Demo 2 演示完成！")
print("接下来请学习 Demo 3: 虚拟环境（pip 的最佳搭档）")
print("=" * 55)
