from tkinter.font import names

from django.contrib import admin
from django.urls import path
from main.views import *
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', test_view),
    path('', index_view),
    path('talabalar/', talabalar_view, name='talabalar'),
    path('kitoblar/', kitoblar_view),
    path('kitoblar/<int:kitob_id>/', kitob_retrieve_view),
    path('kitoblar/<int:kitob_id>/delete/', kitob_delete_view),
    path('kitoblar/<int:kitob_id>/delete/confirm/', kitob_delete_confirm_view),
    path('talabalar/<int:talaba_id>/', talaba_retrieve_view),
    path('mualliflar/', mualliflar_view),
    path('mualliflar/<int:muallif_id>/', muallif_retrieve_view),
    path('mualliflar/<int:muallif_id>/delete/', muallif_delete_view),
    path('mualliflar/<int:muallif_id>/delete/confirm/', muallif_delete_confirm_view),
    path('talabalar/<int:talaba_id>/update/', talaba_update_view,name='talaba-update'),
    path('talabalar/<int:talaba_id>/delete/', talaba_delete_view),
    path('talabalar/<int:talaba_id>/delete/confirm/', talaba_delete_confirm_view),
]
