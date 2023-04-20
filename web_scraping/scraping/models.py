from django.db import models
from django.db.models import Count
from django.utils import timezone
from django.conf import settings

class CompanyInfo(models.Model):

    name    = models.CharField(verbose_name="会社名",max_length=100)
    people_num = models.CharField(verbose_name = "社員数", max_length = 25)
    
    #throughで中間テーブルを明示的に指定する
    good   = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name="良いね", through="GoodCompany")
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'company_info'
        
    
    def good_amount(self):
        print(self.id)
        return len(self.good.all() )
    
    def goodcompanies(self):
        return GoodCompany.objects.filter(company_info = self.id)
        
        
class GoodCompany(models.Model):
    """いいね"""

    dt = models.DateTimeField(verbose_name = 'いいねした時刻',default = timezone.now)
    company_info = models.ForeignKey(CompanyInfo, verbose_name = 'いいねしたトピック', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name = 'いいねしたユーザー', on_delete=models.CASCADE, null=True, blank=True)

    ip = models.GenericIPAddressField(verbose_name="良いねした人のIPアドレス")
    
    def __str__(self):
        return self.company_info.name