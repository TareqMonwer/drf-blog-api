from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from rest_framework import viewsets

from .serializers import PostSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly
from .models import Post


class PostViewsets(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewsets(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

# # THESE VIEWS ARE REPLACED BY VIEWSETS DESCRIBED ABOVE
# class PostList(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthorOrReadOnly, )
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class UserList(generics.ListCreateAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer


# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (permissions.IsAdminUser, )
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer