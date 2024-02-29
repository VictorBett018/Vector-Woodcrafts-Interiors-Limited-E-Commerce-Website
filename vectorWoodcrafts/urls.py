from django.urls import path,include
from vectorWoodcrafts import views

urlpatterns = [
    path('', views.index,name='index'),
    path('login', views.login, name = 'login'),
    path('signup', views.signup, name = 'signup'),
    path('home', views.home, name = 'home'),
    path('products', views.products, name = 'products')
]