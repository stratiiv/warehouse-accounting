from tempfile import TemporaryDirectory

from django.test import TestCase, override_settings
from django.contrib.auth.models import User

from products.models import Product, Category
from .helpers import create_test_image

TEMP_DIR = TemporaryDirectory()


@override_settings(MEDIA_ROOT=TEMP_DIR.name)
class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username='testuser',
                                        password='testpass')
        category = Category.objects.create(name="some category",
                                           description="some description")
        image = create_test_image()
        Product.objects.create(name='someproduct', category=category,
                               image=image, user=user)

    def test_product_preview_generation(self):
        product = Product.objects.get(id=1)
        self.assertIsNotNone(product.preview)

    @classmethod
    def tearDownClass(cls):
        TEMP_DIR.cleanup()
