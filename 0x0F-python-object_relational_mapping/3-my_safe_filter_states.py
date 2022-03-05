#!/usr/bin/python3
"""
a script that takes in arguments and displays all values in the states
"""


def get_states(userName, passWord, dbName, stateName):
    """ Accesses database hbtn_0e_0_usa and displays all values in the states.
    ARGS:
        userName: the username
        passWord: the password
        dbName: the name of the database to access
        stateName: the name of the state to check
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

    cur = db.cursor()
    sqlCommand = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"
    cur.execute(sqlCommand, (stateName,))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    """ Take in arguments and passes to get states from db """
    from sys import argv

    get_states(argv[1], argv[2], argv[3], argv[4])
