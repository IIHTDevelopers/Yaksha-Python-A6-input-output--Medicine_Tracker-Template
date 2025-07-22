import unittest
from medicine_tracker import (
    calculate_strips,
    calculate_loose,
    calculate_discount,
    calculate_stock_value
)
from test.TestUtils import TestUtils


class TestExpectedValuesYaksha(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_obj = TestUtils()

    def test_calculate_strips_expected(self):
        try:
            result = calculate_strips(85, 10) == 8  # 85 // 10 = 8
            self.test_obj.yakshaAssert("TestCalculateStripsExpected", result, "functional")
            print("TestCalculateStripsExpected =", "Passed" if result else "Failed")
        except Exception:
            self.test_obj.yakshaAssert("TestCalculateStripsExpected", False, "functional")
            print("TestCalculateStripsExpected = Failed | Exception")

    def test_calculate_loose_expected(self):
        try:
            result = calculate_loose(85, 10) == 5  # 85 % 10 = 5
            self.test_obj.yakshaAssert("TestCalculateLooseExpected", result, "functional")
            print("TestCalculateLooseExpected =", "Passed" if result else "Failed")
        except Exception:
            self.test_obj.yakshaAssert("TestCalculateLooseExpected", False, "functional")
            print("TestCalculateLooseExpected = Failed | Exception")

    def test_calculate_discount_expected(self):
        try:
            result = round(calculate_discount(28.50, 10.0), 2) == 25.65
            self.test_obj.yakshaAssert("TestCalculateDiscountExpected", result, "functional")
            print("TestCalculateDiscountExpected =", "Passed" if result else "Failed")
        except Exception:
            self.test_obj.yakshaAssert("TestCalculateDiscountExpected", False, "functional")
            print("TestCalculateDiscountExpected = Failed | Exception")

    def test_calculate_stock_value_expected(self):
        try:
            result = round(calculate_stock_value(8, 28.50), 2) == 228.00  # 8 * 28.5
            self.test_obj.yakshaAssert("TestCalculateStockValueExpected", result, "functional")
            print("TestCalculateStockValueExpected =", "Passed" if result else "Failed")
        except Exception:
            self.test_obj.yakshaAssert("TestCalculateStockValueExpected", False, "functional")
            print("TestCalculateStockValueExpected = Failed | Exception")
