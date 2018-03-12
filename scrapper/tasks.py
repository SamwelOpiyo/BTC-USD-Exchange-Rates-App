from celery.task.schedules import crontab
from celery.decorators import task
from scrapper.utils import web_dict
from celery.utils.log import get_task_logger
from datetime import datetime

from Influxdb.Db import InfluxDBInstance
from django.conf import settings

logger = get_task_logger(__name__)

# A periodic task that will run every 10 seconds (the symbol "*" means every)
# @periodic_task(run_every=(crontab())) # minute="*/10"
@task
def scraper_example():
    """
    Celery task that fetches bitcoin exchange rates from blockchain.info/ticker
    and saves the data to Influxdb Database
    """
    logger.info("Start task")
    get_data = web_dict("https://blockchain.info/ticker")
    if type(get_data) == dict:
        logger.info("Task finished: result = %s" % str(get_data))
        new_db_instance = InfluxDBInstance(
            settings.INFLUXDB_DATABASE,
            settings.INFLUXDB_USER,
            settings.INFLUXDB_PASSWORD,
            settings.INFLUXDB_HOST,
            settings.INFLUXDB_PORT
        )
        new_db_instance.create_db()
        for each in get_data:
            new_db_instance.add_data(
                data = [
                    {
                        "measurement": each,
                        "tags": {
                            "Description": "Bitcoin Exchange Rates for " + each,
                            "Source": "https://blockchain.info/ticker"
                         },
                         "time": str(datetime.now()),
                         "fields": get_data[each]
                    }
                ]
        )
    else:
        logger.info("Could not retrieve data!!")
    return get_data["USD"]
