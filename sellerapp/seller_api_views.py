from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from django.db.models import Avg
from django.utils import timezone

from sellerapp.models import Seller
from app1.models import (
    Electronics, Fashion, Footwear, Beauty, Home, Kitchen,
    Health, Sports, Kids, Automotive, Books, Groceries,
    Jewelry, Pets, Tools, order_product, Comment
)


# =========================
# CATEGORY MAP
# =========================
CATEGORY_MAP = {
    "Electronics": Electronics,
    "Fashion": Fashion,
    "Footwear": Footwear,
    "Beauty": Beauty,
    "Home": Home,
    "Kitchen": Kitchen,
    "Health": Health,
    "Sports": Sports,
    "Kids": Kids,
    "Automotive": Automotive,
    "Books": Books,
    "Groceries": Groceries,
    "Jewelry": Jewelry,
    "Pets": Pets,
    "Tools": Tools,
}


# =========================
# PROFILE API
# =========================
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile_api(request):
    seller = get_object_or_404(Seller, user=request.user)

    return Response({
        "username": request.user.username,
        "email": request.user.email,
        "phone": seller.phone,
        "shop_name": seller.shop_name,
        "bio": seller.bio,
    })


# =========================
# ADD PRODUCT API
# =========================
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_product_api(request):

    seller = get_object_or_404(Seller, user=request.user)

    category = request.data.get('category')
    product_name = request.data.get('name')
    brand_name = request.data.get('brand')
    price = request.data.get('price')
    stock = request.data.get('stock')
    description = request.data.get('description')
    image = request.FILES.get('image')

    model = CATEGORY_MAP.get(category)

    if not model:
        return Response({"error": "Invalid category"}, status=400)

    product = model.objects.create(
        seller_relation=seller,
        name=product_name,
        brand=brand_name,
        price=price,
        stock=stock,
        description=description,
        image=image
    )

    return Response({
        "success": True,
        "message": "Product added successfully",
        "id": product.id
    })


# =========================
# PRODUCT INVENTORY API
# =========================
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def product_inventory_api(request):

    seller = get_object_or_404(Seller, user=request.user)

    products = []

    for model_name, model in CATEGORY_MAP.items():
        items = model.objects.filter(seller_relation=seller)

        for item in items:

            if item.stock == 0:
                status = "Out of Stock"
            elif item.stock < 10:
                status = "Low Stock"
            else:
                status = "Active"

            products.append({
                "id": item.id,
                "name": item.name,
                "price": item.price,
                "stock": item.stock,
                "image": item.image.url if item.image else "",
                "category": model_name,
                "status": status,
            })

    return Response({
        "total_products": len(products),
        "products": products
    })


# =========================
# ORDER MANAGEMENT API
# =========================
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def order_management_api(request):

    seller = get_object_or_404(Seller, user=request.user)

    status_filter = request.GET.get("status", "all")

    orders = order_product.objects.filter(seller_relation=seller).order_by('-id')

    if status_filter.lower() != "all":
        orders = orders.filter(status__iexact=status_filter)

    data = []

    for o in orders:
        data.append({
            "id": o.id,
            "product": o.product_name,
            "qty": o.quantity,
            "total_price": o.total_price,
            "status": o.status,
            "email": o.email,
            "phone": o.phone,
            "customer": o.relation_to_user.username if o.relation_to_user else "Guest"
        })

    return Response({
        "total_orders": order_product.objects.filter(seller_relation=seller).count(),
        "orders": data
    })


# =========================
# EDIT PRODUCT API
# =========================
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def edit_product_api(request, category_name, product_id):

    seller = get_object_or_404(Seller, user=request.user)

    model = CATEGORY_MAP.get(category_name)

    if not model:
        return Response({"error": "Invalid category"}, status=400)

    product = get_object_or_404(model, id=product_id, seller_relation=seller)

    product.name = request.data.get('name')
    product.brand = request.data.get('brand')
    product.price = request.data.get('price')
    product.description = request.data.get('description')
    product.category = request.data.get('category')

    if request.FILES.get('image'):
        product.image = request.FILES.get('image')

    product.save()

    return Response({
        "success": True,
        "message": "Product updated successfully"
    })


# =========================
# CUSTOMER REVIEWS API
# =========================
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def customer_reviews_api(request):

    seller = get_object_or_404(Seller, user=request.user)

    comments = Comment.objects.filter(seller_relation=seller)

    total_reviews = comments.count()
    avg_rating = comments.aggregate(avg=Avg('rating'))['avg'] or 0

    return Response({
        "total_reviews": total_reviews,
        "avg_rating": round(avg_rating, 1),
    })


# =========================
# REPLY COMMENT API
# =========================
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def reply_comment_api(request, comment_id):

    seller = get_object_or_404(Seller, user=request.user)
    comment = get_object_or_404(Comment, id=comment_id, seller_relation=seller)

    reply_text = request.data.get('reply_text')

    if not reply_text:
        return Response({"error": "Reply cannot be empty"}, status=400)

    comment.reply_text = reply_text
    comment.reply_time = timezone.now()
    comment.save()

    return Response({
        "success": True,
        "message": "Reply added successfully"
    })


# =========================
# DELETE ORDER API
# =========================
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_order_api(request, order_id):

    seller = get_object_or_404(Seller, user=request.user)

    order = get_object_or_404(order_product, id=order_id, seller_relation=seller)
    order.delete()

    return Response({
        "success": True,
        "message": "Order deleted"
    })