import logging
import csv
from logging import Handler


class CSVLogHandler(Handler):
    def __init__(self, filename, mode='a', encoding=None):
        super().__init__()
        self.filename = filename
        self.mode = mode
        self.encoding = encoding
        self.csv_file = open(self.filename, mode, newline='', encoding=self.encoding)
        self.csv_writer = csv.writer(self.csv_file)

    def emit(self, record):
        log_entry = self.format(record)
        self.csv_writer.writerow(log_entry.split(','))

    def close(self):
        self.csv_file.close()
        super().close()

    def setup_logger(self, name, log_file, level=logging.INFO):
     logger = logging.getLogger(name)
     logger.setLevel(level)

     formatter = logging.Formatter('%(message)s,%(asctime)s',datefmt='%Y-%m-%d %H:%M:%S')

     handler = CSVLogHandler(log_file)
     handler.setFormatter(formatter)

     logger.addHandler(handler)
     return logger
    

