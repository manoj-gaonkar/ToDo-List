# Generated by Django 4.1.1 on 2022-09-06 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0002_alter_todo_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="title",
            field=models.CharField(max_length=50),
        ),
    ]
