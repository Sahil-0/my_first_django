from django.test import TestCase
from PhoneReview.models import Brand

class BrandModelTests(TestCase):

    def test_string_representation(self):
        brand = Brand(name="Apple", origin="USA", manufacturing_since=1976)
        self.assertEqual(str(brand), "Apple")