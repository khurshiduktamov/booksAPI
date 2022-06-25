# Generated by Django 4.0.5 on 2022-06-18 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('title', models.CharField(max_length=250)),
                ('author', models.CharField(max_length=200)),
                ('isbn', models.CharField(max_length=13)),
            ],
        ),
    ]