import sqlite3
from sqlite3 import Error


def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
    except Error as e:
        print(e)

    return conn


def create_table(conn, sentence):
    try:
        c = conn.cursor()
        c.execute(sentence)
        conn.commit()
    except Error as e:
        print(e)


def insert_person(conn, cur, person):
    cur.execute("insert into person (name,lastname,age,height) values (?,?,?,?)", person)
    conn.commit()
    print("Person Created")


def delete_person(conn, cur, id):
    cur.execute("delete from person where id=?", id)
    conn.commit()
    print("Person Deleted")


def update_person(conn, cur, person):
    cur.execute("update person set name=?,lastname=?,age=?,height=? where id=?", person)
    conn.commit()
    print("Person Updated")


def list_person(cur):
    for row in cur.execute("SELECT * FROM person"):
        print(row)


def insert_school(conn, cur, school):
    cur.execute("insert into school (name,address) values (?,?)", school)
    conn.commit()
    print("School Created")


def delete_school(conn, cur, id):
    cur.execute("delete from school where id=?", id)
    conn.commit()
    print("School Deleted")


def update_school(conn, cur, school):
    cur.execute("update school set name=?,address=? where id=?", school)
    conn.commit()
    print("School Updated")


def list_school(cur):
    for row in cur.execute("SELECT * FROM school"):
        print(row)


if __name__ == '__main__':
    table1 = """ CREATE TABLE IF NOT EXISTS person (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        lastname text NOT NULL,
                                        age integer,
                                        height integer
                                    ); """
    table2 = """ CREATE TABLE IF NOT EXISTS school (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        address text NOT NULL,
                                    ); """

    conn = create_connection('clase7')
    cur = conn.cursor()

    create_table(conn, table1)
    create_table(conn, table2)

    conn.close()
