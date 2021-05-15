from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSets, basename='hello-viewset')

urlpatterns = [
    path('helloview/', views.HelloApiView.as_view(), name='helloView'),
    path('', include(router.urls))
]
