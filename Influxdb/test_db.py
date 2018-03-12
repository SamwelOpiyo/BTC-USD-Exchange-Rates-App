from Db import connect_db, create_db, drop_db, add_data, query_data

from influxdb.exceptions import InfluxDBClientError

import unittest


class DbTestCase(unittest.TestCase):
    def setUp(self):
        self.connect = InfluxDBInstance('test')


    def test_connect_db(self):
        self.assertEqual(
            type(self.connect.connect_db),
            "<class 'influxdb.client.InfluxDBClient'>"
        )


    def test_create_db(self):
        self.createdb = self.connect.create_db()
        self.assertRaises(InfluxDBClientError, self.connect.query_data("use test"))


    def test_drop_db(self):
        self.dropdb = self.connect.drop_db()
        self.assertRaises(InfluxDBClientError, self.connect.query_data("use test"))


    def test_add_data(self):
        self.createdb = self.connect.create_db()
        self.assertEqual(self.widget.size(), (100,150),
                         'wrong size after resize')


    def test_query_data(self):
        self.widget.resize(100,150)
        self.assertEqual(self.widget.size(), (100,150),
                         'wrong size after resize')


if __name__ == '__main__':
    unittest.main()
