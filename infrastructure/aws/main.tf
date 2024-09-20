# infrastructure/aws/main.tf

provider "aws" {
  region = var.aws_region
}

resource "aws_ecs_cluster" "human_digital_twin_cluster" {
  name = "human-digital-twin-cluster"
}

resource "aws_ecs_task_definition" "backend_task" {
  family                   = "backend-task"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = "512"
  memory                   = "1024"

  container_definitions = jsonencode([
    {
      name      = "backend"
      image     = "${aws_ecr_repository.backend_repository.repository_url}:latest"
      portMappings = [
        {
          containerPort = 8000
          hostPort      = 8000
          protocol      = "tcp"
        }
      ]
      environment = [
        {
          name  = "SECRET_KEY"
          value = var.secret_key
        },
        # Add other environment variables
      ]
    }
  ])
}

# Similarly define services for frontend, nodejs_backend, databases, etc.
