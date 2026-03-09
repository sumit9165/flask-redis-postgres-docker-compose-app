# Flask Redis PostgreSQL App with Docker Compose

A simple **multi-container web application** built using **Flask**, **Redis**, and **PostgreSQL**, containerized using **Docker** and orchestrated with **Docker Compose**.

This project demonstrates how to deploy a **full-stack application with a backend API, database, caching layer, and frontend UI templates** using containerized infrastructure.

---

# Project Architecture

This application follows a **3-tier architecture**:

1. **Flask Web Application** – Backend API and UI rendering
2. **PostgreSQL Database** – Persistent data storage
3. **Redis Cache** – In-memory data store for fast access

```
User Browser
     │
     ▼
Flask Web Application (Port 5000)
     │
     ├──────────────► Redis Cache (Port 6379)
     │
     └──────────────► PostgreSQL Database (Port 5432)
```

All services run as **separate containers** managed through **Docker Compose**.

---

# Project Structure

```
devops-docker-ui-project
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── app.py
├── README.md
│
├── templates
│   └── index.html
│
└── static
    └── style.css
```

### Explanation

* **Dockerfile** – Builds the Flask application container
* **docker-compose.yml** – Defines multi-container services
* **app.py** – Main Flask application
* **requirements.txt** – Python dependencies
* **templates/** – HTML templates rendered by Flask
* **static/** – Static files such as CSS

---

# Technologies Used

* Python
* Flask
* Redis
* PostgreSQL
* Docker
* Docker Compose
* HTML
* CSS

---

# Features

* Multi-container application using Docker Compose
* Flask web interface with HTML templates
* Static CSS styling
* PostgreSQL database integration
* Redis caching layer
* Container networking
* Health checks for service readiness
* Persistent database storage using Docker volumes

---

# Prerequisites

Before running this project, install:

* Docker
* Docker Compose

Verify installation:

```bash
docker --version
docker compose version
```

---

# Environment Variables

Create a `.env` file in the project root.

```
POSTGRES_DB=mydatabase
POSTGRES_USER=admin
POSTGRES_PASSWORD=password

DB_HOST=postgres_db
REDIS_HOST=redis_db
```

---

# Running the Application

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/repository-name.git
cd repository-name
```

### 2. Build and start containers

```bash
docker compose up --build -d
```

This command will:

* Build the Flask application image
* Pull Redis and PostgreSQL images
* Create the containers
* Start all services

---

# Verify Running Containers

```bash
docker ps
```

Expected services:

* flask-redis-app
* postgres_db
* redis_db

---

# Access the Application

Open a browser and visit:

```
http://localhost:5000
```

If running on **AWS EC2**:

```
http://EC2_PUBLIC_IP:5000
```

---

# Stop the Application

```bash
docker compose down
```

---

# Docker Compose Services

### Flask Application

* Built using the local Dockerfile
* Connects to Redis and PostgreSQL
* Serves UI templates and static files

### PostgreSQL

* Persistent relational database
* Uses Docker volume for storage

### Redis

* In-memory caching database
* Improves application performance

---

# Networking

All services communicate through a **custom Docker network**:

```
three-network
```

Containers communicate using **service names as hostnames**:

```
postgres_db
redis_db
```

---

# Learning Outcomes

This project helped demonstrate several important DevOps and containerization concepts:

### Docker Fundamentals

* Building custom images using Dockerfile
* Running containers for application services

### Docker Compose

* Managing multi-container applications
* Defining services, networks, and volumes
* Managing dependencies between containers

### Backend Integration

* Connecting Flask application with PostgreSQL
* Using Redis for caching

### Container Networking

* Service-to-service communication using Docker networks

### Persistent Storage

* Using Docker volumes for database data persistence

### Application Deployment

* Deploying a containerized web application on a Linux environment

---

# Key Takeaways

* Docker simplifies application deployment by packaging dependencies and runtime environments.
* Docker Compose enables easy management of complex multi-service architectures.
* Container networks allow services to communicate without exposing internal ports.
* Using Redis alongside PostgreSQL improves application performance through caching.
* Containerized applications are portable and can run consistently across environments.

---

# Future Improvements

Potential enhancements for this project:

* Add **Nginx reverse proxy**
* Implement **Docker health monitoring**
* Add **CI/CD pipeline with GitHub Actions**
* Deploy to **AWS EC2 or Kubernetes**
* Implement **environment-based configurations**
* Add **authentication and user management**

---

# Conclusion

This project demonstrates how to deploy a **containerized Flask application with Redis and PostgreSQL using Docker Compose**, showcasing practical DevOps skills such as container orchestration, networking, and persistent storage.

---

⭐ If you found this project useful, consider giving the repository a star.

