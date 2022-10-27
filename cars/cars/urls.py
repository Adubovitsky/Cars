"""cars URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework import routers
from app01.api_view import AgeViewSet, VehicleViewSet, MilgrViewSet, LocationViewSet

router = routers.DefaultRouter()
router.register(r'ages', AgeViewSet)
router.register(r'veh', VehicleViewSet)
router.register(r'mil', MilgrViewSet)
router.register(r'location', LocationViewSet)


# app_name = 'app01'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app01.urls', namespace='cars')),
    path('users/', include('usersapp.urls', namespace='users')),
    path('api-auth/', include('rest_framework.urls')),
    path('ages/', include(router.urls)),
    path('veh/', include(router.urls)),
    path('mil/', include(router.urls)),
    path('location/', include(router.urls)),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls))
    ] + urlpatterns