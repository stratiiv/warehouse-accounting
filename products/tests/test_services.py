from django.test import TestCase
from django.core.exceptions import ValidationError
from django.core.files import File
from io import BytesIO
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile
from products.services import (generate_preview_image, validate_image,
                               SIZE_LIMIT, PREVIEW_SIZE)


class ServicesTest(TestCase):
    def test_preview_generation(self):
        test_image = Image.new('RGB', size=(200, 200), color='red')
        image_io = BytesIO()
        test_image.save(image_io, format='JPEG')
        image_io.seek(0)
        image = SimpleUploadedFile('test_image.jpg', image_io.read(),
                                   content_type='image/jpeg')
        preview = generate_preview_image(image)
        self.assertTrue(preview)
        self.assertTrue(isinstance(preview, File))

    
    