# Generated by Django 3.2.25 on 2024-06-28 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('video', '0004_delete_requestlog'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('method', models.CharField(max_length=10)),
                ('path', models.CharField(max_length=255)),
                ('remote_addr', models.CharField(blank=True, max_length=50)),
                ('query_params', models.TextField(blank=True)),
            ],
        ),
    ]
