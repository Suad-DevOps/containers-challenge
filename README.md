# Flask Redis Multi-Container App

A multi-container application using Python Flask and Redis, managed with Docker Compose with Nginx as a load balancer.

---

## What it does

- Flask web app with two routes
- Redis database to store a visit counter
- Nginx load balances traffic across multiple Flask instances
- Persistent storage using Docker volumes
- Environment variables for Redis configuration

---

## How to run it

1. Clone the repo

git clone https://github.com/Suad-DevOps/containers-challenge.git
cd containers-challenge

2. Start the containers

docker-compose up -d

3. Test it

curl http://localhost:5000
curl http://localhost:5000/count

4. Scale Flask to multiple instances

docker-compose up -d --scale web=3

---

## Project Structure

app.py                 # Flask application
Dockerfile             # Flask image
docker-compose.yml     # Multi-container setup
nginx.conf             # Nginx load balancer config
requirements.txt       # Python dependencies

---

## Tech Stack

- Python Flask
- Redis
- Docker & Docker Compose
- Nginx

---

Built by Suad-DevOps
