import pytest
from test.TestUtils import TestUtils

def test_boundary_cases():
    """Test boundary values for all functions"""
    try:
        import medicine_tracker
        
        # Zero quantity tests
        assert medicine_tracker.calculate_strips(0, 10) == 0
        assert medicine_tracker.calculate_loose(0, 10) == 0
        assert medicine_tracker.calculate_stock_value(0, 50.0) == 0.0
        
        # Exact strip multiples
        assert medicine_tracker.calculate_loose(100, 10) == 0
        assert medicine_tracker.calculate_strips(100, 10) == 10
        
        # Zero discount test
        assert abs(medicine_tracker.calculate_discount(100.0, 0.0) - 100.0) < 0.01
        
        # Maximum values test
        assert medicine_tracker.calculate_strips(1000, 10) == 100
        assert abs(medicine_tracker.calculate_discount(100.0, 100.0) - 0.0) < 0.01
        
        TestUtils.yakshaAssert("test_boundary_cases", True, "boundary")
    except AssertionError as e:
        print(f"Failed: {str(e)}")
        TestUtils.yakshaAssert("test_boundary_cases", False, "boundary")