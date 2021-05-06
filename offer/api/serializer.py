from rest_framework.serializers import ModelSerializer
from offer.models import Offer


class OfferSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Offer

