from rest_framework.serializers import ModelSerializer
from favourite.models import Favourite


class FavouriteListCreateAPISerializer(ModelSerializer):
    class Meta:
        model = Favourite
        fields = '__all__'

