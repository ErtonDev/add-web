# API test file
import psqlapi as api
from rich.console import Console
from rich.prompt import Prompt
from dotenv import load_dotenv
import rich
import os

console = Console()
load_dotenv()

try:
    HOST = os.getenv('HOST')
    USER = os.getenv('DBUSER')
    PASS = os.getenv('PASS')
    DBNAME = os.getenv('DBNAME')

    rich.inspect(HOST)
    rich.inspect(USER)
    rich.inspect(PASS)
    rich.inspect(DBNAME)

except:
    console.print_exception()

try:
    # test area
    conn = api.connect()
    rich.inspect(conn)

    table = "bot"
    param = "stock, cr, cant"
    values = "'e1', 0, 0"

    api.post(conn, table, param, values)
    # api.get(FIXME(Erton): Hay un fallo en la api)
    # api.put(FIXME(Erton): Hay un fallo en la api)

except:
    console.print_exception()
