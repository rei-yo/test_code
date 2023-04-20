from django import template

register = template.Library()

# CompanyInfoのオブジェクトとクライアントのipアドレスを引数に実行する
@register.inclusion_tag("scraping/good_button.html")
def good_check(obj,ip):

    # GoodCompanyのオブジェクトからipが存在するかチェック。あればいいね済みと判断。なければまだ良いねしていない。
    for o in obj.goodcompanies():
        if o.ip == ip:
            print("いいね済み")
            return { "good":True }

    return { "good":False }
