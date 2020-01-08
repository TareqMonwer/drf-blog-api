from django.urls import path
from rest_framework.routers import SimpleRouter

# from .views import PostList, PostDetail, UserList, UserDetail
from .views import UserViewsets, PostViewsets

router = SimpleRouter()
router.register('users', UserViewsets, basename='users')
router.register('', PostViewsets, basename='posts')

urlpatterns = router.urls


# Replaced by routers
# urlpatterns = [
#     path('posts/', PostList.as_view()),
#     path('<int:pk>/', PostDetail.as_view()),
#     path('users/', UserList.as_view()),
#     path('users/<int:pk>/', UserDetail.as_view()),
# ]