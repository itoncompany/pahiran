from django.urls import path
from ContactUs import views
urlpatterns = [
    path('Contact-us/', views.contact_us, name='contact_us'),

]
