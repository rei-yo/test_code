from django import template
register = template.Library()

@register.simple_tag()
def url_replace(request, key, value):
    # keyは'page',valueはページ数を指す
    # request.GET.urlencode()→search=test&page=2
    copied      = request.GET.copy()
    
    # request.get['pege']=intでページ数を書き換え
    copied[key] = value
    return copied.urlencode()