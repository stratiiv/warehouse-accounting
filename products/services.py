from io import BytesIO
from PIL import Image
from django.core.files import File
from django.core.exceptions import ValidationError

PREVIEW_SIZE = (100, 100)
SIZE_LIMIT = 10  # 10MB image limit


def generate_preview_image(image, size=PREVIEW_SIZE):
    """
    Generate a preview image from the provided image.
    """
    with Image.open(image) as im:
        im.convert('RGB')
        im.thumbnail(size)
        thumb_io = BytesIO()
        im.save(thumb_io, 'JPEG')
        preview = File(thumb_io, name=image.name)
    return preview


def validate_image(image):
    """
    Validate the size of the provided image.
    """
    if image.size > SIZE_LIMIT * 1024 * 1024:  # in bytes
        raise ValidationError(f"Max file size is {SIZE_LIMIT}MB")
