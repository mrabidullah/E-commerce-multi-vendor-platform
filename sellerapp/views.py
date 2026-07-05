from django.shortcuts import render, redirect, get_object_or_404
import csv
from django.http import HttpResponse
from django.http import JsonResponse
from django.utils import timezone
from django.db.models import Q, Avg, Count
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from sellerapp.models import Seller
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from app1.models import (
    Electronics, Fashion, Footwear, Beauty, Home, Kitchen,
    Health, Sports, Kids, Automotive, Books, Groceries,
    Jewelry, Pets, Tools, order_product, Comment
)


# ===================== PROFILE VIEW =====================
@login_required
def profile(request):
    seller1 = Seller.objects.get(user=request.user)

    if request.method == "POST":

        # PROFILE UPDATE
        if "update_profile" in request.POST:

            request.user.username = request.POST.get('username', request.user.username)
            request.user.email = request.POST.get('email', request.user.email)
            request.user.save()

            seller1.phone = request.POST.get('phone', seller1.phone)
            seller1.shop_name = request.POST.get('shop_name', seller1.shop_name)
            seller1.bio = request.POST.get('bio', seller1.bio)
            seller1.location = request.POST.get('location', seller1.location)

            if 'image' in request.FILES:
                seller1.image = request.FILES['image']
                
            # BACKGROUND IMAGE SAVE
            if 'background_image' in request.FILES:
                seller1.background_image = request.FILES['background_image']

            seller1.save()
            messages.success(request, "Profile updated successfully!")

        # PASSWORD CHANGE
        elif "change_password" in request.POST:

            old_password = request.POST.get("old_password")
            new_password1 = request.POST.get("new_password1")
            new_password2 = request.POST.get("new_password2")

            if not request.user.check_password(old_password):
                messages.error(request, "Current password is incorrect!")
                return redirect("profile")

            if new_password1 != new_password2:
                messages.error(request, "Passwords do not match!")
                return redirect("profile")

            try:
                validate_password(new_password1, request.user)
            except ValidationError as e:
                messages.error(request, e)
                return redirect("profile")

            request.user.set_password(new_password1)
            request.user.save()
            update_session_auth_hash(request, request.user)
            messages.success(request, "Password updated successfully!")

        return redirect("profile")

    return render(request, "seller_data/profile.html", {"seller": seller1})


# ===================== ADD PRODUCT =====================
@login_required
def add_product(request):
    seller1 = Seller.objects.get(user=request.user)
    category_map = {
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

    if request.method == 'POST':
        category = request.POST.get('category')
        product_name = request.POST.get('name')
        brand_name = request.POST.get('brand')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        
        correct_model = category_map.get(category)
        if correct_model:
            correct_model.objects.create(
                seller_relation=seller1,
                name=product_name,
                brand=brand_name,
                price=price,
                stock=stock,
                description=description,
                image=image
            )
            messages.success(request, 'Product added successfully!')
        return redirect('product_inventory')

    return render(request, 'seller_data/add_product.html')


# ===================== PRODUCT INVENTORY =====================
@login_required
def product_inventory(request):
    seller1 = Seller.objects.filter(user=request.user).first()

    products = []

    active_count = 0
    out_of_stock_count = 0
    low_stock_count = 0

    models = [
        Electronics, Fashion, Footwear, Beauty, Home,
        Kitchen, Health, Sports, Kids, Automotive,
        Books, Groceries, Jewelry, Pets, Tools
    ]

    for model in models:
        items = model.objects.filter(seller_relation=seller1)

        for item in items:

            if item.stock == 0:
                status = "Out of Stock"
                out_of_stock_count += 1

            elif item.stock <= 10:
                status = "Low Stock"
                low_stock_count += 1

            else:
                status = "Active"
                active_count += 1

            products.append({
                "name": item.name,
                "price": item.price,
                "stock": item.stock,
                "image": item.image.url if item.image else "",
                "category": item.category,
                "id": item.id,
                "model": model.__name__,
                "status": status,
            })

    context = {
        "products": products,
        "total_products": len(products),
        "active_count": active_count,
        "out_of_stock_count": out_of_stock_count,
        "low_stock_count": low_stock_count,
    }

    return render(
        request,
        "seller_data/product_inventory.html",
        context
    )

# ===================== ORDER MANAGEMENT =====================
@login_required
def order_management(request):
    seller1 = Seller.objects.get(user=request.user)
    status = request.GET.get("status", "all")

    base_orders = order_product.objects.filter(
        seller_relation=seller1
    ).order_by('-id')

    if status and status.lower() != "all":
        orders = base_orders.filter(status__iexact=status)
    else:
        orders = base_orders

    total_orders = base_orders.count()
    pending_orders = base_orders.filter(status__iexact="Pending").count()
    shipped_orders = base_orders.filter(status__iexact="Shipped").count()
    delivered_orders = base_orders.filter(status__iexact="Delivered").count()

    return render(request, "seller_data/order_management.html", {
        "orders": orders,
        "Total_orders": total_orders,
        "pending_orders": pending_orders,
        "shipped_orders": shipped_orders,
        "delivered_orders": delivered_orders,
        "current_filter": status.lower(),
    })


# ===================== EDIT PRODUCT =====================
@login_required
def edit_product(request, category_name, product_id):
    category_map = {
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

    model = category_map.get(category_name)

    if not model:
        return redirect('seller_dashboard')

    product = get_object_or_404(model, id=product_id)

    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.brand = request.POST.get('brand')
        product.price = request.POST.get('price')
        product.description = request.POST.get('description')
        product.category = request.POST.get('category')

        if 'image' in request.FILES:
            product.image = request.FILES['image']

        product.save()
        messages.success(request, "Product updated successfully!")
        return redirect('product_inventory')

    return render(request, 'seller_data/edit_product.html', {'product': product})


# ===================== CUSTOMER REVIEWS =====================
@login_required
def customer_reviews(request):
    seller = Seller.objects.filter(user=request.user).first()

    if not seller:
        return render(request, 'seller_data/customer_reviews.html', {
            'comments': [],
            'total_reviews': 0,
            'avg_rating': 0,
            'sentiment_score': 0,
            'unanswered_count': 0,
            'response_rate': 0,
        })

    comments = Comment.objects.filter(
        seller_relation=seller
    ).select_related('relation_to_user').order_by('-created_time')

    for c in comments:
        if c.relation_to_user:
            c.display_name = c.relation_to_user.username
            c.user_type = "Customer"
        else:
            c.display_name = "Guest"
            c.user_type = "Guest"

    total_reviews = comments.count()
    avg_rating = comments.aggregate(avg=Avg('rating'))['avg'] or 0
    unanswered_count = comments.filter(reply_text__isnull=True).count()
    response_rate = ((total_reviews - unanswered_count) / total_reviews * 100) if total_reviews > 0 else 0
    positive = comments.filter(rating__gte=4).count()
    sentiment_score = round((positive / total_reviews * 100) if total_reviews > 0 else 0)

    paginator = Paginator(comments, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'seller_data/customer_reviews.html', {
        'comments': page_obj,
        'total_reviews': total_reviews,
        'avg_rating': round(avg_rating, 1),
        'sentiment_score': sentiment_score,
        'unanswered_count': unanswered_count,
        'response_rate': round(response_rate, 1),
    })


# ===================== REPLY TO COMMENT =====================
@login_required
def reply_to_comment(request, comment_id):
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid request'}, status=400)

    comment = get_object_or_404(Comment, id=comment_id)
    seller = Seller.objects.filter(user=request.user).first()

    if not seller or comment.seller_relation != seller:
        return JsonResponse({'error': 'Not authorized'}, status=403)

    reply_text = request.POST.get('reply_text', '').strip()
    if not reply_text:
        return JsonResponse({'error': 'Reply cannot be empty'}, status=400)

    comment.reply_text = reply_text
    comment.reply_time = timezone.now()
    comment.save()

    return JsonResponse({
        'success': True,
        'reply_text': reply_text,
        'reply_time': comment.reply_time.strftime("%Y-%m-%d %H:%M:%S")
    })


# ===================== EXPORT ORDERS CSV =====================
@login_required
def export_orders_csv(request):
    seller1 = Seller.objects.get(user=request.user)
    orders = order_product.objects.filter(seller_relation=seller1).order_by('-id')

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="orders.csv"'

    writer = csv.writer(response)
    writer.writerow(['Order ID', 'Product', 'Customer', 'Qty', 'Total Price', 'Status', 'Email', 'Phone'])

    for o in orders:
        customer = o.relation_to_user.username if o.relation_to_user else "Guest"
        writer.writerow([
            o.id, o.product_name, customer, o.quantity,
            o.total_price, o.status, o.email, o.phone
        ])

    return response


# ===================== DELETE ORDER =====================
@login_required
def delete_order(request, id):
    if request.method == "POST":
        order_product.objects.filter(id=id, seller_relation__user=request.user).delete()
    return redirect("order_management")