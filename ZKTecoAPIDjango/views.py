import datetime

from .requests_methods import ZKTeco
from django.http import JsonResponse

def logs(request, id_user, sdate=None, edate=None):
	zkteco = ZKTeco()
	# return JsonResponse(zkteco.logs(id_user, sdate, edate), safe = False)

	if sdate and not edate:
		return JsonResponse(zkteco.logs(id_user, sdate, sdate), safe = False)

	# if sdate and edate:
	return JsonResponse(zkteco.logs(id_user, sdate, edate), safe = False)

def logsToToday(request, id_user, sdate=None):
	zkteco = ZKTeco()
	edate = datetime.datetime.today().strftime('%Y-%m-%d')

	return JsonResponse(zkteco.logs(id_user, sdate,edate), safe = False)

def users(request, first=None, last=None):
	zkteco = ZKTeco()
	
	return JsonResponse(zkteco.users(first, last), safe = False)

def user(request):

	return JsonResponse({})

def userlogs(request):
	zkteco = ZKTeco()
	#end date will the current date
	edate = datetime.datetime.today().strftime('%Y-%m-%d')

	datas = []

	if not zkteco.createConnection():
		for user in zkteco.users():
			datas.append(zkteco.logs(int(user['uid']),'2020-01-01' ,edate))

	datas = datas if len(datas) > 0 else {'erreur' : 'not connected'}
	# print('================================================')
	# check = zkteco.createConnection()
	# print(check)

	# print('================================================')

	return JsonResponse(datas, safe = False)
