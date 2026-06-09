"""
Demo 8：学员类 - 学生信息管理系统

演示 __init__ 初始化属性，__str__ 控制输出格式
"""


class Student(object):
    """学员类：封装学员的属性信息"""

    def __init__(self, name, age, gender, mobile, description):
        """初始化学员属性"""
        self.name = name
        self.age = age
        self.gender = gender
        self.mobile = mobile
        self.description = description

    def __str__(self):
        """print(student) 时自动调用，输出可读信息而不是内存地址"""
        return f"{self.name}\t{self.age}\t{self.gender}\t{self.mobile}\t{self.description}"


if __name__ == '__main__':
    # 创建学员对象
    s1 = Student("小明", 18, "男", "10086", "算法工程师")
    s2 = Student("小红", 16, "女", "10000", "程序员")

    print(s1)  # 自动调用 __str__
    print(s2)

    # __dict__：查看实例属性字典
    print("\n学员属性字典:", s1.__dict__)
