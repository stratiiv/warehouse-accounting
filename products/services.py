import os
from io import BytesIO
from PIL import Image
from django.conf import settings
from django.core.exceptions import ValidationError

PREVIEW_SIZE = (100, 100)
SIZE_LIMIT = 10  # 10MB image limit


def generate_preview_image(image_data: bytes, image_name: str) -> str:
    """Generate a preview image from the original image data.

    This function takes the image data, resizes it to the specified
    preview size, and saves it as a PNG file in the previews directory.

    Returns path to saved preview.
    """
    preview_filename = f"preview_{os.path.basename(image_name)}"
    preview_filename = os.path.splitext(preview_filename)[0] + ".png"
    preview_directory = os.path.join(settings.MEDIA_ROOT, 'products', 'previews')
    os.makedirs(preview_directory, exist_ok=True)  # Create the directory if it doesn't exist

    with Image.open(BytesIO(image_data)) as im:
        im.convert("RGB")
        im.thumbnail(PREVIEW_SIZE)
        preview_path = os.path.join(preview_directory, preview_filename)
        im.save(preview_path, "PNG")

    return os.path.join('products', 'previews', preview_filename).replace("\\", "/")


def validate_image(image):
    if image.size > SIZE_LIMIT * 1024 * 1024:  # in bytes
        raise ValidationError(f"Max file size is {SIZE_LIMIT}MB")