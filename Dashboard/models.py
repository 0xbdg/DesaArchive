from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.exceptions import ValidationError
from datetime import datetime

def validate_file_extension(value):
    import os
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf', '.docx', ".xlsx"]
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension. Only .pdf and .docx files are allowed.')

# Create your models here.

class tbl_certificate(models.Model):
    file = models.FileField(upload_to='files', validators=[validate_file_extension])
    upload_time = models.DateTimeField(default=datetime.now)

class tbl_income(models.Model):
    file = models.FileField(upload_to='files', validators=[validate_file_extension])
    upload_time = models.DateTimeField(default=datetime.now)

class tbl_outcome(models.Model):
    file = models.FileField(upload_to='files', validators=[validate_file_extension])
    upload_time = models.DateTimeField(default=datetime.now)

class tbl_asset(models.Model):
    file = models.FileField(upload_to='files', validators=[validate_file_extension])
    upload_time = models.DateTimeField(default=datetime.now)