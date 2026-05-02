def get_shipping_cost(weight):
    """
    根据重量计算运费，大于0，小于等于2，10元
    大于2，小于等于10，20元
    大于10，小于等于30，35元
    大于30，小于等于50，50元
    其他情况，抛出 ValueError
    """
    if weight <= 0:
        raise ValueError("重量必须大于 0")
    if weight > 50:
        raise ValueError("重量不能超过 50kg")

    if weight <= 2:
        return 10
    elif weight <= 10:
        return 20
    elif weight <= 30:
        return 35
    else:
        return 50