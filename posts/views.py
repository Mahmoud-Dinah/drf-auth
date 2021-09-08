from rest_framework import generics
from .serializers import PostSerializer
from .models import Posts
from .permissions import IsOwnerOrReadOnly

# Create your views here.

class PostList(generics.ListCreateAPIView):

    queryset = Posts.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Posts.objects.all()
    serializer_class = PostSerializer