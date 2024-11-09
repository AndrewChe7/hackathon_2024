
from django.urls import path, include
from rest_framework import routers
from .views import FileUploadView

router = routers.DefaultRouter()
router.register(r'upload', FileUploadView, basename="upload")

# Wire up our API using automatic URL routing.
urlpatterns = [
    path('', include(router.urls)),
]