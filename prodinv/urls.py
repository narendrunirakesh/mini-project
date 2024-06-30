from django .urls import path
from .import views


urlpatterns=[
    path('home/',views.homepage,name='homeurl'),
    path('create/',views.createproduct,name='createurl'),
    path('read/',views.readproduct,name='readurl'),
    path('delete/',views.deleteproduct,name='deleteurl'),
    path('deleteprd/<int:prodid>',views.deleteprodid,name='deleteprodurl'),
    path('update/<int:prodid>/',views.updateproduct,name='updateproducturl'),
    #path('product/<int:pk>/edit/', views.product_update, name='product_update'),
]