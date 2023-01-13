# MySQL: pymysql, pysql-connector-python, mysql-client
# NOTE: Create db from path witch invoke the interpreter in os console

import sqlite3


name = 'Santiago'
age = '42'
# Step 1: connect to db
conn = sqlite3.connect("my_example_db.db")

# Step 2: create cursor
# This object allow make requests
cursor = conn.cursor()

try:
    # Step 3: make request
    cursor.execute('CREATE TABLE therapists (name TEXT, age NUMBER, degree TEXT)')
except sqlite3.OperationalError:
    pass

# Strings format types (with f):
cursor.execute(f"INSERT INTO therapists VALUES ('{name}', {age}, 'Teacher')")

# Step 4: commit changes
conn.commit()
    
cursor.execute("SELECT * FROM therapists")
# Step 5: get all results
list_of_therapists = cursor.fetchall()

# for with unpacked method
for name, age, degree in list_of_therapists:
    print(name)

# Step 6: close connection to db
conn.close()


