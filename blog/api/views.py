from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from blog.models import Post
from blog.api.serializers import PostSerializer


@api_view(['GET'])
def post_detail_api(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)


@api_view(['PUT'])
def update_post_api(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "update successfull"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_post_api(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    
    if request.method == 'DELETE':
        operation = post.delete()
        data = {}
        if operation:
            data["success"] = "delete successfull"
        else:
            data["failure"] = "delete failed"
        return Response(data=data)


@api_view(['POST'])
def create_post_api(request):
    post = Post(author=request.user)

    if request.method == 'POST':
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        