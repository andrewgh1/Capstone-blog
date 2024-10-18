**Blogging Platform API
Overview**
This Blog API is a built with Django and Django REST Framework. It provides a set of endpoints for managing a blogging platform, including features for creating, reading, updating, and deleting blog posts, user management, and more.
Features

Blog Post Management: Full CRUD operations for blog posts
User Management: User registration, authentication, and authorization
Categories and Tags: Organize posts with categories and tags
Search and Filter: Advanced search and filtering capabilities for blog posts
Authentication: Token-based authentication for secure API access
Permissions: Role-based access control to protect resources
Pagination: Efficient handling of large datasets
Sorting: Flexible sorting options for blog post listings

**Tech Stack**

Python 3.10+
Django 3.2+
Django REST Framework 3.12+
mySQL (default) / PostgreSQL/mySQL (recommended for production)

**Installation**

Clone the repository:
Copy git clone https://github.com/andrewgh1/Capstone-blog.git
cd blogapi

Create a virtual environment and activate it:
Copy python3 -m venv venv
`source venv/bin/activate`  # On Windows, use `venv\Scripts\activate`

Install dependencies:
Copy python3 -m pip install -r requirements.txt

Run migrations:
Copy python3 manage.py migrate

Create a superuser:
Copy python3 manage.py createsuperuser

Start the development server:
Copy python3 manage.py runserver

The API will be available at http://localhost:8000/api/schema/.
**API Endpoints**

/api/blog/posts/: Blog post operations
/api/account/users/: User management
/api/blog/categories/: Category operations
/api/blog/tags/: Tag operations
/api/token/: Authentication endpoints

For detailed API documentation, visit /api/schema/docs/ after starting the server.
Usage
**Authentication**
To use protected endpoints, include the token in the Authorization header:
Copy Authorization: Token your_auth_token_here
Creating a Blog Post
POST to /api/blog/posts/ with the following data:
jsonCopy{
  "title": "My First Blog Post",
  "content": "This is the content of my first blog post.",
  "category": 1,
  "tags": [{"name": "Python"}, {"name": "Django"}]
}
**Retrieving Blog Posts**
GET /api/blog/posts/ to list all posts. Use query parameters for filtering:

/api/blog/posts/?category=technology
/api/blog/posts/?author=andrew
/api/blog/posts/?search=Django
etc ...
