#!/usr/bin/python3
"""a script that takes a state name and lists all cities of that state"""

import MySQLdb
from sys import argv


def liststatecities_db():
    """lists argv arguments

    Arguments:
        argv[1]: mysql username
        argv[2]: mysql password
        argv[3]: database name
        argv[4]: state name
    """

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cursor = db.cursor()

    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities\
                   INNER JOIN states ON cities.state_id = states.id\
                   WHERE states.name=%s ORDER BY cities.id", (argv[4],))

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    liststatecities_db()
