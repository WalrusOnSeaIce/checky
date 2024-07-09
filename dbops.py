from datetime import datetime
import csv
from tabulate import tabulate
from os import get_terminal_size

def savetodb(record):
	date = datetime.now().strftime("%Y-%m-%d")
	record.insert(0, date)
	with open("history.csv", "a", newline="") as ff:
		ff.seek(2)
		writer = csv.writer(ff)
		writer.writerow(record)
	record.clear()


def gethist():
	headers = ["Date", "File", "Checksum type", "Checksum", "Checksum of file", "Result"]
	width = int(get_terminal_size()[0]/6)
	with open("history.csv", "r") as ff:
		record = csv.reader(ff)
		try:
			print(tabulate(record, headers, tablefmt="grid", maxcolwidths=width))
		except IndexError:
			print("No history!")


def delhist():
	with open("history.csv", "a") as ff:
		ff.seek(0)
		ff.truncate()
