from MainApps import views
from django.urls import path
urlpatterns = [
    path('',views.home,name='home'),
    path('product-info/<int:id>/',views.product_info,name='product_info'),
]
