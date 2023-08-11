from django.contrib import admin
from django.urls import path
from zomato import views
urlpatterns = [
    path('', views.menu_view, name='menu'),
    path('add', views.add_dish_view, name='add'),
   path('remove/', views.remove, name='remove'),
    path('update/', views.update, name='update'),
     


    path('order', views.take_order, name='take_order'),
    path('review', views.review_orders, name='review_orders'),
   path('exit', views.exit_option, name='exit_option'),
    path('update-order-status/', views.update_order_status, name='update_order_status'),
]