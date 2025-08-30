terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 2.20.0"
    }
  }
}

provider "docker" {}

# Pull nginx image
resource "docker_image" "nginx" {
  name         = "nginx:latest"
  keep_locally = false
}

# Run nginx container
resource "docker_container" "nginx" {
  name  = "nginx-container"
  image = docker_image.nginx.name

  ports {
    internal = 80
    external = 8081
  }
}

