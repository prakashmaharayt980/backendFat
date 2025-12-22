# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.shortcuts import get_object_or_404
# from rest_framework.permissions import AllowAny
# from rest_framework.exceptions import ValidationError


# from .models import BlogPost
# from .serializers import BlogPostSerializer

# class GetBlogPostsAPIView(APIView):
#     permission_classes = []
#     authentication_classes = ()

#     def get(self,request,format=None):

#         try:
#             posts = BlogPost.objects.all().order_by('-published_at')
#             serializer = BlogPostSerializer(posts,many=True)
#             return Response(serializer.data)
        
#         except ValidationError as e:
#             error_msg = {
#                 "error": str(e)
#             }
#             return Response(error_msg,status=status.HTTP_400_BAD_REQUEST)
#         except Exception as e:
#             error_msg = {
#                 "error": str(e)
#             }
#             return Response(error_msg, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

# class CreateBlogPostAPIView(APIView):

#     def post(self, request):
#         # Assign currently logged-in user as author if authentication is used
#         # Here we assume anonymous creation; for real app, use request.user
#         data = request.data.copy()
#         # data['author'] = request.user.id  # Uncomment if auth
#         serializer = BlogPostSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
    


# class BlogPostAPIView(APIView):
#     permission_classes = [AllowAny]  # Public access

#     def get(self, request, pk=None):
#         if pk:
#             post = get_object_or_404(BlogPost, pk=pk)
#             serializer = BlogPostSerializer(post)
#             return Response(serializer.data)
#         posts = BlogPost.objects.all().order_by('-published_at')
#         serializer = BlogPostSerializer(posts, many=True)
#         return Response(serializer.data)

    

#     def put(self, request, pk):
#         post = get_object_or_404(BlogPost, pk=pk)
#         serializer = BlogPostSerializer(post, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         post = get_object_or_404(BlogPost, pk=pk)
#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

from blog.exceptions import BaseBlogAPIView
from blog.models import BlogPost
from blog.serializers import BlogPostSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from blog.pagination import BlogPostPagination



class GetAllBlogPostsAPIView(BaseBlogAPIView):
    def get(self, request):
        posts = BlogPost.objects.all().order_by('-published_at')

        paginator = BlogPostPagination()
        page = paginator.paginate_queryset(posts,request)
        serializer = BlogPostSerializer(page, many=True)

        return paginator.get_paginated_response(serializer.data)
        # return Response(serializer.data)


class GetBlogPostByIdAPIView(BaseBlogAPIView):
    def get(self, request, pk):
        post = get_object_or_404(BlogPost, pk=pk)
        return Response(BlogPostSerializer(post).data)

class CreateBlogPostAPIView(BaseBlogAPIView):
    def post(self, request):
        serializer = BlogPostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UpdateBlogPostAPIView(BaseBlogAPIView):
    def post(self, request, pk):
        post = get_object_or_404(BlogPost, pk=pk)
        serializer = BlogPostSerializer(post, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class DeleteBlogPostAPIView(BaseBlogAPIView):
    def post(self, request, pk):
        post = get_object_or_404(BlogPost, pk=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)