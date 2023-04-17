from django.urls import path

from mainapp import views

urlpatterns = [
    path('list/', views.ProductListView.as_view(), name='list_view'),
]
