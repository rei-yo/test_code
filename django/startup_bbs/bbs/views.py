from django.shortcuts import render,redirect
from django.views import View
from .models import Topic, Category
from .forms import TopicForm
from django.db.models import Q
from django.contrib import messages
from django.core.paginator import Paginator 

from .models import Album,Document
from .forms import AlbumForm,DocumentForm


class IndexView(View):

    def get(self, request, *args, **kwargs):
        context = {}
        query = Q() #クエリの初期化
        
        if 'search' in request.GET:
            words = request.GET['search'].replace('　',' ').split(' ')
            
            for word in words:
                if word == '': #スペースが2つ以上入っていた場合の対応
                    continue
                query &= Q(comment__contains=word)

            context = Topic.objects.filter(query).order_by('id')
            paginator = Paginator(context, 3)
            
            if "page" in request.GET:
                context = paginator.get_page(request.GET["page"])
            else:
                context = paginator.get_page(1)
            
        else:
            context = {}
            context['topics'] = Topic.objects.all()
            context['categories'] = Category.objects.all()
            paginator = Paginator(context, 3)

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

class SingleView(View):

    def get(self, request, pk, *args, **kwargs):
        context = {}

        context["topic"] = Topic.objects.filter(id=pk).first()
        #first()で単一のオブジェクトを返す（無ければhtml側でforループが必要）
        
        return render(request,"bbs/single.html", context)

single  = SingleView.as_view()


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

        #???
        mime_type   = magic.from_buffer(request.FILES["file"].read(1024) , mime=True)
        
        if not mime_type in ALLOWED_MIME:
            print("このファイルのMIMEは許可されていません。")
            print(mime_type)
            return redirect("bbs:document")


        print("バリデーションOK")
        form.save()

        return redirect("bbs:document")
document    = DocumentView.as_view()

