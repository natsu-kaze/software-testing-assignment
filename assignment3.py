"""
作业：assignment3 - 货币兑换程序
B23-3 2511643 陆晓韬
"""
CNY_TO_JPY_RATE = 20.0 
CNY_TO_USD_RATE = 0.14 

JPY_TO_CNY_RATE = 1 / CNY_TO_JPY_RATE  
USD_TO_CNY_RATE = 1 / CNY_TO_USD_RATE  
def cny_to_jpy(amount):
    jpy = amount * CNY_TO_JPY_RATE
    print(f"{amount}人民币转换成日元为：{jpy:.1f}日元")
    return jpy


def cny_to_usd(amount):
    usd = amount * CNY_TO_USD_RATE
    print(f"{amount}人民币转换成美元为：{usd:.2f}美元")
    return usd


def jpy_to_cny(amount):
    cny = amount * JPY_TO_CNY_RATE
    print(f"{amount}日元转换成人民币为：{cny:.2f}人民币")
    return cny


def usd_to_cny(amount):
    cny = amount * USD_TO_CNY_RATE
    print(f"{amount}美元转换成人民币为：{cny:.2f}人民币")
    return cny


def convert_currency(amount, conversion_func):
    if not callable(conversion_func):
        raise TypeError("第二个参数必须是一个可调用的函数")
    if not isinstance(amount, (int, float)):
        raise TypeError("金额必须是数字类型")
    
    return conversion_func(amount)


def demonstrate_conversions():
    print("\n" + "="*50)
    print("通用货币兑换函数演示")
    print("="*50)
    
    # 100人民币约合的美元和日元值
    print("\n1. 100人民币兑换：")
    convert_currency(100, cny_to_usd)
    convert_currency(100, cny_to_jpy)
    
    # 100美元约合的人民币以及日元的值
    print("\n2. 100美元兑换：")
    convert_currency(100, usd_to_cny)
    convert_currency(100, usd_to_jpy)  # 需要先转人民币再转日元
    
    # 100日元约合的人民币和美元
    print("\n3. 100日元兑换：")
    convert_currency(100, jpy_to_cny)
    convert_currency(100, jpy_to_usd)  # 需要先转人民币再转美元


def usd_to_jpy(amount):
    """美元转日元（通过人民币中转）"""
    cny = usd_to_cny(amount)
    jpy = cny_to_jpy(cny)
    print(f"{amount}美元转换成日元为：{jpy:.1f}日元")
    return jpy


def jpy_to_usd(amount):
    """日元转美元（通过人民币中转）"""
    cny = jpy_to_cny(amount)
    usd = cny_to_usd(cny)
    print(f"{amount}日元转换成美元为：{usd:.2f}美元")
    return usd



'''AI编写的测试函数'''
# ==================== 测试用例部分 ====================

def run_tests():
    """
    测试通用货币兑换函数
    不使用任何第三方库
    """
    print("="*60)
    print("开始执行测试用例")
    print("="*60)
    
    test_cases = [
        # 测试1：人民币转美元
        {
            "name": "测试1：100人民币转美元",
            "amount": 100,
            "func": cny_to_usd,
            "expected": 14.0,
            "tolerance": 0.01
        },
        # 测试2：人民币转日元
        {
            "name": "测试2：100人民币转日元",
            "amount": 100,
            "func": cny_to_jpy,
            "expected": 2000.0,
            "tolerance": 0.1
        },
        # 测试3：美元转人民币
        {
            "name": "测试3：14美元转人民币",
            "amount": 14,
            "func": usd_to_cny,
            "expected": 100.0,
            "tolerance": 0.01
        },
        # 测试4：日元转人民币
        {
            "name": "测试4：2000日元转人民币",
            "amount": 2000,
            "func": jpy_to_cny,
            "expected": 100.0,
            "tolerance": 0.01
        },
        # 测试5：50人民币转美元
        {
            "name": "测试5：50人民币转美元",
            "amount": 50,
            "func": cny_to_usd,
            "expected": 7.0,
            "tolerance": 0.01
        },
        # 测试6：50人民币转日元
        {
            "name": "测试6：50人民币转日元",
            "amount": 50,
            "func": cny_to_jpy,
            "expected": 1000.0,
            "tolerance": 0.1
        },
        # 测试7：1人民币转美元
        {
            "name": "测试7：1人民币转美元",
            "amount": 1,
            "func": cny_to_usd,
            "expected": 0.14,
            "tolerance": 0.01
        },
        # 测试8：1人民币转日元
        {
            "name": "测试8：1人民币转日元",
            "amount": 1,
            "func": cny_to_jpy,
            "expected": 20.0,
            "tolerance": 0.1
        },
        # 测试9：小数金额测试
        {
            "name": "测试9：10.5人民币转美元",
            "amount": 10.5,
            "func": cny_to_usd,
            "expected": 1.47,
            "tolerance": 0.01
        },
        # 测试10：零值测试
        {
            "name": "测试10：0人民币转美元",
            "amount": 0,
            "func": cny_to_usd,
            "expected": 0.0,
            "tolerance": 0.01
        },
        # 测试11：使用通用函数测试人民币转美元
        {
            "name": "测试11：【通用函数】100人民币转美元",
            "amount": 100,
            "func": lambda x: convert_currency(x, cny_to_usd),
            "expected": 14.0,
            "tolerance": 0.01
        },
        # 测试12：使用通用函数测试人民币转日元
        {
            "name": "测试12：【通用函数】100人民币转日元",
            "amount": 100,
            "func": lambda x: convert_currency(x, cny_to_jpy),
            "expected": 2000.0,
            "tolerance": 0.1
        },
        # 测试13：使用通用函数测试美元转人民币
        {
            "name": "测试13：【通用函数】14美元转人民币",
            "amount": 14,
            "func": lambda x: convert_currency(x, usd_to_cny),
            "expected": 100.0,
            "tolerance": 0.01
        },
    ]
    
    passed = 0
    failed = 0
    failed_details = []
    
    # 执行每个测试用例
    for test in test_cases:
        try:
            # 调用通用函数或直接函数
            result = test["func"](test["amount"])
            
            # 检查结果是否在预期范围内
            if abs(result - test["expected"]) <= test["tolerance"]:
                print(f"✓ {test['name']} 通过")
                print(f"  输入: {test['amount']}, 预期: {test['expected']}, 实际: {result:.4f}")
                passed += 1
            else:
                print(f"✗ {test['name']} 失败")
                print(f"  输入: {test['amount']}, 预期: {test['expected']}, 实际: {result:.4f}, 误差: {abs(result - test['expected'])}")
                failed += 1
                failed_details.append(test['name'])
        except Exception as e:
            print(f"✗ {test['name']} 异常")
            print(f"  错误信息: {e}")
            failed += 1
            failed_details.append(test['name'])
    
    # 测试错误处理（应该抛出异常）
    print("\n" + "-"*60)
    print("错误处理测试：")
    print("-"*60)
    
    # 测试1：传入非函数参数
    try:
        convert_currency(100, "not_a_function")
        print("✗ 错误处理测试失败：非函数参数应该抛出异常")
        failed += 1
    except TypeError as e:
        print(f"✓ 错误处理测试通过：正确捕获非函数参数")
        print(f"  错误信息: {e}")
        passed += 1
    
    # 测试2：传入非数字金额
    try:
        convert_currency("100", cny_to_usd)
        print("✗ 错误处理测试失败：非数字金额应该抛出异常")
        failed += 1
    except TypeError as e:
        print(f"✓ 错误处理测试通过：正确捕获非数字金额")
        print(f"  错误信息: {e}")
        passed += 1
    
    # 测试3：传入列表作为金额
    try:
        convert_currency([100], cny_to_usd)
        print("✗ 错误处理测试失败：列表金额应该抛出异常")
        failed += 1
    except TypeError as e:
        print(f"✓ 错误处理测试通过：正确捕获列表金额")
        print(f"  错误信息: {e}")
        passed += 1
    
    # 打印测试总结
    print("\n" + "="*60)
    print("测试结果汇总")
    print("="*60)
    print(f"总测试用例数: {len(test_cases) + 3}")
    print(f"通过: {passed}")
    print(f"失败: {failed}")
    print(f"通过率: {passed/(passed+failed)*100:.1f}%")
    
    if failed_details:
        print(f"\n失败的用例: {failed_details}")
    else:
        print("\n🎉 所有测试用例全部通过！")
    
    return passed, failed

# 主程序入口
if __name__ == "__main__":
    # 演示计算结果
    demonstrate_conversions()
    
    # 运行测试
    print("\n")
    run_tests()


'''测试发现函数不存在以及货币值类型出错会有问题，在通用货币兑换函数进行了检查和错误的抛出'''