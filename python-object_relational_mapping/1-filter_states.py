#!/usr/bin/python3
"""A script that lists all states with a name
starting with N"""
import MySQLdb
import sys


def list_states(mysql username, mysql password, database name):
    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql username,
        passwd=mysql password,
        db=database name)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the query to retrieve all states
    cursor.execute("SELECT * FROM states WHERE 'N%' ORDER BY id ASC")

    # Fetch all the rows from the query result
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()


# Provide the MySQL username, password,
# and database name as command-line arguments
if __name__ == '__main__':
    import sys

    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
    else:
        MySQLdb username = sys.argv[1]
        MySQLdb password = sys.argv[2]
        database name = sys.argv[3]
        list_states(username, password, database)
