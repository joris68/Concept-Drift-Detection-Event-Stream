from google.cloud import storage
from storage_Handler import upload_blob

if __name__ == "__main__":

     upload_blob("experiments-bucket68", 'Images/timedriftpicture.png', 'pic.png')
