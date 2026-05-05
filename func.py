def is_even(number: int) -> bool:
    """
    判断一个整数是否为偶数。
    
    Args:
        number (int): 需要判断的整数。
        
    Returns:
        bool: 如果是偶数返回 True，否则返回 False。
        
    Raises:
        TypeError: 如果输入不是整数类型。
    """
    if not isinstance(number, int):
        raise TypeError(f"Expected an integer, but got {type(number).__name__}")
    
    return number % 2 == 0