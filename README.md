# E-Commerce Backend API

REST API for e-commerce platform built with Django REST Framework.

## Features
- User authentication (JWT)
- Product catalog with categories
- Shopping cart management
- Order processing

## Tech Stack
- Python 3.x
- Django 6.x
- Django REST Framework 3.x
- PostgreSQL 
- JWT Authentication

[//]: # (## Live Demo)

[//]: # (**API Base URL:** https://your-app.onrender.com/api/)

[//]: # (**API Documentation:** https://your-app.onrender.com/api/schema/swagger/)

## API Endpoints

### Authentication
- `POST /api/auth/register/` - Register new user
- `POST /api/auth/login/` - Login (get JWT tokens)
- `POST /api/auth/refresh/` - Refresh access token
- `POST /api/auth/logout/` - Logout

### Products
- `GET /api/products/` - List all products
- `GET /api/products/{slug}/` - Get product details

### Categories
- `GET /api/categories/` - List all categories
- `GET /api/categories/{id}/` - Get category details

### Cart
- `GET /api/cart/` - Get current user's cart
- `POST /api/cart/items/` - Add item to cart
- `PATCH /api/cart/items/{id}/` - Update item quantity
- `DELETE /api/cart/items/{id}/` - Remove item from cart
- `DELETE /api/cart/clear/` - Clear cart

### Orders
- `GET /api/orders/` - List user's orders
- `POST /api/orders/` - Create order from cart
- `GET /api/orders/{id}/` - Get order details

## Setup (Local)

1. Clone repository
```bash
git clone https://github.com/ayush-logs/ecommerce-backend-api.git
cd ecommerce-backend-api
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Setup database
```bash
python manage.py migrate
```

4. Create superuser (optional)
```bash
python manage.py createsuperuser
```

5. Run server
```bash
python manage.py runserver
```

## Example Usage

### Register User
```bash
curl -X POST https://your-app.onrender.com/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "email": "test@example.com", "password": "securepass123"}'
```

### Login
```bash
curl -X POST https://your-app.onrender.com/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "securepass123"}'
```

### Add Item to Cart
```bash
curl -X POST https://your-app.onrender.com/api/cart/items/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"product_id": 1, "quantity": 2}'
```

## Environment Variables
```
SECRET_KEY=your-secret-key
DEBUG=False
DATABASE_URL=postgresql://...
ALLOWED_HOSTS=your-domain.onrender.com
```

## Database Schema

[Optional: Add ERD or describe models]

## Future Enhancements
- Payment integration
- Product search and filtering
- Email notifications
- Admin dashboard

## License
MIT
