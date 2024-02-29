from django.urls import path,include
from vectorWoodcrafts import views

urlpatterns = [
    path('', views.index,name='index'),
    path('user_login', views.user_login, name = 'user_login'),
    path('signup', views.signup, name = 'signup'),
    path('signout', views.signout, name = 'signout'),
    path('home', views.home, name = 'home'),
    path('products', views.products, name = 'products')
]