from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import ProductListView

urlpatterns = [

    path('', views.index, name='product_list'),
    path('', ProductListView.as_view(), name='product_list'),
    path('new/', views.new, name='new_product'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

