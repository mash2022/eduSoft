# Generated by Django 4.1.6 on 2023-03-16 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course_course_code_course_course_credit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.CharField(max_length=255)),
                ('teacher_details', models.TextField()),
                ('teacher_image', models.ImageField(upload_to='')),
            ],
        ),
    ]
