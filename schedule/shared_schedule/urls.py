from django.urls import path
from . import views

urlpatterns = [
    path('', views.SharedSch, name='sharedSch'),
    path('vertical-cal/', views.vSharedSch, name='vsharedSch'),
    path('event/create/', views.EventCreate.as_view(), name='EventCreate'),
    path('event/update/<int:pk>/', views.EventUpdate.as_view(), name='EventUpdate'),
    path('event/<int:pk>/', views.EventDetail.as_view(), name='EventDetail'),
    path('event/delete/<int:pk>/', views.EventDelete.as_view(), name='EventDelete'),
    path('resource/create/', views.ResourceCreate.as_view(), name='ResourceCreate'),
    path('resource/update/<str:pk>/',
         views.ResourceUpdate.as_view(), name='ResourceUpdate'),
    path('resource/<str:pk>/', views.ResourceDetail.as_view(), name='ResourceDetail'),
]
