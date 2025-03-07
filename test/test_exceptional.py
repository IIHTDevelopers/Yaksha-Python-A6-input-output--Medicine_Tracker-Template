import pytest
from test.TestUtils import TestUtils

def test_exceptional_cases():
    """Test exceptional cases for all functions"""
    try:
        import medicine_tracker
        
        # Negative quantity handling
        assert medicine_tracker.calculate_strips(-100, 10) == -10
        assert medicine_tracker.calculate_loose(-95, 10) <= 0
        
        # Invalid price handling
        assert medicine_tracker.calculate_discount(-100.0, 10.0) < 0
        assert abs(medicine_tracker.calculate_discount(0.0, 10.0)) < 0.01
        
        # Invalid discount handling
        assert medicine_tracker.calculate_discount(100.0, -10.0) > 100.0
        assert medicine_tracker.calculate_discount(100.0, 200.0) < 0
        
        # Division by zero should raise exception
        with pytest.raises(ZeroDivisionError):
            medicine_tracker.calculate_strips(100, 0)
        with pytest.raises(ZeroDivisionError):
            medicine_tracker.calculate_loose(100, 0)
        
        TestUtils.yakshaAssert("test_exceptional_cases", True, "exceptional")
    except AssertionError as e:
        print(f"Failed: {str(e)}")
        TestUtils.yakshaAssert("test_exceptional_cases", False, "exceptional")