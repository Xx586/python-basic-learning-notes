"""
自定义包内的格式化模块

定义文本、数字、日期的格式化函数。
"""

from datetime import datetime


def format_currency(amount, symbol='¥'):
    """格式化为货币字符串

    Args:
        amount: 金额
        symbol: 货币符号，默认 ¥
    """
    return f"{symbol}{amount:,.2f}"


def format_percentage(value, total, decimal_places=1):
    """格式化为百分比字符串"""
    if total == 0:
        return "N/A"
    pct = (value / total) * 100
    return f"{pct:.{decimal_places}f}%"


def format_table(rows, headers=None, col_widths=None):
    """将数据格式化为表格字符串

    Args:
        rows: 数据列表，每行是一个列表或元组
        headers: 表头列表
        col_widths: 每列宽度列表，None 则自动计算
    """
    if not rows:
        return ""

    n_cols = len(rows[0])

    # 自动计算列宽
    if col_widths is None:
        col_widths = [0] * n_cols
        all_rows = rows[:]
        if headers:
            all_rows.insert(0, list(headers))
        for row in all_rows:
            for i, cell in enumerate(row):
                # 考虑中文字符宽度（粗略处理）
                cell_str = str(cell)
                col_widths[i] = max(col_widths[i], len(cell_str))

    def format_row(row):
        cells = []
        for i, cell in enumerate(row):
            cells.append(f" {str(cell):<{col_widths[i]}} ")
        return "|" + "|".join(cells) + "|"

    lines = []

    # 表头
    if headers:
        lines.append(format_row(headers))
        separator = "|" + "|".join("-" * (w + 2) for w in col_widths) + "|"
        lines.append(separator)

    # 数据行
    for row in rows:
        lines.append(format_row(row))

    return "\n".join(lines)


def format_timestamp(ts=None, fmt="%Y-%m-%d %H:%M:%S"):
    """格式化时间戳或当前时间

    Args:
        ts: 时间戳（秒），None 表示当前时间
        fmt: 格式化字符串
    """
    if ts is None:
        dt = datetime.now()
    else:
        dt = datetime.fromtimestamp(ts)
    return dt.strftime(fmt)


def format_file_size(size_bytes):
    """将字节数格式化为人类可读的文件大小"""
    if size_bytes == 0:
        return "0 B"
    units = ['B', 'KB', 'MB', 'GB', 'TB']
    i = 0
    size = float(size_bytes)
    while size >= 1024 and i < len(units) - 1:
        size /= 1024
        i += 1
    return f"{size:.1f} {units[i]}"


class TableFormatter:
    """表格格式化类：演示包内模块中的类"""

    def __init__(self):
        self._rows = []
        self._headers = None

    def set_headers(self, *headers):
        """设置表头"""
        self._headers = headers
        return self

    def add_row(self, *values):
        """添加一行数据"""
        self._rows.append(values)
        return self

    def build(self):
        """生成表格字符串"""
        return format_table(self._rows, self._headers)

    def clear(self):
        """清空数据"""
        self._rows = []
        self._headers = None


# 模块自测
if __name__ == '__main__':
    print("=== formatter 模块自测 ===\n")

    # 货币格式化
    print(f"format_currency(1234.5): {format_currency(1234.5)}")
    print(f"format_currency(1000000, '$'): {format_currency(1000000, '$')}")

    # 百分比格式化
    print(f"\nformat_percentage(45, 200): {format_percentage(45, 200)}")
    print(f"format_percentage(1, 3, 2): {format_percentage(1, 3, 2)}")

    # 表格格式化
    print(f"\n表格示例:")
    tf = TableFormatter()
    tf.set_headers("姓名", "年龄", "成绩")
    tf.add_row("张三", 18, 92)
    tf.add_row("李四", 17, 88)
    tf.add_row("王五", 19, 95)
    print(tf.build())

    # 时间戳格式化
    print(f"\n当前时间: {format_timestamp()}")
    print(f"指定时间戳: {format_timestamp(0, '%Y-%m-%d')}")

    # 文件大小
    print(f"\nformat_file_size(0): {format_file_size(0)}")
    print(f"format_file_size(1024): {format_file_size(1024)}")
    print(f"format_file_size(1536000): {format_file_size(1536000)}")
