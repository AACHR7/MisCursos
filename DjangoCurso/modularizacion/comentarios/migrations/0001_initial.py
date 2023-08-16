# Generated by Django 4.1.3 on 2022-12-21 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('score', models.IntegerField(default=3)),
                ('comments', models.TextField(max_length=1000, null=True)),
            ],
        ),
    ]
