from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="estatelist"),
    path('<int:apartment_id>', views.apartment, name="apartment"),
    path('search', views.search, name="search"),
    path('favorite', views.favorite, name="favorite"),

]
