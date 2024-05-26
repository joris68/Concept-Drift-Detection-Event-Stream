from google.cloud import storage

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    try:
        print(f"this is the source file name {source_file_name}")
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)
        blob.upload_from_filename(source_file_name)
        print(f"File {source_file_name} successfully uploaded to {destination_blob_name}.")
    
    except Exception as e:
        print(f"Failed to upload blob: {e}")

    finally:
        print("This is the end of the upload process.")


def download_blob(bucket_name, source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    try:
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(source_blob_name)
        blob.download_to_filename(destination_file_name)

        print(f"Blob {source_blob_name} downloaded to {destination_file_name}.")
    except Exception as e:
        print(f"Failed to download blob: {e}")



