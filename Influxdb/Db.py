# -*- coding: utf-8 -*-

import os

from influxdb import InfluxDBClient

import logging

# Logging Settings
logger = logging.getLogger('Influx Database')
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler('logs/influxdb.log')
fh.setLevel(logging.DEBUG)

# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

fh.setFormatter(formatter)

# add the handlers to logger
logger.addHandler(fh)

class InfluxDBInstance(object):
    # create a connection to database
    def __init__(
        self,
        dbname,
        user='root',
        password='root',
        host='localhost',
        port=8086
    ):
        self.dbname=dbname
        self.user = user
        self.password = password
        self.host=host
        self.port=port
        self.client = InfluxDBClient(
            self.host,
            self.port,
            self.user,
            self.password,
            self.dbname
        )
        logger.debug("Connection Successfully.")


    # Create database
    def create_db(self):
        self.client.create_database(self.dbname)
        logger.debug("Database created Successfully.")
        return


    # Delete Database
    def drop_db(self):
        self.client.drop_database(self.dbname)
        logger.debug("Database dropped Successfully.")
        return


    # Add data to database
    def add_data(self, data):
        self.client.write_points(data)
        logger.debug("Data added Successfully.")
        return


    # Query database
    def query_data(self, search_query):
        results = self.client.query(search_query)
        return results


def db_main(**kwargs):
    try:
        # get environment variables
        db_host = kwargs.get('INFLUXDB_HOST', os.environ["INFLUXDB_HOST"])
        db_port = kwargs.get('PORT', os.environ["PORT"])
        db_name = kwargs.get('DATABASE_NAME', os.environ["DATABASE_NAME"])

    except KeyError:
        db_host = 'localhost'
        db_port = 8086
        db_name = "default"

    # connect to influxdb
    new_connection = InfluxDBInstance(db_name, db_host, db_port)
    # Create database
    new_connection.create_db()
    logger.debug("Database " + db_name + " created.")
    return


if __name__ == '__main__':
    # execute only if run as the entry point into the program
    db_main()
