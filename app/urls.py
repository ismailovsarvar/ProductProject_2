from django.urls import path

from app.views import index, product_detail, add_product, add_customer

urlpatterns = [
    path('index/', index, name='index'),
    path('product_detail/<int:product_id>', product_detail, name='product_detail'),

]
