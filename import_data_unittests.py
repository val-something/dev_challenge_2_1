# TODO: Complete this

import os
import sys
import re
import unittest
from psycopg2 import connect, DatabaseError, OperationalError, errorcodes, errors
from sample_app.credentials import db_details

# Class to test Postgres connection
class TestAdminMethods(unittest.TestCase):
    def setUp(self):
        pass

# Class to test Postgres CRUD
class TestDataMethods(unittest.TestCase):
    def setUp(self):
        pass

# Kickoff functions
def run_tests(data=None):
    unittest.main(data)

if __name__ == '__main__':
    run_tests()
