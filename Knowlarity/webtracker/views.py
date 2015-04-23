from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import Context, loader,RequestContext
from django.core.mail import send_mail, EmailMessage, BadHeaderError
import requests, os

def index(request):
    if request.method == 'POST':
        urls = request.POST.getlist('urls')
        files = request.FILES.get('files')
        urls_dict = {}
        try:
            if urls:
                for u in urls:
                    try:
                        r = requests.get(u)
                        urls_dict[u] = "%s - %s"%(str(r.status_code), str(r.reason))
                    except Exception as e:
                        urls_dict[u] = e.message
            if files:
                f = files.readlines()
                for u in list(f):
                    try:
                        r = requests.get(u)
                        urls_dict[u] = "%s - %s"%(str(r.status_code), str(r.reason))
                    except Exception as e:
                        urls_dict[u] = e.message
        except:
            pass
    return render_to_response('index.html', locals(), context_instance = RequestContext(request))




