# Django Project with Docker and SQLite

## 🚀 Overview
This project is a Django web application that runs inside a **Docker container** using SQLite as the database.

## 📂 Project Structure
```
├── myproject/ ( BharatFD)       # Django Project
│   ├── settings.py   # Django Settings
│   ├── urls.py       # URL Routing
│   ├── views.py      # Views
│   ├── models.py     # Database Models
│   ├── templates/    # HTML Templates
├──  Django APP ( APP )
├── Dockerfile        # Docker Configuration
├── docker-compose.yml # Docker Compose Config
├── requirements.txt  # Python Dependencies
├── README.md         # Project Documentation
├──  sqlite
```

---

## 📦 Setup & Installation

### 🔹 1. Install Prerequisites
- [Docker](https://www.docker.com/get-started)
- [Python 3](https://www.python.org/downloads/)

### 🔹 2. Clone the Repository
```bash
git clone [https://github.com/yourusername/yourrepo.git](https://github.com/SINGHBP29/translator.git)
cd new1
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
- Use **PostgreSQL** instead of SQLite.

---

### 💬 Need Help?
If you face any issues, feel free to open an **issue** on GitHub! 🚀
