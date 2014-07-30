import csv
import datetime

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

# Abstract: Turn camera on before sunrise, off after sunset
# Returns True if date is between 30 minutes before sunrise
# and 30 minutes after sunset; False otherwise
# Params:
#	(datetime)date - datetime object to retrieve and manipulate time
def daytime(date):
	key = getKey(date)

	sunrise, sunset = getSunData(key)

	on_time = datetime.datetime.combine(date, sunrise) - datetime.timedelta(minutes=30)
	off_time = datetime.datetime.combine(date, sunset) + datetime.timedelta(minutes=30)

	return on_time <= date < off_time

# Abstract: Turn camera on before sunset; off after sunrise
# Returns True if date is either 30 minutes before sunset
# or 30 minutes after sunrise; False otherwise
# Params:
#	(datetime)date - datetime object to retrieve and manipulate time
def nighttime(date):
	key = getKey(date)

	sunrise, sunset = getSunData(key)

	on_time = datetime.datetime.combine(date, sunset) - datetime.timedelta(minutes=30)
	off_time = datetime.datetime.combine(date, sunrise) + datetime.timedelta(minutes=30)

	return date >= on_time or off_time > date

# Returns the current date in string format according to the time_table keys
# e.g. '3-Jul', '15-Sep'
def getKey(date):
	current_day = int(date.strftime('%d')) # we need to remove padded 0
	return str(current_day) + date.strftime('-%b')

# Returns the sunrise and sunset times from the date (key) as time objects
def getSunData(key):
        today = time_table[key]
        sunrise_hour = today['sunrise'][0:2]
        sunrise_minute = today['sunrise'][2:4]
        sunset_hour = today['sunset'][0:2]
        sunset_minute = today['sunset'][2:4]

	sunrise = datetime.time(hour=int(sunrise_hour), minute=int(sunrise_minute))
	sunset = datetime.time(hour=int(sunset_hour), minute=int(sunset_minute))

	return sunrise, sunset

def test():
	date = datetime.datetime.now()
	print "Date:", getKey(date)
	print "Daytime camera ON?", daytime(date)
	print "Nighttime camera ON?", nighttime(date)

if __name__ == "__main__":
	test()
