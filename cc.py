import web.psqlapi

from datetime import datetime

import rich
from rich import box
from rich import print
from rich.traceback import install
from rich.console import Console
from rich.table import Table
from rich.markdown import Markdown
from rich.layout import Layout
from rich.panel import Panel
from rich.align import Align, VerticalCenter
from rich.panel import Panel

from rich.live import Live
from time import sleep

console = Console()
install(show_locals=True)


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

def get_variables():
	# TODO(Erton): Code the API connection to GET values from DB
	pass

def show_variable_display() -> Panel:
    # variable display
    table = Table(title="[b]----- VARIABLE DISPLAY -----[/]")

    table.add_column("Variable Name", justify="right", style="yellow", no_wrap=True)
    table.add_column("Actual Value", style="cyan")
    table.add_column("Information Obtained From", justify="right", style="cyan")

    # values
    # TODO(Erton): get_variables() here
    table.add_row("CANT e1", "250", "bot/ cant | e1")
    table.add_row("CANT e2", "250", "bot/ cant | e2")
    table.add_row("CANT e3", "250", "bot/ cant | e3")
    table.add_row("CANT e4", "250", "bot/ cant | e4")

    # centering
    table = Align.center(table)
    
    return Panel(table,  
    	subtitle="ccvar.txt",
    	box=box.ROUNDED,
    	padding=(2, 2),
    	border_style="bright_blue")


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
layout["body"].update(show_variable_display())
print(layout)

with Live(layout, refresh_per_second=10, screen=True):
	while True:
		sleep(0.1)
