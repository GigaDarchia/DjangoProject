# Django Project

This is a Django-based web application. The project is still under development and consists of multiple apps.

## Pre-configured Superuser:

- Email: `test@admin.com`
- Username: `Giga`
- Password: `pass123!`

## Project Structure

- `djangoproject/`
  - `settings.py` - Contains the settings for the Django project.
  - `urls.py` - Contains the URL declarations for the Django project.
  - `views.py` - Contains the views for the Django project.
  - `media` - Directory that contains project media files
  
- `order/`
  - `models.py` - Contains the cart model.
  - `urls.py` - Contains the URL declarations for the order app.
  - `views.py` - Contains the views for the order app.
  - `signals.py` - Contains the signal that assigns a newly registered user a cart.
  
- `store/`
  - `models.py` - Contains the models for the store app.
  - `urls.py` - Contains the URL declarations for the store app.
  - `views.py` - Contains the views for the store app.

- `user_app`
  - `models.py` - Contains the custom user model.


## Setup

1. Clone the repository
   ```bash
   git clone https://github.com/GigaDarchia/DjangoProject.git
   ```
2. Install the dependencies
   ```bash
   pip install -r requirements.txt
   ```
3. Apply migrations
   ```bash
   python manage.py migrate
   ```
4. Run the development server
   ```bash
   python manage.py runserver
   ```


