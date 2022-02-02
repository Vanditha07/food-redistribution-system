from django.urls import path
from .views import (
    IndexView,
    FoodInfoView,
    DonorInfoView,
    ReceiverInfoView,
    )

urlpatterns = [ 
    path('', IndexView, name='index'),
    path('info', FoodInfoView, name='info'),
    path('donate', DonorInfoView.as_view, name='donate'),
    path('collect', ReceiverInfoView.as_view, name='collect'),
   
]