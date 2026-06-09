"""
自定义字符串工具模块 — 被其他文件导入使用

包含：字符串处理函数、统计函数、格式化函数
"""


def reverse_string(s):
    """反转字符串"""
    return s[::-1]


def is_palindrome(s):
    """判断是否为回文字符串（忽略大小写和空格）"""
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]


def count_words(s):
    """统计字符串中的单词数"""
    return len(s.split())


def count_chars(s, count_spaces=True):
    """统计字符数

    Args:
        s: 输入字符串
        count_spaces: 是否计入空格，默认 True
    """
    if count_spaces:
        return len(s)
    return len(s.replace(' ', ''))


def capitalize_words(s):
    """将每个单词的首字母大写"""
    return ' '.join(word.capitalize() for word in s.split())


def remove_duplicates(s):
    """去除字符串中的重复字符，保留首次出现顺序"""
    seen = set()
    result = []
    for ch in s:
        if ch not in seen:
            seen.add(ch)
            result.append(ch)
    return ''.join(result)


def truncate(s, max_len, suffix='...'):
    """截断字符串到指定长度，超出部分用 suffix 替代

    Args:
        s: 输入字符串
        max_len: 最大长度
        suffix: 截断后缀，默认 '...'
    """
    if len(s) <= max_len:
        return s
    return s[:max_len - len(suffix)] + suffix


def mask_string(s, start=3, end=3, mask_char='*'):
    """遮掩字符串中间部分（适合手机号、身份证脱敏）

    Args:
        s: 输入字符串
        start: 开头保留位数
        end: 结尾保留位数
        mask_char: 遮罩字符
    """
    if len(s) <= start + end:
        return s
    return s[:start] + mask_char * (len(s) - start - end) + s[-end:]


class StringWrapper:
    """字符串包装类：演示被导入模块中的类"""

    def __init__(self, content):
        self.content = content

    def __len__(self):
        return len(self.content)

    def __repr__(self):
        return f"StringWrapper('{self.content}')"

    def upper(self):
        return self.content.upper()

    def lower(self):
        return self.content.lower()

    def title(self):
        return self.content.title()


# ========== 模块自测代码 ==========
if __name__ == '__main__':
    print("=== my_string 模块自测 ===\n")

    # 基本操作
    print(f"reverse_string('hello'): {reverse_string('hello')}")
    print(f"is_palindrome('A man a plan a canal Panama'): {is_palindrome('A man a plan a canal Panama')}")
    print(f"is_palindrome('python'): {is_palindrome('python')}")

    # 统计
    print(f"\ncount_words('Hello World Python'): {count_words('Hello World Python')}")
    print(f"count_chars('Hello World'): {count_chars('Hello World')}")
    print(f"count_chars('Hello World', count_spaces=False): {count_chars('Hello World', count_spaces=False)}")

    # 转换
    print(f"\ncapitalize_words('hello world'): {capitalize_words('hello world')}")
    print(f"remove_duplicates('abracadabra'): {remove_duplicates('abracadabra')}")

    # 实用工具
    print(f"\ntruncate('这是一段很长的文本', 7): {truncate('这是一段很长的文本', 7)}")
    print(f"mask_string('13812345678'): {mask_string('13812345678')}")

    # StringWrapper 类
    sw = StringWrapper("Hello World")
    print(f"\n{sw}")
    print(f"len: {len(sw)}")
    print(f"upper: {sw.upper()}")
    print(f"lower: {sw.lower()}")
