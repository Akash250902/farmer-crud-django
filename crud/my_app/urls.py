from django.urls import path
from . import views

urlpatterns = [
    path("", views.farmer_all, name="all_farmer"),
    path("add/", views.add_farmer, name="add_farmer"),
    path("update/<int:id>/", views.update_farmer, name="update_farmer"),
    path("delete/<int:id>/", views.delete_farmer, name="delete_farmer"),
    path('about/', views.about, name='about'),
]
