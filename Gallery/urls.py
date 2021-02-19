from django.urls import path
from . import views

urlpatterns = [
    path('', views.Gallery.as_view(), name='main'),
    path('AddImage/', views.AddImage.as_view(), name='new'),
    path('add_image/', views.Load.as_view(), name='load'),
    path('<int:pk>/', views.PhotoPreview.as_view(), name='preview'),
]




