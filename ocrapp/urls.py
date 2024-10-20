# ocrapp/urls.py
from django.urls import path
from .views import pdf_to_csv_view

urlpatterns = [
    path('', pdf_to_csv_view, name='pdf_to_csv'),
]
