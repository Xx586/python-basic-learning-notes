"""
Demo 3: JSON 读写
演示：loads/dumps 字符串转换、load/dump 文件读写、ensure_ascii中文处理、datetime序列化

运行方式：python 3_json_demo.py
"""

import json
import os
from datetime import datetime, date

# ========== 准备工作：清理旧文件 ==========
for f in ['demo_data.json', 'demo_users.json', 'demo_log.json']:
    try:
        os.remove(f)
    except FileNotFoundError:
        pass

# ========== 1. json.loads() 和 json.dumps() 字符串转换 ==========
print("=" * 40)
print("1. loads / dumps 字符串转换")
print("=" * 40)

# JSON 字符串 → Python 对象（loads = load string）
json_str = '{"name": "张三", "age": 25, "skills": ["Python", "SQL"], "active": true, "address": null}'
data = json.loads(json_str)
print(f"类型: {type(data).__name__}")
print(f"姓名: {data['name']}")
print(f"技能: {data['skills']}")
print(f"活跃: {data['active']}")    # JSON true → Python True
print(f"地址: {data['address']}")    # JSON null → Python None

# Python 对象 → JSON 字符串（dumps = dump string）
data = {
    "name": "李四",
    "age": 30,
    "hobbies": ["读书", "游泳", "编程"],
    "is_vip": True,
    "score": None,
}
json_str = json.dumps(data)
print(f"\n默认 dumps（中文被转义）:\n{json_str}")

# ========== 2. ensure_ascii=False 保留中文 ==========
print("\n" + "=" * 40)
print("2. ensure_ascii=False 保留中文")
print("=" * 40)

city_data = {
    "城市": "北京",
    "景点": ["故宫", "长城", "颐和园"],
    "特色": "烤鸭",
}

# 不加 ensure_ascii=False → 中文变成 \uXXXX
ascii_json = json.dumps(city_data)
print(f"默认 (ascii): {ascii_json}")

# 加上 ensure_ascii=False → 中文保留原文
cn_json = json.dumps(city_data, ensure_ascii=False)
print(f"保留中文: {cn_json}")

# ========== 3. indent 格式化缩进 ==========
print("\n" + "=" * 40)
print("3. indent 格式化 + sort_keys 排序")
print("=" * 40)

data = {"name": "王五", "age": 28, "city": "上海", "email": "wang@example.com"}
formatted = json.dumps(data, ensure_ascii=False, indent=4, sort_keys=True)
print(formatted)

# ========== 4. json.dump() 和 json.load() 文件读写 ==========
print("=" * 40)
print("4. dump / load 文件读写")
print("=" * 40)

# 写入 JSON 文件（dump = 写入文件）
users = [
    {"id": 1, "name": "Alice", "score": 85},
    {"id": 2, "name": "Bob", "score": 92},
    {"id": 3, "name": "Charlie", "score": 78},
]

with open('demo_users.json', 'w', encoding='utf-8') as f:
    json.dump(users, f, ensure_ascii=False, indent=2)
print("已写入 demo_users.json")

# 读取 JSON 文件（load = 从文件读取）
with open('demo_users.json', 'r', encoding='utf-8') as f:
    loaded_users = json.load(f)
print(f"读取到 {len(loaded_users)} 条用户数据:")
for user in loaded_users:
    print(f"  ID:{user['id']} - {user['name']} - {user['score']}分")

# ========== 5. 记忆技巧：带 s = string，不带 s = file ==========
print("\n" + "=" * 40)
print("5. 记忆口诀")
print("=" * 40)
print("  json.loads(s)  — load String（从字符串解析）")
print("  json.dumps(obj) — dump String（转为字符串）")
print("  json.load(f)   — load File（从文件读取）")
print("  json.dump(obj, f) — dump to File（写入文件）")

# ========== 6. datetime 等不可序列化类型的处理 ==========
print("\n" + "=" * 40)
print("6. datetime 序列化处理")
print("=" * 40)

# 直接序列化 datetime 会报 TypeError
# data = {"time": datetime.now()}
# json.dumps(data)  # TypeError: Object of type datetime is not JSON serializable

# 方案1：使用 default 参数
def custom_serializer(obj):
    """将不可序列化的类型转为可序列化类型"""
    if isinstance(obj, datetime):
        return obj.strftime('%Y-%m-%d %H:%M:%S')
    if isinstance(obj, date):
        return obj.strftime('%Y-%m-%d')
    if isinstance(obj, set):
        return list(obj)
    raise TypeError(f'类型 {type(obj)} 不可序列化')

log_entry = {
    "event": "user_login",
    "time": datetime.now(),
    "user_id": 1001,
    "tags": {"重要", "紧急"},
}
json_str = json.dumps(log_entry, ensure_ascii=False, indent=2, default=custom_serializer)
print("使用 default 参数序列化:")
print(json_str)

# 方案2：继承 JSONEncoder
class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        if isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        return super().default(obj)

json_str2 = json.dumps(
    {"time": datetime.now(), "name": "测试"},
    ensure_ascii=False,
    cls=CustomEncoder,
)
print(f"\n使用 CustomEncoder: {json_str2}")

# 方案3：序列化前手动转换（最简单）
data = {
    "name": "用户A",
    "created_at": datetime.now().isoformat(),  # 转为字符串
}
json_str3 = json.dumps(data, ensure_ascii=False)
print(f"\n手动转换 isoformat: {json_str3}")

# ========== 7. JSON 类型映射对照 ==========
print("\n" + "=" * 40)
print("7. JSON Python 类型映射")
print("=" * 40)

mappings = [
    ("Python dict",      "JSON object",  '{"key": "value"}'),
    ("Python list/tuple", "JSON array",  '[1, 2, 3]'),
    ("Python str",       "JSON string",  '"hello"'),
    ("Python int/float", "JSON number",  '42 / 3.14'),
    ("Python True",      "JSON true",    'true'),
    ("Python False",     "JSON false",   'false'),
    ("Python None",      "JSON null",    'null'),
]
print(f"{'Python':<20} {'JSON':<15} {'示例':<15}")
print("-" * 50)
for py, js, example in mappings:
    print(f"{py:<20} {js:<15} {example:<15}")

# ========== 8. 实战：JSON 日志系统 ==========
print("\n" + "=" * 40)
print("8. 实战：JSON 日志系统")
print("=" * 40)

LOG_FILE = 'demo_log.json'

def write_log(event, detail):
    """追加写入 JSON 格式日志"""
    # 读取已有日志
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r', encoding='utf-8') as f:
            try:
                logs = json.load(f)
            except json.JSONDecodeError:
                logs = []
    else:
        logs = []

    # 追加新条目
    logs.append({
        "time": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "event": event,
        "detail": detail,
    })

    # 写回
    with open(LOG_FILE, 'w', encoding='utf-8') as f:
        json.dump(logs, f, ensure_ascii=False, indent=2)

# 写几条日志
write_log("app_start", "应用启动")
write_log("user_login", "用户 admin 登录成功")
write_log("data_sync", "同步了 150 条数据")

print("已写入 3 条日志到 demo_log.json")

# 读取日志验证
with open(LOG_FILE, 'r', encoding='utf-8') as f:
    logs = json.load(f)
for log in logs:
    print(f"  [{log['time']}] {log['event']}: {log['detail']}")

# 清理
os.remove(LOG_FILE)

print("\nJSON 读写演示完成！")
