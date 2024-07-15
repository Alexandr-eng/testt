from django.urls import path
from .views import StoreListView, VisitCreateView

urlpatterns = [
    path('stores/', StoreListView.as_view(), name='store-list'),
    path('visit/', VisitCreateView.as_view(), name='visit-create'),
]