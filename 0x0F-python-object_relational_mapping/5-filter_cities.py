#!/usr/bin/python3
'''
a script that takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa.
'''
import MySQLdb
from sys import argv

if __name__ == "__main__":
    cont = 0
    conn = MySQLdb.connect(
            host="localhost", port=3306, user=argv[1],
            passwd=argv[2], db=argv[3], charset="utf8")
    cursor = conn.cursor()
    cursor.execute("""SELECT cities.id, cities.name, states.name
    FROM cities
    LEFT JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC""")
    qrows = cursor.fetchall()
    for row in qrows:
        if row[2] == argv[4]:
            if cont > 0:
                print(", ", end="")
            print(row[1], end="")
            cont = cont + 1
    print()
    cursor.close()
    conn.close()
