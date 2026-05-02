def check_age(age):
    if age < 18:
        return "未成年"
    elif age <= 60:
        return "成年"
    else:
        return "老年"