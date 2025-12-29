from django.shortcuts import render
from MainApps.models import Product
from django.shortcuts import render, get_object_or_404

def home(request):
    # All active products (Men, Women, Children)
    products = Product.objects.filter(is_active=True).order_by('-created_at')

    # Optional: filter by category
    men_products = Product.objects.filter(is_active=True, category='men').order_by('-created_at')
    women_products = Product.objects.filter(is_active=True, category='women').order_by('-created_at')
    children_products = Product.objects.filter(is_active=True, category='children').order_by('-created_at')

    context = {
        'products': products,
        'men_products': men_products,
        'women_products': women_products,
        'children_products': children_products,
    }

    return render(request, 'MainApps/home.html', context)


def product_info(request, id=None):
    product = get_object_or_404(Product, id=id, is_active=True)
    images = product.images.all()

    sizes = [product.size] if product.size else []

    colors_qs = product.images.values('color_choice', 'custom_color').distinct()
    colors = []
    for c in colors_qs:
        if c['custom_color']:
            colors.append(c['custom_color'])
        elif c['color_choice']:
            colors.append(c['color_choice'])

    unique_colors = list(dict.fromkeys(colors))

    best_sellers = (
        Product.objects
        .filter(is_active=True)
        .exclude(id=product.id)
        .order_by('-sold')[:6]
    )
    related_products = (
        Product.objects
        .filter(
            is_active=True,
            category=product.category
        )
        .exclude(id=product.id)
        .order_by('-created_at')[:6]
    )

    context = {
        'product': product,
        'images': images,
        'sizes': sizes,
        'colors': unique_colors,
        'best_sellers': best_sellers,
        'related_products': related_products[:4],
    }

    return render(request, 'MainApps/product.html', context)