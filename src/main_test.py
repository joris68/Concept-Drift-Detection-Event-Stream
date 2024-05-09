from google.cloud import storage

if __name__ == "__main__":

     bucket_name = "your-bucket-name"
     file_name = "example.txt"
     content = "Hello, World!"

     for i in range(0, 1000):
          print(f"Hello world the {i}th")

     storage_client = storage.Client()

     # Get the bucket.
     bucket = storage_client.bucket(bucket_name)

     # Create a new blob and upload the file's content.
     blob = bucket.blob("my-first-blob")
     blob.upload_from_string(content)     