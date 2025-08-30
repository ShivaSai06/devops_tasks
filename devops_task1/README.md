
---

### 📦 Node.js CI/CD Pipeline with GitHub Actions and Docker

This project demonstrates how to automate code deployment using a **CI/CD pipeline** built with **GitHub Actions** and **DockerHub**.

---

### 🚀 Project Overview

* A simple Node.js app (`app.js`) that runs an HTTP server on port `3000`.
* A Dockerfile to containerize the app.
* A GitHub Actions workflow that runs on every push to the `main` branch:

  * Installs dependencies
  * Runs tests
  * Builds Docker image
  * Pushes the image to DockerHub

---

### 🛠️ Technologies Used

* Node.js
* Docker
* GitHub Actions
* DockerHub

---

### ⚙️ Workflow Summary (`.github/workflows/main.yml`)

```yaml
on:
  push:
    branches: [ "main" ]

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - Checkout code
      - Set up Node.js
      - Install dependencies
      - Run tests
      - Login to DockerHub
      - Build and push Docker image
```

---

### 🔐 Secrets Configured in GitHub

Go to your repo → **Settings → Secrets → Actions**, and add:

* `DOCKER_USERNAME` — your DockerHub username
* `DOCKER_PASSWORD` — your DockerHub access token or password

---

### 📤 Result

On each push to `main`:

* The Docker image is automatically built
* It is pushed to: `docker.io/<your-username>/nodejs-demo-app:latest`

You can run the image locally:

```bash
docker pull <your-username>/nodejs-demo-app
docker run -p 3000:3000 <your-username>/nodejs-demo-app
```

Visit [http://localhost:3000](http://localhost:3000)

---

