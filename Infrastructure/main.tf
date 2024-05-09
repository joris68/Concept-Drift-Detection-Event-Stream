

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

# the service accounts for cloud build batch jobs
resource "google_service_account" "cloud_run_sa" {
  account_id   = "cloud-run-batch-job-sa"
  display_name = "Service Account for Cloud Run Batch Jobs"
  project      = var.project_id
}



# Docker repo for the images
resource "google_artifact_registry_repository" "my-repo" {
  location      = var.region
  repository_id = "mythesisimages"
  description   = "Repository for the experiment "
  format        = "DOCKER"
}

# 

resource "google_storage_bucket" "my_bucket" {
  name          = "experiments-bucket68"
  location      = var.region
  force_destroy = true  # Enables deleting bucket with contents in it

  storage_class = "STANDARD"
}

resource "google_storage_bucket_iam_binding" "bucket_writer" {
  bucket = google_storage_bucket.my_bucket.name
  role   = "roles/storage.objectCreator"

  members = [
    "serviceAccount:${google_service_account.cloud_run_sa.email}"
  ]
}

resource "google_cloud_run_service" "batch_job" {
  for_each = toset(["gradualexperiments", "suddenexperiments", "incrementalexperiments", "recurringexperiments", "test"])
  
  name     = "${each.key}-service"
  location = var.region
  project  = var.project_id

  template {
    spec {
      containers {
        image = "${var.region}.pkg.dev/${var.project_id}/${var.docker_repo_name}/${each.key}:latest"
      }
      service_account_name = google_service_account.cloud_run_sa.email
    }
  }

  traffic {
    percent         = 100
    latest_revision = true
  }
}

resource "google_artifact_registry_repository_iam_binding" "repo_writer" {
  location      = var.region
  repository    = google_artifact_registry_repository.my-repo.repository_id
  role          = "roles/artifactregistry.writer"

  members = [
    "serviceAccount:${google_service_account.cloud_run_sa.email}"
  ]
}





