from io import BytesIO
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile


def create_test_image():
    """
    Generate image for tests.
    """
    test_image = Image.new('RGB', size=(200, 200), color='red')
    image_io = BytesIO()
    test_image.save(image_io, format='JPEG')
    image_io.seek(0)
    image = SimpleUploadedFile('test_image.jpg', image_io.read(),
                               content_type='image/jpeg') 
    return image