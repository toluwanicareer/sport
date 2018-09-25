from django.core.management.base import BaseCommand
from django.utils import timezone
import datetime
from ...models import Query, Track
import requests
from django.conf import settings
import json
import urllib
import pdb

class Command(BaseCommand):
    help="update time"

    def handle(self, *args, **kwargs):
        now=datetime.datetime.now().date()
        queries=Query.objects.all()
        Track.objects.all().delete()
        for query in queries:
            url=build_url(query)
            response=requests.post(settings.CRON_URL, json={'url':url})
            process_response(response.text, query)

def build_url(query):
    url='http://api.sportsdatabase.com/' + query.category.name.lower() + '/query.json'
    query=query.query
    query='date,team,o:team@'+query
    data={'sdql':query,  'output': 'json',
                 'api_key': 'guest'}
    params=urllib.parse.urlencode(data)
    url=url+'?'+params
    return url


def process_response(text, query):
    response=text.strip().replace('json_callback(','').replace(');','')
    pdb.set_trace()
    response=json.loads(''.join(response.split()).replace('\'', '"'))
    dates=[]
    teams=[]
    opps=[]
    for group in response['groups']:
        # dates=list(set(group['columns'][0]+dates))
        dates = group['columns'][0] + dates
        teams = group['columns'][1] + teams
        opps = group['columns'][2] + opps

    dates = [datetime.datetime(year=int(str(s)[0:4]), month=int(str(s)[4:6]), day=int(str(s)[6:8])) for s in dates]
    now = datetime.datetime.now()
    # now=timezone.now()
    # pdb.set_trace()
    for index, date in enumerate(dates):
        if now.date() <= date.date():
            Track(query=query, date=date, team=teams[index], opp=opps[index]).save()







