from django.urls import path
from . import views

urlpatterns = [
    path('',views.destination_list),
    path('<int:pk>',views.DestinationList.as_view())
]