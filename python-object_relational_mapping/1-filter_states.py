#!/usr/bin/python3
"""A script that lists all states with a name starting with N"""
import MySQLdb
import sys


def list_states(username, password, database):
    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database
                         )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the query to retrieve states starting with N (upper N)
    query = "SELECT * FROM states ORDER BY ASC"
    
    cursor.execute(query)
    for elemets in cursor:
    if elemets[1].startswith("N"):
            print(elemets)

    # Fetch all the rows from the query result
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        list_states(username, password, database)
    