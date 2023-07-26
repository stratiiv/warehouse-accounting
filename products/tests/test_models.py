from io import BytesIO
import shutil
from django.test import TestCase, override_settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
from PIL import Image
from products.models import Product, Category

TEST_DIR = 'test_data'


class ProductModelTest(TestCase):
    @classmethod
    @override_settings(MEDIA_ROOT=(TEST_DIR+'/media'))
    def setUpTestData(cls):
        user = User.objects.create_user(username='testuser',
                                        password='testpass')
        category = Category.objects.create(name="some category",
                                           description="some description")
        test_image = Image.new('RGB', size=(200, 200), color='red')
        image_io = BytesIO()
        test_image.save(image_io, format='JPEG')
        image_io.seek(0)
        image = SimpleUploadedFile('test_image.jpg', image_io.read(),
                                   content_type='image/jpeg')

        Product.objects.create(name='Laptop', category=category,
                               image=image, user=user)

    def test_product_preview_generation(self):
        product = Product.objects.get(id=1)
        self.assertIsNotNone(product.preview)

    @classmethod
    def tearDownClass(cls):
        print("\nDeleting temporary files...\n")
        try:
            shutil.rmtree(TEST_DIR)
        except OSError:
            pass
