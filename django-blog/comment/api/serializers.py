from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from comment.models import Comment
from post.models import Post


class CommentCreateSerializer(ModelSerializer):
    class Meta:
        model = Comment
        exclude = ['created', ]  # Created harici müdahele edebiliriz. Bu yüzden fields kullanmadık.

    def validate(self, attrs):
        if (attrs['parent']):
            if attrs['parent'].post != attrs['post']:
                # Parent'ın konusuyla, post aynı olmalı. Comment eklerken ki post ile Parent aynı olmalı.
                raise serializers.ValidationError('Something went wrong')

        return attrs


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'id', 'email')


class PostCommentSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'id')



class CommentListSerializer(ModelSerializer):
    # related_name = 'replies' olduğu için parent altında olan child'ları görmek için yaptık.
    replies = SerializerMethodField()
    user = UserSerializer() # User'a ait bilgileri UserSerializer'de verildiği gibi getirir.
    post = PostCommentSerializer() # Posta ait bilgileri PostCommentSerializer'e göre getirir.

    class Meta:
        model = Comment
        fields = '__all__'

    def get_replies(self, obj):
        if obj.any_children:
            return CommentListSerializer(obj.children(), many=True).data


class CommentDeleteUpdateSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'content',
        ]
