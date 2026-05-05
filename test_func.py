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

    def test_odd_numbers(self):
        """测试奇数"""
        assert is_even(1) is False
        assert is_even(3) is False
        assert is_even(-1) is False
        assert is_even(99) is False

    def test_large_numbers(self):
        """测试大数值"""
        assert is_even(10**6) is True
        assert is_even(10**6 + 1) is False

    def test_type_error_for_float(self):
        """测试浮点数输入应抛出 TypeError"""
        with pytest.raises(TypeError):
            is_even(2.5)

    def test_type_error_for_string(self):
        """测试字符串输入应抛出 TypeError"""
        with pytest.raises(TypeError):
            is_even("2")

    def test_type_error_for_none(self):
        """测试 None 输入应抛出 TypeError"""
        with pytest.raises(TypeError):
            is_even(None)

    def test_type_error_for_list(self):
        """测试列表输入应抛出 TypeError"""
        with pytest.raises(TypeError):
            is_even([2])