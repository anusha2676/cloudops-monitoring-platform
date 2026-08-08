☁️ CloudOps Monitoring & Auto-Healing Platform

A cloud-based system monitoring and auto-healing platform built with Python, FastAPI, SQLAlchemy, Docker, and GitHub Actions.

The platform continuously monitors system resources such as CPU, memory, disk, and network usage. It provides health information, generates alerts for critical conditions, records monitoring data, and recommends controlled recovery actions.

🚀 Live Demo

Live Application:
https://cloudops-monitoring-platform.onrender.com

📌 Project Overview

The CloudOps Monitoring Platform is designed to demonstrate how cloud and DevOps concepts can be combined with Python application development.

The application provides REST APIs and a web dashboard for monitoring system health and resource utilization.

Key capabilities

- Real-time CPU monitoring
- Memory usage monitoring
- Disk usage monitoring
- Network statistics
- System health evaluation
- Automated alert generation
- Severity-based alert classification
- Controlled auto-healing logic
- Metric and alert persistence using SQLite
- REST APIs using FastAPI
- Web dashboard using Jinja2
- Docker containerization
- Docker Compose support
- Automated testing with Pytest
- Continuous Integration with GitHub Actions
- Cloud deployment using Render

🏗️ Architecture

                    ┌─────────────────────┐
                    │       User          │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   FastAPI Server    │
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
        Monitoring         Health Check      Dashboard
        System             Service           (Jinja2)
              │                │
              ▼                ▼
        Alert Generation ──► Auto-Healing
              │
              ▼
        SQLAlchemy / SQLite
              │
              ▼
        Persistent Metrics
        & Alerts

        Docker → GitHub Actions → Render

🛠️ Technologies Used

Technology| Purpose
Python| Application development
FastAPI| REST API framework
Psutil| System resource monitoring
SQLAlchemy| Database ORM
SQLite| Data storage
Jinja2| Dashboard templates
Pytest| Automated testing
Docker| Containerization
Docker Compose| Container orchestration
GitHub Actions| CI/CD
Render| Cloud deployment

📂 Project Structure

cloudops-monitoring-platform/
│
├── app/
│   ├── alerts/
│   │   └── alert_manager.py
│   │
│   ├── dashboard/
│   │   └── templates/
│   │       └── index.html
│   │
│   ├── healing/
│   │   └── auto_healer.py
│   │
│   ├── monitoring/
│   │   ├── system_monitor.py
│   │   └── health_checker.py
│   │
│   ├── services/
│   │   ├── metric_service.py
│   │   └── alert_service.py
│   │
│   ├── database.py
│   ├── models.py
│   └── main.py
│
├── tests/
│   ├── test_api.py
│   ├── test_monitoring.py
│   └── test_alerts.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md

🔌 API Endpoints

Home / Dashboard

GET /

Displays the monitoring dashboard.

Health

GET /health

Returns:

- Overall system status
- CPU usage
- Memory usage
- Disk usage

Metrics

GET /metrics

Returns:

- CPU usage
- Memory usage
- Disk usage
- Network statistics

Metrics are also stored in the database.

Alerts

GET /alerts

Returns:

- Generated alerts
- Alert count
- Healing results

🚨 Alert Thresholds

Resource| Warning| Critical
CPU| ≥ 80%| ≥ 90%
Memory| ≥ 80%| ≥ 90%
Disk| ≥ 85%| ≥ 95%

Critical alerts trigger the controlled auto-healing logic.

🩺 Auto-Healing

The platform evaluates critical alerts and generates a controlled recovery recommendation.

Examples include:

- CPU recovery recommendation
- Memory recovery recommendation
- Disk recovery recommendation

The current implementation records the recovery action rather than performing destructive system operations.

This design keeps the system safe while demonstrating the concept of automated remediation.

🧪 Testing

The project includes automated tests using Pytest.

Run the tests locally:

PYTHONPATH=. pytest

The test suite covers:

- API endpoints
- System monitoring
- CPU usage
- Memory usage
- Disk usage
- Network statistics
- Alert generation

🐳 Run with Docker

Build the Docker image:

docker build -t cloudops-monitoring-platform .

Run the container:

docker run -p 8000:8000 cloudops-monitoring-platform

Open:

http://localhost:8000

🐳 Run with Docker Compose

docker compose up --build

Then open:

http://localhost:8000

⚙️ CI/CD

GitHub Actions automatically:

1. Checks out the repository
2. Sets up Python
3. Installs dependencies
4. Runs automated tests
5. Builds the Docker image

This helps ensure that changes are tested before deployment.

☁️ Cloud Deployment

The application is deployed as a Dockerized web service on Render.

Live application:

https://cloudops-monitoring-platform.onrender.com

🔮 Future Enhancements

- Prometheus integration
- Grafana dashboards
- CloudWatch integration
- Email and Slack notifications
- Kubernetes deployment
- Redis-based caching
- PostgreSQL database
- Advanced anomaly detection using machine learning
- Role-based authentication
- Real infrastructure remediation
- Centralized logging
- Multi-server monitoring

👩‍💻 Author

Anusha B

BCA – Cloud Computing

Interested in Cloud Computing, DevOps, Python Development, and Software Engineering.

⭐ Project Highlights

This project demonstrates practical experience with:

Python • FastAPI • Cloud Computing • DevOps • Docker • CI/CD • REST APIs • SQLAlchemy • Monitoring • Alerting • Auto-Healing
