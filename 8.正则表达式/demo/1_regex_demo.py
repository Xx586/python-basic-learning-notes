"""
=============================================================================
 正则表达式 (Regular Expression) 综合演示
=============================================================================
 本文件分 8 个部分，全面展示 Python re 模块的各项功能：
   部分 1：基础元字符匹配
   部分 2：re 模块核心函数 (match / search / findall / finditer / sub / split)
   部分 3：分组——捕获、非捕获、命名分组、反向引用
   部分 4：替换与分割进阶
   部分 5：编译标志 (re.I / re.M / re.S / re.X)
   部分 6：常用验证 (手机号 / 邮箱 / URL / IP / 身份证 / 日期)
   部分 7：贪婪 vs 非贪婪
   部分 8：零宽断言 (前瞻 / 后顾)

 每个部分可独立运行，输出结果紧跟其后。
=============================================================================
"""

import re


# =============================================================================
# 部分 1：基础元字符匹配
# =============================================================================
def section_1() -> None:
    print("=" * 70)
    print("部分 1：基础元字符匹配")
    print("=" * 70)

    # --- 1.1 点号 . : 匹配任意单个字符（默认不含换行符） ---
    print("\n[1.1] . 匹配任意字符")
    print(re.findall(r"a.c", "abc a1c a c a@c a\nc"))
    # ['abc', 'a1c', 'a c', 'a@c']  —— 换行符 \n 不匹配

    # --- 1.2 星号 * : 0次或多次 ---
    print("\n[1.2] * 0次或多次")
    print(re.findall(r"ab*c", "ac abc abbc abbbc"))
    # ['ac', 'abc', 'abbc', 'abbbc']

    # --- 1.3 加号 + : 1次或多次 ---
    print("\n[1.3] + 1次或多次")
    print(re.findall(r"ab+c", "ac abc abbc abbbc"))
    # ['abc', 'abbc', 'abbbc']  —— ac 不在内

    # --- 1.4 问号 ? : 0次或1次 ---
    print("\n[1.4] ? 0次或1次")
    print(re.findall(r"ab?c", "ac abc abbc"))
    # ['ac', 'abc']  —— abbc 不在内

    # --- 1.5 {n} / {n,} / {n,m} : 精确次数 ---
    print("\n[1.5] {} 量词")
    print("{3}   :", re.findall(r"a{3}", "a aa aaa aaaa"))
    # ['aaa', 'aaa'] —— "aaaa" 中匹配前 3 个 a
    print("{2,}  :", re.findall(r"a{2,}", "a aa aaa aaaa"))
    # ['aa', 'aaa', 'aaaa']
    print("{2,4} :", re.findall(r"a{2,4}", "a aa aaa aaaa aaaaa"))
    # ['aa', 'aaa', 'aaaa', 'aaaa']

    # --- 1.6 字符简写 \d \D \w \W \s \S ---
    print("\n[1.6] 字符简写")
    text = "手机 13812345678 价格 99.9 元"
    print("原文 :", text)
    print("\\d+  :", re.findall(r"\d+", text))
    # ['13812345678', '99', '9']
    print("\\D+  :", re.findall(r"\D+", text))
    # ['手机 ', ' 价格 ', '.', ' 元']
    print("\\w+  :", re.findall(r"\w+", "hello_world 你好123 abc"))
    # ['hello_world', '你好123', 'abc']
    print("\\S+  :", re.findall(r"\S+", "hello world\tfoo\nbar"))
    # ['hello', 'world', 'foo', 'bar']

    # --- 1.7 单词边界 \b 和 \B ---
    print("\n[1.7] \\b 单词边界")
    print("独立单词 cat:", re.findall(r"\bcat\b", "cat category cat. scat"))
    # ['cat', 'cat']
    print("非边界的 cat:", re.findall(r"\Bcat\B", "category scat concat"))
    # ['cat']  —— 只有 category 中的 cat 满足

    # --- 1.8 字符集 [] 和否定字符集 [^] ---
    print("\n[1.8] 字符集")
    print("[aeiou] :", re.findall(r"[aeiou]", "apple banana cherry"))
    # ['a', 'a', 'a', 'a', 'e']
    print("[a-z]  :", re.findall(r"[a-z]", "Hello World 123"))
    # ['e', 'l', 'l', 'o', 'o', 'r', 'l', 'd']
    print("[^0-9] :", re.findall(r"[^0-9]", "A1 B2 C3"))
    # ['A', ' ', 'B', ' ', 'C']
    print("[]内 . 是字面量:", re.findall(r"[.]", "a.b.c"))
    # ['.', '.']

    # --- 1.9 锚点 ^ 和 $ ---
    print("\n[1.9] 锚点 ^ 和 $")
    print(re.findall(r"^\d+$", "12345"))    # ['12345']   —— 整串都是数字
    print(re.findall(r"^\d+$", "123abc"))   # []          —— 不匹配

    # ^ 和 $ 在多行模式 (re.M)
    text = "line1\nline2\nline3"
    print("默认 ^ :", re.findall(r"^line\d", text))
    # ['line1']
    print("re.M ^ :", re.findall(r"^line\d", text, re.M))
    # ['line1', 'line2', 'line3']

    # --- 1.10 | 或 ---
    print("\n[1.10] | 或")
    print(re.findall(r"cat|dog|bird", "I have a cat and a dog"))
    # ['cat', 'dog']


# =============================================================================
# 部分 2：re 模块核心函数
# =============================================================================
def section_2() -> None:
    print("\n" + "=" * 70)
    print("部分 2：re 模块核心函数")
    print("=" * 70)

    text = "我的手机号是 13812345678，备用 13987654321"

    # --- 2.1 re.match : 从开头匹配 ---
    print("\n[2.1] re.match —— 从开头匹配")
    m = re.match(r"\d+", text)
    print("match \\d+                    :", m)  # None —— 开头是中文
    m = re.match(r"我的手机号是", text)
    print("match '我的手机号是'            :", m.group() if m else None)
    # '我的手机号是'

    # --- 2.2 re.search : 搜索第一个匹配 ---
    print("\n[2.2] re.search —— 搜索第一个")
    m = re.search(r"\d+", text)
    print("search \\d+ :", m.group() if m else None)
    # '13812345678'

    # --- 2.3 re.findall : 所有匹配 ---
    print("\n[2.3] re.findall —— 所有匹配")
    phones = re.findall(r"1[3-9]\d{9}", text)
    print("所有手机号:", phones)
    # ['13812345678', '13987654321']

    # --- 2.4 re.finditer : 迭代器 ---
    print("\n[2.4] re.finditer —— 迭代器（节省内存）")
    for i, m in enumerate(re.finditer(r"1[3-9]\d{9}", text)):
        print(f"  第 {i+1} 个: {m.group()}  位置: {m.span()}")
    # 第 1 个: 13812345678  位置: (6, 17)
    # 第 2 个: 13987654321  位置: (22, 33)

    # --- 2.5 re.sub : 替换 ---
    print("\n[2.5] re.sub —— 替换")
    # 替换为固定字符串
    masked = re.sub(r"1[3-9]\d{9}", "[手机号]", text)
    print("替换为固定文字:", masked)
    # 我的手机号是 [手机号]，备用 [手机号]

    # 替换为函数处理结果 —— 手机号脱敏
    def mask_phone(m: re.Match) -> str:
        """将手机号中间 4 位替换为 ****"""
        phone = m.group()
        return phone[:3] + "****" + phone[7:]

    masked2 = re.sub(r"1[3-9]\d{9}", mask_phone, text)
    print("手机号脱敏    :", masked2)
    # 我的手机号是 138****5678，备用 139****4321

    # count 参数限制替换次数
    masked3 = re.sub(r"1[3-9]\d{9}", "[手机号]", text, count=1)
    print("只替换第一个  :", masked3)
    # 我的手机号是 [手机号]，备用 13987654321

    # --- 2.6 re.split : 分割 ---
    print("\n[2.6] re.split —— 分割")
    s = "apple, banana; cherry  date|elderberry"
    parts = re.split(r"[,;| ]+", s)
    print("按多种分隔符分割:", parts)
    # ['apple', 'banana', 'cherry', 'date', 'elderberry']

    # 保留分隔符（使用捕获组）
    parts2 = re.split(r"([,;| ]+)", s)
    print("保留分隔符      :", parts2)

    # --- 2.7 re.compile : 预编译 ---
    print("\n[2.7] re.compile —— 预编译（复用效率高）")
    phone_pattern = re.compile(r"1[3-9]\d{9}")

    test_phones = ["13811112222", "abcdefg", "13922223333", "12345678901"]
    for p in test_phones:
        m = phone_pattern.fullmatch(p)
        print(f"  {p:>15s}  -> {'有效' if m else '无效'}")
    # 13811112222  -> 有效
    # abcdefg      -> 无效
    # 13922223333  -> 有效
    # 12345678901  -> 无效 (第2位是2)


# =============================================================================
# 部分 3：分组——捕获、非捕获、命名分组、反向引用
# =============================================================================
def section_3() -> None:
    print("\n" + "=" * 70)
    print("部分 3：分组——捕获、非捕获、命名分组、反向引用")
    print("=" * 70)

    # --- 3.1 捕获分组 ---
    print("\n[3.1] 捕获分组 ()")
    m = re.search(r"姓名：(\w+)，年龄：(\d+)", "姓名：张三，年龄：28")
    if m:
        print("group(0)  :", m.group(0))   # 完整匹配: 姓名：张三，年龄：28
        print("group(1)  :", m.group(1))   # 张三
        print("group(2)  :", m.group(2))   # 28
        print("groups()  :", m.groups())   # ('张三', '28')
        print("start(1) :", m.start(1))    # 索引
        print("end(1)   :", m.end(1))
        print("span(1)  :", m.span(1))

    # --- 3.2 findall 有捕获组时的行为 ---
    print("\n[3.2] findall 有捕获组时的行为")
    text = "姓名：张三，姓名：李四，姓名：王五"
    print("无捕获组:", re.findall(r"姓名：\w+", text))
    # ['姓名：张三', '姓名：李四', '姓名：王五']
    print("有捕获组:", re.findall(r"姓名：(\w+)", text))
    # ['张三', '李四', '王五']  —— 只返回捕获组内容！

    # 多个捕获组时返回元组列表
    pairs = re.findall(r"(\w+)=(\d+)", "x=10 y=20 z=30")
    print("多捕获组:", pairs)
    # [('x', '10'), ('y', '20'), ('z', '30')]

    # --- 3.3 非捕获分组 (?:xxx) ---
    print("\n[3.3] 非捕获分组 (?:)")
    # 捕获版
    m1 = re.search(r"(http|https)://(www\.)?(\w+)\.(com|org)",
                   "https://www.example.com")
    print("捕获版 groups :", m1.groups())
    # ('https', 'www.', 'example', 'com')

    # 非捕获版
    m2 = re.search(r"(?:http|https)://(?:www\.)?(\w+)\.(com|org)",
                   "https://www.example.com")
    print("非捕获版 groups:", m2.groups())
    # ('example', 'com')  —— 清爽多了！

    # --- 3.4 命名分组 (?P<name>xxx) ---
    print("\n[3.4] 命名分组 (?P<name>)")
    pattern = r"(?P<protocol>https?)://(?P<domain>\w+\.\w+)/(?P<path>\w+)"
    m = re.search(pattern, "https://example.com/home")
    if m:
        print("groupdict():", m.groupdict())
        # {'protocol': 'https', 'domain': 'example.com', 'path': 'home'}
        print("group('domain'):", m.group("domain"))
        # example.com

    # --- 3.5 反向引用 \1 \2 ---
    print("\n[3.5] 反向引用 \\1 \\2")
    # 匹配重复出现的单词
    dup_words = re.findall(r"\b(\w+)\s+\1\b", "hello hello world world foo bar bar")
    print("重复单词:", dup_words)
    # ['hello', 'world', 'bar']

    # 匹配成对出现的 HTML 标签（简化版）
    html = "<div>内容</div> <span>文字</span> <div>错配</span>"
    pairs = re.findall(r"<(\w+)>.*?</\1>", html)
    print("成对标签名:", pairs)
    # ['div', 'span']

    # --- 3.6 命名分组反向引用 (?P=name) ---
    print("\n[3.6] 命名反向引用 (?P=name)")
    m = re.search(r"(?P<word>\w+)\s+(?P=word)", "hello hello")
    print("命名反向引用匹配:", m.group() if m else None)
    # 'hello hello'


# =============================================================================
# 部分 4：替换与分割进阶
# =============================================================================
def section_4() -> None:
    print("\n" + "=" * 70)
    print("部分 4：替换与分割进阶")
    print("=" * 70)

    # --- 4.1 用分组重排内容 ---
    print("\n[4.1] 用分组重排日期格式")
    # 将 2024-12-25 → 12/25/2024
    date_str = "2024-12-25"
    result = re.sub(r"(\d{4})-(\d{2})-(\d{2})", r"\2/\3/\1", date_str)
    print("日期格式转换:", result)
    # 12/25/2024

    # 批量处理
    dates = "2024-01-15, 2024-06-30, 2024-12-31"
    result = re.sub(r"(\d{4})-(\d{2})-(\d{2})", r"\2/\3/\1", dates)
    print("批量日期转换:", result)
    # 01/15/2024, 06/30/2024, 12/31/2024

    # --- 4.2 替换函数的高级用法 ---
    print("\n[4.2] 替换函数：数字千分位格式化")
    def add_commas(m: re.Match) -> str:
        """将纯数字字符串添加千分位逗号"""
        return f"{int(m.group()):,}"

    text = "价格 1234567 元，库存 987654321 件"
    result = re.sub(r"\d+", add_commas, text)
    print("千分位格式化:", result)
    # 价格 1,234,567 元，库存 987,654,321 件

    # --- 4.3 用 re.split 处理复杂分割 ---
    print("\n[4.3] 复杂分割：解析日志行")
    log_line = '2024-01-15 10:30:45 [ERROR] /api/users - "Connection timeout"'
    # 把时间、级别、路径、消息分开
    parts = re.split(r"\s+", log_line, maxsplit=3)
    print("日志分段:", parts)
    # ['2024-01-15', '10:30:45', '[ERROR]', '/api/users - "Connection timeout"']

    # 按多种符号分割并去掉空串
    data = "x=10, y=20; z=30"
    kv_pairs = [p for p in re.split(r"[,;]\s*", data) if p]
    print("键值对分割:", kv_pairs)
    # ['x=10', 'y=20', 'z=30']


# =============================================================================
# 部分 5：编译标志 (Flags)
# =============================================================================
def section_5() -> None:
    print("\n" + "=" * 70)
    print("部分 5：编译标志 (re.I / re.M / re.S / re.X)")
    print("=" * 70)

    # --- 5.1 re.IGNORECASE / re.I ---
    print("\n[5.1] re.I —— 忽略大小写")
    print(re.findall(r"hello", "Hello HELLO hello"))
    # ['hello']
    print(re.findall(r"hello", "Hello HELLO hello", re.I))
    # ['Hello', 'HELLO', 'hello']

    # 嵌入式写法: (?i)
    print(re.findall(r"(?i)hello", "Hello HELLO"))
    # ['Hello', 'HELLO']

    # --- 5.2 re.MULTILINE / re.M ---
    print("\n[5.2] re.M —— 多行模式")
    text = """第一行 开头
第二行 开头
第三行 结尾"""
    print("默认 ^ :", re.findall(r"^第.+$", text))
    # []
    print("re.M ^ :", re.findall(r"^第.+$", text, re.M))
    # ['第一行 开头', '第二行 开头', '第三行 结尾']

    # --- 5.3 re.DOTALL / re.S ---
    print("\n[5.3] re.S —— 让 . 也匹配换行符")
    text = """<div>
内容1
</div>
<div>
内容2
</div>"""
    print("不开 re.S:", re.findall(r"<div>.*?</div>", text))
    # []
    print("开了 re.S:", re.findall(r"<div>.*?</div>", text, re.S))
    # ['<div>\n内容1\n</div>', '<div>\n内容2\n</div>']

    # --- 5.4 re.VERBOSE / re.X ---
    print("\n[5.4] re.X —— 可读模式（在正则中写注释和空格）")

    # 用 VERBOSE 写的邮箱正则
    email_pattern = re.compile(r"""
        ^                       # 字符串开头
        [a-zA-Z0-9._%+-]+       # 用户名
        @                       # @ 符号
        [a-zA-Z0-9.-]+          # 域名
        \.                      # 字面量句点
        [a-zA-Z]{2,}            # 顶级域名（至少2个字母）
        $                       # 字符串结尾
    """, re.VERBOSE)

    test_emails = [
        "user@example.com",
        "user.name@company.co.uk",
        "invalid-email",
        "@no-username.com",
    ]
    for e in test_emails:
        print(f"  {e:>30s} -> {'有效' if email_pattern.match(e) else '无效'}")

    # --- 5.5 组合多个标志 ---
    print("\n[5.5] 组合标志 re.I | re.M")
    result = re.findall(r"^hello", "Hello\nhello\nHELLO", re.I | re.M)
    print(result)
    # ['Hello', 'hello', 'HELLO']


# =============================================================================
# 部分 6：常用验证——开箱即用的正则
# =============================================================================
def section_6() -> None:
    print("\n" + "=" * 70)
    print("部分 6：常用验证——手机号 / 邮箱 / URL / IP / 身份证 / 日期")
    print("=" * 70)

    # --- 6.1 手机号 ---
    print("\n[6.1] 手机号验证")
    def is_valid_phone(phone: str) -> bool:
        """验证中国大陆手机号：1[3-9]xxxxxxxxx"""
        return bool(re.fullmatch(r"1[3-9]\d{9}", phone))

    phones = ["13812345678", "12812345678", "1381234567", "13900001111a"]
    for p in phones:
        print(f"  {p:>15s} -> {'有效' if is_valid_phone(p) else '无效'}")

    # 从一个段落中提取所有手机号
    text = "联系人：张三 13811112222，李四 13922223333，王五 13733334444"
    found = re.findall(r"1[3-9]\d{9}", text)
    print("  提取所有手机号:", found)

    # --- 6.2 邮箱 ---
    print("\n[6.2] 邮箱验证")
    def is_valid_email(email: str) -> bool:
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return bool(re.fullmatch(pattern, email))

    emails = [
        "user@example.com",
        "user.name@company.co.uk",
        "user@domain",              # 无顶级域名
        "@domain.com",              # 无用户名
        "user name@domain.com",     # 含空格
    ]
    for e in emails:
        print(f"  {e:>30s} -> {'有效' if is_valid_email(e) else '无效'}")

    # --- 6.3 URL 提取 ---
    print("\n[6.3] URL 提取")
    text = """
    官网：https://www.example.com
    API：http://api.example.org/v1/users
    博客：https://blog.site.cn/article/123?id=456
    文档：ftp://files.server.com/data.zip
    """
    urls = re.findall(r"https?://[^\s]+", text)
    for url in urls:
        print(f"  {url}")

    # --- 6.4 IP 地址 ---
    print("\n[6.4] IP 地址验证")
    def is_valid_ip(ip: str) -> bool:
        pattern = (
            r"^(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}"
            r"(?:25[0-5]|2[0-4]\d|[01]?\d\d?)$"
        )
        return bool(re.fullmatch(pattern, ip))

    ips = ["192.168.1.1", "255.255.255.255", "256.1.1.1", "192.168.1", "0.0.0.0"]
    for ip in ips:
        print(f"  {ip:>20s} -> {'有效' if is_valid_ip(ip) else '无效'}")

    # --- 6.5 身份证号 ---
    print("\n[6.5] 身份证号验证")
    def is_valid_id_card(id_card: str) -> bool:
        """简单验证18位身份证格式（仅格式，不校验校验码）"""
        return bool(re.fullmatch(r"\d{17}[\dXx]", id_card))

    ids = ["110101199001011234", "11010119900101123X", "123456789012345", "11010119900101123Y"]
    for idc in ids:
        print(f"  {idc:>20s} -> {'有效' if is_valid_id_card(idc) else '无效'}")

    # --- 6.6 日期 ---
    print("\n[6.6] 日期提取与简单验证")
    text = "会议时间：2024-01-15、2024-12-31、2024-13-01、2024-02-30"
    dates = re.findall(r"\d{4}-\d{2}-\d{2}", text)
    print("  提取所有日期:", dates)
    # ['2024-01-15', '2024-12-31', '2024-13-01', '2024-02-30']
    # 注意：13 月 和 2月30日 格式上也匹配了，真正严谨的日期验证需要额外逻辑
    print("  提醒: 格式正确不代表日期合法 (如 13月、2月30日)")


# =============================================================================
# 部分 7：贪婪 vs 非贪婪
# =============================================================================
def section_7() -> None:
    print("\n" + "=" * 70)
    print("部分 7：贪婪 vs 非贪婪")
    print("=" * 70)

    # --- 7.1 HTML 标签匹配经典案例 ---
    print("\n[7.1] HTML 标签匹配——经典案例")
    html = "<div>内容1</div><div>内容2</div>"
    print("原文     :", html)
    print("贪婪 .*  :", re.findall(r"<div>.*</div>", html))
    # ['<div>内容1</div><div>内容2</div>']  —— 太贪了
    print("非贪 .*? :", re.findall(r"<div>.*?</div>", html))
    # ['<div>内容1</div>', '<div>内容2</div>']  —— 正确！

    # --- 7.2 引号内容提取 ---
    print("\n[7.2] 引号内容提取")
    text = '他说："你好"，然后说："再见"'
    print("原文           :", text)
    print("贪心 .*  :", re.findall(r'"(.*)"', text))
    # ['你好"，然后说："再见']  —— 错误！
    print("非贪 .*? :", re.findall(r'"(.*?)"', text))
    # ['你好', '再见']  —— 正确！

    # --- 7.3 各种量词的贪/非贪对比 ---
    print("\n[7.3] 量词贪/非贪对比")
    s = "aaaaaa"
    print(f'原文 = "{s}"')

    tests = [
        ("a+    (贪)", r"a+"),
        ("a+?   (非贪)", r"a+?"),
        ("a*    (贪)", r"a*"),
        ("a*?   (非贪)", r"a*?"),
        ("a{2,4}  (贪)", r"a{2,4}"),
        ("a{2,4}? (非贪)", r"a{2,4}?"),
    ]
    for label, pat in tests:
        print(f"  {label:18s} -> {re.findall(pat, s)}")

    # --- 7.4 贪婪陷阱: 多行注释 ---
    print("\n[7.4] 贪婪陷阱：多行注释提取")
    code = "/* 注释1 */ x = 1; /* 注释2 */ y = 2;"
    print("原文:", code)
    print("贪心 .* :", re.findall(r"/\*.*\*/", code))
    # ['/* 注释1 */ x = 1; /* 注释2 */']  —— 错了
    print("非贪 .*?:", re.findall(r"/\*.*?\*/", code))
    # ['/* 注释1 */', '/* 注释2 */']  —— 正确！


# =============================================================================
# 部分 8：零宽断言（Lookaround）
# =============================================================================
def section_8() -> None:
    print("\n" + "=" * 70)
    print("部分 8：零宽断言 —— 前瞻 (?=)(?!) / 后顾 (?<=)(?<!)")
    print("=" * 70)

    # --- 8.1 (?=xxx) 正向前瞻：后面要跟着 xxx ---
    print("\n[8.1] (?=) 正向前瞻 —— 后面跟着……")
    text = "Windows10 WindowsXP Windows7 WindowsVista"
    print("原文:", text)
    # 匹配后面跟着数字的 "Windows"
    print("(?=\\d)    :", re.findall(r"Windows(?=\d)", text))
    # ['Windows', 'Windows']  —— Windows10 和 Windows7 中的 Windows
    # 匹配后面跟着字母的 "Windows"
    print("(?=[A-Z]) :", re.findall(r"Windows(?=[A-Z])", text))
    # ['Windows', 'Windows']  —— WindowsXP 和 WindowsVista 中的 Windows

    # --- 8.2 (?!xxx) 负向前瞻：后面不能跟着 xxx ---
    print("\n[8.2] (?!) 负向前瞻 —— 后面不能跟着……")
    # 匹配后面不跟数字的 "Windows"
    print("(?!\\d)    :", re.findall(r"Windows(?!\d)", text))
    # ['Windows', 'Windows']

    # --- 8.3 (?<=xxx) 正向后顾：前面要有 xxx ---
    print("\n[8.3] (?<=) 正向后顾 —— 前面要有……")
    text2 = "价格：￥99元，$50美元，€30欧元"
    print("原文:", text2)
    print("(?<=\\￥)\\d+     :", re.findall(r"(?<=￥)\d+", text2))
    # ['99']
    print("(?<=[\\￥\\$\\€])\\d+ :", re.findall(r"(?<=[￥$€])\d+", text2))
    # ['99', '50', '30']

    # --- 8.4 (?<!xxx) 负向后顾：前面不能有 xxx ---
    print("\n[8.4] (?<!) 负向后顾 —— 前面不能有……")
    text3 = "原价￥100，折扣价80，税费20"
    print("原文:", text3)
    # 匹配前面没有 ￥ 的数字
    print("(?<!\\￥)\\b\\d+\\b :", re.findall(r"(?<!￥)\b\d+\b", text3))
    # ['80', '20']  —— 100 前面有 ￥，被排除

    # --- 8.5 综合应用：密码强度验证（单条正则） ---
    print("\n[8.5] 综合：密码强度验证（零宽断言一条龙）")
    def check_password_strength(password: str) -> dict:
        """用零宽断言检查密码强度"""
        checks = {
            "长度 >= 8": bool(re.search(r".{8,}", password)),
            "含小写字母": bool(re.search(r"[a-z]", password)),
            "含大写字母": bool(re.search(r"[A-Z]", password)),
            "含数字": bool(re.search(r"\d", password)),
            "含特殊字符": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)),
        }
        return checks

    def is_strong_password_one_liner(password: str) -> bool:
        """零宽断言写法：一条正则检查多项条件"""
        # 每条 (?=.*xxx) 从头扫描一遍，确保 xxx 在字符串某处出现
        pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*]).{8,}$"
        return bool(re.match(pattern, password))

    test_pwds = ["Abcdef1!", "abcdef1!", "ABCDEF1!", "Abcdefg!", "Ab1!", "Abcdef1!"]
    print("单条正则强密码验证:")
    for pwd in test_pwds:
        ok = is_strong_password_one_liner(pwd)
        print(f"  {pwd:>15s} -> {'强密码' if ok else '弱密码'}")

    # 详细检查
    print("\n详细强度检查:")
    checks = check_password_strength("Abc123!@#")
    for key, val in checks.items():
        print(f"  {key}: {'YES' if val else 'NO'}")

    # --- 8.6 后顾断言宽度限制提醒 ---
    print("\n[8.6] 后顾断言宽度限制")
    print("Python re 中 (?<=) 必须是固定宽度，下面这句会报错:")
    print('  # re.findall(r"(?<=\\w{2,5})\\d+", text)  # 报错: variable-length look-behind')
    print("  解法: 改用 re.search 分步匹配 或 使用 regex 第三方库")


# =============================================================================
# 主入口
# =============================================================================
if __name__ == "__main__":
    # 依次执行所有部分
    section_1()
    section_2()
    section_3()
    section_4()
    section_5()
    section_6()
    section_7()
    section_8()

    print("\n" + "=" * 70)
    print("  全部 8 个部分演示完毕！")
    print("=" * 70)
