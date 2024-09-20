# infrastructure/aws/variables.tf

variable "aws_region" {
  description = "AWS region"
  default     = "us-west-2"
}

variable "secret_key" {
  description = "Django secret key"
  type        = string
}

# Define other variables as needed
