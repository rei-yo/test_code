from django.shortcuts import render

from django.views import View
from django.http import JsonResponse
from django.shortcuts import render
from graph.models import RandomNumber
import random
from .forms import RandomNumberForm
from rest_framework.views import APIView


class IndexGraphView(View):
    
    def get(self, request, *args, **kwargs):
        # # DBからランダムな10個の数字を取得
        # values = RandomNumber.objects.all().order_by('created_at').reverse()[:10]
        # # numbers = RandomNumber.objects.all().order_by('-created_at')[:10][::-1]
        
        # context = {}
        # context['values'] =  values
  
        return render(request, 'indexgraph.html')

    def post(self, request, *args, **kwargs):
         
        form = RandomNumberForm(request.POST)
        print('request_post', request.POST)
        
        if form.is_valid():
            print('OK')
            form.save()
        
        all_values = RandomNumber.objects.all().order_by('created_at').reverse()[:10] 
        context = {}
        
        # 毎回、forで一つ一つ取り出してdictにする必要があるのか？
        values = [val.value for val in all_values]
        label = [val.id for val in all_values]
        data = {'labels': label, 'values':values }
        
        # json["error"]   = False????
        
        print('postされて返すデータ', data)
        return JsonResponse(data)
         
         

index   = IndexGraphView.as_view()

class GetValuesAPIView(APIView):
    
    def get(self, request, *args, **kwargs):
        all_values = RandomNumber.objects.order_by('created_at').reverse()[:10]
        values = [val.value for val in all_values]
        label = [val.id for val in all_values]
    
        print('label',label)
        print('values', values)
        data = {'labels': label, 'values':values }
        
        #なぜjsonresponse？
        return JsonResponse(data)

get_values   = GetValuesAPIView.as_view()
    
class UpdateViewAPIView(APIView):
    def post(self, request, *args, **kwargs):
        # ランダムな10個の数字を生成
        values = random.sample(range(10, 101), 10)

        # データベースに値を格納
        # RandomNumber.objects.all().delete()
        for value in values:
            RandomNumber.objects.create(value=value)

        all_values = RandomNumber.objects.order_by('created_at').reverse()[:10]
        values = [val.value for val in all_values]
        label = [val.id for val in all_values]
   
        # print('label',label)
        # print('values', values)
        data = {'labels': label, 'values':values }

        return JsonResponse(data)

update_view =  UpdateViewAPIView.as_view()




# Create your views here.
