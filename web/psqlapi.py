import psycopg2
import os
from dotenv import load_dotenv

# load_dotenv will look for the environment variables
load_dotenv()

HOST = os.getenv('HOST')
USER = os.getenv('DBUSER')
PASS = os.getenv('PASS')
DBNAME = os.getenv('DBNAME')

#CONNECT Function
def connect():
    print(". . . Connecting to database . . . ")
    try:
        conn = psycopg2.connect(
            host=HOST,
            user=USER,
            password=PASS,
            dbname=DBNAME
        )
        # credentials not included in git
        print("CONNECTED!")
        return conn
    except Exception as error:
        print(f"ERROR: Failed to connect to database!\nERROR INFO: {error}\nEXCEPTION TYPE: {type(error)}\n-------------------")

#POST Function
def post(conn, table, param, values):
    try:
        cur = conn.cursor();
        cur.execute(f"""INSERT INTO {table}({param})
        VALUES({values})""")
        conn.commit()
        cur.close()
    except Exception as error:
        print(f"ERROR: Failed to insert data!\nERROR INFO: {error}\nEXCEPTION TYPE: {type(error)}\n-------------------")

#GET(User) Function
def get_user(conn, id, param):
    try:
        cur = conn.cursor();
        cur.execute(f"""SELECT {param} FROM users WHERE user_id = {id}""")
        result = cur.fetchall()
        conn.commit()
        cur.close()
        #Result is a list of tuples, so to get the string we have to access both with index 0
        return result[0][0]
    except Exception as error:
        print(f"ERROR: Failed to get data!\nERROR INFO: {error}\nEXCEPTION TYPE: {type(error)}\n-------------------")

#GET(Bot) Function
#name can be: "e-1", "e-2", "e-3", "e-4", "en-1", "en-2"
def get_bot(conn, name, param):
    try:
        cur = conn.cursor();
        cur.execute(f"""SELECT {param} FROM bot WHERE stock = {name}""")
        result = cur.fetchall()
        conn.commit()
        cur.close()
        #Result is a list of tuples, so to get the string we have to access both with index 0
        return result[0][0]
    except Exception as error:
        print(f"ERROR: Failed to get data!\nERROR INFO: {error}\nEXCEPTION TYPE: {type(error)}\n-------------------")

#PUT(User) Function
def put_user(conn, id, param, values):
    try:
        cur = conn.cursor();
        cur.execute(f"""UPDATE users SET {param} = {values} WHERE user_id = {id}""")
        conn.commit()
        cur.close()
    except Exception as error:
        print(f"ERROR: Failed to put data!\nERROR INFO: {error}\nEXCEPTION TYPE: {type(error)}\n-------------------")

#PUT(Bot) Function
#name can be: "e-1", "e-2", "e-3", "e-4", "en-1", "en-2"
def put_bot(conn, name, param, values):
    try:
        cur = conn.cursor();
        cur.execute(f"""UPDATE bot SET {param} = {values} WHERE stock = {name}""")
        result = cur.fetchall()
        conn.commit()
        cur.close()
        #Result is a list of tuples, so to get the string we have to access both with index 0
        return result[0][0]
    except Exception as error:
        print(f"ERROR: Failed to get data!\nERROR INFO: {error}\nEXCEPTION TYPE: {type(error)}\n-------------------")