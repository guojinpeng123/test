def Day_num(birth_year,birth_month,birth_day):
	day = 0
	for month in range(birth_month,12):
		if month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
			day = day+31
		elif month==2:
			day = day+28
		else:
			day = day+30

		if birth_year%4==0:
			day = day+1-birth_day
		else:
			day = day-birth_day

		for year in range(birth_year+1,2020):
		if(year%4==0):
			day = day+366
		else:
			day = day+356

			day = day+31+29+31+30+31+16
		return day

			Day = Day_num(1985,7,10)
	print(Day)
