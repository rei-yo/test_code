from django.shortcuts import render,redirect
from django.views import View
from .models import Topic, Category, User
from .forms import TopicForm
from django.db.models import Q
from django.contrib import messages
from django.core.paginator import Paginator 

from .models import Album,Document
from .forms import AlbumForm,DocumentForm


class IndexView(View):

    def get(self, request, *args, **kwargs):
        context = {}
        query = Q() #クエリの初期化→検索していないときも対応させるため
        
        if 'search' in request.GET:
            words = request.GET['search'].replace('　',' ').split(' ')
            
            for word in words:
                if word == '': #スペースが2つ以上入っていた場合の対応
                    continue
                query &= Q(Q(comment__contains=word) | Q(category__name__contains=word))

        topics = Topic.objects.filter(query).order_by('id')
        paginator = Paginator(topics, 3)
            
        if "page" in request.GET:
            context['topics'] = paginator.get_page(request.GET["page"])
        else:
            context['topics'] = paginator.get_page(1)
        
        context['categories'] = Category.objects.all()
        context['user_name'] = User.objects.all()   
        # else:
        #     context = {}
        #     context['topics'] = Topic.objects.all()
        #     context['categories'] = Category.objects.all()
        #     paginator = Paginator(context, 3)

        return render(request,"bbs/index.html",context)

    def post(self, request, *args, **kwargs):

        # posted  = Topic( comment = request.POST["comment"] )
        # posted.save()

        form = TopicForm(request.POST, request.FILES)
        # user = request.POST["user_check"]
  
        if form.is_valid():
            print('OK')
            form.save()
            messages.add_message(request, messages.INFO, '投稿完了')
            messages.add_message(request, messages.INFO, '投稿完了')
        else:
            print('NG')
            error_message = form.errors.get_json_data().values()
            
            for error in error_message:
                for err in error:
                    messages.error(request, err["message"])
                
        
        return redirect("bbs:index")

index   = IndexView.as_view()


class SingleView(View):

    def get(self, request, pk, *args, **kwargs):
        context = {}

        context["topic"] = Topic.objects.filter(id=pk).first()
        #first()で単一のオブジェクトを返す（無ければhtml側でforループが必要）
        
        return render(request,"bbs/single.html", context)

single  = SingleView.as_view()



#ここでpdfのみ許可するように定義をしている。
#MIMEタイプで検索するとOK。
ALLOWED_MIME    = [ "application/pdf" ]

class AlbumView(View):

    def get(self, request, *args, **kwargs):

        context             = {}
        context["albums"]   = Album.objects.all()

        return render(request,"bbs/album.html",context)

    def post(self, request, *args, **kwargs):

        form    = AlbumForm(request.POST, request.FILES)
        
        if not form.is_valid():
            print("バリデーションNG")
            print(form.errors)
            return redirect("bbs:album")

        print("バリデーションOK")
        form.save()

        return redirect("bbs:album")

album   = AlbumView.as_view()



class DocumentView(View):

    def get(self, request, *args, **kwargs):

        context                 = {}
        context["documents"]    = Document.objects.all()

        return render(request,"bbs/document.html",context)

    def post(self, request, *args, **kwargs):

        form        = DocumentForm(request.POST,request.FILES)

        if not form.is_valid():
            print("バリデーションNG")
            print(form.errors)
            return redirect("bbs:document")

        #全てのファイルを受け付けてしまうので、ここで制約
        # magicでMIMEタイプはファイル形式（PDF、jpegとか）を取り出している。
        #.read(1024)でファイルのヘッダー？を読みに行っている？ので偽装しにくいと言われている。
        mime_type   = magic.from_buffer(request.FILES["file"].read(1024) , mime=True)
    
        #アーリーリターン。条件に一致していればここでreturnで終了。    
        if not mime_type in ALLOWED_MIME:
            print("このファイルのMIMEは許可されていません。")
            print(mime_type)
            return redirect("bbs:document")


        print("バリデーションOK")
        form.save()

        return redirect("bbs:document")
document    = DocumentView.as_view()

