# Cloud-Hosted Business API – Project 1

**Internship Company:** Arrowstack Technologies  
**Project:** Cloud-Hosted Business API  
**Project Number:** 01  
**Status:** In Progress

## Project Overview

This project involves building and deploying a cloud-hosted Employee Management API.

The application allows users to create, view, update and delete employee records through REST API endpoints.

The application is built using FastAPI and PostgreSQL, containerized using Docker, and will be deployed on AWS as part of the cloud computing internship.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| FastAPI | Backend API framework |
| PostgreSQL | Relational database |
| SQLAlchemy | Database interaction |
| Docker | Application containerization |
| Docker Compose | Managing multiple containers |
| Git & GitHub | Version control and source code hosting |
| AWS | Planned cloud deployment platform |

## Current Project Features

- Create employee records.
- Retrieve all employee records.
- Retrieve employee records through API endpoints.
- Update existing employee details.
- Delete employee records.
- PostgreSQL database integration.
- Docker-based application containerization.
- Docker Compose for managing the API and database.
- Persistent PostgreSQL storage using Docker volumes.
- Environment variables for database configuration.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Welcome message |
| POST | `/employees` | Create an employee |
| GET | `/employees` | Retrieve employees |
| PUT | `/employees/{employee_id}` | Update an employee |
| DELETE | `/employees/{employee_id}` | Delete an employee |

Interactive API documentation is available through FastAPI Swagger UI at `/docs`.

## Project Structure

```text
employee-api/
│
├── main.py
├── database.py
├── models.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── .gitignore
└── README.md
```

## Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/thealilabs/cloud-internship-project-1-business-api.git
```

### 2. Navigate into the project

```bash
cd cloud-internship-project-1-business-api
```

### 3. Create a `.env` file

Add your local database configuration:

```env
POSTGRES_USER=admin
POSTGRES_PASSWORD=your_local_password
POSTGRES_DB=employeedb
```

Use your own local development password.

### 4. Start the application

```bash
docker compose up -d --build
```

### 5. Access the API

Open the following URL in your browser:

```text
http://localhost:8000/docs
```

You can now test the API endpoints using Swagger UI.

## Cloud Deployment – Planned Work

The next phase involves deploying the application using AWS services.

Planned areas include:

- Amazon EC2 for application hosting.
- Amazon RDS for managed PostgreSQL database hosting.
- Amazon VPC and Security Groups for network security.
- AWS IAM for access management.
- AWS Secrets Manager for sensitive configuration.
- Amazon CloudWatch for monitoring and logging.
- Database backup and recovery.
- Cost monitoring and optimization.

These services will be added and documented as the project progresses.

## Learning Objectives

- Understand REST API development.
- Work with relational databases.
- Containerize applications using Docker.
- Manage multi-container applications using Docker Compose.
- Understand cloud infrastructure and deployment.
- Apply security, monitoring and backup practices.
- Document and maintain a cloud computing project.

## Repository

GitHub: https://github.com/thealilabs/cloud-internship-project-1-business-api

---

**Developed as part of the Cloud Computing Internship at Arrowstack Technologies.**