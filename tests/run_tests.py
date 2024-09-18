import sqlite3
import unittest
from testcontainers.mysql import MySqlContainer

from example import DatabaseManager


class TestDatabaseManager(unittest.TestCase):
    def setUp(self):
        self.container = MySqlContainer()
        self.container.start()
        self.db = DatabaseManager(self.container.get_connection_url())

    def tearDown(self):
        self.db.close()
        self.container.stop()

    def test_insert_data(self):
        self.db.insert_data('Sample data')
        data = self.db.read_data()
        self.assertEqual(data, [(1, 'Sample data')])
            
    def test_read_data(self):
        self.db.insert_data('Sample data')
        data = self.db.read_data()
        self.assertEqual(data, [(1, 'Sample data')])


if __name__ == '__main__':
    unittest.main()
