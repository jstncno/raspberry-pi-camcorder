import csv

PATH = '/home/pi/sunrise_sunset_tables.csv'

file = open(PATH)
reader = csv.reader(file)

time_table = {}

# row[0]: (string)date, e.g. '3-Jul'
# row[1]: (string)sunrise time, e.g. '0545'
# row[2]: (string)sunset time, e.g. '1715'
for row in reader:
	time_table[row[0]] = {}
	time_table[row[0]]['sunrise'] = row[1]
	time_table[row[0]]['sunset'] = row[2]

# Returns if it is daytime at the current_date
# at the current_hour
# Params:
#	(string)current_date = date index to time_table, e.g. '3-Jul'
#	(int)current_time = current time to compare to sunrise/sunset
def daytime(current_date, current_time):
	print current_date, current_time
	day = time_table[current_date]
	sunrise = day['sunrise']
	sunset = day['sunset']
	print sunrise, sunset
	return True
