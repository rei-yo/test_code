# Generated by Django 4.1.7 on 2023-03-11 23:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0009_topic_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='user_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='bbs.user', verbose_name='ユーザー名'),
        ),
    ]
