from django.urls import path
from .views import PartidaInvoicePdfView


urlpatterns = [
    path('crear_pdf/<int:pk>/', PartidaInvoicePdfView.as_view(), name='crear_pdf')
]