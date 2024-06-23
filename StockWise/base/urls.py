from django.urls import path
from .views import *

urlpatterns = [
    path('', ProductView.as_view(), name = 'list'),
    path('<int:pk>/', ProductRetrieveView.as_view(), name = 'retrieve'),
    path('delete/<int:pk>/', ProductRetrieveView.as_view(), name = 'retrieve'),
    path('update/<int:pk>/', ProductRetrieveView.as_view(), name = 'retrieve')
]
