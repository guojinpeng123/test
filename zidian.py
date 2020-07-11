#  创建一个用于存储外星人的空列表
aliens = []
#  创建 30 个绿色的外星人
for alien_number in range (0,30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)
for alien in aliens[10:20]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10
for alien in aliens[20:30]:
	if alien['color'] == 'green':
		alien['color'] = 'red'
		alien['speed'] = 'fast'
		alien['points'] = 15
#  显示前五个外星人
for alien in aliens:
	print(alien)
print("...")