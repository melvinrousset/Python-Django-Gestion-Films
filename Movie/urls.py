from django.contrib import admin
from django.urls import path
from .views import (
    Home_View,
    Film_List_View,
    Film_Detail_View,
    Film_Update_View,
    Film_Delete_View,
    Film_Create_View

)

app_name = 'Movie'
urlpatterns = [
    path('', Home_View.as_view(),name="home-view"),
    path('Film/', Film_List_View.as_view(),name="Movie-list-view"),
    path('Film/create/', Film_Create_View.as_view(),name="Movie-create-view"),
    path('Film/<str:title>/', Film_Detail_View.as_view(),name="Movie-detail-view"),
    path('Film/<str:title>/update/', Film_Update_View.as_view(),name="Movie-update-view"),
    path('Film/<str:title>/delete/', Film_Delete_View.as_view(),name="Movie-delete-view"),

    

 
]
