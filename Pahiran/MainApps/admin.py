from django.contrib import admin
from .models import Product, ProductImage

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1  # Number of extra blank forms
    fields = ('image', 'color_choice', 'custom_color',)
    readonly_fields = ()
    show_change_link = True


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'size', 'selling_price', 'stock', 'views', 'sold', 'is_active', 'created_at')
    list_filter = ('category', 'size', 'is_active', 'created_at')
    search_fields = ('title', 'tags', 'brand', 'manufacturer')
    inlines = [ProductImageInline]
    readonly_fields = ('views', 'sold', 'discount_percentage')
    ordering = ('-created_at',)


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'get_color_display', 'custom_color', 'image_tag')
    list_filter = ('color_choice',)
    search_fields = ('product__title', 'custom_color')

    def get_color_display(self, obj):
        return obj.get_color_choice_display()
    get_color_display.short_description = 'Color'

    def image_tag(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="60" height="60" />'
        return "-"
    image_tag.allow_tags = True
    image_tag.short_description = 'Image Preview'