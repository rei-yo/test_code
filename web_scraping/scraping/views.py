from django.shortcuts import render, redirect
from django.views import View
from .models import CompanyInfo, GoodCompany

from .forms import GoodCompanyForm
from django.utils import timezone
# from users.models import CustomUser
import datetime 

class IndexView(View):

    def get(self, request, *args, **kwargs):
        context = {}
        context["company_info"] = CompanyInfo.objects.all()
        
        return render(request, 'scraping/index.html', context)

index = IndexView.as_view()

class GoodView(View):
    
    def post(self, request, pk, *args, **kwargs):
        
        copied_req = request.POST.copy()
        print('request', copied_req)
        
        copied_req["user"] = request.user
        print('user', request.user)
        copied_req["company_info"] = pk
        print(pk)
        
        ip_list = request.META.get('HTTP_X_FORWARDED_FOR')
        
        if ip_list:
            ip = ip_list.split(',')[0]
            
        else:
            ip = request.META.get('REMOTE_ADDR')
            
        copied_req['ip'] = ip
        
        form = GoodCompanyForm(copied_req)
        
        if not form.is_valid():
            return redirect('scraping:index')
        
        last_week = timezone.now() - datetime.timedelta(days=7)
        
        #gteで～以上、lastweek以上でipが一致する場合はtrueが返ってくる。
        
        if not GoodCompany.objects.filter(dt__gte = last_week, ip = ip, pk = pk).exists():
            form.save()
            
        return redirect("scraping:index")
    
good = GoodView.as_view()
        
        

        
