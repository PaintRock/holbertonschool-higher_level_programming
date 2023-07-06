#!/usr/bin/python3
"""A script that lists all states with a name starting with N"""
import MySQLdb
import sys


def filter_states(username, password, database, state_name):
    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database
                         )

    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Execute the query to retrieve states starting with N (upper N)
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY\
                 '{}' ORDER BY id".format(sys.argv[4]))

    # Fetch all the rows from the query result
    rows = cur.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()


if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Usage: python script.py <username> <password> <database> <state_name>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        state_name = sys.argv[4]
        filter_states(username, password, database, state_name)
