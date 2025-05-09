# 🚀 Flask Application with HAProxy Load Balancing

This is a containerized Flask application that can be run in multiple ways, including with HAProxy-based load balancing via Docker Compose.

## 📦 Prerequisites

Ensure the following are installed:

* Docker
* Docker Compose
* Python 3.8+ (only for local run)

## 🔧 Installation

If you're running locally (Option 3 below), install dependencies with:

```bash
pip install -r requirements.txt
```

## 🧭 Ways to Start the App

You can run the Flask application using any of the following methods:

### ✅ Option 1: Docker Compose with HAProxy (Recommended)

This method runs multiple Flask containers behind an HAProxy load balancer.

```bash
docker-compose up --build
```

* Builds the Flask image using the Dockerfile
* Spins up multiple instances of the Flask app
* Uses HAProxy to distribute traffic across them

Access the app at: [http://localhost:8080](http://localhost:8080)

To stop and remove containers:

```bash
docker-compose down
```

### 🐳 Option 2: Run Flask App Manually with Docker

1. Build the Docker image:

```bash
docker build -t flask-app .
```

2. Run the container:

```bash
docker run -p 5000:5000 flask-app
```

Access the app at: [http://localhost:5000](http://localhost:5000)

**Note:** This runs only a single instance and does not include load balancing.

### 🐍 Option 3: Run Locally Without Docker

1. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Flask development server:

```bash
python app.py
```

Access the app at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## 📁 Project Structure

```
.
├── app.py
├── Dockerfile                # Docker build instructions
├── docker-compose.yml        # Multi-container setup with HAProxy
├── haproxy.cfg               # HAProxy configuration
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

## ⚙️ HAProxy Configuration

The `haproxy.cfg` file is used to route incoming traffic across multiple Flask app containers.

Sample HAProxy configuration:

```
frontend http_front
   bind *:8080
   default_backend http_back

backend http_back
   balance roundrobin
   server flask1 flask-app1:5000 check
   server flask2 flask-app2:5000 check
```

Make sure the service names in `docker-compose.yml` match the server names above (e.g., `flask-app1`, `flask-app2`).

## 🧼 Clean Up

To stop and remove all running containers:

```bash
docker-compose down
```

To remove all images and volumes (use with caution):

```bash
docker system prune -a
```
