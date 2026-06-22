from decimal import Decimal

from django.test import TestCase

from calculate import math_operation


class MathTests(TestCase):

    def test_add_two_numbers(self):
        self.assertEqual(math_operation.add_two_numbers(1, 1),2)

    def test_add_two_numbers_negative_result(self):
        self.assertEqual(math_operation.add_two_numbers(1, -2),-1)

    def test_add_two_numbers_decimal(self):
        self.assertEqual(math_operation.add_two_numbers(Decimal(1.25),Decimal(1.25)),2.5)

    def test_add_two_numbers_float(self):
        self.assertEqual(math_operation.add_two_numbers(1.25,1.25),2.5)