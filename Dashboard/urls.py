from django.urls import path
from .views import *

urlpatterns = [
    path('', SigninView.as_view(), name='signin'),
    path('dashboard/',DashboardView.as_view(),name='dashboard'),
    #path('file-manager/', FilemanagerView.as_view(), name="filemanager"),
    path('surat-keterangan', SuratKeteranganView.as_view(), name="keterangan"),
    path('surat-masuk', SuratMasukView.as_view(), name="masuk"),
    path('surat-keluar', SuratKeluarView.as_view(), name="keluar"),
    path('asset', AssetView.as_view(), name="asset"),
    path('account-manager/', SuperuserManagerView.as_view(), name="accountmanager"),
    path("logout/", user_logout, name="logout"),
    #path('delete-file/<int:id>', file_delete, name="del"),
    path('delete-suratketerangan/<int:id>', keterangan_delete, name="ket-del"),
    path('delete-suratmasuk/<int:id>', masuk_delete, name="m-del"),
    path('delete-suratkeluar/<int:id>', keluar_delete, name="kel-del"),
    path('delete-fileaset/<int:id>', aset_delete, name="a-del"),
    path('delete-user/<int:id>', user_delete, name="user-del"),
    path('user/edit/<int:id>', user_update, name="user-edit")
]