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