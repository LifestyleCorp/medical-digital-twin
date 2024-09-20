# infrastructure/gcp/main.tf

provider "google" {
  project = var.project_id
  region  = var.region
}

resource "google_container_cluster" "human_digital_twin_cluster" {
  name     = "human-digital-twin-cluster"
  location = var.region

  initial_node_count = 3

  node_config {
    machine_type = "e2-medium"
  }
}

# Define services, deployments, etc.
