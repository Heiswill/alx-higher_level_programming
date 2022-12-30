#!/usr/bin/python3
'''
lists all states with starting name N
from the the database.
'''

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(
            host="localhost", port=3306, user=argv[1],
            passwd=argv[2], db=argv[3])
    cursor = conn.cursor()
    cursor.execute(
            "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")
    db = cursor.fetchall()
    for i in db:
        print(i)
    
    cursor.close()
    conn.close()
