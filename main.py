# NSE Scrapper

import pandas as pd
from datetime import datetime as dt
from timeit import default_timer as timer
import requests
import threading
import time
import schedule

# file path
path = "/Users/puneetrajput/Documents/Finesse/NSE_preopen/data/"
# at_hour = 9
# at_minute = 15
# at_second = 1
#
# while_loop_run_till = 15

# attempts = 10


class NseScraper:

    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 ('
                                      'KHTML, like Gecko) Chrome/98.0.4758.102 Mobile Safari/537.36'}

        self.session = requests.Session()
        self.session.get("http://nseindia.com", headers=self.headers)

    def pre_market_data(self, which_data):
        start_time = timer()
        file_date = dt.now().strftime("%d%m%Y")
        pre_market_key = {"NIFTY 50": "NIFTY", "NIFTY BANK": "BANKNIFTY", "Emerge": "SME", "Securities in F&O": "FO",
                          "Others": "OTHERS", "All": "ALL"}
        # key = "NIFTY 50"
        data = self.session.get(f"https://www.nseindia.com/api/market-data-pre-open?key={pre_market_key[which_data]}",
                                headers=self.headers).json()["data"]
        new_data = []
        for i in data:
            new_data.append(i["metadata"])
        df = pd.DataFrame(new_data)
        if path == "":
            df.to_csv(which_data + "_" + file_date + ".csv", index=False)
        else:
            df.to_csv(path + which_data + "_" + file_date + ".csv", index=False)
        end_time = timer()
        print("Time taken in getting " + which_data + ": ", end_time - start_time)


nse = NseScraper()


# if int(dt.now().hour) == int(at_hour) and int(dt.now().minute) == int(at_minute) and int(dt.now().second) == int(
# at_second):

key_list = ['NIFTY 50', 'NIFTY BANK', 'Emerge', 'Securities in F&O', 'Others', 'All']
thread_list = []
for key in key_list:
    threads = threading.Thread(target=nse.pre_market_data, args=(key,))
    threads.start()
    thread_list.append(threads)

for thread in thread_list:
    thread.join()

