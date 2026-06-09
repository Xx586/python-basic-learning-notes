"""
Demo 8：学生管理系统类 - 学生信息管理系统

演示面向对象综合应用：
- 实例方法：增删改查
- @staticmethod：显示菜单
- __dict__：对象序列化
- 文件读写：数据持久化
"""

from student import Student


class StudentCms(object):
    """学生管理系统：管理所有学员"""

    def __init__(self):
        """初始化空的学生列表"""
        self.student_list = []

    @staticmethod
    def show_operate_view():
        """显示操作菜单 - 静态方法：不依赖实例数据"""
        print("*" * 40)
        print("学生管理系统 V2.0")
        print("\t1.添加学生")
        print("\t2.修改学生")
        print("\t3.删除学生")
        print("\t4.查询某个学生")
        print("\t5.显示所有学生")
        print("\t6.保存信息")
        print("\t0.退出系统")
        print("*" * 40)

    def start(self):
        """系统主循环 - 调度中心"""
        self.load_student()  # 启动时加载已有数据
        while True:
            self.show_operate_view()
            try:
                number = int(input("请输入操作序号:"))
            except ValueError:
                print("请输入数字！")
                continue

            if number == 1:
                print("----------1.添加学生------------")
                self.add_student()
            elif number == 2:
                print("----------2.修改学生------------")
                self.update_student()
            elif number == 3:
                print("----------3.删除学生------------")
                self.delete_student()
            elif number == 4:
                print("----------4.查询某个学生-----------")
                self.query_student()
            elif number == 5:
                print("----------5.显示所有学生-----------")
                self.show_all_student()
            elif number == 6:
                print("----------6.保存信息-----------")
                self.save_student()
            elif number == 0:
                out = input("您是否真的确认退出(Y/N):")
                if out.lower() == "y":
                    print("感谢使用，下次再见！")
                    break
            else:
                print("您选中的序号暂不存在，敬请期待~")

    def add_student(self):
        """添加学员"""
        name = input("请输入要添加的姓名:")
        age = int(input("请输入要添加的年龄:"))
        gender = input("请输入要添加的性别:")
        mobile = input("请输入要添加的联系方式:")
        description = input("请输入要添加的简介信息:")

        # 创建学员对象
        student = Student(name, age, gender, mobile, description)
        print(student)
        # 添加到列表
        self.student_list.append(student)
        print("学生信息已添加成功!!")

    def show_all_student(self):
        """显示所有学员信息"""
        print('\t姓名\t年龄\t性别\t手机\t备注')
        for student in self.student_list:
            print(student)  # 自动调用 Student.__str__

    def delete_student(self):
        """删除学员 - for...else 处理找不到学员的情况"""
        delete_name = input("请输入要删除的学生姓名:")
        for student in self.student_list:
            if student.name == delete_name:
                self.student_list.remove(student)
                print(f"学生信息已删除成功.{student.name}")
                break
        else:
            # for 循环没有被 break 中断时执行
            print("您要删除的学生不存在...")

    def update_student(self):
        """修改学员信息"""
        name = input("请输入要修改的学生姓名:")
        for student in self.student_list:
            if student.name == name:
                student.age = int(input("请输入要添加的年龄:"))
                student.gender = input("请输入要添加的性别:")
                student.mobile = input("请输入要添加的联系方式:")
                student.description = input("请输入要添加的简介信息:")
                print("学生信息:", student)
                break
        else:
            print("您要修改的学生信息不存在...")

    def query_student(self):
        """查询某个学员"""
        query_name = input("请输入要查询的学生姓名:")
        for student in self.student_list:
            if query_name in student.name:
                print(student)
                break
        else:
            print("您要查找的学生不存在...")

    def save_student(self):
        """保存学员信息到文件 - 用 __dict__ 将对象转字典"""
        # 将学员对象列表转为字典列表
        data = [student.__dict__ for student in self.student_list]
        with open("student.data", "w", encoding="utf-8") as f:
            f.write(str(data))
        print("学生信息已保存成功!!")

    def load_student(self):
        """从文件加载学员信息 - 启动时调用"""
        try:
            with open("student.data", "r", encoding="utf-8") as f:
                content = f.read()
            if content:
                # eval 将字符串还原为 Python 列表
                data_list = eval(content)
                self.student_list = [
                    Student(d["name"], d["age"], d["gender"],
                            d["mobile"], d["description"])
                    for d in data_list
                ]
        except FileNotFoundError:
            # 第一次运行，文件还不存在
            pass
