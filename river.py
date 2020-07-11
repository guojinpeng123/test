rivers = {
'Yellow River': 'china',
'nile': 'egypt',
'Danube': 'Ukraine',
'Amazon': 'Brazil',
'Yangtze': 'china',
'Mississippi': 'U.S.A',
'Seine': 'France',
'Thames': 'England',
         }
for name, country  in rivers.items():
	print(name.title()+ "flows through "+ country.title()+ "."  )
