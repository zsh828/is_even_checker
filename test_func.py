from func import is_even
# 测试代码
# 请保存此代码到 test_counter.py

from func import is_even

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