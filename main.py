from search_engine import filteredData
from datetime import datetime, timedelta
import time
import socket

delta = timedelta(hours=12)


if __name__ == "__main__":
    filteredData()
    time.sleep(60)
    while True:
        print("Server is running on", socket.gethostbyname(socket.gethostname()), time.ctime())
        time.sleep(2)   
        if datetime.now().hour == timedelta and datetime.now().minute == 0:
            filteredData()
            time.sleep(60)
            
        
        


        
