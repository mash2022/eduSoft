# Generated by Django 4.1.7 on 2023-12-21 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_rename_studentinfo_paymentadmission_student_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymentadmission',
            name='student_id',
        ),
        migrations.AddField(
            model_name='paymentadmission',
            name='studentInfo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.studentinfo'),
        ),
    ]
