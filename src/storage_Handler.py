from google.cloud import storage

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    try:
        print(f"this is the source file name {source_file_name}")
        # Create a Cloud Storage client
        storage_client = storage.Client()
        # Get the bucket
        bucket = storage_client.bucket(bucket_name)
        # Create a new blob and upload the file's content
        blob = bucket.blob(destination_blob_name)
        blob.upload_from_file(source_file_name)
        print(f"File {source_file_name} successfully uploaded to {destination_blob_name}.")
    
    except Exception as e:
        print(f"Failed to upload blob: {e}")

    finally:
        print("This is the end of the upload process.")
