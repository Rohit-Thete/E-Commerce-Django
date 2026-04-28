from .views import register,login_user,UserView,CategoryView,ProductView
from django.urls import path

urlpatterns = [
    path('register/',register),
    path('login/',login_user),
    path('user/',UserView.as_view()),
    path('category/',CategoryView.as_view()),
    path('category/<int:pk>/',CategoryView.as_view()),
    path('product/',ProductView.as_view()),
    path('product/<int:pk>/',ProductView.as_view()),

]
