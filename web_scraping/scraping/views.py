from django.shortcuts import render
from django.views import View
from .models import CompanyInfo, Likes
# from users.models import CustomUser

class IndexView(View):

    def get(self, request, *args, **kwargs):
        context = {}
        context["company_info"] = CompanyInfo.objects.all()
        context["likes"] = Likes.objects.all()
        
        return render(request, 'scraping/index.html', context)

index = IndexView.as_view()

        
# from django.shortcuts import render,redirect
# from django.views import View
# from .models import Topic, Category, User
# from .forms import TopicForm
# from django.db.models import Q
# from django.contrib import messages
# from django.core.paginator import Paginator 

# from .models import Album,Document
# from .forms import AlbumForm,DocumentForm
# import magic

# class IndexView(View):

#     def get(self, request, *args, **kwargs):
#         context = {}
#         query = Q() #クエリの初期化→検索していないときも対応させるため
        
#         if 'search' in request.GET:
#             words = request.GET['search'].replace('　',' ').split(' ')
            
#             for word in words:
#                 if word == '': #スペースが2つ以上入っていた場合の対応
#                     continue
#                 query &= Q(Q(comment__contains=word) | Q(category__name__contains=word))

#         topics = Topic.objects.filter(query).order_by('id')
#         paginator = Paginator(topics, 3)
            
#         if "page" in request.GET:
#             context['topics'] = paginator.get_page(request.GET["page"])
#         else:
#             context['topics'] = paginator.get_page(1)
        
#         context['categories'] = Category.objects.all()
#         context['user_name'] = User.objects.all()   
        
#         # print("context", topics[0])
#         # else:
#         #     context = {}
#         #     context['topics'] = Topic.objects.all()
#         #     context['categories'] = Category.objects.all()
#         #     paginator = Paginator(context, 3)

#         return render(request,"bbs/index.html",context)
# # Create your views here.
