'''
	####### Plugin-version to get all dates for ex. every Monday between 2 dates ########


	Done by: Anton Andersson @ 2021-03-10
	Free to use by anyone.

	
'''
def days_between_two_dates(startdate, enddate):
	from dateutil.rrule import rrule, WEEKLY, MO, TU, WE , TH, FR, SA, SU
	from datetime import date


	# The list where the dates will be stored
	result_dates = []


	week_days = {
		"Monday" : MO,
		"Tuesday" : TU,
		"Wednesday" : WE,
		"Thursday" : TH,
		"Friday" : FR,
		"Saturday" : SA,
		"Sunday" : SU
	}


	def get_dates(date_entry):
		year, month, day = map(int, date_entry.split('-'))
		return date(int(year), int(month), int(day))


	def get_day(day_entry):
		return week_days[day_entry]


	# Start date
	start_date = get_dates(startdate)

	# End date
	end_date = get_dates(enddate)

	# Get the days name (ex. Monday)
	dayOfWeek = get_day(start_date.strftime('%A'))


	for date in rrule(WEEKLY, byweekday=dayOfWeek, dtstart=start_date, until=end_date):
		# Add the dates into the result_date list
		result_dates.append(date)

	return result_dates
