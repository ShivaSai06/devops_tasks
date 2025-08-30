


# DevOps Task 2 - Full Stack ToDo Application

This project is a **Full Stack ToDo App** built with:
- **Backend**: Node.js + Express + MongoDB (Mongoose models for tasks)
- **Frontend**: Vite + React
- **CI/CD**: Jenkins pipeline (`Jenkinsfile`)
- **Containerization**: Docker & Docker Compose

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/devops_tasks.git
cd devops_tasks/devops_task2
````

### 2. Run with Docker Compose

This project is fully containerized. To start both frontend & backend:

```bash
docker-compose up --build
```

* Backend will run on [http://localhost:5000](http://localhost:5000)
* Frontend will run on [http://localhost:3000](http://localhost:3000)

### 3. Run Backend Locally (Optional)

```bash
cd backend
npm install
node app.js
```

### 4. Run Frontend Locally (Optional)

```bash
cd frontend
npm install
npm run dev
```

---

## ⚙️ Jenkins CI/CD

The `Jenkinsfile` defines a pipeline with the following stages:

1. **Checkout Code** – Pull source from GitHub.
2. **Build Backend** – Build Docker image for Node.js backend.
3. **Build Frontend** – Build Docker image for React frontend.
4. **Run Tests** (if added later).
5. **Deploy** – Deploy containers using Docker Compose.

---

## 🛠️ Technologies Used

* **Node.js / Express**
* **MongoDB (via Mongoose)**
* **React (Vite)**
* **Docker & Docker Compose**
* **Jenkins CI/CD**

---

## 📌 Notes

* Ensure **Docker & Docker Compose** are installed before running.
* Update environment variables (like MongoDB connection string) as needed inside the backend.
* The project is designed to be modular – you can replace the frontend or backend independently.


