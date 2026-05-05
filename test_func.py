from func import is_even
# 测试代码
from func import is_even
import pytest


class TestIsEven:
    """测试 is_even 函数的单元测试类"""

    def test_positive_even(self):
        """测试正偶数"""
        assert is_even(2) is True
        assert is_even(4) is True
        assert is_even(10) is True
        assert is_even(100) is True

    def test_negative_even(self):
        """测试负偶数"""
        assert is_even(-2) is True
        assert is_even(-4) is True
        assert is_even(-10) is True
        assert is_even(-100) is True

    def test_zero(self):
        """测试零（0 是偶数）"""
        assert is_even(0) is True

    def test_positive_odd(self):
        """测试正奇数"""
        assert is_even(1) is False
        assert is_even(3) is False
        assert is_even(9) is False
        assert is_even(101) is False

    def test_negative_odd(self):
        """测试负奇数"""
        assert is_even(-1) is False
        assert is_even(-3) is False
        assert is_even(-9) is False
        assert is_even(-101) is False

    def test_large_numbers(self):
        """测试大数"""
        assert is_even(1000000) is True
        assert is_even(1000001) is False
        assert is_even(-1000000) is True
        assert is_even(-1000001) is False

    def test_single_digit_numbers(self):
        """测试单个数字"""
        for i in range(10):
            if i % 2 == 0:
                assert is_even(i) is True
            else:
                assert is_even(i) is False