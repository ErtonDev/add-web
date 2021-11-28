import web.psqlapi
import io

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

import pynput
from pynput import keyboard

console = Console()
install(show_locals=True)


# display the gui header
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

# selector methods as well as position handling
class Selector:
	# FIXME(Erton): Currently giving a strange error, stack overflow says indentations may be the issue
	# sublime text has been giving me some problems with indentations so I may want to try using another code editor

	def __init__(self):
		self.position = 0
		self.selections = ['100.txt', '101.txt', '102.txt'] # TODO(Erton): Provisional files for testing
		self.path = "../profile/"

	def __rich__(self) -> Panel:
		# NOTE(Erton): Provisional code for testing
		self.selector = Table.grid()
		self.selector.add_column(style="yellow", no_wrap=True)
		self.selector.add_column(justify="right", style="cyan")
		self.set_pos()
		self.selector = Align.center(self.selector)

		return Panel(self.selector,
			title="Selector",
			box=box.ROUNDED,
			padding=(2, 2),
			border_style="bright_blue")

	# TODO(Erton): Get path from the directory watching
	def get_path(self):
		pass

	# TODO(Erton): Has to change selections inside class, selections are checked outside
	def get_sel(self, selections):
		# something like self.selections = selections
		pass

	# TODO(Erton): Update the selector to show the highlighting
	def set_pos(self):

		# adds rows inside selector
		self.pos_counter = 0
		for i in self.selections:
			# underlines i in position
			if self.pos_counter == self.position:
				# underlined
				self.selector.add_row(f"[u]{i}[/u]", " -> " + self.path)
			else:
				self.selector.add_row(i, " -> " + self.path)
			self.pos_counter += 1
		self.pos_counter = 0

	# TODO(Erton): Change highlighting when going up in the selector
	def up_pos(self):
		global selector

		if self.position == 0:
			self.position = len(self.selections)
			self.set_pos()
		else:
			self.position -= 1
			self.set_pos()

	# TODO(Erton): Change highlighting when going down in the selector
	def down_pos(self):
		global selector

		if self.position == len(self.selections):
			self.position = 0
			self.set_pos()
		else:
			self.position += 1
			self.set_pos()

	# TODO(Erton): Makes a selection, so it must change the entire display
	def select(self):
		pass


# defines the main layout of the gui
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

# get the predefined values in ccvar.txt
def get_variables():
	# TODO(Erton): Code the API connection to GET values from DB
	pass

# display body content
def show_body() -> Panel:
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


layout = make_layout()
layout["header"].update(Header())
layout["body"].update(show_body())
layout["box1"].update(Selector())
print(layout)

sel = Selector()

# main loop with live functionality
with Live(layout, refresh_per_second=10, screen=True):
	while True:

		# key input check
		# TODO(Erton): code with pynput module.
		# Search for 'pynput monitoring the keyboard'

		sleep(0.1)
