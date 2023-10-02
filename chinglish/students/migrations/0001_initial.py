# Generated by Django 3.2.15 on 2023-10-01 06:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='first name')),
                ('second_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='second name')),
                ('last_name', models.CharField(max_length=50, verbose_name='last name')),
                ('phone', models.CharField(max_length=15, verbose_name='number phone')),
                ('birthday', models.DateField(verbose_name='birthday')),
                ('classroom', models.CharField(max_length=12, verbose_name='classroom')),
                ('is_child', models.BooleanField(default=False, verbose_name='is this a child?')),
                ('phone_parents', models.CharField(blank=True, max_length=15, null=True, verbose_name='number phone parents')),
                ('photo', models.ImageField(upload_to='student', verbose_name='photo student')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
