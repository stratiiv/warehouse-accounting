from django.db import models
from django.contrib.auth.models import User
from .services import generate_preview_image, validate_image


class Category(models.Model):
    """
    Model representing a category for products.
    """
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.id} {self.name}"


class Product(models.Model):
    """
    Model representing a product in the inventory.
    """
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products',
                              validators=[validate_image])
    preview = models.ImageField(upload_to='products/previews', blank=True,
                                null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        """Generate image preview before saving."""
        image_data = self.image.read()  # Read the image data
        preview_path = generate_preview_image(image_data, self.image.name)
        self.preview = preview_path
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.id} {self.name}"
