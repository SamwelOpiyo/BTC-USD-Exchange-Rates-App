import requests
import json

import logging

logger = logging.getLogger(__name__)
"""
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler('logs/influxdb.log')
fh.setLevel(logging.DEBUG)

# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

fh.setFormatter(formatter)

# add the handlers to logger
logger.addHandler(fh)
"""

def get_url(url):
    return requests.get(url)


def get_text(request_url):
    return request_url.text


def convert_to_dict(text):
    return json.loads(text)


def web_dict(url):
    try:
        request = get_url(url)
        json_text = get_text(request)
        dict_data = convert_to_dict(json_text)
        return dict_data
    except ValueError as e:
        logger.error("No json found.")
        return False
