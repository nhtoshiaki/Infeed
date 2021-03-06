# Generated by Django 2.2 on 2019-05-07 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0004_auto_20190429_2010'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField()),
                ('url', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('summary', models.TextField()),
                ('readed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('login', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='source',
            name='source_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feed.List'),
        ),
        migrations.DeleteModel(
            name='SourceItem',
        ),
        migrations.DeleteModel(
            name='SourceList',
        ),
        migrations.AddField(
            model_name='list',
            name='list_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feed.User'),
        ),
        migrations.AddField(
            model_name='item',
            name='item_source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feed.Source'),
        ),
    ]
