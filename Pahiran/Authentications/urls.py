from django.urls import path
from Authentications import views
urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('create-account/', views.create_account, name='create_account'),
    path('dashboard/',views.dashboard,name='dashboard'),
]
