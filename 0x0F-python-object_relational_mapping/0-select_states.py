#!/usr/bin/python3
'''
A script that lists all nstates from the database htbn_0e_0_usa.
'''


from sys import argv
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(
            host='localhost', port=3306, user=argv[1],
            passwd=argv[2], db=argv[3])

    cur = conn.cursor()
    cur.execute('SELECT * FROM states ORDER BY id ASC')
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    conn.close()
