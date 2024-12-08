# Blog API Using GraphQL
> This project is a simple Blog API built using Django and GraphQL. The API allows users to perform basic CRUD operations on blog posts and comments.

---

## Tech Stack
>[![django](https://img.shields.io/badge/Django-092E20.svg?style=flat&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![python](https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white)](https://www.python.org/)
[![Graphene-Django](https://img.shields.io/badge/Graphene-Django-000000.svg?style=flat&logo=python&logoColor=white)](https://docs.graphene-python.org/projects/django/en/latest/)
[![GraphQL](https://img.shields.io/badge/GraphQL-E10098.svg?style=flat&logo=graphql&logoColor=white)](https://graphql.org/)
[![SQLite](https://img.shields.io/badge/SQLite-003B57.svg?style=flat&logo=sqlite&logoColor=white)](https://www.sqlite.org/)

---


## Setup

---

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Dhanshree019/Blog-API.git

2. **Create a virtual environment and activate it**:
   ```bash
   mkvirtualenv blog_api

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt

4. **Apply migrations to set up the database**:
   ```bash
   python manage.py migrate

5. **Start the development server**:
   ```bash
   python manage.py runserver
---

## Choices Made

1. **models.py**: Created two models, Post and Comment, and established a one-to-many relationship between them, i.e., one post has many comments.

2. **schema.py**: Created queries and mutations in this file.

3. **services.py**: Created helper functions in this file to maintain clean code and provide easy access.

4. **Logger and exception handling**: Implemented a logger and exception handling for required actions. Note: By running the program, you will find an app.log file in the main directory, which stores the logs. (Kept old logs for better understanding; remove them during a fresh run.)


## Create Post

![Alt Text](screenshots\create_post.png)

## Update Post
![Alt Text](screenshots\update_post.png)

## Create Comment
![Alt Text](screenshots\create_comment.png)

## Get All Posts
![Alt Text](screenshots\all_posts.png)

## Get Post By Id
![Alt Text](screenshots\post_by_id.png)

## Delete Post
![Alt Text](screenshots\delete_comment.png)