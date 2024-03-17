#!/usr/bin/python3
"""a script that takes an arg and displays values where name matches the arg"""

import MySQLdb
from sys import argv


def listsafe_db():
    """lists argv arguments.

    Arguments:
        argv[1]: mysql username
        argv[2]: mysql password
        argv[3]: database name
        argv[4]: state name searched
    """

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name=%s ORDER BY id", (argv[4]))

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    listsafe_db()
