import schedule
import time
import subprocess
from datetime import datetime as dt

run_NSE_premarket = "09:15"


def nse_pre_market_runner():
    print("Running NSE PRE MARKET SCAPER")
    subprocess.call('start /min "NSE PRE MARKET" python main.py', shell=True, cwd='')


# Run
schedule.every().monday.at(run_NSE_premarket).do(nse_pre_market_runner)
schedule.every().tuesday.at(run_NSE_premarket).do(nse_pre_market_runner)
schedule.every().wednesday.at(run_NSE_premarket).do(nse_pre_market_runner)
schedule.every().thursday.at(run_NSE_premarket).do(nse_pre_market_runner)
schedule.every().friday.at(run_NSE_premarket).do(nse_pre_market_runner)

while True:
    print(dt.today())
    schedule.run_pending()
    time.sleep(5)
