# 测试代码
from func import is_even

import pytest

class TestIsEven:
    """测试 is_even 函数的单元测试类"""
    
    def test_positive_even(self):
        """测试正偶数"""
        assert is_even(2) is True
        assert is_even(4) is True
        assert is_even(100) is True
    
    def test_negative_even(self):
        """测试负偶数"""
        assert is_even(-2) is True
        assert is_even(-4) is True
        assert is_even(-100) is True
    
    def test_zero(self):
        """测试零（0 是偶数）"""
        assert is_even(0) is True
    
    def test_positive_odd(self):
        """测试正奇数"""
        assert is_even(1) is False
        assert is_even(3) is False
        assert is_even(99) is False
    
    def test_negative_odd(self):
        """测试负奇数"""
        assert is_even(-1) is False
        assert is_even(-3) is False
        assert is_even(-99) is False
    
    def test_large_numbers(self):
        """测试大数"""
        assert is_even(10**6) is True
        assert is_even(10**6 + 1) is False
        assert is_even(-10**6) is True
        assert is_even(-10**6 - 1) is False
    
    def test_edge_cases(self):
        """测试边界情况"""
        # 最小和最大的常见整数范围边缘
        assert is_even(2147483646) is True  # 接近 sys.maxsize 的偶数
        assert is_even(2147483647) is False # 接近 sys.maxsize 的奇数