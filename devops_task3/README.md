
---

````markdown
# Terraform Docker Container Provisioning

## 📌 Objective

Provision a local **Docker container** using **Terraform** to learn Infrastructure as Code (IaC).

## 🧰 Tools Used

- Terraform
- Docker

## 📁 Files

- `main.tf` – Terraform configuration file

## 🚀 How to Run

### 1. Clone this repo (if needed)

```bash
git clone <repo-url>
cd terraform-docker-container
````

### 2. Initialize Terraform

```bash
terraform init
```

### 3. Preview the plan

```bash
terraform plan
```

### 4. Apply the configuration

```bash
terraform apply
```

> Access the Nginx container at: [http://localhost:8080](http://localhost:8080)

### 5. Check Docker container

```bash
docker ps
```

### 6. Destroy the infrastructure

```bash
terraform destroy
```

## ✅ Outcome

* Learn how to provision Docker containers using Terraform.
* Practice the full Terraform workflow: `init → plan → apply → destroy`.

```

---


