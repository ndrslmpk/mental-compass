import psycopg2
import json as JSON

json_users_path = './data/users.json'
conn = psycopg2.connect(database="mentalcompass", user="postgres", password="postgres")

# allows to perform database operations
cursor = conn.cursor()

# drop any existing todos table
# CASCADE needs to be used to DROP also the hierarchically dpeending tables, e.g. lectures
cursor.execute("""
  DROP TABLE users;
  DROP TABLE emotions;
  DROP TABLE courses CASCADE;
  DROP TABLE lectures;
""")

# (re)create the todos table
# (note: triple quotes allow multiline text in python)
cursor.execute("""
  CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    nickname VARCHAR NOT NULL,
    email VARCHAR NOT NULL
  );

  CREATE TABLE emotions (
    id serial PRIMARY KEY,
    date TIMESTAMP,
    rating SMALLINT NOT NULL CHECK (rating > 0),
    remarks TEXT,
    type VARCHAR(255)
  );

  CREATE TABLE courses (
    id serial PRIMARY KEY,
    name VARCHAR NOT NULL
  );

  CREATE TABLE lectures (
    id serial PRIMARY KEY,
    CONSTRAINT course_id 
      FOREIGN KEY (id) 
        REFERENCES courses(id)
  );
""")

# cur.execute("""
#   INSERT INTO users (id, nickname, email) VALUES (1, 'Dennis', 'dennis@web.de');
# """)

# cur.execute("""
#   INSERT INTO users (id, nickname, email) VALUES (%s, %s);
# """, (2, 'Andi', 'andi@web.de')
# )

SQL = 'INSERT INTO users (id, nickname, email) VALUES (%(id)s, %(nickname)s, %(email)s);'
SQL1 = 'INSERT INTO users (nickname, email) VALUES (%(nickname)s, %(email)s);'

with open (json_users_path, 'r') as j:
  users = JSON.loads(j.read())
  print("NEW JSON ENTRY")
  print(users)
  print(type(users))

for u in users:
  # _temp = JSON.loads(u)
  # print(_temp)
  data = ""
  print(u)
  print(type(u))
  print(u['id'])
  print(type(u['id']))
  print(u['nickname'])
  print(type(u['nickname']))
  print(u['email'])
  print(type(u['email']))
  print("VARIABLES")
  u_id = int(u['id'])
  u_nickname = str(u['nickname'])
  u_email = str(u['email'])
  # data = "{" + u_id+ ", " + u_nickname  + ", " + u['email'] + "}"   
  _temp = {
    "id": u_id,
    "nickname": u_nickname,
    "email": u_email
  }
  _jsondata = JSON.dumps(_temp)
  print("### _jsondata")
  print(_jsondata)
  print("u")
  print(u)
  print(type(u))
  # cur.execute(SQL, _jsondata)
  # cur.execute(SQL, u)
  cursor.execute(SQL1, u)

cursor.execute('SELECT * FROM users;')
result = cursor.fetchall();
print("RESULT")
print(result)

# commit, so it does the executions on the db and persists in the db
conn.commit()

conn.close()
cursor.close()