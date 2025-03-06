# Blogging Platform API

A simple Django-based API that provides Create, Read, Update, Delete (CRUD) operations, along with search functionality for title,contact and category.

## Prerequisites

- Python 3.x
- PostgreSQL (or any database you use)


## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mbnahmadi/blogging-platform-api.git

2. Navigate to the project directory
3. Create and activate a virtual environment
4. Install dependencies:
- pip install -r requirements.txt
5. Setup the database:
- python manage.py makemigrations
- python manage.py migrate
6. Run the development server:
- python manage.py runserver


### Endpoints

- `POST /blog/create-post/` - Create a new post
- `GET /blog/get-all-posts/` - Get a list of all posts
- `GET /blog/get-post/<id>/` - Get a specific post by ID
- `PUT /blog/update-post/<id>/` - Update a post
- `DELETE /blog/delete-post/<id>/` - Delete a post
- `search /blog/search/` - search a term in title,contact and category


### Example: Creating a resource

Request:

{
    "title": "string",
    "content": "string",
    "category": "string",
    "tags": [
        "string"
    ]
}

### Search Functionality

You can search for post by specific fields.

GET /api/resource/?search=example


## API Documentation

The API documentation is available at `/swagger/` for Swagger UI and `/redoc/` for ReDoc.

Simply navigate to:
http://localhost:8000/swagger/

https://roadmap.sh/projects/blogging-platform-api


blogdrf app created for writing classes in views.py with genericsView