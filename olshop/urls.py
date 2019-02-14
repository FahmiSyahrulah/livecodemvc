from django.urls import path
from . import views

urlpatterns = [
   path('', views.barang, name='barang'),
   path('barang/<int:barang_id>', views.barang_detail, name='barang_detail')
]
