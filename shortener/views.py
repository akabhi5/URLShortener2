from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponseRedirect
from .models import Urls
import random
import string

def randomString(stringLength=6):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


class HomePageView(View):
    def get(self, request):
        all_urls = Urls.objects.all()
        return render(request, 'home.html', {'all_urls': all_urls})

class ResultPageView(View):
    def post(self, request):
        url = request.POST['url']
        fake_url=randomString()
        model_url = Urls(fake_url=fake_url, original_url=url)
        model_url.save()
        return render(request, 'result.html', {'url': fake_url})

    def get(self, request):
        return HttpResponseRedirect('/')

class RedirectToUrl(View):
    def get(self, request, url):
        try:
            redirect_url = Urls.objects.get(fake_url=url)
        except:
            return render(request, 'error.html')
        final_url = str(redirect_url.original_url)
        if 'http' not in final_url:
            final_url = 'http://'+str(redirect_url.original_url)
        return redirect(final_url)
