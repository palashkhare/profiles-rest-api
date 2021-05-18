from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSets, basename='hello-viewset')
router.register('profile', views.UserProfileViewSet)    # Basename is not defined here vecause UserProfileViewSet is defined with queryset variable
                                                        # Django rest framework by default assign the basename from queryset variable
router.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [
    path('helloview/', views.HelloApiView.as_view(), name='helloView'),
    path('login/', views.UserLoginApiView.as_view(), name='login'),
    path('', include(router.urls))
]
