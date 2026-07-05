from rest_framework import serializers
from django.contrib.auth.models import User
from sellerapp.models import Seller
from app1.models import order_product, Comment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class SellerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Seller
        fields = '__all__'
        
        
class ProductCreateSerializer(serializers.Serializer):
    category = serializers.CharField()
    name = serializers.CharField()
    brand = serializers.CharField()
    price = serializers.DecimalField(max_digits=12, decimal_places=2)
    stock = serializers.IntegerField()
    description = serializers.CharField()
    image = serializers.ImageField(required=False)
    
    
    
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = order_product
        fields = '__all__'
        
        
        
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'