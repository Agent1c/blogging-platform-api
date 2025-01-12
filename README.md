# Blogging_Platform_API

## Overview

The Blogging Platform API is a backend service built using Django and Django REST Framework. It allows users to manage blog posts by creating, updating, deleting, and viewing posts. The API also supports features like categorization, author-based filtering, and user authentication.

## Features

- **Blog Post Management (CRUD)**: Create, Read, Update, and Delete blog posts.
- **User Management (CRUD)**: Create, Read, Update, and Delete users.
- **Categorization**: View posts by category.
- **Author-based Filtering**: View posts by a specific author.
- **Search and Filter**: Search for blog posts by title, content, tags, or author with optional filters for published date or category.
- **Authentication**: User authentication using Django’s built-in authentication system and JWT.
- **Pagination and Sorting**: Pagination for blog post listings and sorting options.

## Models

### User

- `username`: Unique username for the user.
- `email`: Unique email address for the user.
- `password`: Password for the user.
- `groups`: Many-to-many relationship with `Group`.
- `user_permissions`: Many-to-many relationship with `Permission`.

### BlogPost

- `title`: Title of the blog post.
- `content`: Content of the blog post.
- `author`: Foreign key to the `User` model.
- `category`: Foreign key to the `Category` model.
- `published_date`: Date when the post was published.
- `created_date`: Date when the post was created.
- `tags`: Many-to-many relationship with `Tag`.

### Category

- `name`: Name of the category.

### Tag

- `name`: Name of the tag.

## API Endpoints

### User Endpoints

- `GET /users/`: List all users.
- `POST /users/`: Create a new user.
- `GET /users/<int:pk>/`: Retrieve a user by ID.
- `PUT /users/<int:pk>/`: Update a user by ID.
- `DELETE /users/<int:pk>/`: Delete a user by ID.
- `POST /users/register/`: Register a new user.
- `POST /users/login/`: Log in a user.
- `POST /users/logout/`: Log out a user.

### Blog Post Endpoints

- `GET /blog/`: List all blog posts.
- `POST /blog/`: Create a new blog post.
- `GET /blog/<int:pk>/`: Retrieve a blog post by ID.
- `PUT /blog/<int:pk>/`: Update a blog post by ID.
- `DELETE /blog/<int:pk>/`: Delete a blog post by ID.
- `GET /blog/category/<str:category>/`: List blog posts by category.
- `GET /blog/author/<str:author_username>/`: List blog posts by author.
- `GET /blog/search/`: Search for blog posts.

## Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/Agent1c/Blogging_Platform_API.git
   cd Blogging_Platform_API

## Create a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

## Install dependencies:
pip install -r requirements.txt

## Apply migrations:
python manage.py migrate

## Create a superuser:
python manage.py createsuperuser

## Run the development server:
python manage.py runserver

Usage
Access the admin panel at http://127.0.0.1:8000/admin/ to manage users and blog posts.
Use the API endpoints to interact with the blogging platform.
Deployment
To deploy the API on Heroku or PythonAnywhere, follow their respective documentation for deploying Django applications.

Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.