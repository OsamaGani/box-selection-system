
# Box Selection System

## About the Project

This project is made using Python and Django. It helps select a suitable shipping box for an order based on the product dimensions, product weight, and box cost.

The main goal is to find the lowest-cost box that can hold the products and stay within the box's weight limit.

## Technologies Used

- Python
- Django
- SQLite
- JSON API

## Features

- Add and manage products through Django Admin.
- Add shipping boxes with their dimensions and weight limits.
- Check product dimensions and total order weight.
- Recommend a suitable shipping box.
- Return the recommendation through an API.
- Test the main functionality using Django tests.

## How to Run the Project

First, activate the virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install Django if it is not installed:

```powershell
python -m pip install django
```

Apply migrations:

```powershell
python manage.py migrate
```

Start the server:

```powershell
python manage.py runserver
```

Open the following URL in your browser:

http://127.0.0.1:8000/admin/

## API

**Endpoint:** `POST /api/recommend/`

Example request:

```json
{
  "product_ids": [1]
}
```

The product ID must exist in the database.

The API returns the recommended box details if a suitable box is found.

## Run Tests

```powershell
python manage.py test boxes
```

## Limitations

The current packing algorithm uses a heuristic, so it may not find every possible valid arrangement of products inside a box.
