# book-api
README file for a basic book api for managing inventory.

```markdown
# Book API

## Overview

This is a Django-based RESTful API for managing books. It supports operations like searching for books by category and retrieving low-stock book entries.

## Requirements

- **Docker**: Make sure Docker is installed on your machine.
- **Python**: This project is built using Python version **3.11.3**.

## Getting Started

Follow these steps to run the application using Docker.

### Step 1: Clone the Repository

```bash
git clone https://github.com/davidmizra17/book-api.git
cd book-api
```

### Step 2: Install Docker

If you don't have Docker installed, please follow the official installation guide for your operating system:

- **[Docker Installation Guide](https://docs.docker.com/get-docker/)**

### Step 3: Build and Run the Docker Container

1. Make sure you're in the root directory of the cloned repository.

2. Build the Docker image and start the container:

```bash
docker compose -f docker-compose.yml up --build
```

### Step 4: Access the API

Once the container is running, you can access the API at:

```plaintext
http://0.0.0.0:8000/api/
```

### API Endpoints

- **GET /api/books/**: Retrieve all books.
- **GET /api/books/{id}** Retrieve a book by it's ID
- **POST /api/books/** Create a book
- **DELETE /api/books/** Delete a book
- **POST /api/books/{id}/calculate-price/** Calculate the selling price for a book consulting an external api
- **PUT /api/books/{id}** Update a book
- **GET /api/books/search?category={category}**: Search for books by category.
- **GET /api/books/low-stock?threshold=10**: Get books with stock below the specified threshold.

### Step 5: Stop the Application

To stop the application, press `Ctrl + C` in the terminal where the Docker container is running. You can also remove the containers with:

```bash
docker compose down
```

## Development

### Python Requirements

Make sure the following packages are listed in `requirements.txt`:

```
Django>=4.2
djangorestframework
django-filter
requests
# Add any other dependencies here
```

After modifying the requirements, rebuild the Docker container to ensure all dependencies are met.

```

### Explanation of Sections

- **Overview**: Brief description of what the project does.
- **Requirements**: Lists necessary software and versions.
- **Getting Started**: Step-by-step guide to clone, install, and run the project.
- **API Endpoints**: Lists available API endpoints.
- **Development**: Instructions for modifying dependencies and rebuilding.
- **Contact and License**: Provides information for reaching out or licensing details.

Feel free to modify any part of this README to better match your project's specifics!
