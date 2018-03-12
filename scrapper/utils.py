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
    # returns response code for a get request object made to a url
    return requests.get(url)


def get_text(request_url):
    # takes a get request object and returns the text in the url
    return request_url.text


def convert_to_dict(text):
    # converts json objects to python dictionary
    return json.loads(text)


def web_dict(url):
    """
    Takes a url
    Gets the json response
    Return a dictionary of the response
    """
    try:
        request = get_url(url)
        json_text = get_text(request)
        dict_data = convert_to_dict(json_text)
        return dict_data
    except ValueError as e:
        logger.error("No json found.")
        return False
