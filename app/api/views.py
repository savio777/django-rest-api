from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import BlogPost
from .serializers import BlogPostSerializer


class BlogPostCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    # delete all posts
    def delete(self, request, *args, **kwargs):
        BlogPost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = "pk"


class BlogPostList(APIView):
    def get(self, request, format=None):
        titleParam = request.query_params.get("title", "")

        if titleParam:
            blog_posts = BlogPost.objects.filter(title__icontains=titleParam)
        else:
            blog_posts = BlogPost.objects.all()

        serializer = BlogPostSerializer(blog_posts, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
