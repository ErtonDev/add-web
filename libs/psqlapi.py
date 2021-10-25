import psycopg2

#CONNECT Function
def connect():
    print("Connecting to database . . . ")
    try:
        conn = psycopg2.connect(host="ec2-54-73-68-39.eu-west-1.compute.amazonaws.com", user="zinavvopoesljt",
                    password="e9acadc681b670392c65be283556f2b67f34875f6fbbc56d4055114f4f39dff9", dbname="d2qnnn465f5n23")
        print("CONNECTED!")
        return conn
    except Exception as error:
        print(f"ERROR: Failed to connect to database!\nERROR INFO: {error}\nEXCEPTION TYPE: {type(error)}")

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

#GET Function
def get(conn, table, param):
    try:
        cur = conn.cursor();
        cur.execute(f"""SELECT {param} FROM {table} ORDER BY user_id""")
        result = cur.fetchall()
        conn.commit()
        cur.close()
        return result
    except Exception as error:
        print(f"ERROR: Failed to get data!\nERROR INFO: {error}\nEXCEPTION TYPE: {type(error)}\n-------------------")

#PUT Function
def put(conn, table, param):
    try:
        cur = conn.cursor();
        cur.execute(f"""UPDATE {param} FROM {table} ORDER BY user_id""")
        conn.commit()
        cur.close()
    except Exception as error:
        print(f"ERROR: Failed to put data!\nERROR INFO: {error}\nEXCEPTION TYPE: {type(error)}\n-------------------")
conn = connect()

