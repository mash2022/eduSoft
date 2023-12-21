# Generated by Django 4.1.6 on 2023-12-21 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_delete_rmplmf_remove_admission_admission_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('fatherName', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('courseName', models.CharField(max_length=255)),
                ('address', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='admissionform',
            name='admission_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='admissionform',
            name='edu_qualification',
            field=models.CharField(choices=[('SSC', 'SSC'), ('HSC', 'HSC'), ('HONOURS', 'HONOURS'), ('MASTERS', 'MASTERS')], max_length=10, verbose_name='Educational qualification:'),
        ),
        migrations.AlterField(
            model_name='admissionform',
            name='is_pharmacy_have',
            field=models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], max_length=10, verbose_name='Have any Pharmacy:'),
        ),
        migrations.AlterField(
            model_name='admissionform',
            name='marrietal_status',
            field=models.CharField(choices=[('MARRIED', 'MARRIED'), ('UNMARRIED', 'UNMARRIED')], max_length=50, verbose_name='Marrital status:'),
        ),
        migrations.AlterField(
            model_name='admissionform',
            name='religion',
            field=models.CharField(choices=[('ISLAM', 'ISLAM'), ('OTHERS', 'OTHERS')], default='ISLAM', max_length=10, verbose_name='Religion:'),
        ),
    ]
