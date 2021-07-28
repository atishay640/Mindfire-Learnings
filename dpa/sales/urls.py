from os import name
from django.urls import path
from sales.views import DashboardView, getDashboardData


urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='sales_dashboard'),
    path('dashboard/data/', getDashboardData, name='dashboard_data')
]   

