# Electro Store

Electro Store is an online store built with Django and PostgreSQL. It features a user-friendly interface for browsing and purchasing electronic products, along with an administrative dashboard for managing products, orders, and customers.

## Features

- **Product Management**: Add, edit, and delete products with detailed descriptions, images, and prices.
- **User Authentication**: User registration, login, and secure session management.
- **Shopping Cart**: Add products to the cart, view cart details, and checkout.
- **Order Management**: Track orders and manage order status.
- **Search and Filtering**: Easily search for products and filter by categories or price range.
- **Admin Dashboard**: Comprehensive dashboard for managing products, orders, and users.

## Technologies Used

- **Backend**: Django
- **Database**: SQLite
- **Frontend**: HTML, CSS, JavaScript

## Installation

To get started with Electro Store, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/error-00/electro-store.git
   cd electro-store
   ```

2. **Create a virtual environment and activate it:**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

## Usage

- **Admin Dashboard**: Access the admin dashboard at `/admin` to manage products, orders, and users.
- **Shopping**: Browse products, add them to the cart, and proceed to checkout.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss your ideas.
