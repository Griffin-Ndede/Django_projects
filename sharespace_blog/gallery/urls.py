from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('productdetails/<int:id>/', views.product_detail, name='product_detail'),
    path('edit/<int:id>/', views.edit_product, name='edit_product'),
    path('delete/<int:id>/', views.delete_product, name='delete_product'),
]

