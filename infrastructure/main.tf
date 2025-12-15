provider "google" {
  project = var.project_id
  region  = var.region
}

variable "project_id" {
  description = "The Google Cloud Project ID"
  type        = string
}

variable "region" {
  description = "The Google Cloud Region"
  type        = string
  default     = "us-central1"
}

# Placeholder for Cloud Run Service
# resource "google_cloud_run_service" "default" { ... }
