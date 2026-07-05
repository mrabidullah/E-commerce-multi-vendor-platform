# E-Commerce Platform

A comprehensive e-commerce backend built with **Django** and **Django REST Framework**. This platform provides a complete system for managing products across multiple categories, seller profiles, user authentication, and order management.

---

##  Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Configuration](#configuration)
- [API Endpoints](#api-endpoints)
- [Database Models](#database-models)
- [Usage](#usage)
- [Contributing](#contributing)

---

##  Features

### Customer Features
- **User Authentication**: Sign up, login, logout functionality
- **Product Browsing**: Browse products across 13 categories
- **Product Search**: Search products by name and keywords
- **Product Details**: View detailed product information with images
- **Order Management**: Create and track orders
- **Reviews & Comments**: Leave feedback and comments on products
- **Category Filtering**: Filter products by category

### Seller Features
- **Seller Dashboard**: Manage your shop and products
- **Product Management**: Add, edit, and manage inventory
- **Order Management**: View and manage customer orders
- **Customer Reviews**: View customer feedback and respond to comments
- **Seller Profile**: Customize your shop profile with images and bio
- **Inventory Tracking**: Monitor product stock levels

### Admin Features
- **Full Django Admin**: Manage all platform data
- **User Management**: Manage customers and sellers
- **Product Management**: Oversee all products
- **Order Monitoring**: Track all platform orders

---

## 📁 Project Structure

```
My_Ecommecre/
├── app1/                      # Main product management app
│   ├── models.py              # Product models (Electronics, Fashion, etc.)
│   ├── api_urls.py            # Product API endpoints
│   ├── api_views.py           # Product API views
│   ├── views.py               # Web views
│   └── serializers.py         # DRF serializers
│
├── authentication/            # User authentication app
│   ├── models.py              # Authentication models
│   ├── auth_api_urls.py       # Auth API endpoints
│   ├── auth_api_views.py      # Auth API views
│   ├── urls.py                # Web URLs
│   └── forms.py               # Authentication forms
│
├── sellerapp/                 # Seller management app
│   ├── models.py              # Seller profile model
│   ├── seller_api_urls.py     # Seller API endpoints
│   ├── seller_api_views.py    # Seller API views
│   └── serializers.py         # Seller serializers
│
├── contact/                   # Contact & support app
│   ├── models.py              # Contact models
│   ├── views.py               # Contact views
│   └── urls.py                # Contact URLs
│
├── My_Ecommecre/              # Main Django project settings
│   ├── settings.py            # Project settings & configuration
│   ├── urls.py                # Main URL routing
│   ├── wsgi.py                # WSGI configuration
│   └── asgi.py                # ASGI configuration
│
├── media/                     # User-uploaded files
│   ├── electronics/
│   ├── fashion/
│   ├── footwear/
│   ├── beauty/
│   ├── seller_profile/
│   └── ... (13 product categories)
│
├── templates/                 # HTML templates for web views
│   ├── base templates
│   ├── category templates
│   └── product templates
│
├── static/                    # Static files (CSS, JS, images)
└── requirements.txt           # Python dependencies
```

---

## 🛠 Tech Stack

- **Backend Framework**: Django 4.2.0
- **API Framework**: Django REST Framework
- **Database**: PostgreSQL (with psycopg2)
- **Image Processing**: Pillow
- **Frontend**: Django Templates + Tailwind CSS
- **Configuration**: python-decouple
- **Development Tools**: django-browser-reload

---

##  Installation

### Prerequisites
- Python 3.8+
- PostgreSQL
- Git

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd E_commerce_platform_A
   ```

2. **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create .env file**
   ```bash
   # In My_Ecommecre directory
   SECRET_KEY=your-secret-key-here
   ```

5. **Configure PostgreSQL database**
   - Create a PostgreSQL database
   - Update `settings.py` with your database credentials

6. **Run migrations**
   ```bash
   python manage.py migrate
   ```

7. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

8. **Collect static files**
   ```bash
   python manage.py collectstatic
   ```

9. **Run development server**
   ```bash
   python manage.py runserver
   ```

   Access the application at: `http://localhost:8000`

---

## ⚙️ Configuration

### CORS Settings
The project is configured to allow cross-origin requests from multiple sources:
- Flutter web (port 50488)
- Development servers (ports 5000, 3000, 8000)
- All methods: GET, POST, PUT, PATCH, DELETE
- All headers supported

### Database Configuration
Located in [My_Ecommecre/settings.py](My_Ecommecre/My_Ecommecre/settings.py):
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

## 🔌 API Endpoints

### Authentication API
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/auth/signup/` | Create new user account |
| POST | `/api/auth/login/` | User login |
| POST | `/api/auth/logout/` | User logout |

### Product API
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/all-products/` | Get all products |
| GET | `/api/category/<category>/` | Get products by category |
| GET | `/api/product/<category>/<id>/` | Get product details |
| GET | `/api/search/` | Search products |
| POST | `/api/create-order/` | Create new order |
| POST | `/api/create-comment/` | Add comment to product |

### Seller API
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/seller/profile/` | Get seller profile |
| POST | `/api/seller/add-product/` | Add new product |
| GET | `/api/seller/inventory/` | Get seller's inventory |
| PUT | `/api/seller/edit-product/<category>/<id>/` | Edit product |
| GET | `/api/seller/orders/` | View seller's orders |
| DELETE | `/api/seller/delete-order/<id>/` | Delete order |
| GET | `/api/seller/reviews/` | View customer reviews |
| POST | `/api/seller/reply-comment/<id>/` | Reply to comment |

### Web Routes
| Route | Purpose |
|-------|---------|
| `/` | Home page |
| `/admin/` | Django admin panel |
| `/products/` | All products page |
| `/electronics/`, `/fashion/`, `/footwear/`, etc. | Category pages |
| `/product/<category>/<id>/` | Product detail page |
| `/order/<category>/<id>/` | Order page |
| `/contact/` | Contact page |

---

##  Database Models

### Product Models (app1)
All product categories share a similar structure:

```python
class ProductCategory(models.Model):
    - seller_relation (ForeignKey to Seller)
    - name (CharField)
    - price (DecimalField)
    - description (TextField)
    - image (ImageField)
    - stock (PositiveIntegerField)
    - category (CharField)
    - brand (CharField)
    - created_time (DateTimeField)
```

**Supported Categories:**
- Electronics
- Fashion
- Footwear
- Beauty
- Home & Kitchen
- Health & Wellness
- Sports & Outdoors
- Kids & Toys
- Automotive
- Books
- Groceries
- Jewelry
- Pets

### Seller Model (sellerapp)
```python
class Seller(models.Model):
    - user (OneToOneField to User)
    - shop_name (CharField)
    - phone (CharField)
    - image (ImageField) - Profile picture
    - bio (TextField)
    - location (CharField)
    - background_image (ImageField) - Shop banner
```

### User Model
Uses Django's built-in `User` model with fields:
- username
- email
- password
- first_name
- last_name

---

##  Usage

### Starting the Server
```bash
cd My_Ecommecre
python manage.py runserver
```

### Accessing Admin Panel
1. Navigate to: `http://localhost:8000/admin/`
2. Login with superuser credentials
3. Manage products, users, sellers, and orders

### Creating a New Product (via Admin)
1. Go to Admin panel
2. Select the product category (Electronics, Fashion, etc.)
3. Click "Add [Category]"
4. Fill in product details (name, price, description, image, stock)
5. Save

### Registering a Seller
1. User registers via `/api/auth/signup/`
2. Admin assigns seller status
3. Seller creates profile via seller API
4. Seller can manage products and orders

---

##  Key Features Implementation

### Search Functionality
- Full-text search across product names and descriptions
- Category-based filtering
- Real-time search results

### Order Management
- Create orders with order details
- Seller can view and manage orders
- Delete order functionality for sellers

### Review System
- Customers can leave comments on products
- Sellers can reply to customer feedback
- Comment management for sellers

### Inventory System
- Track product stock levels
- Update stock when orders are placed
- Real-time inventory visibility

---

##  Security Features

- CORS configuration for API security
- User authentication and authorization
- Django's built-in protection against CSRF attacks
- Secure password hashing
- Environment-based configuration (using python-decouple)

---

## 📝 Database Supported Categories

The platform supports 13+ product categories:
1. **Electronics** - Devices, gadgets, and tech
2. **Fashion** - Clothing and apparel
3. **Footwear** - Shoes and boots
4. **Beauty** - Cosmetics and beauty products
5. **Home & Kitchen** - Home and kitchen items
6. **Health & Wellness** - Health and wellness products
7. **Sports & Outdoors** - Sports equipment
8. **Kids & Toys** - Children's products
9. **Automotive** - Car and vehicle products
10. **Books** - Books and publications
11. **Groceries** - Food and groceries
12. **Jewelry** - Jewelry and accessories
13. **Pets** - Pet products and supplies

---

##  Frontend Integration

This backend is designed to work with mobile and web frontends:
- **Flutter Mobile App** - Communicates via REST API
- **Web Interface** - Django templates for traditional web experience
- **API-First Design** - Easy integration with any frontend framework

---

##  Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

##  Support

For issues or questions:
1. Check the documentation
2. Review API endpoint specifications
3. Check Django and DRF documentation

---

##  License

This project is licensed under the MIT License - see the LICENSE file for details.

---

##  Future Enhancements

- Payment gateway integration
- Advanced analytics dashboard
- Email notifications
- SMS alerts for orders
- Recommendation system
- Advanced reporting tools
- Multi-language support
- Mobile app optimization

---

**Project Status**: Active Development

Last Updated: 2026-06-12
