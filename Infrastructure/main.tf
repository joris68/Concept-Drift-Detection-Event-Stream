

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


#resource "google_cloudbuild_trigger" "github_trigger" {
 ##    provider = google
  #   name = "github-trigger"
 #    description = "Trigger for GitHub repo changes"

 # github {
 #   owner = "joris68"
 #   name  = "Concept-Drift-Detection-Event-Stream"
#    push {
#      branch = "^experiments$"  // Trigger on changes to the main branch
#    }
#  }

##  filename = "cloudbuild.yaml"  // The name of your Cloud Build config file
#}





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

resource "google_storage_bucket" "my_data_bucket" {
  name          = "experiments-data-bucket68"
  location      = var.region
  force_destroy = true  # Enables deleting bucket with contents in it

  storage_class = "STANDARD"
}

# the service accounts for cloud build batch jobs
resource "google_service_account" "cloud_run_sa" {
  account_id   = "cloud-run-batch-job-sa"
  display_name = "Service Account for Cloud Run Batch Jobs"
  project      = var.project_id
}

#resource "google_storage_bucket_iam_member" "bucket_writer" {#
 # bucket = google_storage_bucket.my_bucket.name
 # role   = "roles/storage.objectCreator"

 # member = "serviceAccount:${google_service_account.cloud_run_sa.email}"
  
#}

resource "google_cloud_run_v2_job" "test_experiments" {
  name     = "test-job"
  location = var.region

  template {
    template {
      timeout = "82500s"
      containers {
        image = "${var.region}-docker.pkg.dev/${var.project_id}/${var.docker_repo_name}/test:latest"
        resources {
          limits = {
            cpu    = "1"
            memory = "512Mi"
          }
        }
      }
      service_account = google_service_account.cloud_run_sa.email
    }
  }
}

resource "google_cloud_run_v2_job" "sudden_experiments" {
  name     = "sudden-job"
  location = var.region

  template {
    template {
      timeout = "82500s"
      containers {
        image = "${var.region}-docker.pkg.dev/${var.project_id}/${var.docker_repo_name}/suddenexperiments:latest"
        resources {
          limits = {
            cpu    = "1"
            memory = "512Mi"
          }
        }
      }
      service_account = google_service_account.cloud_run_sa.email
    }
  }
}
resource "google_cloud_run_v2_job" "recurring_experiments" {
  name     = "recurring-job"
  location = var.region

  template {
    template {
      timeout = "82500s"
      containers {
        image = "${var.region}-docker.pkg.dev/${var.project_id}/${var.docker_repo_name}/recurringexperiments:latest"
        resources {
          limits = {
            cpu    = "1"
            memory = "512Mi"
          }
        }
      }
      service_account = google_service_account.cloud_run_sa.email
    }
  }
}

resource "google_cloud_run_v2_job" "gradual_experiments" {
  name     = "gradual-job"
  location = var.region

  template {
    template {
      timeout = "82500s"
      containers {
        image = "${var.region}-docker.pkg.dev/${var.project_id}/${var.docker_repo_name}/gradualexperiments:latest"
        resources {
          limits = {
            cpu    = "1"
            memory = "512Mi"
          }
        }
      }
      service_account = google_service_account.cloud_run_sa.email
    }
  }
}

resource "google_cloud_run_v2_job" "incremental_experiments" {
  name     = "incremental-job"
  location = var.region

  template {
    template {
      timeout = "82500s"
      containers {
        image = "${var.region}-docker.pkg.dev/${var.project_id}/${var.docker_repo_name}/incrementalexperiments:latest"
        resources {
          limits = {
            cpu    = "1"
            memory = "512Mi"
          }
        }
      }
      service_account = google_service_account.cloud_run_sa.email
    }
  }
}
###################################################################
# Jobs for real world Data

resource "google_cloud_run_v2_job" "traffic_job" {
  name     = "traffic-job"
  location = var.region

  template {
    template {
      timeout = "82500s"
      containers {
        image = "${var.region}-docker.pkg.dev/${var.project_id}/${var.docker_repo_name}/traffic:latest"
        resources {
          limits = {
            cpu    = "2"
            memory = "4096Mi"
          }
        }
      }
      service_account = google_service_account.cloud_run_sa.email
    }
  }
}

resource "google_cloud_run_v2_job" "hospital_job" {
  name     = "hospital-job"
  location = var.region

  template {
    template {
      timeout = "82500s"
      containers {
        image = "${var.region}-docker.pkg.dev/${var.project_id}/${var.docker_repo_name}/hospital:latest"
        resources {
          limits = {
            cpu    = "2"
            memory = "4096Mi"
          }
        }
      }
      service_account = google_service_account.cloud_run_sa.email
    }
  }
}

resource "google_cloud_run_v2_job" "challenge_job" {
  name     = "challenge-job"
  location = var.region

  template {
    template {
      timeout = "82500s"
      containers {
        image = "${var.region}-docker.pkg.dev/${var.project_id}/${var.docker_repo_name}/challenge:latest"
        resources {
          limits = {
            cpu    = "2"
            memory = "4096Mi"
          }
        }
      }
      service_account = google_service_account.cloud_run_sa.email
    }
  }
}

resource "google_storage_bucket_iam_binding" "new_bucket_writer" {
  bucket = google_storage_bucket.my_bucket.name
  role   = "roles/storage.objectCreator"

  members = ["serviceAccount:${google_service_account.cloud_run_sa.email}"]
}

resource "google_storage_bucket_iam_binding" "new_bucket_data_writer" {
  bucket = google_storage_bucket.my_data_bucket.name
  role   = "roles/storage.objectCreator"

  members = ["serviceAccount:${google_service_account.cloud_run_sa.email}"]
}
resource "google_storage_bucket_iam_binding" "new_bucket_data_getter" {
  bucket = google_storage_bucket.my_data_bucket.name
  role   = "roles/storage.objectViewer"
  members = ["serviceAccount:${google_service_account.cloud_run_sa.email}"]
}

resource "google_artifact_registry_repository_iam_binding" "repo_writer" {
  location      = var.region
  repository    = google_artifact_registry_repository.my-repo.repository_id
  role          = "roles/artifactregistry.writer"

  members = [
    "serviceAccount:${google_service_account.cloud_run_sa.email}"
  ]
}






