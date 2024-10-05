# Django Project

This is a Django-based web application. The project is still under development and consists of multiple apps.

## Project Structure

- `djangoproject/`
  - `settings.py` - Contains the settings for the Django project.
  - `urls.py` - Contains the URL declarations for the Django project.
  - `views.py` - Contains the views for the Django project.
  
- `order/`
  - `urls.py` - Contains the URL declarations for the order app.
  - `views.py` - Contains the views for the order app.
  
- `store/`
  - `urls.py` - Contains the URL declarations for the store app.
  - `views.py` - Contains the views for the store app.

## Setup

1. Clone the repository
   ```bash
   git clone <https://github.com/GigaDarchia/DjangoProject.git>
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

