def check_age(age):
    if age < 0:
        raise ValueError("年龄不能为负数")
    if age > 150:
        raise ValueError("年龄不合法")
    if age < 18:
        return "未成年"
    elif age <= 60:
        return "成年"
    else:
        return "老年"