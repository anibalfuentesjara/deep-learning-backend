from django.urls import path
from .views import Classification

urlpatterns = [
    path('classify_image', Classification.as_view(), name=Classification.name)
]
