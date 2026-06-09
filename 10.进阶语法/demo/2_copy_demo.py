"""
演示赋值 / 浅拷贝 / 深拷贝的 id 和内容对比

本文件通过可视化输出展示：
- 赋值（=）:  引用传递，id 完全相同
- 浅拷贝:     新容器，但内层元素共享
- 深拷贝:     完全独立的副本
- 可变 vs 不可变类型的拷贝行为差异
- 自定义 __copy__ / __deepcopy__

可以独立运行，用 = 分隔线和 print 明确展示输出。
"""

import copy


# ============================================================================
# 一、赋值 = 是引用（id 相同）
# ============================================================================
print("=" * 60)
print("一、赋值 = 是引用（id 相同）")
print("=" * 60)

list_a = [1, 2, 3]
list_b = list_a  # 赋值，不是拷贝！

print(f"list_a       = {list_a}")
print(f"list_b       = {list_b}")
print(f"id(list_a)   = {id(list_a)}")
print(f"id(list_b)   = {id(list_b)}")
print(f"is same?     = {list_a is list_b}")  # True

# 修改 b 会影响 a
list_b.append(999)
print(f"\n[修改 list_b 后]")
print(f"list_a       = {list_a}")   # [1, 2, 3, 999] — 也变了！
print(f"list_b       = {list_b}")   # [1, 2, 3, 999]
print()

# 图解
print("[图解]")
print("  list_a ──→ [1, 2, 3, 999]  ←── list_b")
print("              (同一个对象)")


# ============================================================================
# 二、浅拷贝 copy.copy()（只复制第一层）
# ============================================================================
print("\n" + "=" * 60)
print("二、浅拷贝 copy.copy() — 只复制第一层")
print("=" * 60)

# --- 一维列表：浅拷贝看起来"独立"（元素是不可变的）---
print("\n[2.1] 一维列表浅拷贝:")
simple_a = [1, 2, 3]
simple_b = copy.copy(simple_a)

print(f"simple_a     = {simple_a}")
print(f"simple_b     = {simple_b}")
print(f"id(simple_a) = {id(simple_a)}")
print(f"id(simple_b) = {id(simple_b)}")
print(f"外层不同?    = {simple_a is not simple_b}")  # True

simple_b.append(4)
print(f"\n[simple_b 追加 4 后]")
print(f"simple_a     = {simple_a}")  # [1, 2, 3] — 不受影响
print(f"simple_b     = {simple_b}")  # [1, 2, 3, 4]

# --- 二维列表：浅拷贝只复制第一层，内层共享！---
print("\n[2.2] 二维列表浅拷贝（关键！）:")
nested_a = [[1, 2], [3, 4]]
nested_b = copy.copy(nested_a)

print(f"nested_a     = {nested_a}")
print(f"nested_b     = {nested_b}")
print(f"外层id不同?  = {id(nested_a) != id(nested_b)}")     # True（外层容器不同）
print(f"内层[0]id相同? = {id(nested_a[0]) == id(nested_b[0])}")  # True（内层列表相同！）

# 修改内层 → 两个都变！
nested_b[0].append(999)
print(f"\n[nested_b[0] 追加 999 后]")
print(f"nested_a     = {nested_a}")  # [[1, 2, 999], [3, 4]] — 也变了！
print(f"nested_b     = {nested_b}")  # [[1, 2, 999], [3, 4]]

print("\n[图解] 浅拷贝:")
print("  nested_a ──→ [ □ , □ ]")
print("                 ↓    ↓")
print("              [1,2,999] [3,4]")
print("                 ↑    ↑")
print("  nested_b ──→ [ □ , □ ]")
print("  (外层容器不同，内层元素是同一个对象)")

# --- 常见浅拷贝方式 ---
print("\n[2.3] 常见的浅拷贝方式:")
a = [[1, 2], [3, 4]]
b1 = a[:]          # 切片
b2 = list(a)       # list()
b3 = a.copy()      # .copy()
b4 = [*a]          # 解包
b5 = copy.copy(a)  # 显式浅拷贝
print(f"切片 a[:]      内层相同: {id(a[0]) == id(b1[0])}")
print(f"list(a)       内层相同: {id(a[0]) == id(b2[0])}")
print(f"a.copy()      内层相同: {id(a[0]) == id(b3[0])}")
print(f"[*a]          内层相同: {id(a[0]) == id(b4[0])}")
print(f"copy.copy(a)  内层相同: {id(a[0]) == id(b5[0])}")
# 全部 True！都是浅拷贝


# ============================================================================
# 三、深拷贝 copy.deepcopy()（完全独立）
# ============================================================================
print("\n" + "=" * 60)
print("三、深拷贝 copy.deepcopy() — 完全独立")
print("=" * 60)

deep_a = [[1, 2], [3, 4]]
deep_b = copy.deepcopy(deep_a)

print(f"deep_a        = {deep_a}")
print(f"deep_b        = {deep_b}")
print(f"外层id相同?   = {id(deep_a) == id(deep_b)}")     # False
print(f"内层[0]id相同? = {id(deep_a[0]) == id(deep_b[0])}")  # False
print(f"内层[1]id相同? = {id(deep_a[1]) == id(deep_b[1])}")  # False

# 修改内层 → 互不影响
deep_b[0].append(999)
print(f"\n[deep_b[0] 追加 999 后]")
print(f"deep_a        = {deep_a}")  # [[1, 2], [3, 4]] — 不受影响
print(f"deep_b        = {deep_b}")  # [[1, 2, 999], [3, 4]]

print("\n[图解] 深拷贝:")
print("  deep_a ──→ [ □ , □ ]  →  [1,2] [3,4]   (完全独立)")
print("  deep_b ──→ [ □ , □ ]  →  [1,2,999] [3,4]  (完全独立)")


# ============================================================================
# 四、可变 vs 不可变类型的拷贝行为
# ============================================================================
print("\n" + "=" * 60)
print("四、可变 vs 不可变类型的拷贝行为")
print("=" * 60)

print("\n[4.1] 不可变对象（int, str, tuple）的浅拷贝 → 返回自身:")
immutable_val = (1, 2, 3)
shallow_val = copy.copy(immutable_val)
deep_val = copy.deepcopy(immutable_val)
print(f"  原始      id: {id(immutable_val)}")
print(f"  浅拷贝    id: {id(shallow_val)}  相同? {immutable_val is shallow_val}")  # True
print(f"  深拷贝    id: {id(deep_val)}     相同? {immutable_val is deep_val}")     # True

# 陷阱：不可变容器内包含可变元素
print("\n[4.2] 陷阱：元组内含可变元素:")
tricky_a = ([1, 2], [3, 4])  # 元组不可变，但元素是可变的列表
tricky_b = copy.copy(tricky_a)
print(f"  外层id相同? = {tricky_a is tricky_b}")         # True（元组本身返回自身）
print(f"  内层id相同? = {tricky_a[0] is tricky_b[0]}")   # True（内层列表共享！）
# 虽然元组不可变，但内层的列表是共享的 → 修改列表会影响两边
tricky_b[0].append(999)
print(f"  tricky_a = {tricky_a}")  # ([1, 2, 999], [3, 4]) — 也被影响！

tricky_c = copy.deepcopy(tricky_a)
print(f"  deepcopy 外层id相同? = {tricky_a is tricky_c}")  # False


# ============================================================================
# 五、自定义 __copy__ 和 __deepcopy__
# ============================================================================
print("\n" + "=" * 60)
print("五、自定义 __copy__ 和 __deepcopy__")
print("=" * 60)

class Person:
    """演示自定义拷贝逻辑的类"""

    def __init__(self, name: str, hobbies: list):
        self.name = name       # 字符串（不可变）
        self.hobbies = hobbies # 列表（可变）

    def __copy__(self):
        """自定义浅拷贝：hobbies 仍共享同一列表"""
        print("    [调用 __copy__]")
        return Person(self.name, self.hobbies)

    def __deepcopy__(self, memo):
        """自定义深拷贝：递归拷贝所有属性"""
        print("    [调用 __deepcopy__]")
        return Person(
            copy.deepcopy(self.name, memo),
            copy.deepcopy(self.hobbies, memo)
        )

    def __repr__(self):
        return f"Person(name='{self.name}', hobbies={self.hobbies})"

p1 = Person("Alice", ["reading", "coding"])
print(f"  p1 = {p1}")

p_shallow = copy.copy(p1)
print(f"  p_shallow = {p_shallow}")
print(f"  hobbies 共享? {p1.hobbies is p_shallow.hobbies}")  # True

p_deep = copy.deepcopy(p1)
print(f"  p_deep = {p_deep}")
print(f"  hobbies 共享? {p1.hobbies is p_deep.hobbies}")    # False

# 验证独立性
p_shallow.hobbies.append("gaming")
print(f"\n[修改浅拷贝的 hobbies 后]")
print(f"  p1.hobbies        = {p1.hobbies}")          # 也变了！
print(f"  p_shallow.hobbies = {p_shallow.hobbies}")

p_deep.hobbies.append("swimming")
print(f"\n[修改深拷贝的 hobbies 后]")
print(f"  p1.hobbies        = {p1.hobbies}")          # 不变！
print(f"  p_deep.hobbies    = {p_deep.hobbies}")


# ============================================================================
# 六、循环引用与深拷贝
# ============================================================================
print("\n" + "=" * 60)
print("六、深拷贝处理循环引用")
print("=" * 60)

# 创建循环引用：a 包含 b，b 包含 a
a = [1, 2]
b = [3, 4, a]
a.append(b)  # a = [1, 2, [3, 4, a]]
             # 形成循环：a → b → a

print(f"  a = {a}")

# deepcopy 通过 memo 字典追踪已复制对象，不会无限递归
c = copy.deepcopy(a)
print(f"  c = {c}")
print(f"  c 是独立副本? {c is not a}")          # True
print(f"  c[2] 是独立副本? {c[2] is not b}")    # True
print(f"  c 内部保持循环引用? {c[2][2] is c}")  # True（保持了内部循环结构）


# ============================================================================
# 七、实际场景：防配置意外修改
# ============================================================================
print("\n" + "=" * 60)
print("七、实际场景：深拷贝保护默认配置")
print("=" * 60)

DEFAULT_CONFIG = {
    "host": "localhost",
    "port": 8080,
    "cache": {"enabled": True, "ttl": 300},
    "retry": 3,
}

def make_request(user_overrides=None):
    """
    基于默认配置创建请求配置
    使用深拷贝防止修改影响默认值
    """
    # 深拷贝：user_overrides 的修改不影响 DEFAULT_CONFIG
    config = copy.deepcopy(DEFAULT_CONFIG)

    if user_overrides:
        for key, value in user_overrides.items():
            if isinstance(value, dict) and isinstance(config.get(key), dict):
                config[key].update(value)  # 合并嵌套字典
            else:
                config[key] = value
    return config

# 第一次调用
config1 = make_request({"cache": {"ttl": 600}, "port": 9090})
print(f"  config1 = {config1}")
print(f"  DEFAULT_CONFIG 未被修改: {DEFAULT_CONFIG}")
print(f"  DEFAULT_CONFIG['cache']['ttl'] = {DEFAULT_CONFIG['cache']['ttl']}  (仍是 300)")

# 第二次调用（互不影响）
config2 = make_request({"cache": {"ttl": 60}})
print(f"\n  config2 = {config2}")
print(f"  config1['cache']['ttl'] = {config1['cache']['ttl']}  (仍是 600)")


# ============================================================================
# 八、汇总对比表
# ============================================================================
print("\n" + "=" * 60)
print("八、三种方式对比汇总")
print("=" * 60)

original = [[1, 2], [3, 4]]
assigned = original                          # 赋值
shallow = copy.copy(original)               # 浅拷贝
deep = copy.deepcopy(original)              # 深拷贝

# 修改外部列表
assigned.append([5, 6])
shallow.append([7, 8])
deep.append([9, 10])

print(f"  原始列表: {original}")   # [[1, 2], [3, 4], [5, 6]]
print(f"  赋值:     {assigned}")   # [[1, 2], [3, 4], [5, 6]] — 和原始一样
print(f"  浅拷贝:   {shallow}")    # [[1, 2], [3, 4], [7, 8]] — 外层独立
print(f"  深拷贝:   {deep}")       # [[1, 2], [3, 4], [9, 10]] — 完全独立

# 修改内层元素
assigned[0].append(999)
print(f"\n[修改 assigned[0] 追加 999 后]")
print(f"  原始内层: {original[0]}")  # [1, 2, 999] — 变了！赋值和原始同一个
print(f"  浅拷内层: {shallow[0]}")   # [1, 2, 999] — 也变了！浅拷贝内层共享
print(f"  深拷内层: {deep[0]}")      # [1, 2] — 不变！深拷贝完全独立

print("\n" + "=" * 60)
print("全部演示完成！")
print("=" * 60)
