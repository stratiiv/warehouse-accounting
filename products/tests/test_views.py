from tempfile import TemporaryDirectory

from django.test import TestCase, override_settings
from django.urls import reverse
from django.contrib.auth.models import User

from products.models import Product, Category
from .helpers import create_test_image

TEMP_DIR = TemporaryDirectory()


@override_settings(MEDIA_ROOT=TEMP_DIR.name)
class PermissionsTest(TestCase):
    def setUp(self):
        User.objects.create_user(username='user', password='pass')
        product_owner = User.objects.create_user(username='owner',
                                                 password='pass')
        self.category = Category.objects.create(name="some category")
        image = create_test_image()
        self.product = Product.objects.create(name='someproduct',
                                              category=self.category,
                                              image=image, user=product_owner)

    def test_authentication_login(self):
        r = self.client.post(reverse('account_login'),
                             {'login': 'user', 'password': 'pass'})
        self.assertEqual(r.status_code, 302)  # redirect if success

    def test_authentication_signup(self):
        r = self.client.post(reverse('account_signup'),
                             {'username': 'someuser',
                             'password1': 'chBqNrdL@R74RwA',
                              'password2': 'chBqNrdL@R74RwA'})
        self.assertEqual(r.status_code, 302)  # redirect if success

    def test_product_owner_or_read_only_valid(self):
        image = create_test_image()
        self.client.login(username='owner', password='pass')
        payload = {
            'name': 'edited',
            'category': self.category.id,
            'image': image     
        }
        r = self.client.post(
            reverse('product-update', kwargs={'pk': self.product.id}),
            data=payload
        )
        edited_product = Product.objects.get(id=self.product.id)
        self.assertEqual(r.status_code, 302)
        self.assertEqual(edited_product.name, 'edited')

    def test_product_owner_or_read_only_non_valid(self):
        image = create_test_image()
        self.client.login(username='user', password='pass')
        payload = {
            'name': 'edited',
            'category': self.category.id,
            'image': image     
        }
        r = self.client.post(
            reverse('product-update', kwargs={'pk': self.product.id}),
            data=payload
        )
        edited_product = Product.objects.get(id=self.product.id)
        self.assertEqual(r.status_code, 403)
        self.assertEqual(edited_product.name, 'someproduct')
