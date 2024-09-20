# infrastructure/aws/outputs.tf

output "ecs_cluster_id" {
  description = "The ID of the ECS cluster"
  value       = aws_ecs_cluster.human_digital_twin_cluster.id
}

# Define other outputs as needed
