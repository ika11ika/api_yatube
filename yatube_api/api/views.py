from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from .permissions import CreateOrReadOnly
from .serializers import CommentSerializer, GroupSerializer, PostSerializer

from posts.models import Comment, Group, Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (CreateOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        super(PostViewSet, self).perform_update(serializer)

    def perform_destroy(self, serializer):
        super(PostViewSet, self).perform_destroy(serializer)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (CreateOrReadOnly,)

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs["post_id"])
        new_queryset = Comment.objects.filter(post=post.pk)
        return new_queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        super(CommentViewSet, self).perform_update(serializer)

    def perform_destroy(self, serializer):
        super(CommentViewSet, self).perform_destroy(serializer)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
