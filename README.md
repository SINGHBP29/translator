# Django Project with Docker, SQLite & Redis

## 🚀 Overview
This project is a Django web application that runs inside a **Docker container** using SQLite as the database and **Redis** for caching.

## 📂 Project Structure
```
├── myproject/        # Django Project
│   ├── myapp/        # Django App
│   ├── settings.py   # Django Settings
│   ├── urls.py       # URL Routing
│   ├── views.py      # Views
│   ├── models.py     # Database Models
│   ├── templates/    # HTML Templates
├── Dockerfile        # Docker Configuration
├── docker-compose.yml # Docker Compose Config
├── requirements.txt  # Python Dependencies
├── README.md         # Project Documentation
```

---

## 📦 Setup & Installation

### 🔹 1. Install Prerequisites
- [Docker](https://www.docker.com/get-started)
- [Python 3](https://www.python.org/downloads/)

### 🔹 2. Clone the Repository
```bash
git clone [GitHub](https://github.com/SINGHBP29/translator.git)
cd app
```

### 🔹 3. Build and Run with Docker
```bash
docker-compose up --build
```

### 🔹 4. Run Migrations & Create Superuser
```bash
docker exec -it django_app python manage.py migrate
docker exec -it django_app python manage.py createsuperuser
```

### 🔹 5. Access the Application
- **Django App**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Admin Panel**: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---
Features Implemented

✅ 1. FAQ Model with WYSIWYG Editor

Uses django-ckeditor for rich text support.

Stores FAQs with multilingual translations.

✅ 2. API Development

Implements Django REST Framework (DRF).

Supports ?lang= query parameter for language-based responses.

✅ 3. Caching with Redis

Uses django-redis for performance optimization.

Stores translated FAQs in cache.

✅ 4. Multi-language Translation

Integrates googletrans for automatic translations.

Fallback mechanism to English if translation fails.

✅ 5. Admin Panel

Registers FAQ model for easy management.

Supports django-ckeditor in admin for rich text editing.

✅ 6. Unit Testing

Uses pytest for testing.

Covers models, API responses, and caching mechanisms.

✅ 7. Docker & Deployment

Includes Dockerfile and docker-compose.yml.

Can be deployed to Heroku or AWS.

API Endpoints

Retrieve FAQs

# Default (English)
curl http://localhost:8000/api/faqs/

# Hindi Translation
curl http://localhost:8000/api/faqs/?lang=hi

# Bengali Translation
curl http://localhost:8000/api/faqs/?lang=bn

Admin Panel

Access the Django Admin at http://127.0.0.1:8000/admin/





## 🐳 Docker Configuration

### **Dockerfile**
```dockerfile
FROM python:3.10
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY . /app/
RUN pip install --upgrade pip && pip install -r requirements.txt
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

### **docker-compose.yml**
```yaml
version: '3'
services:
  web:
    build: .
    container_name: django_app
    ports:
      - "8000:8000"
    volumes:
      - .:/app
    depends_on:
      - redis

  redis:
    image: "redis:alpine"
    container_name: redis_cache
    ports:
      - "6379:6379"
```

---

## 📜 Configure Redis in Django

### **1. Install Redis Python Client**
```bash
pip install django-redis
```

### **2. Update `settings.py`**
```python
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://redis:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}
```

---

## 📜 Available Commands
| Command | Description |
|---------|-------------|
| `docker-compose up --build` | Build & start the container |
| `docker-compose down` | Stop the container |
| `docker exec -it django_app python manage.py migrate` | Run migrations |
| `docker exec -it django_app python manage.py createsuperuser` | Create admin user |

---

## 📌 Notes
- The **SQLite database (`db.sqlite3`)** is stored in the container, so **it won't persist** if the container is removed.
- To persist the database, **mount a volume** or switch to **PostgreSQL or MySQL**.
- Update `.gitignore` to **ignore `db.sqlite3`**.

---

## 💡 Next Steps
- Add **Redis** for caching.
- Deploy with **Gunicorn & Nginx**.

---

### 💬 Need Help?
If you face any issues, feel free to open an **issue** on GitHub! or Email me at **bhanups292004@gmail.com** 🚀

