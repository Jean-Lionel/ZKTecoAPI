from django.http import JsonResponse
from .requests_methods import ZKTeco

def logs(request, id_user, sdate=None, edate=None):
	zkteco = ZKTeco()
	# return JsonResponse(zkteco.logs(id_user, sdate, edate), safe = False)

	if sdate and not edate:
		return JsonResponse(zkteco.logs(id_user, sdate, sdate), safe = False)

	# if sdate and edate:
	return JsonResponse(zkteco.logs(id_user, sdate, edate), safe = False)

def logsToToday(request, id_user, sdate=None):
	zkteco = ZKTeco()
	return JsonResponse(zkteco.logs(id_user, sdate), safe = False)

def users(request, first=None, last=None):
	zkteco = ZKTeco()
	
	return JsonResponse(zkteco.users(first, last), safe = False)

def user(request):
	return JsonResponse({})