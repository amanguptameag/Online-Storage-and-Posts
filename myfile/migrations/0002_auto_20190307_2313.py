# Generated by Django 2.1 on 2019-03-07 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Share',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(blank=True, max_length=120)),
                ('title', models.CharField(blank=True, max_length=120)),
                ('description', models.CharField(blank=True, max_length=120)),
                ('file', models.FileField(upload_to='files/')),
            ],
        ),
        migrations.AddField(
            model_name='uploadfile',
            name='user',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]
