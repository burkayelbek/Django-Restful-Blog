from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import (ListAPIView,
                                     RetrieveAPIView,
                                     UpdateAPIView,
                                     DestroyAPIView,
                                     CreateAPIView,
                                     RetrieveUpdateAPIView, )
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin

from post.api.pagination import PostPagination
from post.api.serializers import PostSerializer, PostUpdateCreateSerializer
# from post.api.throttles import RegisterThrottle
from post.models import Post
from rest_framework.permissions import (IsAuthenticated, IsAdminUser)
from post.api.permissions import IsOwnerOrAdmin


# Listeleme sayfasında create mixin kullanılabilmektedir.

# class PostListApiView(ListAPIView, CreateModelMixin):
#     # queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     pagination_class = PostPagination
#     filter_backends = [SearchFilter, OrderingFilter]
#     search_fields = ['title', 'content']
#     # ?search=merhaba%20yeni&ordering=title / arama işlemi ile kullanılır
#     # ?search=merhaba%20yeni&ordering=-user / user'ı tersten sıralar.
#
#     def get_queryset(self):
#         queryset = Post.objects.filter(draft=False)  # Taslakta olmayan verileri gösterme (Admin Panelde var)
#         return queryset
#
#     def post(self, request, *args, **kwargs):
#         return self.post(request, *args, **kwargs)
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)

class PostListApiView(ListAPIView):
    # queryset = Post.objects.all()
    # throttle_classes = [RegisterThrottle],
    throttle_scope = 'testScopedThrottle'
    serializer_class = PostSerializer
    pagination_class = PostPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'content']
    # ?search=merhaba%20yeni&ordering=title / arama işlemi ile kullanılır
    # ?search=merhaba%20yeni&ordering=-user / user'ı tersten sıralar.

    def get_queryset(self):
        queryset = Post.objects.filter(draft=False)  # Taslakta olmayan verileri gösterme (Admin Panelde var)
        return queryset


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'
    # slug'a göre detay sayfasına gidecektir. www.burkay.com/Testdasd-asdsd / Default olarak lookup_field = 'pk' dır.


# PostUpdateApiView içinde DestroyModelMixin kullandığımızdan Silme + Update yapılabilmektedir.

# class PostDeleteApiView(DestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     lookup_field = 'slug'
#     permission_classes = [IsOwnerOrAdmin]


class PostUpdateApiView(RetrieveUpdateAPIView, DestroyModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostUpdateCreateSerializer
    lookup_field = 'slug'
    permission_classes = [IsOwnerOrAdmin]

    def perform_update(self, serializer):
        serializer.save(modified_by=self.request.user)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class PostCreateApiView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostUpdateCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
