

terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "4.51.0"
    }
  }
}


provider "google" {
  project     = var.project_id
  region      = var.region
}


resource "google_cloudbuild_trigger" "github_trigger" {
  provider = google
  name = "github-trigger"
  description = "Trigger for GitHub repo changes"

  github {
    owner = "joris68"
    name  = "Concept-Drift-Detection-Event-Stream"
    push {
      branch = "^experiments$"  // Trigger on changes to the main branch
    }
  }

  filename = "cloudbuild.yaml"  // The name of your Cloud Build config file
}


# Docker repo for the images
resource "google_artifact_registry_repository" "my-repo" {
  location      = "europe-west1"
  repository_id = "mythesisimages"
  description   = "Repository for the experiment "
  format        = "DOCKER"
}