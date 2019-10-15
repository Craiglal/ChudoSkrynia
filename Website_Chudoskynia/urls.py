"""Website_Chudoskynia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path, include
from products import views as products_views
from homepage import views as homepage_views
from cart import urls as cart_urls
from contact import views as contact_views
from products import urls as products_urls

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'', homepage_views.index, name='home'),
    path(r'contact/', contact_views.contactView, name='contact'),
    path(r'products/', include(products_urls, namespace='products')),
    path(r'cart/', include(cart_urls, namespace='cart')),
    path(r'order/', include('orders.urls', namespace='orders')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
