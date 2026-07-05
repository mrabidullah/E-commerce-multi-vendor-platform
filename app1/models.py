from django.db import models
from django.contrib.auth.models import User
from sellerapp.models import Seller 




# =========================
# ELECTRONICS
# =========================
class Electronics(models.Model):
    seller_relation=models.ForeignKey(Seller, on_delete=models.CASCADE,null=True,blank=True) 
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='electronics/')
    stock = models.PositiveIntegerField()
    category = models.CharField(max_length=100, default='Electronics')
    brand = models.CharField(max_length=100, default='Generic')
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# =========================
# FASHION
# =========================
class Fashion(models.Model):
    seller_relation=models.ForeignKey(Seller, on_delete=models.CASCADE,null=True,blank=True) 
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='fashion/')
    stock = models.PositiveIntegerField()
    category = models.CharField(max_length=100, default='Fashion')
    brand = models.CharField(max_length=100, default='Generic')
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# =========================
# FOOTWEAR
# =========================
class Footwear(models.Model):
    seller_relation=models.ForeignKey(Seller, on_delete=models.CASCADE,null=True,blank=True) 
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='footwear/')
    stock = models.PositiveIntegerField()
    category = models.CharField(max_length=100, default='Footwear')
    brand = models.CharField(max_length=100, default='Generic')
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# =========================
# BEAUTY
# =========================
class Beauty(models.Model):
    seller_relation=models.ForeignKey(Seller, on_delete=models.CASCADE,null=True,blank=True) 
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='beauty/')
    stock = models.PositiveIntegerField()
    category = models.CharField(max_length=100, default='Beauty')
    brand = models.CharField(max_length=100, default='Generic')
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# =========================
# HOME
# =========================
class Home(models.Model):
    seller_relation=models.ForeignKey(Seller, on_delete=models.CASCADE,null=True,blank=True) 
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='home/')
    stock = models.PositiveIntegerField()
    category = models.CharField(max_length=100, default='Home')
    brand = models.CharField(max_length=100, default='Generic')
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# =========================
# KITCHEN
# =========================
class Kitchen(models.Model):
    seller_relation=models.ForeignKey(Seller, on_delete=models.CASCADE,null=True,blank=True) 
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='kitchen/')
    stock = models.PositiveIntegerField()
    category = models.CharField(max_length=100, default='Kitchen')
    brand = models.CharField(max_length=100, default='Generic')
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# =========================
# HEALTH
# =========================
class Health(models.Model):
    seller_relation=models.ForeignKey(Seller, on_delete=models.CASCADE,null=True,blank=True) 
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='health/')
    stock = models.PositiveIntegerField()
    category = models.CharField(max_length=100, default='Health')
    brand = models.CharField(max_length=100, default='Generic')
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# =========================
# SPORTS
# =========================
class Sports(models.Model):
    seller_relation=models.ForeignKey(Seller, on_delete=models.CASCADE,null=True,blank=True) 
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='sports/')
    stock = models.PositiveIntegerField()
    category = models.CharField(max_length=100, default='Sports')
    brand = models.CharField(max_length=100, default='Generic')
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# =========================
# KIDS
# =========================
class Kids(models.Model):
    seller_relation=models.ForeignKey(Seller, on_delete=models.CASCADE,null=True,blank=True) 
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='kids/')
    stock = models.PositiveIntegerField()
    category = models.CharField(max_length=100, default='Kids')
    brand = models.CharField(max_length=100, default='Generic')
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# =========================
# AUTOMOTIVE
# =========================
class Automotive(models.Model):
    seller_relation=models.ForeignKey(Seller, on_delete=models.CASCADE,null=True,blank=True) 
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='automotive/')
    stock = models.PositiveIntegerField()
    category = models.CharField(max_length=100, default='Automotive')
    brand = models.CharField(max_length=100, default='Generic')
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# =========================
# BOOKS
# =========================
class Books(models.Model):
    seller_relation=models.ForeignKey(Seller, on_delete=models.CASCADE,null=True,blank=True) 
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='books/')
    stock = models.PositiveIntegerField()
    category = models.CharField(max_length=100, default='Books')
    brand = models.CharField(max_length=100, default='Generic')
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# =========================
# GROCERIES
# =========================
class Groceries(models.Model):
    seller_relation=models.ForeignKey(Seller, on_delete=models.CASCADE,null=True,blank=True) 
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='groceries/')
    stock = models.PositiveIntegerField()
    category = models.CharField(max_length=100, default='Groceries')
    brand = models.CharField(max_length=100, default='Generic')
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# =========================
# JEWELRY
# =========================
class Jewelry(models.Model):
    seller_relation=models.ForeignKey(Seller, on_delete=models.CASCADE,null=True,blank=True) 
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='jewelry/')
    stock = models.PositiveIntegerField()
    category = models.CharField(max_length=100, default='Jewelry')
    brand = models.CharField(max_length=100, default='Generic')
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# =========================
# PETS
# =========================
class Pets(models.Model):
    seller_relation=models.ForeignKey(Seller, on_delete=models.CASCADE,null=True,blank=True) 
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='pets/')
    stock = models.PositiveIntegerField()
    category = models.CharField(max_length=100, default='Pets')
    brand = models.CharField(max_length=100, default='Generic')
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# =========================
# TOOLS
# =========================
class Tools(models.Model):
    seller_relation=models.ForeignKey(Seller, on_delete=models.CASCADE,null=True,blank=True) 
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='tools/')
    stock = models.PositiveIntegerField()
    category = models.CharField(max_length=100, default='Tools')
    brand = models.CharField(max_length=100, default='Generic')
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# =========================
# ORDER
# =========================
class order_product(models.Model):
    seller_relation=models.ForeignKey(Seller, on_delete=models.CASCADE,null=True,blank=True)
    relation_to_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    relation_to_electronics = models.ForeignKey(Electronics, on_delete=models.CASCADE, null=True, blank=True)
    relation_to_fashion = models.ForeignKey(Fashion, on_delete=models.CASCADE, null=True, blank=True)
    relation_to_footwear = models.ForeignKey(Footwear, on_delete=models.CASCADE, null=True, blank=True)
    relation_to_beauty = models.ForeignKey(Beauty, on_delete=models.CASCADE, null=True, blank=True)
    relation_to_home = models.ForeignKey(Home, on_delete=models.CASCADE, null=True, blank=True)
    relation_to_kitchen = models.ForeignKey(Kitchen, on_delete=models.CASCADE, null=True, blank=True)
    relation_to_health = models.ForeignKey(Health, on_delete=models.CASCADE, null=True, blank=True)
    relation_to_sports = models.ForeignKey(Sports, on_delete=models.CASCADE, null=True, blank=True)
    relation_to_kids = models.ForeignKey(Kids, on_delete=models.CASCADE, null=True, blank=True)
    relation_to_automotive = models.ForeignKey(Automotive, on_delete=models.CASCADE, null=True, blank=True)
    relation_to_books = models.ForeignKey(Books, on_delete=models.CASCADE, null=True, blank=True)
    relation_to_groceries = models.ForeignKey(Groceries, on_delete=models.CASCADE, null=True, blank=True)
    relation_to_jewelry = models.ForeignKey(Jewelry, on_delete=models.CASCADE, null=True, blank=True)
    relation_to_pets = models.ForeignKey(Pets, on_delete=models.CASCADE, null=True, blank=True)
    relation_to_tools = models.ForeignKey(Tools, on_delete=models.CASCADE, null=True, blank=True)
    product_name = models.CharField(max_length=255)
    image1 = models.ImageField(upload_to='order_images/')
    quantity = models.PositiveIntegerField()
    shipping_address = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    status = models.CharField(
    max_length=20,
    choices=[
        ('pending', 'Pending'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('returned', 'Returned'),
    ],
    default='pending'
)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name


# =========================
# COMMENT
# =========================
class Comment(models.Model):
    relation_to_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    seller_relation=models.ForeignKey(Seller,on_delete=models.CASCADE,null=True,blank=True)

    relation_to_electronics = models.ForeignKey('Electronics', on_delete=models.CASCADE, null=True, blank=True)
    relation_to_fashion = models.ForeignKey('Fashion', on_delete=models.CASCADE, null=True, blank=True)
    relation_to_footwear = models.ForeignKey('Footwear', on_delete=models.CASCADE, null=True, blank=True)
    relation_to_beauty = models.ForeignKey('Beauty', on_delete=models.CASCADE, null=True, blank=True)
    relation_to_home = models.ForeignKey('Home', on_delete=models.CASCADE, null=True, blank=True)
    relation_to_kitchen = models.ForeignKey('Kitchen', on_delete=models.CASCADE, null=True, blank=True)
    relation_to_health = models.ForeignKey('Health', on_delete=models.CASCADE, null=True, blank=True)
    relation_to_sports = models.ForeignKey('Sports', on_delete=models.CASCADE, null=True, blank=True)
    relation_to_kids = models.ForeignKey('Kids', on_delete=models.CASCADE, null=True, blank=True)
    relation_to_automotive = models.ForeignKey('Automotive', on_delete=models.CASCADE, null=True, blank=True)
    relation_to_books = models.ForeignKey('Books', on_delete=models.CASCADE, null=True, blank=True)
    relation_to_groceries = models.ForeignKey('Groceries', on_delete=models.CASCADE, null=True, blank=True)
    relation_to_jewelry = models.ForeignKey('Jewelry', on_delete=models.CASCADE, null=True, blank=True)
    relation_to_pets = models.ForeignKey('Pets', on_delete=models.CASCADE, null=True, blank=True)
    relation_to_tools = models.ForeignKey('Tools', on_delete=models.CASCADE, null=True, blank=True)

    comment_text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    # In your Comment model, add:
    rating = models.IntegerField(default=5, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
    reply_text = models.TextField(null=True, blank=True)
    reply_time = models.DateTimeField(null=True, blank=True)  
    is_reported = models.BooleanField(default=False)

    def __str__(self):
        return self.comment_text[:30]