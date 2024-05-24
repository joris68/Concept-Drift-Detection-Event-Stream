from google.cloud import storage
from storage_Handler import upload_blob
import csv

if __name__ == "__main__":

     try:
          file = open("./New/sudden_100.csv")
          writer = csv.writer(file)
          print("we could open the file successfully")
     except Exception as e:
          print(e)
     finally:
          file.close()
          

     #upload_blob("experiments-bucket68", './New/sudden_100.csv', 'pic.csv')
