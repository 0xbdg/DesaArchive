from django.urls import path
from .views import *

urlpatterns = [
    path('', SigninView.as_view(), name='signin'),
    path('file-manager/', FilemanagerView.as_view(), name="filemanager"),
    path('account-manager/', AccountManagerView.as_view(), name="accountmanager")
]