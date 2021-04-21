from django.urls import path
from . import views


app_name = 'auto'
urlpatterns = [
    # path('', views.index, name='index')
    path('', views.CarList.as_view(), name='index'),
    # path('car_create_form/', views.CarAdd.as_view(), name='car_create_form'),
    # path('car/<int:pk>', views.CarDetail.as_view, name='car_detail')
    path('car_new/', views.car_new, name='car_new'),
    path('search/', views.SearchResult.as_view(), name='search_result')
]