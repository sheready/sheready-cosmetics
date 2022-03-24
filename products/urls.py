from django.urls import include, path
from .views import ItemsCreate, ItemsDetail, ItemsList, ItemsUpdate, ItemsDelete

urlpatterns = [
    path('create/', ItemsCreate.as_view(), name='create_item'),
    path('',ItemsList.as_view()),
    path('<int:pk>/',ItemsDetail.as_view(),name='retrieve_item'),
    path('update/<int:pk>/',ItemsUpdate.as_view(),name="update_item"),
    path('delete/<int:pk>/', ItemsDelete.as_view(),name="delete_item"),
]