from django.urls import path

from mainapp import views

urlpatterns = [
    path('list/', views.ProductListView.as_view(), name='list_view'),
    path('create/', views.ProductCreateView.as_view(), name='create-view'),
]
