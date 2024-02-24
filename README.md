# Dashboard

Dashboard is a web application built using Django framework for managing posts, allowing users to upload, view, and share posts.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

#To run this project locally, follow these steps:
1.
  # pip install django djangorestframework
  # django-admin startproject Dashboard

2. Navigate to the project directory:
  # cd Dashboard
  # python manage.py startapp register


3. Apply migrations:
  # python manage.py makemigratations
  # python manage.py migrate

4. Create Superuser:
  # python manage.py createsuperuser
  And create super by giving username and password
  And you can access it by http://localhost:8000/admin

5. Start the server:
   # python manage.py runserver


6. Access the application in your browser at [http://localhost:8000](http://localhost:8000).

## Usage

- **Upload Post**: Visit `/upload_post/` to upload a new post.
- **View Post List**: Visit `/post_list/` to view all posts.
- **Delete All Posts**: Visit `/post/delete_post/` to delete all posts.

## Contributing

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.






