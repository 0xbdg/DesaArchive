from django.urls import path
from .views import *

urlpatterns = [
    path('', SigninView.as_view(), name='signin'),
    path('file-manager/', FilemanagerView.as_view(), name="filemanager"),
    path('account-manager/', AccountManagerView.as_view(), name="accountmanager"),
    path('delete-file/<int:id>', delete, name="del"),
    path('delete-user/<int:id>', user_delete, name="user-del")
]