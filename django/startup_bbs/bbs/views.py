from django.shortcuts import render,redirect

from django.views import View
from .models import Topic, Category
from .forms import TopicForm
from django.db.models import Q
from django.contrib import messages
from django.core.paginator import Paginator 

class IndexView(View):

    def get(self, request, *args, **kwargs):
        context = {}
        query = Q() #クエリの初期化？
        
        if 'search' in request.GET:
            words = request.GET['search'].replace('　',' ').split(' ')
            
            for word in words:
                if word == '': #スペースが2つ以上入っていた場合の対応
                    continue
                query &= Q(comment__contains=word)
                print(Topic.objects.filter(query).query)
            context["topics"] = Topic.objects.filter(query)
                
        else:
            context = {}
            context['topics'] = Topic.objects.all()
            context['categories'] = Category.objects.all()

        return render(request,"bbs/index.html",context)

    def post(self, request, *args, **kwargs):

        # posted  = Topic( comment = request.POST["comment"] )
        # posted.save()

        form = TopicForm(request.POST)
        if form.is_valid():
            print('OK')
            form.save()
            messages.add_message(request, messages.INFO, '投稿完了')
        else:
            print('NG')
            error_message = form.errors.get_json_data().values()
            
            for error in error_message:
                for err in error:
                    messages.error(request, err["message"])
                
        
        return redirect("bbs:index")

index   = IndexView.as_view()


# Create your views here.
