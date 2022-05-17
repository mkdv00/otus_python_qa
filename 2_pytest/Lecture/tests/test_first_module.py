import pytest


def division(a, b):
    return a / b


@pytest.mark.usefixtures('environment')
class TestDivision:

    def test_division_by_5(self):
        assert division(10, 5) == 2, f"Division 10 by 5 is not equal 2"

    def test_division_by_10(self):
        assert division(20, 10) == 2, f"Division 20 by 10 is not equal 2"
        
    def test_division_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            assert division(5, 0), f"Division by zero is working"
