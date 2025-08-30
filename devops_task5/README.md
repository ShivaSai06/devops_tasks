# 🔐 Local Password Manager – Kubernetes Deployment

A simple **Flask-based Password Manager** application running on **Kubernetes** using Minikube.  
This project demonstrates deploying a small real-world utility application with Kubernetes objects like Deployments, Services, Persistent Volumes, and Persistent Volume Claims.

---

## 🚀 Project Overview
The Local Password Manager allows users to securely store and retrieve passwords locally using a SQLite database.  
It is packaged in a Docker container and deployed to a Minikube Kubernetes cluster.

---

## 🛠️ Technologies Used
- **Flask** – Web framework for the application
- **SQLite** – Local database storage
- **Docker** – Containerization
- **Kubernetes** – Deployment and service management
- **Minikube** – Local Kubernetes cluster

---

## ⚙️ Setup & Deployment Steps

### 1️⃣ Start Minikube
```bash
minikube start --driver=docker
2️⃣ Build Docker Image (inside Minikube environment)
bash
Copy
Edit
eval $(minikube docker-env)
docker build -t password-manager:latest .
3️⃣ Deploy Application
bash
Copy
Edit
kubectl apply -f k8s/deployment.yaml
4️⃣ Expose Service
bash
Copy
Edit
kubectl apply -f k8s/service.yaml
minikube service password-manager-service
5️⃣ Verify Pods
bash
Copy
Edit
kubectl get pods
6️⃣ Scale Deployment
bash
Copy
Edit
kubectl scale deployment password-manager --replicas=3
kubectl get pods
7️⃣ View Pod Details & Logs
bash
Copy
Edit
kubectl describe pod <pod-name>
kubectl logs <pod-name>
📸 Expected Output
kubectl get pods → shows running pods (scaled replicas if scaled)

kubectl get services → shows NodePort for browser access

Application accessible via Minikube service URL

Logs showing Flask app startup and request handling

🔑 Key Learnings
Building and containerizing a Python web application

Deploying applications in Kubernetes using Deployment and Service

Using Persistent Volumes with SQLite for data persistence

Scaling pods using kubectl scale

Inspecting and debugging pods with kubectl describe and kubectl logs


