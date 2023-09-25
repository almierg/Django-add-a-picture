from django.contrib import admin
from django.urls import path
from image import views

# this import show upload images in browser 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)# this import show upload images in browser
