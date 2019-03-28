from django.urls import path
from depreciationapp import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


app_name = 'depreciationapp'

urlpatterns = [
	path('', views.index),  
	path('search-model/<str:brand>/', views.serchModel),
	path('search-data/<str:brand>/<str:model>/', views.serchData), 
]


urlpatterns += staticfiles_urlpatterns()