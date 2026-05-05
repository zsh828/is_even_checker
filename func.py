# 功能代码
def is_even(number: int) -> bool:
    """
    判断一个数字是否为偶数。
    
    Args:
        number (int): 待判断的整数
        
    Returns:
        bool: 如果是偶数返回 True，否则返回 False
    """
    return number % 2 == 0