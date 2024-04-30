# Vendor Management System

This Django-based application provides a comprehensive solution for managing vendors, tracking purchase orders, and evaluating vendor performance based on various metrics. The system includes features for CRUD operations on vendors and purchase orders, as well as calculating and storing performance metrics such as on-time delivery rate, quality rating average, average response time, and fulfillment rate.

## Features

- **Vendor Profile Management**: Create, retrieve, update, and delete vendor profiles with details like name, contact information, address, and a unique vendor code.
- **Purchase Order Tracking**: Manage purchase orders by creating, listing, retrieving, updating, and deleting orders. Filter purchase orders by vendor name.
- **Vendor Performance Evaluation**: Calculate and track vendor performance metrics, including on-time delivery rate, quality rating average, average response time, and fulfillment rate.
- **Historical Performance Tracking**: Store historical records of vendor performance metrics for trend analysis.
- **Purchase Order Acknowledgment**: Vendors can acknowledge purchase orders, triggering the calculation of average response time.
- **Token-based Authentication**: Secure API endpoints with token-based authentication using Django REST Framework.

## Installation

1. Clone the repository:

```
git clone https://github.com/nabeelahmdd/fatmug.git
```

2. Create a virtual environment and activate it:

```
python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
```

3. Install the required dependencies:

```
pip install -r requirements.txt
```

4. Create a `.env` file in the project directory and add variable with value:

```
SECRET_KEY=your_secret_key_value
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your_db_host
DB_PORT=your_db_port
```

5. Apply database migrations:

```
python manage.py migrate
```

6. Create a superuser (optional, if you want to access the Django admin):

```
python manage.py createsuperuser
```

## Usage

1. Start the development server:

```
python manage.py runserver
```

2. Access the API endpoints from `http://localhost:8000/api/`. You can find the detailed documentation for each endpoint in the `API_DOCUMENTATION.md` file.

3. Obtain access and refresh tokens by sending a POST request to `http://localhost:8000/api/login/` with your username and password.

4. Include the access token in the `Authorization` header as `Bearer <access_token>` for authenticated requests.

