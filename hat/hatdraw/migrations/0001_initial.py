# Generated by Django 4.1.3 on 2022-12-03 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HatNames',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hat_names_text', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='HatTasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hat_tasks_text', models.CharField(max_length=400)),
            ],
        ),
    ]