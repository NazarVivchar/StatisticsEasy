from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from django_app import views

router = routers.DefaultRouter()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('/api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include('django_app.urls'))
]
