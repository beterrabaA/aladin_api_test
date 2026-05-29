from django.contrib import admin
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/items/", views.items, name="items"),
    path('api/v1/schema/', SpectacularAPIView.as_view(), name='api-schema'),
    path('api/v1/docs/', SpectacularSwaggerView.as_view(url_name='api-schema'), name='api-docs'),
]
