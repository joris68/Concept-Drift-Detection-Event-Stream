from google.cloud import storage
from storage_Handler import upload_blob

if __name__ == "__main__":

     upload_blob("experiments-bucket68", 'staticAnalysis/ExecutionTimes/gradual.csv', 'gradual.csv')