from django.db import models
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field


class Product(models.Model):
    CATEGORY_CHOICES = [
        ('men', 'Men'),
        ('women', 'Women'),
        ('children', 'Children'),
    ]

    SIZE_CHOICES = [
        ('XS', 'Extra Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
        ('XXL', 'XXL'),
    ]

    title = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = CKEditor5Field('Text', config_name='extends')

    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percentage = models.PositiveIntegerField(default=0)
    brand = models.CharField(max_length=50, default='Pahiran')
    manufacturer = models.CharField(max_length=50, default='Pahiran')

    views = models.PositiveIntegerField(default=0)
    sold = models.PositiveIntegerField(default=0)
    tags = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)

    # Size and stock
    size = models.CharField(
        max_length=5,
        choices=SIZE_CHOICES,
        blank=True,
        null=True,
        verbose_name="Size"
    )
    stock = models.PositiveIntegerField(
        default=0,
        verbose_name="Stock Quantity",
        help_text="Number of items available for this color/size"
    )

    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='products'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    COLOR_CHOICES = [
        ('white', 'White'),
        ('black', 'Black'),
        ('gray', 'Gray'),
        ('navy', 'Navy Blue'),
        ('red', 'Red'),
        ('maroon', 'Maroon'),
        ('green', 'Green'),
        ('olive', 'Olive'),
        ('brown', 'Brown'),
        ('beige', 'Beige'),
        ('yellow', 'Yellow'),
        ('orange', 'Orange'),
        ('pink', 'Pink'),
        ('purple', 'Purple'),
        ('teal', 'Teal'),
        ('coral', 'Coral'),
        ('sky_blue', 'Sky Blue'),
        ('mint', 'Mint'),
        ('peach', 'Peach'),
        ('mustard', 'Mustard'),
        ('rust', 'Rust'),
    ]

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ImageField(upload_to='products/')

    # Color fields
    color_choice = models.CharField(
        max_length=20,
        choices=COLOR_CHOICES,
        blank=True,
        null=True,
        verbose_name="Select a color"
    )
    custom_color = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Or enter custom color"
    )

    def __str__(self):
        color_display = self.custom_color or (self.get_color_choice_display() if self.color_choice else "")
        parts = [f"Image of {self.product.title}"]
        if color_display:
            parts.append(color_display)
        # Include size from product
        if self.product.size:
            parts.append(self.product.size)
        return " - ".join(parts)
