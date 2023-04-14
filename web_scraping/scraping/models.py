from django.db import models
from django.db.models import Count
from users.models import CustomUser

class CompanyInfo(models.Model):

    name    = models.CharField(verbose_name="会社名",max_length=100)
    people_num = models.CharField(verbose_name = "社員数", max_length = 25)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'company_info'
        
        
class Likes(models.Model):
    """いいね"""
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    company_name = models.ForeignKey(CompanyInfo, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user','compay_name'],
                name='user_like'
            )
        ]