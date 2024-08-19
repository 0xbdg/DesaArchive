from django.urls import path
from .views import *

urlpatterns = [
    path('', SigninView.as_view(), name='signin'),
    path('dashboard/',DashboardView.as_view(),name='dashboard'),
    path('file-manager/', FilemanagerView.as_view(), name="filemanager"),
    path('account-manager/', SuperuserManagerView.as_view(), name="accountmanager"),
    path("logout/", user_logout, name="logout"),
    path('delete-file/<int:id>', file_delete, name="del"),
    path('delete-user/<int:id>', user_delete, name="user-del"),
    path('user/edit/<int:id>', user_update, name="user-edit")
]