from django.urls import path
from post.api.views import (PostListApiView,
                            PostDetailAPIView,
                            #PostDeleteApiView,
                            PostUpdateApiView,
                            PostCreateApiView,)
from django.views.decorators.cache import cache_page


app_name = "post"

urlpatterns = [
    path('list',  cache_page(60 * 1)(PostListApiView.as_view()), name='list'),
    path('detail/<slug>', PostDetailAPIView.as_view(), name='detail'),
    #path('delete/<slug>', PostDeleteApiView.as_view(), name='delete'),
    path('update/<slug>', PostUpdateApiView.as_view(), name='update'),
    path('create/', PostCreateApiView.as_view(), name='create')
]
