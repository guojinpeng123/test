favorite_places= {
'My': ['suzhou', 'qingdao','qinghuangdao'],
'laopo': ['hai','suzhou','chengdu'],
'zenxin': ['xian', 'beijing'],
'zerui': ['U.S.A', 'bali','shanghai'],
}
for name, plance in favorite_places.items():
	print("\n" + name.title() + "'s favorite places are:")
	for place in places:
		print("\t" + place.title())
