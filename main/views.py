from django.shortcuts import render


# Create your views here.

from django.views.generic import ListView, CreateView, UpdateView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Query, Track, Category
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from django.shortcuts import render
import pdb
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from .forms import QueryForm
from bs4 import BeautifulSoup
import datetime
from django.utils import timezone


class Home(ListView):
    model=Category
    context_object_name = 'category'
    template_name='index.html'


class saveQuery(CreateView):
    model=Query
    form_class = QueryForm
    success_url = '/'

@method_decorator(csrf_exempt, name='dispatch')
class handleContent(View):

    def post(self, request, *args, **kwargs):
        content=request.POST.get('result')
        content=json.loads(content)
        form=QueryForm(request.POST)
        query=request.POST.get('query')
        query=query.strip()
        if form.is_valid():
            try:
                query=Query.objects.get(query__icontains=query)
                return JsonResponse({'status': False, 'detail':'Query already exist'})
            except Query.DoesNotExist:
                query=form.save()
        else:
            return JsonResponse({'status':False, 'detail':form.errors})
        dates=[]
        teams=[]
        opps=[]
        for group in content:
            #dates=list(set(group['columns'][0]+dates))
            dates=group['columns'][0]+dates
            teams=group['columns'][1]+teams
            opps=group['columns'][2]+opps

        dates=[datetime.datetime(year=int(str(s)[0:4]), month=int(str(s)[4:6]), day=int(str(s)[6:8])) for s in dates ]
        now=datetime.datetime.now()
        #now=timezone.now()
        #pdb.set_trace()
        for index,date in enumerate(dates):
            if now.date() <= date.date():
                Track(query=query, date=date, team=teams[index],opp=opps[index]).save()
        return JsonResponse({'status':True, 'detail':'Successful'})


class getActiveQuery(View):

    def get(self, request,*args, **kwargs):
        cat_id=request.GET.get('cat_id')
        #active_queries=Query.c_objects.active(cat_id)
        now=datetime.datetime.now().date()
        active_trends=Track.objects.filter(date=now).filter(query__category__id=cat_id).order_by('query').distinct('query')
        active_games=Track.objects.filter(date=now).filter(query__category__id=cat_id).order_by('query')
        categories=Category.objects.all()
        sport=Category.objects.get(id=cat_id)
        #response=render_to_string('includes/query_list.html',{'queries':active_trends})
        return render(request, 'queries.html', {'trends':active_trends, 'active_games':active_games, 'category':categories, 'sport':sport,  'cat_tile':'Active ' + sport.name})

@method_decorator(csrf_exempt, name='dispatch')
class format_data(View):

    def post(self,request, *args, **kwargs):
        headers=json.loads(request.POST.get('header'))
        results=json.loads(request.POST.get('result'))
        format_data=[]
        count=0
        for value in results[0]:

            inn_arr=[value]
            for arr in results[1::]:
                inn_arr.append(arr[count])
            count+=1
            format_data.append(inn_arr)

        headers=[{'title':header} for header in headers]

        return JsonResponse({'result':format_data, 'headers':headers})

class getAllQuery(View):

    def get(self, request,*args, **kwargs):
        cat_id=request.GET.get('cat_id')
        categories=Category.objects.all()
        sport=Category.objects.get(id=cat_id)
        all_query=Query.objects.filter(category__id=cat_id).order_by('-query_date')
        return render(request, 'queries.html', {'queries':all_query, 'category':categories, 'sport':sport, 'all':True,
                                                'cat_tile':'All ' + sport.name})


class deleteQuery(View):

    def get(self, request, *args, **kwargs):
        id=request.GET.get('id')
        Query.objects.get(id=id).delete()
        return HttpResponseRedirect('/active_queries?cat_id=5')

class updateQuery(UpdateView):
    model=Query
    form_class = QueryForm
    template_name = 'edit_query.html'
    success_url = '/active_queries?cat_id=5'
    context_object_name = 'query'



        







