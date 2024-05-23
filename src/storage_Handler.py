from google.cloud import storage


def upload_blob(bucket_name, source_file_name, destination_blob_name):
     try:
    
          storage_client = storage.Client()
          bucket =storage_client.bucket(bucket_name)
          blob = bucket.blob(destination_blob_name)
          blob.upload_from_filename(source_file_name)
     
     except:
       print("upload ob blob did not work!")

     finally:
       print("This is the finally Script")

   

