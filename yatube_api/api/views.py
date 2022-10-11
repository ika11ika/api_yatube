from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from posts.models import Comment, Group, Post
from rest_framework import viewsets

from .serializers import CommentSerializer, GroupSerializer, PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        super(PostViewSet, self).perform_update(serializer)

    def perform_destroy(self, serializer):
        if serializer.author != self.request.user:
            raise PermissionDenied('Удаление чужого контента запрещено!')
        super(PostViewSet, self).perform_destroy(serializer)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs["pk3"])
        new_queryset = Comment.objects.filter(post=post.pk)
        return new_queryset

class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
