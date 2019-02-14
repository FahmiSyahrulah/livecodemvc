from django.db import models
from django.utils import timezone

class katalog(models.Model):
    judul = models.CharField(max_length = 255)
    image = models.CharField(max_length = 255)
    deskripsi = models.CharField(max_length = 255)
    harga = models.CharField(max_length = 255)

    def __str__(self):
        return self.judul
