import pytest
import re
from test.TestUtils import TestUtils

test_obj = TestUtils()

def test_variable_structure():
    """Test variables and functions are defined correctly"""
    try:
        with open('medicine_tracker.py', 'r') as file:
            content = file.read()
        
        # Check critical variables
        required_vars = [
            'medicine_name', 'manufacturer', 'batch_number', 
            'quantity', 'min_quantity', 'tablets_per_strip',
            'price_per_strip', 'discount_percent', 
            'total_strips', 'loose_tablets', 'discounted_price', 'stock_value'
        ]
        
        # Check required functions with parameters
        required_patterns = [
            r'def\s+calculate_strips\s*\(\s*quantity\s*,\s*tablets_per_strip\s*\)',
            r'def\s+calculate_loose\s*\(\s*quantity\s*,\s*tablets_per_strip\s*\)',
            r'def\s+calculate_discount\s*\(\s*price\s*,\s*discount_percent\s*\)',
            r'def\s+calculate_stock_value\s*\(\s*strips\s*,\s*price\s*\)'
        ]
        
        all_found = True
        # Check variables
        for var in required_vars:
            if not re.search(r'\b' + var + r'\s*=', content):
                all_found = False
                break
                
        # Check function patterns
        for pattern in required_patterns:
            if not re.search(pattern, content):
                all_found = False
                break
        
        test_obj.yakshaAssert("TestVariableStructure", all_found, "functional")
    except Exception as e:
        test_obj.yakshaAssert("TestVariableStructure", False, "functional")

def test_calculation_logic():
    """Test if calculation logic is implemented correctly"""
    try:
        import medicine_tracker
        
        # Test all calculation functions
        strips_exact = medicine_tracker.calculate_strips(100, 10) == 10
        strips_remainder = medicine_tracker.calculate_strips(95, 10) == 9
        
        loose_exact = medicine_tracker.calculate_loose(100, 10) == 0
        loose_remainder = medicine_tracker.calculate_loose(95, 10) == 5
        
        discount_10 = abs(medicine_tracker.calculate_discount(100.0, 10.0) - 90.0) < 0.01
        discount_20 = abs(medicine_tracker.calculate_discount(50.0, 20.0) - 40.0) < 0.01
        
        stock_value = abs(medicine_tracker.calculate_stock_value(10, 50.0) - 500.0) < 0.01
        
        all_correct = strips_exact and strips_remainder and loose_exact and loose_remainder and discount_10 and discount_20 and stock_value
        
        test_obj.yakshaAssert("TestCalculationLogic", all_correct, "functional")
    except Exception as e:
        test_obj.yakshaAssert("TestCalculationLogic", False, "functional")

def test_implementation_details():
    """Test specific implementation requirements"""
    try:
        with open('medicine_tracker.py', 'r') as file:
            content = file.read()
        
        # Check for required operators and type conversions
        requirements_met = True
        
        # Check operators in functions
        requirements_met = requirements_met and '//' in content  # Integer division
        requirements_met = requirements_met and '%' in content   # Modulo
        requirements_met = requirements_met and '1 -' in content and '/100' in content  # Discount formula
        requirements_met = requirements_met and 'strips * price' in content  # Stock calculation
        
        # Check type conversions
        num_conversions = len(re.findall(r'int\(.*?input', content))
        float_conversions = len(re.findall(r'float\(.*?input', content))
        requirements_met = requirements_met and num_conversions >= 3 and float_conversions >= 2
        
        # Check output sections
        requirements_met = requirements_met and 'Rs.' in content
        requirements_met = requirements_met and 'REORDER REQUIRED' in content
        requirements_met = requirements_met and 'STOCK SUFFICIENT' in content
        
        test_obj.yakshaAssert("TestImplementationDetails", requirements_met, "functional")
    except Exception as e:
        test_obj.yakshaAssert("TestImplementationDetails", False, "functional")