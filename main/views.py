from django.shortcuts import render
from .models import Category, Query

# Create your views here.

from django.views.generic import ListView, CreateView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Query
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from django.shortcuts import render
import pdb
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from .forms import QueryForm

class Home(ListView):
    model=Category
    context_object_name = 'category'
    template_name='index.html'


class saveQuery(CreateView):
    model=Query
    form_class = QueryForm
    success_url = '/'



class getActiveQuery(View):

    def get(self, request,*args, **kwargs):
        cat_id=request.GET.get('cat_id')
        active_queries=Query.c_objects.active(cat_id)
        categories=Category.objects.all()
        response=render_to_string('includes/query_list.html',{'queries':active_queries})
        return render(request, 'queries.html', {'queries':active_queries, 'category':categories})

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







