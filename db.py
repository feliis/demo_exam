import psycopg2
from psycopg2._psycopg import cursor
from psycopg2.extras import RealDictCursor

conn = psycopg2.connect(
    dbname='fitness-tracker',
    user='postgres',
    password='75689',
    host='localhost'
)


def printUsers():
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(f"""SELECT users.id, users.name, users.password, users.birthday, users.sex, roles.name as role 
                        FROM users 
                        INNER JOIN roles
                        ON users.role = roles.id""")
    all_users = cur.fetchall()
    cur.close()

    return all_users

def get_info_user(id):
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(f"""SELECT users.id, users.name, users.password, users.birthday, users.sex, roles.name as role 
                        FROM users 
                        INNER JOIN roles
                        ON users.role = roles.id
                        WHERE users.id='{id}'""")
    user = cur.fetchone()
    cur.close()
    return user

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

def update_user(id, name, sex, role, password):
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(f"""UPDATE users
                    SET name='{name}', sex='{sex}', role='{role}', password='{password}'
                    WHERE id='{id}'""")
    conn.commit()
    cursor.close()

def get_roles():
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(f"""SELECT * FROM roles""")
    all_roles = cur.fetchall()
    cur.close()
    return all_roles

def getUser(name):
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(f"""SELECT users.id, users.name, users.password, users.birthday, users.sex, roles.name as role 
                        FROM users 
                        INNER JOIN roles
                        ON users.role = roles.id
                        WHERE users.name='{name}'""")
    user = cur.fetchone()
    cur.close()
    return user

if __name__ == "__main__":
   # print(getUser('Georg'))
    print(create_new_user('sfaf', True, 'bigBoy', 'ddddd'))

