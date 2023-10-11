from django.urls import include, path
from rest_framework import routers

from api.views import PostViewSet, GroupViewSet, CommentViewSet

v1_router = routers.DefaultRouter()
v1_router.register('posts', PostViewSet, basename='posts')
v1_router.register('groups', GroupViewSet, basename='groups')
v1_router.register(
    'posts/(?P<post_id>\\d+)/comments', CommentViewSet, basename='comments'
)

urlpatterns = [
    path('v1/', include(v1_router.urls)),
]
