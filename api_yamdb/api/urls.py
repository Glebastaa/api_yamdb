from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    ReviewViewSet, CommentViewSet,
    TitlesViewSet, GenresViewSet,
    CategoriesViewSet, UserViewSet,
    signup_post, token_view,
)


router_v1 = DefaultRouter()
router_v1.register('users', UserViewSet)
router_v1.register('categories', CategoriesViewSet)
router_v1.register('genres', GenresViewSet)
router_v1.register('titles', TitlesViewSet, basename='titles')
router_v1.register(r'^titles/(?P<titles_id>\d+)/reviews',
                   ReviewViewSet, basename='reviews')
router_v1.register(
    r'^titles/(?P<titles_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comments'
)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/token/', token_view, name='token_obtain_pair'),
    path('v1/auth/signup/', signup_post),
]
