from django.db import models
from django.utils import timezone

class CustomerDevice(models.Model):

    infra_customer_id = models.CharField(verbose_name="infra_customer_id", max_length=15)
    address = models.CharField(verbose_name="住所", max_length=50)
    device_list_id = models.CharField(verbose_name="デバイスリストid", max_length=15)
    delete_flag = models.IntegerField(verbose_name="デリートフラグ")
    update_time = models.DateTimeField(help_text = "更新日")
    create_time = models.DateTimeField(help_text = "作成日")


    def save(self, *args, **kwargs):
        if not self.infra_customer_id:
            self.created_time = timezone.now()
        self.update_time = timezone.now()

        return super(CustomerDevice, self).save(*args, **kwargs)
