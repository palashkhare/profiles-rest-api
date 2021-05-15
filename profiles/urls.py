from django.urls import path

from profiles import views

urlpatterns = [
    path('helloview/', views.HelloApiView.as_view(), name='helloView'),
]
