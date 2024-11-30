# Generated by Django 5.1.3 on 2024-11-29 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('book_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=55)),
                ('release_date', models.DateField()),
                ('create_at', models.DateField()),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('department_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=55)),
            ],
        ),
    ]