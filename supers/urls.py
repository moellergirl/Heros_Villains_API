from django.urls import path
from. import views

urlpatterns=[
    path ('', views.Super_list),
    path('<int:pk>/', views.supers_details),

]