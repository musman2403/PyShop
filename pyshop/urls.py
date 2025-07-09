from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', lambda request: redirect('product_list')),

    path('products/', include('products.urls')),

    path('accounts/', include('allauth.urls')),
    path('users/', include('accounts.urls')),

    path('cart/', include('cart.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
