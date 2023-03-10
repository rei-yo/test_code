# Generated by Django 4.1.7 on 2023-02-28 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='カテゴリ')),
            ],
        ),
        migrations.CreateModel(
            name='TodoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('memo', models.TextField()),
                ('priority', models.CharField(choices=[('danger', 'high'), ('warning', 'normal'), ('primary', 'low')], max_length=50)),
                ('duedate', models.DateField()),
                ('category', models.ForeignKey(default='未分類', on_delete=django.db.models.deletion.CASCADE, to='todo.category', verbose_name='カテゴリ')),
            ],
        ),
    ]
