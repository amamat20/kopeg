from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    path('pembelian/', views.get_all_pembelian, name='get_all_pembelian'),    
    path('pembelian/add', views.add_pembelian, name='add_pembelian'),
    path('pembelian/edit/<str:pembelian_id>/', views.edit_pembelian, name='edit_pembelian'),
    path('pembelian/delete/<str:pembelian_id>/', views.delete_pembelian, name='delete_pembelian'),
    
    path('penjualan/', views.get_all_penjualan, name='get_all_penjualan'),
    path('penjualan/add', views.add_penjualan, name='add_penjualan'),
    path('penjualan/edit/<str:penjualan_id>/', views.edit_penjualan, name='edit_penjualan'),
    path('penjualan/delete/<str:penjualan_id>/', views.delete_penjualan, name='delete_penjualan'),

    path('retur/', views.get_all_retur, name='get_all_retur'),
    path('retur/add/', views.add_retur, name='add_retur'),
    path('retur/edit/<str:retur_id>/', views.edit_retur, name='edit_retur'),
    path('retur/delete/<str:retur_id>/', views.delete_retur, name='delete_retur'),
    
    path('perbulan/', views.upload_perbulan, name='upload_perbulan'),
    
    path('dashboard-utama/', views.dashboard_utama, name='dashboard_utama'),
    
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/pembelian/', views.dashboard_pembelian, name='dashboard_pembelian'),
    path('dashboard/penjualan/', views.dashboard_penjualan, name='dashboard_penjualan'),
    path('dashboard/retur/', views.dashboard_retur, name='dashboard_retur'),
    path('dashboard/stok/', views.dashboard_stok, name='dashboard_stok'),
    path('dashboard/perbandingan/', views.dashboard_perbandingan, name='dashboard_perbandingan'),


    
    path('dashboard/export/', views.export_data_csv, name='export_data_csv'),

    path('prediksi/', views.prediksi_stok, name='prediksi_stok'),
    
    path('', views.index, name='index'),

]
