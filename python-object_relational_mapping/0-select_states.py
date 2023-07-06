#!/usr/bin/python3
""" This module will list all states from the database hbtn_0e_0_usa """
Import MySQLdb
Import Sys 

def list_states (
    username,
    password, 
    database
    ):
    
    db = MySQLdb.connect(host="localhost", post=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
    
    if __name__ == '__main__':
        import sys
        
        if len(sys.argv) != 4:
            print("Usage: python script.py <username> <password> <database>")
        else:
            username = sys.argv[1]
            password = sys.argv[2]
            database = sys.argv[3]
            list_states(username, password, database)
