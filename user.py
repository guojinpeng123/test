users = {
'ming ren': {
'xg': 'taoqi',
'zh': 'hama',
'rs': 'xww',
},
'zuo zhu': {
'xg': 'lengku',
'zh': 'she',
'rs': 'qianniao',
},
'xiao ying': {
'xg': 'huachi',
'zh': 'huoqu',
'rs': 'yiliao',
},
}
for username, user_info in users.items():
	print("\nUsername: " + username.title())
	xingge = user_info['xg']
	zhaohuan = user_info['zh']
	renshu = user_info['rs']
	print("\txingge: " + xingge.title())
	print("\tzhaohuan: " + zhaohuan.title())
	print("\trenshu: " + renshu.title())
