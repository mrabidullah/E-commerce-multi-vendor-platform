
from django.contrib import messages

from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db import transaction
from itertools import chain
from django.db.models import Q
from decimal import Decimal
from .models import *
from app1.models import (
    Electronics, Fashion, Footwear, Beauty, Home, Kitchen,
    Health, Sports, Kids, Automotive, Books,
    Groceries, Jewelry, Pets, Tools, order_product, Comment
)

# =========================
# HOME PAGE
# =========================
def home(request):
    electronic = Electronics.objects.order_by('-created_time')[:2]
    fashion = Fashion.objects.order_by('-created_time')[:2]
    footwear = Footwear.objects.order_by('-created_time')[:2]
    beauty = Beauty.objects.order_by('-created_time')[:2]
    home_qs = Home.objects.order_by('-created_time')[:2]
    kitchen = Kitchen.objects.order_by('-created_time')[:2]
    health = Health.objects.order_by('-created_time')[:2]
    sports = Sports.objects.order_by('-created_time')[:2]
    kids = Kids.objects.order_by('-created_time')[:2]
    automotive = Automotive.objects.order_by('-created_time')[:2]
    books = Books.objects.order_by('-created_time')[:2]
    groceries = Groceries.objects.order_by('-created_time')[:2]
    jewelry = Jewelry.objects.order_by('-created_time')[:2]
    pets = Pets.objects.order_by('-created_time')[:2]
    tools = Tools.objects.order_by('-created_time')[:2]

    all_home_products_list = list(chain(
        electronic, fashion, footwear, beauty, home_qs,
        kitchen, health, sports, kids, automotive,
        books, groceries, jewelry, pets, tools
    ))

    home_products = sorted(
        all_home_products_list,
        key=lambda x: x.created_time,
        reverse=True
    )

    return render(request, 'home.html', {'home_products': home_products})


# =========================
# PRODUCT DETAIL
# =========================
def product_detail(request, category, id):

    model_map = {
        'Electronics': Electronics,
        'Fashion': Fashion,
        'Footwear': Footwear,
        'Beauty': Beauty,
        'Home': Home,
        'Kitchen': Kitchen,
        'Health': Health,
        'Sports': Sports,
        'Kids': Kids,
        'Automotive': Automotive,
        'Books': Books,
        'Groceries': Groceries,
        'Jewelry': Jewelry,
        'Pets': Pets,
        'Tools': Tools,
    }

    model_class = model_map.get(category)
    product = get_object_or_404(model_class, id=id)

    related_products = model_class.objects.order_by('-created_time')[:4]

    COMMENT_MAP = {
        "Electronics": "relation_to_electronics",
        "Fashion": "relation_to_fashion",
        "Footwear": "relation_to_footwear",
        "Beauty": "relation_to_beauty",
        "Home": "relation_to_home",
        "Kitchen": "relation_to_kitchen",
        "Health": "relation_to_health",
        "Sports": "relation_to_sports",
        "Kids": "relation_to_kids",
        "Automotive": "relation_to_automotive",
        "Books": "relation_to_books",
        "Groceries": "relation_to_groceries",
        "Jewelry": "relation_to_jewelry",
        "Pets": "relation_to_pets",
        "Tools": "relation_to_tools",
    }

    relation_field = COMMENT_MAP.get(category)

    if relation_field:
        comments = Comment.objects.filter(**{relation_field: product}).order_by('-created_time')
    else:
        comments = Comment.objects.none()

    return render(request, 'product_detail.html', {
        'product': product,
        'related_products': related_products,
        'comments': comments,
        'reviews': comments.count(),
    })


# =========================
# ORDER + COMMENT PAGE
# =========================

def order_page(request, category, id):

    model_map = {
        'Electronics': Electronics,
        'Fashion': Fashion,
        'Footwear': Footwear,
        'Beauty': Beauty,
        'Home': Home,
        'Kitchen': Kitchen,
        'Health': Health,
        'Sports': Sports,
        'Kids': Kids,
        'Automotive': Automotive,
        'Books': Books,
        'Groceries': Groceries,
        'Jewelry': Jewelry,
        'Pets': Pets,
        'Tools': Tools,
    }

    relation_map = {
        'Electronics': 'relation_to_electronics',
        'Fashion': 'relation_to_fashion',
        'Footwear': 'relation_to_footwear',
        'Beauty': 'relation_to_beauty',
        'Home': 'relation_to_home',
        'Kitchen': 'relation_to_kitchen',
        'Health': 'relation_to_health',
        'Sports': 'relation_to_sports',
        'Kids': 'relation_to_kids',
        'Automotive': 'relation_to_automotive',
        'Books': 'relation_to_books',
        'Groceries': 'relation_to_groceries',
        'Jewelry': 'relation_to_jewelry',
        'Pets': 'relation_to_pets',
        'Tools': 'relation_to_tools',
    }

    model_class = model_map.get(category)
    product = get_object_or_404(model_class, id=id)
    relation_field = relation_map.get(category)

    comments = Comment.objects.filter(
        **{relation_field: product}
    ).order_by('-created_time')[:5]

    if request.method == "POST":

        form_type = request.POST.get("form_type")

        # -------- ORDER --------



        if form_type == "order":
            try:
                qty = int(request.POST.get("qty"))

                # 🔥 CHECK STOCK FIRST
                if product.stock <= 0:
                    messages.success(
                        request,
                        "❌ This product is not available anymore"
                    )
                    return JsonResponse({'error': 'This product is not available anymore'}, status=400)

                if qty > product.stock:
                    messages.error(
                        request,
                        f"❌ Only {product.stock} items left in stock"
                    )
                    return JsonResponse({'error': f"Only {product.stock} items left in stock"}, status=400)
                price = Decimal(product.price)

                if price > 99999999:
                    messages.error(request, "❌ Invalid product price")
                    return JsonResponse({'error': 'Invalid product price'}, status=400)

                with transaction.atomic():
                    # 🔥 reduce stock safely
                    product.stock -= qty
                    product.save()

                    shipping_address = request.POST.get("address")
                    phone = request.POST.get("phone")
                    email = request.POST.get("email")
                    street = request.POST.get("street")
                                            
                    
                    if not shipping_address:
                        messages.error(request, "❌ Shipping address is required")
                        return JsonResponse({'error': 'Shipping address is required'}, status=400)
                    if not phone:
                        messages.error(request, "❌ Phone number is required")
                        return JsonResponse({'error': 'Phone number is required'}, status=400)
                    if not email:
                        messages.error(request, "❌ Email is required")
                        return JsonResponse({'error': 'Email is required'}, status=400)
                    if not street:
                        messages.error(request, "❌ Street is required")
                        return JsonResponse({'error': 'Street is required'}, status=400)
                    
                    order=order_product.objects.create(
                        relation_to_user=request.user if request.user.is_authenticated else None,
                        seller_relation=product.seller_relation,
                        image1=product.image,
                        product_name=request.POST.get("product_name"),
                        total_price=float(product.price) * qty,
                        quantity=qty,
                        shipping_address=request.POST.get("address"),
                        street=request.POST.get("street"),
                        email=request.POST.get("email"),
                        phone=request.POST.get("phone"),
                    )

                    setattr(order, relation_field, product)
                    order.save()

                messages.success(request, "✅ Order placed successfully!")
                return JsonResponse({'success': 'Order placed successfully!'})

            except Exception as e:
                return JsonResponse({"error": str(e)}, status=400)
            
            
            
            
        # -------- COMMENT --------
        if form_type == "comment":

            comment_text = request.POST.get("comment")

            if not comment_text:
                return JsonResponse({"error": "Comment cannot be empty"})

            try:
                Comment.objects.create(
                    comment_text=comment_text,
                    relation_to_user=request.user if request.user.is_authenticated else None,
                    seller_relation=product.seller_relation,   # ⭐ THIS LINE FIXES EVERYTHING
                    **{relation_field: product}
                )
                return JsonResponse({"success": "Comment added successfully!"})

            except Exception as e:
                return JsonResponse({"error": str(e)})

    return render(request, "order_page.html", {
        "product": product,
        "comments": comments,
        "reviews": comments.count(),
    })

# =========================
# ALL PRODUCTS PAGE
# =========================
def all_products_page(request):
    electronic = Electronics.objects.all()
    fashion = Fashion.objects.all()
    footwear = Footwear.objects.all()
    beauty = Beauty.objects.all()
    home = Home.objects.all()
    kitchen = Kitchen.objects.all()
    health = Health.objects.all()
    sports = Sports.objects.all()
    kids = Kids.objects.all()
    automotive = Automotive.objects.all()
    books = Books.objects.all()
    groceries = Groceries.objects.all()
    jewelry = Jewelry.objects.all()
    pets = Pets.objects.all()
    tools = Tools.objects.all()

    all_products_list = list(chain(
        electronic, fashion, footwear, beauty, home,
        kitchen, health, sports, kids, automotive,
        books, groceries, jewelry, pets, tools
    ))

    all_products = sorted(
        all_products_list,
        key=lambda x: x.created_time,
        reverse=True
    )

    return render(request, 'category/all_product.html', {'products': all_products})


# =========================
# CATEGORY PAGES (ALL OK)
# =========================
def electronics_page(request):
    return render(request, 'category/electronic.html', {'products': Electronics.objects.all()})

def fashion_page(request):
    return render(request, 'category/fashion.html', {'products': Fashion.objects.all()})

def footwear_page(request):
    return render(request, 'category/footwear.html', {'products': Footwear.objects.all()})

def beauty_page(request):
    return render(request, 'category/beauty.html', {'products': Beauty.objects.all()})

def home_page(request):
    return render(request, 'category/home.html', {'products': Home.objects.all()})

def kitchen_page(request):
    return render(request, 'category/kitchen.html', {'products': Kitchen.objects.all()})

def health_page(request):
    return render(request, 'category/health.html', {'products': Health.objects.all()})

def sports_page(request):
    return render(request, 'category/sports.html', {'products': Sports.objects.all()})

def kids_page(request):
    return render(request, 'category/kids.html', {'products': Kids.objects.all()})

def automotive_page(request):
    return render(request, 'category/automotive.html', {'products': Automotive.objects.all()})

def books_page(request):
    return render(request, 'category/books.html', {'products': Books.objects.all()})

def groceries_page(request):
    return render(request, 'category/groceries.html', {'products': Groceries.objects.all()})

def jewelry_page(request):
    return render(request, 'category/jewelry.html', {'products': Jewelry.objects.all()})

def pets_page(request):
    return render(request, 'category/pets.html', {'products': Pets.objects.all()})

def tools_page(request):
    return render(request, 'category/tools.html', {'products': Tools.objects.all()})





def search(request):

    search1 = request.GET.get('q')
    result = []

    all_model = [
        Electronics,
        Fashion,
        Footwear,
        Beauty,
        Home,
        Kitchen,
        Health,
        Sports,
        Kids,
        Automotive,
        Books,
        Groceries,
        Jewelry,
        Pets,
        Tools,
    ]

    if search1:

        for i in all_model:

            data = i.objects.filter(
                Q(name__icontains=search1) |
                Q(description__icontains=search1) |
                Q(category__icontains=search1) |
                Q(brand__icontains=search1)
            )

            result.extend(data)

    dic = {
        'search1': search1,
        'result': result
    }

    return render(request, 'search.html', dic)
            
            
            
            
            
            
            
def about(request):
    return render(request, 'about.html')