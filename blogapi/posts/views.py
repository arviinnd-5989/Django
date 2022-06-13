from django.contrib.auth import get_user_model # new
from rest_framework import viewsets # new
from django.shortcuts import render

# Create your views here.
# posts/views.py
from .models import Post
from .permissions import IsAuthorOrReadOnly # new
from .serializers import PostSerializer, UserSerializer # new

class PostViewSet(viewsets.ModelViewSet): # new
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class UserViewSet(viewsets.ModelViewSet): # new
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer