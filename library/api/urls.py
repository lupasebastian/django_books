from django.urls import path, include
from rest_framework import routers
from .views import BookViewSet, AuthorViewSet

router = routers.DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'authors', AuthorViewSet)

urlpatterns = [
    path('', include(router.urls))
]