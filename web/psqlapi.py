import psycopg2

#CONNECT Function
def connect():
    print(". . . Connecting to database . . . ")
    try:
        conn = psycopg2.connect(host="ec2-54-73-68-39.eu-west-1.compute.amazonaws.com", user="zinavvopoesljt",
                    password="e9acadc681b670392c65be283556f2b67f34875f6fbbc56d4055114f4f39dff9", dbname="d2qnnn465f5n23")
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

#GET Function
def get(conn, id, table, param):
    try:
        cur = conn.cursor();
        cur.execute(f"""SELECT {param} FROM {table} WHERE user_id = {id}""")
        result = cur.fetchall()
        conn.commit()
        cur.close()
        #Result is a list of tuples, so to get the string we have to access both with index 0
        return result[0][0]
    except Exception as error:
        print(f"ERROR: Failed to get data!\nERROR INFO: {error}\nEXCEPTION TYPE: {type(error)}\n-------------------")

#PUT Function
def put(conn, id, table, param, values):
    try:
        cur = conn.cursor();
        cur.execute(f"""UPDATE {table} SET {param} = {values} WHERE user_id = {id}""")
        conn.commit()
        cur.close()
    except Exception as error:
        print(f"ERROR: Failed to put data!\nERROR INFO: {error}\nEXCEPTION TYPE: {type(error)}\n-------------------")


conn = connect()

result = get(conn, "124", "tab", "user_name")
print(result)