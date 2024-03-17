#!/usr/bin/python3
"""a script that lists all cities from database hbtn_0e_4_usa"""

import MySQLdb
from sys import argv


def listcities_db():
    """lists argv arguments

    Arguments:
        argv[1]: mysql username
        argv[2]: mysql password
        argv[3]: database name
    """

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cursor = db.cursor()

    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities\
                   INNER JOIN states ON cities.state_id = states.id\
                   ORDER BY cities.id")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    listcities_db()
