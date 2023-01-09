from django.urls import path
from . import views

urlpatterns = [
    path('hello/<color>', views.hello),
    path('color/<color>', views.color, name="color-url")
]
