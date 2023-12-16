# Generated by Django 4.1.7 on 2023-12-16 16:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0019_rmplmf'),
    ]

    operations = [
        migrations.AddField(
            model_name='rmplmf',
            name='student_image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='student_pic'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rmplmf',
            name='age',
            field=models.CharField(max_length=50, verbose_name='Age:'),
        ),
        migrations.AlterField(
            model_name='rmplmf',
            name='blood_group',
            field=models.CharField(max_length=20, verbose_name='Blood group:'),
        ),
        migrations.AlterField(
            model_name='rmplmf',
            name='district_ban',
            field=models.CharField(max_length=100, verbose_name='District:'),
        ),
        migrations.AlterField(
            model_name='rmplmf',
            name='district_eng',
            field=models.CharField(max_length=100, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='rmplmf',
            name='edu_qualification',
            field=models.CharField(choices=[('SSC', 'ssc'), ('HSC', 'hsc'), ('HONOURS', 'Honours'), ('MASTERS', 'Masters')], max_length=10, verbose_name='Educational qualification:'),
        ),
        migrations.AlterField(
            model_name='rmplmf',
            name='father_or_hus_name_ban',
            field=models.CharField(max_length=150, verbose_name='Father/Husband name:'),
        ),
        migrations.AlterField(
            model_name='rmplmf',
            name='father_or_hus_name_eng',
            field=models.CharField(max_length=150, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='rmplmf',
            name='is_pharmacy_have',
            field=models.CharField(choices=[('YES', 'Yes'), ('No', 'No')], max_length=10, verbose_name='Have any Pharmacy:'),
        ),
        migrations.AlterField(
            model_name='rmplmf',
            name='marrietal_status',
            field=models.CharField(choices=[('MARRIED', 'Married'), ('UNMARRIED', 'Unmarried')], max_length=50, verbose_name='Marrital status:'),
        ),
        migrations.AlterField(
            model_name='rmplmf',
            name='mobile',
            field=models.CharField(max_length=20, verbose_name='Mobile number:'),
        ),
        migrations.AlterField(
            model_name='rmplmf',
            name='nationality',
            field=models.CharField(max_length=100, verbose_name='Nationality:'),
        ),
        migrations.AlterField(
            model_name='rmplmf',
            name='nid',
            field=models.IntegerField(verbose_name='National ID no.:'),
        ),
        migrations.AlterField(
            model_name='rmplmf',
            name='past_training_name',
            field=models.CharField(max_length=100, verbose_name='Have any training:'),
        ),
        migrations.AlterField(
            model_name='rmplmf',
            name='pharmacy_name_address',
            field=models.CharField(max_length=255, verbose_name='Pharmacy name and address:'),
        ),
        migrations.AlterField(
            model_name='rmplmf',
            name='post_office_ban',
            field=models.CharField(max_length=100, verbose_name='Post office:'),
        ),
        migrations.AlterField(
            model_name='rmplmf',
            name='post_office_eng',
            field=models.CharField(max_length=100, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='rmplmf',
            name='religion',
            field=models.CharField(choices=[('ISLAM', 'Islam'), ('HINDU', 'Hindu'), ('CHRITIAN', 'Christian'), ('OTHERS', 'Others')], default='ISLAM', max_length=10, verbose_name='Religion:'),
        ),
        migrations.AlterField(
            model_name='rmplmf',
            name='student_name_ban',
            field=models.CharField(max_length=150, verbose_name='Student name:'),
        ),
        migrations.AlterField(
            model_name='rmplmf',
            name='student_name_eng',
            field=models.CharField(max_length=150, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='rmplmf',
            name='upozila_ban',
            field=models.CharField(max_length=100, verbose_name='Upazilla:'),
        ),
        migrations.AlterField(
            model_name='rmplmf',
            name='upozila_eng',
            field=models.CharField(max_length=100, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='rmplmf',
            name='village_ban',
            field=models.CharField(max_length=100, verbose_name='Village:'),
        ),
        migrations.AlterField(
            model_name='rmplmf',
            name='village_eng',
            field=models.CharField(max_length=100, verbose_name=''),
        ),
    ]
