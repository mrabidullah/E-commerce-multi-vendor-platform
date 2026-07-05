from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404
from django.db.models import Q

from .models import (
    Electronics, Fashion, Footwear, Beauty, Home,
    Kitchen, Health, Sports, Kids, Automotive,
    Books, Groceries, Jewelry, Pets, Tools
)

from .serializers import (
    ElectronicsSerializer,
    FashionSerializer,
    FootwearSerializer,
    BeautySerializer,
    HomeSerializer,
    KitchenSerializer,
    HealthSerializer,
    SportsSerializer,
    KidsSerializer,
    AutomotiveSerializer,
    BooksSerializer,
    GroceriesSerializer,
    JewelrySerializer,
    PetsSerializer,
    ToolsSerializer,
    OrderSerializer,
    CommentSerializer
)

# =========================
# PAGINATION
# =========================

class StandardPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50


# =========================
# MODEL MAP
# =========================

MODEL_MAP = {
    'electronics': (Electronics, ElectronicsSerializer),
    'fashion': (Fashion, FashionSerializer),
    'footwear': (Footwear, FootwearSerializer),
    'beauty': (Beauty, BeautySerializer),
    'home': (Home, HomeSerializer),
    'kitchen': (Kitchen, KitchenSerializer),
    'health': (Health, HealthSerializer),
    'sports': (Sports, SportsSerializer),
    'kids': (Kids, KidsSerializer),
    'automotive': (Automotive, AutomotiveSerializer),
    'books': (Books, BooksSerializer),
    'groceries': (Groceries, GroceriesSerializer),
    'jewelry': (Jewelry, JewelrySerializer),
    'pets': (Pets, PetsSerializer),
    'tools': (Tools, ToolsSerializer),
}


# =========================
# HOME API
# =========================

@api_view(['GET'])
def home_api(request):

    all_products = []

    for model, serializer_class in MODEL_MAP.values():

        products = model.objects.order_by('-created_time')[:2]

        serializer = serializer_class(
            products,
            many=True,
            context={'request': request}
        )

        all_products.extend(serializer.data)

    paginator = StandardPagination()
    page = paginator.paginate_queryset(all_products, request)

    return paginator.get_paginated_response(page)


# =========================
# PRODUCT DETAIL API
# =========================

@api_view(['GET'])
def product_detail_api(request, category, id):

    category = category.lower().strip()

    model_data = MODEL_MAP.get(category)

    if not model_data:
        return Response(
            {"error": "Invalid category"},
            status=status.HTTP_400_BAD_REQUEST
        )

    model, serializer_class = model_data

    product = get_object_or_404(model, id=id)

    serializer = serializer_class(product, context={'request': request})

    return Response(serializer.data)


# =========================
# CATEGORY API (PAGINATION)
# =========================

@api_view(['GET'])
def category_api(request, category):

    category = category.lower().strip()

    model_data = MODEL_MAP.get(category)

    if not model_data:
        return Response(
            {"error": "Invalid category"},
            status=status.HTTP_400_BAD_REQUEST
        )

    model, serializer_class = model_data

    products = model.objects.order_by('-created_time')

    paginator = StandardPagination()
    page = paginator.paginate_queryset(products, request)

    serializer = serializer_class(
        page,
        many=True,
        context={'request': request}
    )

    return paginator.get_paginated_response({
        "category": category,
        "results": serializer.data
    })


# =========================
# ALL PRODUCTS API (PAGINATION FIXED)
# =========================

@api_view(['GET'])
def all_products_api(request):

    all_products = []

    for model, serializer_class in MODEL_MAP.values():

        products = model.objects.order_by('-created_time')

        serializer = serializer_class(
            products,
            many=True,
            context={'request': request}
        )

        all_products.extend(serializer.data)

    all_products = sorted(
        all_products,
        key=lambda x: x.get('created_time', ''),
        reverse=True
    )

    paginator = StandardPagination()
    page = paginator.paginate_queryset(all_products, request)

    return paginator.get_paginated_response(page)


# =========================
# SEARCH API (PAGINATION FIXED)
# =========================

@api_view(['GET'])
def search_api(request):

    query = request.GET.get('q', '').strip()

    if not query:
        return Response(
            {"error": "Search query required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    final_results = []

    for model, serializer_class in MODEL_MAP.values():

        data = model.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(category__icontains=query) |
            Q(brand__icontains=query)
        )

        serializer = serializer_class(
            data,
            many=True,
            context={'request': request}
        )

        final_results.extend(serializer.data)

    paginator = StandardPagination()
    page = paginator.paginate_queryset(final_results, request)

    return paginator.get_paginated_response({
        "query": query,
        "results": page
    })


# =========================
# ORDER API (SAFE)
# =========================

@api_view(['GET', 'POST'])
def create_order_api(request):

    if request.method == 'GET':
        return Response({"message": "Use POST request to create order"})

    serializer = OrderSerializer(data=request.data)

    if serializer.is_valid():

        serializer.save(
            relation_to_user=request.user
            if request.user.is_authenticated else None
        )

        return Response({
            "success": True,
            "message": "Order created successfully",
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# =========================
# COMMENT API (SAFE)
# =========================

@api_view(['GET', 'POST'])
def create_comment_api(request):

    if request.method == 'GET':
        return Response({"message": "Use POST request to create comment"})

    serializer = CommentSerializer(data=request.data)

    if serializer.is_valid():

        serializer.save(
            relation_to_user=request.user
            if request.user.is_authenticated else None
        )

        return Response({
            "success": True,
            "message": "Comment created successfully",
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)