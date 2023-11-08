from django.urls import path
from .views import *

app_name = "core"

urlpatterns = [
  # Mostrara en la direccion base la vista definida
  path('', primera_vista, name='primera_vista')
]
