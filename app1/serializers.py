# serializers.py

from rest_framework import serializers
from .models import (
    Electronics, Fashion, Footwear, Beauty, Home,
    Kitchen, Health, Sports, Kids, Automotive,
    Books, Groceries, Jewelry, Pets, Tools,
    order_product, Comment
)


# =========================
# BASE PRODUCT SERIALIZER
# =========================

class BaseProductSerializer(serializers.ModelSerializer):

    image = serializers.SerializerMethodField()
    seller_name = serializers.SerializerMethodField()

    class Meta:
        fields = '__all__'

    def get_image(self, obj):

        request = self.context.get('request')

        if obj.image:

            if request:
                return request.build_absolute_uri(obj.image.url)

            return obj.image.url

        return None

    def get_seller_name(self, obj):

        if obj.seller_relation:
            return str(obj.seller_relation)

        return None


# =========================
# PRODUCT SERIALIZERS
# =========================

class ElectronicsSerializer(BaseProductSerializer):

    class Meta(BaseProductSerializer.Meta):
        model = Electronics


class FashionSerializer(BaseProductSerializer):

    class Meta(BaseProductSerializer.Meta):
        model = Fashion


class FootwearSerializer(BaseProductSerializer):

    class Meta(BaseProductSerializer.Meta):
        model = Footwear


class BeautySerializer(BaseProductSerializer):

    class Meta(BaseProductSerializer.Meta):
        model = Beauty


class HomeSerializer(BaseProductSerializer):

    class Meta(BaseProductSerializer.Meta):
        model = Home


class KitchenSerializer(BaseProductSerializer):

    class Meta(BaseProductSerializer.Meta):
        model = Kitchen


class HealthSerializer(BaseProductSerializer):

    class Meta(BaseProductSerializer.Meta):
        model = Health


class SportsSerializer(BaseProductSerializer):

    class Meta(BaseProductSerializer.Meta):
        model = Sports


class KidsSerializer(BaseProductSerializer):

    class Meta(BaseProductSerializer.Meta):
        model = Kids


class AutomotiveSerializer(BaseProductSerializer):

    class Meta(BaseProductSerializer.Meta):
        model = Automotive


class BooksSerializer(BaseProductSerializer):

    class Meta(BaseProductSerializer.Meta):
        model = Books


class GroceriesSerializer(BaseProductSerializer):

    class Meta(BaseProductSerializer.Meta):
        model = Groceries


class JewelrySerializer(BaseProductSerializer):

    class Meta(BaseProductSerializer.Meta):
        model = Jewelry


class PetsSerializer(BaseProductSerializer):

    class Meta(BaseProductSerializer.Meta):
        model = Pets


class ToolsSerializer(BaseProductSerializer):

    class Meta(BaseProductSerializer.Meta):
        model = Tools


# =========================
# ORDER SERIALIZER
# =========================

class OrderSerializer(serializers.ModelSerializer):

    image1 = serializers.SerializerMethodField()

    class Meta:
        model = order_product
        fields = '__all__'

    def get_image1(self, obj):

        request = self.context.get('request')

        if obj.image1:

            if request:
                return request.build_absolute_uri(obj.image1.url)

            return obj.image1.url

        return None


# =========================
# COMMENT SERIALIZER
# =========================

class CommentSerializer(serializers.ModelSerializer):

    user = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = '__all__'

    def get_user(self, obj):

        if obj.relation_to_user:
            return obj.relation_to_user.username

        return "Anonymous"