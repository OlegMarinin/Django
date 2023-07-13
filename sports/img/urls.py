from . import views
from django.urls import path, include
from .views import upload_images
urlpatterns = [
    path('', upload_images, name="images"),
]