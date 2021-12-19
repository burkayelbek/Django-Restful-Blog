from rest_framework import serializers
# rom rest_framework.serializers import ModelSerializer
from post.models import Post


# class PostSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=200)
#     content = serializers.CharField(max_length=200)


class PostSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        # view_name='namespace:name' # "url": "http://127.0.0.1:8000/api/post/detail/deneme", gibi link oluşturduk.
        view_name='post:detail',  # api/urls içindeki post, api namespace'den geliyor ilk parametre. İkincisi django-blog/urls.
        lookup_field='slug'
    )
    # username = serializers.SerializerMethodField(method_name='username_new')
    username = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            # 'user',  # id si yazmak yerine username olarak adını yazdırdık.
            'username',
            'title',
            'content',
            'image',
            # 'slug', #slug yerine url yazdık.
            'url',
            'created',
            'modified_by'
        ]

    def get_username(self, obj):
        return str(obj.user.username)

    # def username_new(self, obj):
    #     return str(obj.user.username)


class PostUpdateCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'image',

        ]

    # bu işlemler view içinde perform_create veya perform_update ile view içinde yapılması daha doğru olur.

    # def create(self, validated_data):
    #     return Post.objects.create(user=self.context["request"].user, **validated_data)  # Sözlük olduğu için kwargs user bilgilerini tutar

    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.content = validated_data.get('content', instance.title)
    #     instance.image = validated_data.get('image', instance.title)
    #     instance.save()
    #     return instance

    # Tek bir element değeri için kontrol eder

    # def validate_title(self, value):
    #
    #     if value == "burkay":
    #         raise serializers.ValidationError("Bu değer olmaz")
    #     return value

    # Tüm elemenetteki değerler için kontrol yapar.

    # def validate(self, attrs):
    #     if attrs["title"] == "burkay":
    #         raise serializers.ValidationError("Bu değer olmaz")
    #     return attrs
