import psycopg2
from psycopg2.extras import RealDictCursor

conn = psycopg2.connect(
    dbname='fitness-tracker',
    user='postgres',
    password='75689',
    host='localhost'
)


def printUsers():
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('SELECT * FROM users')
    all_users = cur.fetchall()
    cur.close()

    return all_users

def create_new_user(name, sex, role, password):
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(f"""SELECT * FROM users WHERE name='{name}'""")
    user = cur.fetchone()

    if user:
        return False
    else:
        cursor = conn.cursor()
        cursor.execute(f"""INSERT INTO users (name, sex, role, password) VALUES ('{name}', '{sex}', '{role}', '{password}') """)
        conn.commit()
        cursor.close()

        return True

def remove_user(id):
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(f"""DELETE FROM users where id='{id}'""")
    conn.commit()
    cur.close()


def getUser(name):
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(f"""SELECT * FROM users WHERE name='{name}'""")
    user = cur.fetchone()
    cur.close()
    return user

if __name__ == "__main__":
   # print(getUser('Georg'))
    print(create_new_user('sfaf', True, 'bigBoy', 'ddddd'))

