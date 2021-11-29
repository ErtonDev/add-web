import psycopg2
import os
from dotenv import load_dotenv

# load_dotenv will look for the environment variables
load_dotenv()

HOST = os.getenv('DBHOST')
USER = os.getenv('DBUSER')
PASS = os.getenv('PASS')
DBNAME = os.getenv('DBNAME')

#CONNECT Function
def connect():
    try:
        conn = psycopg2.connect(
            host=HOST,
            user=USER,
            password=PASS,
            dbname=DBNAME
        )
        # credentials not included in git
        return conn
    except Exception as error:
        print(f"ERROR: Failed to connect to database!\nERROR INFO: {error}\nEXCEPTION TYPE: {type(error)}\n-------------------")

#POST(Bot) Function
def post_bot(conn, stock, cant, cr):
    try:
        cur = conn.cursor()
        cur.execute(f"""INSERT INTO bot(stock, cant, cr)
        VALUES('{stock}',{cant}, {cr})""")
        conn.commit()
        cur.close()
    except Exception as error:
        conn.rollback()
        print(f"ERROR: Failed to insert data!\nERROR INFO: {error}\nEXCEPTION TYPE: {type(error)}\n-------------------")
    else:
        conn.commit()

#POST(User) Function
def post_user(conn, user_id, user_name, user_cr, user_e1, user_e2, user_e3, user_e4, user_n1, user_n2, user_lvl, user_pt, user_prestige, user_transac):
    try:
        cur = conn.cursor();
        cur.execute(f"""INSERT INTO users(user_id, user_name, user_cr, user_e1, user_e2, user_e3, user_e4, user_n1, user_n2, user_lvl, user_pt, user_prestige, user_transac)
        VALUES({user_id}, '{user_name}', {user_cr}, {user_e1}, {user_e2}, {user_e3}, {user_e4}, {user_n1}, {user_n2}, {user_lvl}, {user_pt}, '{user_prestige}', {user_transac})""")
        conn.commit()
        cur.close()
    except Exception as error:
        conn.rollback()
        print(f"ERROR: Failed to insert data!\nERROR INFO: {error}\nEXCEPTION TYPE: {type(error)}\n-------------------")
    else:
        conn.commit()

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
#name can be: "e_1", "e_2", "e_3", "e_4", "e_n1", "e_n2"
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
#name can be: "e_1", "e_2", "e_3", "e_4", "e_n1", "e_n2"
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
