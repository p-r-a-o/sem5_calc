"""
Unit tests for Simple Calculator CLI Application
"""

import pytest
from calculator import add, subtract, multiply, divide

class TestAddition:
    """Test cases for addition function"""
    
    def test_add_positive_numbers(self):
        assert add(5, 3) == 8
    
    def test_add_negative_numbers(self):
        assert add(-5, -3) == -8
    
    def test_add_mixed_numbers(self):
        assert add(-5, 3) == -2
    
    def test_add_zero(self):
        assert add(5, 0) == 5
    
    def test_add_decimals(self):
        assert add(2.5, 3.7) == pytest.approx(6.2)

class TestSubtraction:
    """Test cases for subtraction function"""
    
    def test_subtract_positive_numbers(self):
        assert subtract(10, 4) == 6
    
    def test_subtract_negative_numbers(self):
        assert subtract(-5, -3) == -2
    
    def test_subtract_mixed_numbers(self):
        assert subtract(5, 10) == -5
    
    def test_subtract_zero(self):
        assert subtract(5, 0) == 5
    
    def test_subtract_decimals(self):
        assert subtract(5.5, 2.3) == pytest.approx(3.2)

class TestMultiplication:
    """Test cases for multiplication function"""
    
    def test_multiply_positive_numbers(self):
        assert multiply(4, 5) == 20
    
    def test_multiply_negative_numbers(self):
        assert multiply(-4, -5) == 20
    
    def test_multiply_mixed_numbers(self):
        assert multiply(-4, 5) == -20
    
    def test_multiply_by_zero(self):
        assert multiply(5, 0) == 0
    
    def test_multiply_decimals(self):
        assert multiply(2.5, 4) == pytest.approx(10.0)

class TestDivision:
    """Test cases for division function"""
    
    def test_divide_positive_numbers(self):
        assert divide(10, 2) == 5
    
    def test_divide_negative_numbers(self):
        assert divide(-10, -2) == 5
    
    def test_divide_mixed_numbers(self):
        assert divide(-10, 2) == -5
    
    def test_divide_decimals(self):
        assert divide(7.5, 2.5) == pytest.approx(3.0)
    
    def test_divide_by_zero(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10, 0)
    
    def test_divide_zero_by_number(self):
        assert divide(0, 5) == 0

class TestEdgeCases:
    """Test edge cases"""
    
    def test_large_numbers(self):
        assert add(1000000, 2000000) == 3000000
    
    def test_very_small_decimals(self):
        assert multiply(0.0001, 0.0001) == pytest.approx(0.00000001)
    
    def test_negative_zero(self):
        assert add(-0, 0) == 0