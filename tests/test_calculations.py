import unittest
from datetime import time, date
from logic.calculations import calculate_duration, calculate_total_pay, calculate_mileage

class TestCalculations(unittest.TestCase):
    """
    Tests that gig duration function is correct, both for same-day and overnight gigs.
    """
    def test_calculate_duration_same_day(self):
        start = time(9, 0)
        end = time(10, 30)
        d = calculate_duration(start, end, date(2024, 1, 1))
        self.assertEqual(d, 90)

    def test_calculation_duration_overnight(self):
        start = time(23, 0)
        end = time(1, 0)
        d = calculate_duration(start, end, date(2024, 1, 1))
        self.assertEqual(d, 120)
