from django.db import models
import os

# Create your models here.

'''
class Document(models.Model):
    CATEGORIES = [
        ('keterangan', 'Surat Keterangan'),
        ('masuk', 'Surat Masuk'),
        ('keluar', 'Surat Keluar'),
        ('asset', 'Asset'),
    ]

    category = models.CharField(max_length=20, choices=CATEGORIES)
    file = models.FileField(upload_to='')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def get_file_extension(self):
        _, extension = os.path.splitext(self.file.name)
        return extension

    def __str__(self):
        return f"{self.get_category_display()} - {self.file.name}"
'''

class SuratKeterangan(models.Model):
    file = models.FileField(upload_to='')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def get_file_extension(self):
        _, extension = os.path.splitext(self.file.name)
        return extension
    
    def __str__(self):
        return self.file.name

class SuratMasuk(models.Model):
    file = models.FileField(upload_to='')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def get_file_extension(self):
        _, extension = os.path.splitext(self.file.name)
        return extension
    
    def __str__(self):
        return self.file.name

class SuratKeluar(models.Model):
    file = models.FileField(upload_to='')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def get_file_extension(self):
        _, extension = os.path.splitext(self.file.name)
        return extension
    
    def __str__(self):
        return self.file.name

class Asset(models.Model):
    file = models.FileField(upload_to='')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def get_file_extension(self):
        _, extension = os.path.splitext(self.file.name)
        return extension
    
    def __str__(self):
        return self.file.name
