# urls.py (main)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('library.urls')),  # Replace 'your_app' with the name of your app
]
