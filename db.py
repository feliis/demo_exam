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
    conn.close()
    print(all_users)

def getUser(name):
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(f"""SELECT * FROM users WHERE name='{name}'""")
    user = cur.fetchone()
    return user

if __name__ == "__main__":
    print(getUser('Georg'))

