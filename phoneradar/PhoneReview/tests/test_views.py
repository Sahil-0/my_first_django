from django.test import TestCase
from django.urls import reverse
from PhoneReview.models import Brand

class BrandViewTests(TestCase):

    def setUp(self):
        Brand.objects.create(name="Samsung", origin="Korea", manufacturing_since=1938)

    def test_index_status_code(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_index_template(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'PhoneReview/index.html')

    def test_index_contains_brand(self):
        response = self.client.get(reverse('index'))
        self.assertContains(response, "Samsung")