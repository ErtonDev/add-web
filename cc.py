import web.psqlapi

import rich
from rich import print
from rich.traceback import install
from rich.console import Console
from rich.table import Table
from rich.markdown import Markdown
from rich.layout import Layout

console = Console()
install(show_locals=True)

'''
table = Table(title="----- Values -----")


def getvar():
	table.add_row("CANT e1", "250", "bot/ cant | e1")

def update():
	with open("ccdata/mkdn.md") as md:
		markdown = Markdown(md.read())

	table.add_column("Variable", justify="left", style="yellow", no_wrap=True)
	table.add_column("Value", style="cyan")
	table.add_column("From", justify="right", style="cyan")

	getvar()
	console.print(markdown)
	console.print(table)


update()
input = input("Press ENTER key to quit: ")
'''

def make_layout() -> Layout:
	# Define the layout
	layout = Layout(name="Control Center")

	layout.split(
		Layout(name="header", size=3),
		Layout(name="main", ratio=1),
		Layout(name="footer", size=7)
	)

	layout["main"].split_row(
		Layout(name="side"),
		Layout(name="body", ratio=2, minimum_size=60)
	)

	layout["side"].split(
		Layout(name="box1"),
		Layout(name="box2")
	)

	return layout

layout = make_layout()
print(layout)

input = input("Press ENTER key to quit: ")
