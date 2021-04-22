from django.urls import path
from . import views

urlpatterns = [
    path('', views.cheatsheets, name='cheatsheets'),
    # path('<int:sheet_id>/', views.cheatsheet, name='sheet'),
]
