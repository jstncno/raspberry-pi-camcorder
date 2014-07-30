import csv

PATH = '/home/pi/sunrise_sunset_tables.csv'

file = open(PATH)
reader = csv.reader(file)

time_table = {}

for row in reader:
	time_table[row[0]] = {}
	time_table[row[0]]['sunrise'] = row[1]
	time_table[row[0]]['sunset'] = row[2]

