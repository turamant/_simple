from rest_framework import generics

# Create your views here.
from api.serializers import PostSerializer
from pages.models import Post

class PostAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

