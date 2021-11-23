import web.psqlapi

from datetime import datetime

import rich
from rich import print
from rich.traceback import install
from rich.console import Console
from rich.table import Table
from rich.markdown import Markdown
from rich.layout import Layout
from rich.panel import Panel

from rich.live import Live
from time import sleep

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
		Layout(name="header", size=5),
		Layout(name="main", ratio=1),
		Layout(name="footer", size=5)
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



class Header:

	def __rich__(self) -> Panel:
		grid = Table.grid(expand=True)
		grid.add_column(justify="center", ratio=1)
		grid.add_column(justify="right")
		grid.add_row(
			"[b]CC[/b] Control Center",
			datetime.now().ctime().replace(":", "[blink]:[/]")
		)
		return Panel(grid, style="white on blue")


layout = make_layout()
layout["header"].update(Header())
print(layout)

with Live(layout, refresh_per_second=10, screen=True):
	while True:
		sleep(0.1)
