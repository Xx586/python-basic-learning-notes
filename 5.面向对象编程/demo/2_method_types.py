"""
Demo 2: 方法类型
演示：实例方法、类方法、静态方法、@property

运行方式：python 2_method_types.py
"""


class Student:
    """演示四种方法类型"""
    school = "第一中学"  # 类属性
    student_count = 0    # 类属性：统计学生总数

    def __init__(self, name, score):
        self.name = name
        self._score = score  # 保护属性
        Student.student_count += 1

    # ---- 实例方法（最常见） ----
    def introduce(self):
        """实例方法：操作实例数据"""
        return f"我叫{self.name}，{self._score}分"

    # ---- 类方法 ----
    @classmethod
    def change_school(cls, new_name):
        """类方法：修改类属性"""
        print(f"学校改名：{cls.school} → {new_name}")
        cls.school = new_name

    @classmethod
    def from_string(cls, info_str):
        """工厂方法：从字符串创建实例"""
        name, score = info_str.split(",")
        return cls(name, int(score))

    # ---- 静态方法 ----
    @staticmethod
    def grade_level(score):
        """静态方法：工具函数"""
        if score >= 90:
            return "优秀"
        elif score >= 80:
            return "良好"
        elif score >= 60:
            return "及格"
        else:
            return "不及格"

    # ---- @property ----
    @property
    def score(self):
        """getter：读取分数"""
        return self._score

    @score.setter
    def score(self, value):
        """setter：设置分数（带校验）"""
        if not 0 <= value <= 100:
            raise ValueError(f"分数必须在0-100之间，收到: {value}")
        self._score = value


# ========== 测试 ==========
print("=== 创建学生 ===")
s1 = Student("小明", 85)
s2 = Student("小红", 55)

print(s1.introduce())
print(s2.introduce())
print(f"学生总数：{Student.student_count}")

print("\n=== 类方法：修改学校 ===")
Student.change_school("第二中学")

print("\n=== 类方法：工厂方法 ===")
s3 = Student.from_string("小刚,92")
print(s3.introduce())

print("\n=== 静态方法：评级 ===")
for s in [s1, s2, s3]:
    print(f"{s.name}: {Student.grade_level(s.score)}")

print("\n=== @property：分数校验 ===")
print(f"当前分数: {s1.score}")
s1.score = 95    # 触发 setter 校验
print(f"修改后: {s1.score}")
try:
    s1.score = 150   # 触发 setter 校验失败
except ValueError as e:
    print(f"校验失败: {e}")
