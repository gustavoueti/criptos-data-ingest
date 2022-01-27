# from email.policy import default
import schedule
import time
import datetime

from writers import DataWriter
from ingestors import DaySummaryIngestor


if __name__ == "__main__":
    day_summary_ingestor = DaySummaryIngestor(
        writer=DataWriter, coins=["BTC", "ETH", "LTC", "BCH"], 
        default_start_date=datetime.date(2021, 6, 1)
    )



def job():
    day_summary_ingestor.ingest()

schedule.every(1).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(0.5)