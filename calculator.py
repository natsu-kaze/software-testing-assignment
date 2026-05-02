class NegativeNumberError(Exception):
    pass


def add(a, b):
    """返回 a + b"""
    return a + b


def is_positive(n):
    """判断 n 是否为正数（>0）"""
    return n > 0


def sqrt(n):
    """计算平方根，负数时抛出 NegativeNumberError"""
    if n < 0:
        raise NegativeNumberError("不能对负数开平方根")
    return n ** 0.5