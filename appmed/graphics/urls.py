from django.urls import path
from . import views

urlpatterns = [
    path('interactive_graph/', views.interactive_graphic, name='interactive_graphic'),
    path('temperature_chart/', views.temperature_chart, name='temperature_chart'),
]