"""
Demo 8：学生管理系统 - 程序入口

演示：
- if __name__ == '__main__' 的作用
- 面向对象编程的项目启动方式

运行方式：在终端中 cd 到本目录，执行 python main.py
"""

from studentcms import StudentCms

if __name__ == '__main__':
    # 创建管理系统对象并启动
    student_cms = StudentCms()
    student_cms.start()
