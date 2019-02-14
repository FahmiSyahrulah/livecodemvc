from django.shortcuts import render
from .models import katalog
from django.utils import timezone


def barang(request):
    item = katalog.objects.all()
    return render(request, 'katalog.html', {'items' : item})

def barang_detail(request, barang_id):
    item = katalog.objects.get(pk=barang_id)
    return render(request, 'detail_barang.html', {'item' : item})