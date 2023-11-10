from django.urls import path

from .views import FootprintListView, FootprintDetailView, FootprintRefresh

urlpatterns = [
    path('footprint/', FootprintListView.as_view(), name='footprint_list'),
    path('footprint/<int:pk>/', FootprintDetailView.as_view(), name='footprint_detail'),
    path('footprint/refresh/', FootprintRefresh.as_view(), name='footprint_refresh'),
]
