from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from api.models import Post
from api.serializers import PostSerializer


@csrf_exempt
def post_list(request):
    """
    List all posts
    """
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def create_post(request):
    """
    Create a new post.
    """
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    return JsonResponse({}, status=400)


@csrf_exempt
def post_detail(request, id):
    """
    Retrieve post by id
    """
    post = Post.objects.get(id=id)
    if not post:
        return JsonResponse({}, status=404)
    return JsonResponse({'post': post}, status=200)
