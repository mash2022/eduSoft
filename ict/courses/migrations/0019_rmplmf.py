# Generated by Django 4.1.7 on 2023-12-15 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0018_customsettings'),
    ]

    operations = [
        migrations.CreateModel(
            name='RmpLmf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name_ban', models.CharField(max_length=150)),
                ('student_name_eng', models.CharField(max_length=150)),
                ('father_or_hus_name_ban', models.CharField(max_length=150)),
                ('father_or_hus_name_eng', models.CharField(max_length=150)),
                ('village_ban', models.CharField(max_length=100)),
                ('village_eng', models.CharField(max_length=100)),
                ('post_office_ban', models.CharField(max_length=100)),
                ('post_office_eng', models.CharField(max_length=100)),
                ('upozila_ban', models.CharField(max_length=100)),
                ('upozila_eng', models.CharField(max_length=100)),
                ('district_ban', models.CharField(max_length=100)),
                ('district_eng', models.CharField(max_length=100)),
                ('religion', models.CharField(choices=[('ISLAM', 'Islam'), ('HINDU', 'Hindu'), ('CHRITIAN', 'Christian'), ('OTHERS', 'Others')], default='ISLAM', max_length=10)),
                ('nid', models.IntegerField()),
                ('mobile', models.CharField(max_length=20)),
                ('nationality', models.CharField(max_length=100)),
                ('blood_group', models.CharField(max_length=20)),
                ('marrietal_status', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=50)),
                ('edu_qualification', models.CharField(choices=[('SSC', 'ssc'), ('HSC', 'hsc'), ('HONOURS', 'Honours'), ('MASTERS', 'Masters')], default='SSC', max_length=10)),
                ('is_pharmacy_have', models.CharField(choices=[('YES', 'Yes'), ('No', 'No')], default='YES', max_length=10)),
                ('pharmacy_name_address', models.CharField(max_length=255)),
                ('past_training_name', models.CharField(max_length=100)),
            ],
        ),
    ]
