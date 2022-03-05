#!/usr/bin/python3
"""
a script that lists all states with a name starting with N (upper N)
"""


def get_states(userName, passWord, dbName):
    """ Accesses database hbtn_0e_0_usa and fetch states that begin with 'N'.
    ARGS:
        userName: the username
        passWord: the password
        dbName: the name of the database to access
    """

    import MySQLdb

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=userName,
        passwd=passWord,
        db=dbName,
        charset="utf8"
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY \
                id ASC")
    query_rows = cursor.fetchall()

    for row in query_rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    """ Take in arguments and passes to get states from db """
    from sys import argv

    get_states(argv[1], argv[2], argv[3])
