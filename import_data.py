# TODO: Complete this with unit tests

import os
import sys
import re
import csv
from psycopg2 import connect, DatabaseError, OperationalError, errorcodes, errors

from sample_app.credentials import db_details

import import_data_unittests

table_name_countries = "sample_data_countries"
table_name_incidents = "sample_data_incidents"

# Use regex to verify rows as a first pass
# with more detailed logic we may need to iterate through all the elements too but this works for now
# TODO: handle header out of order .csv files by casting to a dict
def verify_row(row):
    try:
        if (True): # Replace this with row type for multiple allowable row formats
            return re.match("^.*$", row)
        elif (True):
            return re.match("^.*$", row)
        else:
            raise Exception("Unhandled row type")
    except Exception as e:
        print(e)
        sys.exit()

# Check that there the file is consistent
def verify_file(csv):
    try:
        for row in csv:
            if (False):
                raise Exception("File invalid")
            else:
                continue
        return True
    except Exception as e:
        print(e)
        sys.exit()

# Create a SQL insert command from csv row
def generate_script(rows):
    try:
        return ""
    except Exception as e:
        print(e)
        sys.exit()

# Run queries
def execute_script(cursor, command):
    try:
        cursor.execute(command)
    except OperationalError as e:
        print("Command skipped: ", e)

# Check that an argument is passed in
try: 
    assert len(sys.argv) > 1 and len(sys.argv) < 4, "Invalid number of arguments. Usage: python import_data.py <<path_to_data_file>> <<dev/test (optional)>>"
    if (len(sys.argv) == 3):
        env = sys.argv[2]
        assert sys.argv[2] in ['dev', 'test'], "Invalid dev/test argument. Usage: python import_data.py <<path_to_data_file>> <<dev/test (optional)>>"
    else:
        env = 'dev'
except AssertionError as e:
    print(e)
    sys.exit()

# Check that the argument leads to a valid file
try:
    file_path = os.path.join(sys.argv[1])
    if not (os.path.exists(file_path) and os.path.isfile(file_path)):
        raise FileNotFoundError("Invalid path to file. Check that the file to be imported exists")
except FileNotFoundError as e:
    print(e)
    sys.exit()

# Load and parse the file
try:
    raw_data = []
    with open(file_path, 'r') as raw_file:
        for row in raw_file:
            if not (verify_row(row)):
                raise Exception("Invalid row found: %s" % row)
            else:
                raw_data.append(row.strip())
        if not (verify_file(raw_data)):
            raise Exception("Invalid file format found")
except Exception as e:
    print (e)
    sys.exit()

# Create postgres connection
# TODO: Externalise this into its own class with test cases!
db_connection = None
try:
    if (env == 'dev'):
        # Connect to the db server
        db_connection = connect(
            host = db_details["db_host"],
            port = db_details["db_port"],
            database = db_details[f"{env}_db_name"],
            user = db_details["sa_username"],
            password = db_details["sa_password"]
        )
        
        # Create a session cursor
        db_cursor = db_connection.cursor()

        statement = generate_script(raw_data)

        # Execute statements
        if (len(statement) > 1):
            execute_script(db_cursor, statement)

        print(f"Row insertion complete")
        
        # close the communication with the PostgreSQL
        db_cursor.close()
    elif (env == 'test'):
        import_data_unittests.run_tests(data=raw_data)
except (Exception, DatabaseError) as error:
    err_type, err_obj, traceback = sys.exc_info()
    line_num = traceback.tb_lineno
    print(f"{str(error)}")
    print(f"Type {str(err_type)} at line {str(line_num)}")
finally:
    if db_connection is not None:
        db_connection.close()
        print('Database connection closed.')
