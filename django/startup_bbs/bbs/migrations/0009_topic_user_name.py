# Generated by Django 4.1.7 on 2023-03-11 23:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0008_remove_user_name_user_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='user_name',
            field=models.ForeignKey(default='無し', on_delete=django.db.models.deletion.SET_DEFAULT, to='bbs.user', verbose_name='ユーザー名'),
        ),
    ]
