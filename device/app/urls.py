from django.urls import path
from app.views import BarcodeScanner,StoreBarcode

urlpatterns = [
    path('my-page/', BarcodeScanner.as_view(), name='my_page'),
    path('store-barcode/', StoreBarcode.as_view(), name='store_barcode'),
]
