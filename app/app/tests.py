from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    """Tes the calc module"""

    def test_add_numbers(self):
        """Test adding numbers"""
        res = calc.add(5, 6)
        self.assertEquals(res, 11)

    def test_subtract_number(self):
        res = calc.subtract(6.4, 5)
        self.assertAlmostEqual(res, 1.4, delta=1e-9)
