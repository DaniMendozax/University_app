from django.contrib import admin
from django.urls import path
from Academic.views import contactForm, contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contactform/', contactForm),
    path('contact/', contact)
]
