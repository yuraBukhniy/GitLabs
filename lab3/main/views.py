from django.shortcuts import render
from django.http import JsonResponse
import platform
from datetime import datetime


def main(request):
    return render(request, 'main.html', {'parameter': "test"})


def health(request):
    rawdate = datetime.now()
    date = rawdate.strftime("%H:%M:%S %Y-%m-%d")
    page = request.path
    server = platform.uname()
    client = request.META['HTTP_USER_AGENT']
    response = {'date': date,
                'current_page': page,
                'server_info': {
                    'system': server.system,
                    'hostname': server.node,
                    'release': server.release,
                    'type': server.machine,
                },
                'client_info': client}
    return JsonResponse(response)