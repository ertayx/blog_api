from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import PostListCreateView, PostDetailView
from . import views

router = DefaultRouter()
router.register('', views.PostViewSet)

urlpatterns = [
    path('', include(router.urls))
    # path('', PostListCreateView.as_view()),
    # path('<int:id>/', PostDetailView.as_view()),
]
