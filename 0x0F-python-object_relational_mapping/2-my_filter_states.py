#!/usr/bin/python3
'''
A script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
'''

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(
            host="localhost", port=3306, user=argv[1],
            passwd=argv[2], db=argv[3])
    cursor = conn.cursor()
    cursor.execute(
            "SELECT * FROM states WHERE name LIKE"
            " '{:s}' ORDER BY id ASC".format(argv[4]))
    db = cursor.fetchall()
    for i in db:
        if i[1] == argv[4]:
            print(i)

    cursor.close()
    conn.close()
