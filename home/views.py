
from django.http import JsonResponse
from .models import log
from .models import user
def get_all_logs(request):
    logs = log.objects.all().values()  
    logs_list = list(logs)  
    return JsonResponse(logs_list,safe=False)


def get_all_userinfo(request):
    users = user.objects.all().values()
    users_list = list(users)
    return JsonResponse(users_list, safe=False)
