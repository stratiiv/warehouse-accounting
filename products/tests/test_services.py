from tempfile import TemporaryDirectory

from django.test import TestCase, override_settings
from django.core.exceptions import ValidationError
from django.core.files import File

from products.services import generate_preview_image, validate_image
from .helpers import create_test_image

TEMP_DIR = TemporaryDirectory()


@override_settings(MEDIA_ROOT=TEMP_DIR.name)
class ServicesTest(TestCase):
    def setUp(self):
        self.image = create_test_image()

    def test_preview_generation(self):
        preview = generate_preview_image(self.image)
        self.assertTrue(preview)
        self.assertTrue(isinstance(preview, File))

    def test_valid_image_size_validation(self):
        validate_image(self.image)

    def test_too_large_image_size_validation(self):
        self.image.name = 'large_image.jpg'
        self.image.size = 11 * 1024 * 1024
        with self.assertRaises(ValidationError):
            validate_image(self.image)

    @classmethod
    def tearDownClass(cls):
        TEMP_DIR.cleanup()
