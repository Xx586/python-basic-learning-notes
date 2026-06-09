"""
Demo 5: 魔术方法
演示：__str__/__repr__、__eq__/__lt__、__add__、__len__/__getitem__、__enter__/__exit__

运行方式：python 5_magic_methods.py
"""


# ========== 1. __str__ 与 __repr__ ==========
print("=" * 40)
print("1. __str__ 与 __repr__")
print("=" * 40)


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        """print() 时显示"""
        return f"《{self.title}》作者：{self.author}"

    def __repr__(self):
        """开发者调试时显示"""
        return f"Book(title='{self.title}', author='{self.author}')"


b = Book("Python编程", "张三")
print(f"print(): {b}")       # 使用 __str__ → 《Python编程》
print(f"repr(): {repr(b)}")   # 使用 __repr__ → Book(title=...)


# ========== 2. 比较方法 ==========
print("\n" + "=" * 40)
print("2. 比较方法：__eq__、__lt__")
print("=" * 40)


class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __eq__(self, other):
        return self.score == other.score

    def __lt__(self, other):
        return self.score < other.score

    def __repr__(self):
        return f"Student({self.name}, {self.score})"


students = [
    Student("张三", 85),
    Student("李四", 92),
    Student("王五", 78),
]

print(f"张三 == 李四？{students[0] == students[1]}")

students.sort()  # 使用 __lt__ 排序
print(f"按分数排序: {students}")


# ========== 3. 运算方法 ==========
print("\n" + "=" * 40)
print("3. 运算方法：__add__")
print("=" * 40)


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(f"v1 + v2 = {v1 + v2}")
print(f"v1 - v2 = {v1 - v2}")
print(f"v1 * 3 = {v1 * 3}")


# ========== 4. 容器模拟 ==========
print("\n" + "=" * 40)
print("4. 容器模拟：__len__、__getitem__")
print("=" * 40)


class Playlist:
    """播放列表：支持 len()、[] 访问、for 循环"""

    def __init__(self, name):
        self.name = name
        self._songs = []

    def add(self, song):
        self._songs.append(song)

    def __len__(self):
        return len(self._songs)

    def __getitem__(self, index):
        return self._songs[index]

    def __contains__(self, song):
        return song in self._songs


pl = Playlist("我的歌单")
pl.add("晴天")
pl.add("七里香")
pl.add("夜曲")

print(f"歌单: {pl.name}")
print(f"歌曲数: {len(pl)}")
print(f"第一首: {pl[0]}")
print(f"有'晴天'吗？{'晴天' in pl}")

print("全部歌曲：")
for song in pl:
    print(f"  - {song}")


# ========== 5. 上下文管理器 ==========
print("\n" + "=" * 40)
print("5. 上下文管理器：__enter__/__exit__")
print("=" * 40)


class Timer:
    """用魔术方法实现的计时器上下文管理器"""

    def __enter__(self):
        import time
        self.start = time.time()
        return self

    def __exit__(self, *args):
        import time
        elapsed = time.time() - self.start
        print(f"  耗时: {elapsed:.4f} 秒")


with Timer():
    # 在这个代码块里的操作会被计时
    total = sum(range(1000000))
    print(f"  计算完成，sum = {total}")
