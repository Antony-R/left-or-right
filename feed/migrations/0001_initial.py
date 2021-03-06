# Generated by Django 3.2.6 on 2021-08-06 15:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Left',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('left_title', models.CharField(default='', max_length=200)),
                ('left_content', models.CharField(default='', max_length=200)),
                ('left_vote', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Right',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('right_title', models.CharField(default='', max_length=200)),
                ('right_content', models.CharField(default='', max_length=200)),
                ('right_vote', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=250)),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('left', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feed.left')),
                ('right', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feed.right')),
                ('uname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
