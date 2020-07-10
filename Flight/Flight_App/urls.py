from django.urls import path
from . import views


urlpatterns = [
    path('', views.index,name = "index"),
    path('<int:flight_id>/', views.flight_def, name="flight_def"),
]