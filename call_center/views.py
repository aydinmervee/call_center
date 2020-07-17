import requests
import json

from django.shortcuts import render
from django.conf import settings

from call_center.forms import DateFilterForm


def get_call_center_data(request):
    query_params = {
        'function': 'reportsCDRLogs',
        'app_token': settings.APP_TOKEN,
    }

    form = DateFilterForm(request.POST or None)
    if form.is_valid():
        start_date = form.cleaned_data.get('start_date')
        end_date = form.cleaned_data.get('end_date')

        start_date = start_date.strftime("%Y-%m-%d %H:%M:%S")
        end_date = end_date.strftime("%Y-%m-%d %H:%M:%S")

        query_params['startdate'] = start_date
        query_params['finishdate'] = end_date
    else:
        return render(request, "index.html",
                      {'call_list': [], 'form': form})

    params = "&".join("%s=%s" % (k, v) for k, v in query_params.items())

    base = 'http://staging1.alo-tech.com/api/'
    url = base + '?' + params
    try:
        response = requests.get(url)
        json_data = json.loads(response.text)
        call_list = json_data['CallList']
    except Exception as e:
        call_list = []
    return render(request, "index.html",
                  {'call_list': call_list, 'form': form})
