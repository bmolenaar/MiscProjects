import pandas as pd
from datetime import datetime
from datetime import timedelta
import requests
import time
import psutil
import speedtest
import socket

##class for data_generation


def get_specs():
    st = speedtest.Speedtest()
    date = datetime.today().strftime("%Y-%m-%d") 
    time = datetime.now().isoformat()
    cpuUsage = psutil.cpu_percent()
    ramUsage = psutil.virtual_memory().percent
    #ping = st.ping()
    downloadSpeed = st.download()
    uploadSpeed = st.upload()
    hostname = socket.gethostname()

    
    return[ date, time, cpuUsage, ramUsage, downloadSpeed, uploadSpeed, hostname]

if __name__ == '__main__':

    REST_API_URL = 'https://api.powerbi.com/beta/8ce3ccc6-8fa2-409b-be83-3d11ab838c1b/datasets/b2fc6ea5-663a-4e15-8bf8-b5ac330cd8ac/rows?key=dGepKe3jwCZ4MJ2BH6GVIk%2BYLRvOxtUs9vmo6SYurugWDATDbfI6gobtPrYQgJ%2BSO5a8bGUkKgBQFpeg7o7Zmg%3D%3D'

    while True:
        data_raw = []
        for i in range(1):
            row = get_specs()
            data_raw.append(row)
            print("Raw data - ", data_raw)

        # set the header record
        HEADER = ["date", "time", "cpuUsage", "ramUsage", "downloadSpeed", "uploadSpeed", "hostname"]

        data_df = pd.DataFrame(data_raw, columns=HEADER)
        data_json = bytes(data_df.to_json(orient='records'), encoding='utf-8')
        print("JSON dataset", data_json)

        # Post the data on the Power BI API
        req = requests.post(REST_API_URL, data_json)

        print("Data posted in Power BI API")
        time.sleep(0.2)