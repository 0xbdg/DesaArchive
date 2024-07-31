from django.urls import path
from .views import *

url_patterns = [
    path('', SigninView.as_view(), name='signin'),
    path('filemanager/', FilemanagerView.as_view(), name="filemanager")
]