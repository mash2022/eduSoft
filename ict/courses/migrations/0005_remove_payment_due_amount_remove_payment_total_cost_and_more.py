# Generated by Django 4.1.7 on 2024-01-03 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_committee_member_voice_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='due_amount',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='total_cost',
        ),
        migrations.AddField(
            model_name='payment',
            name='balance',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='payment',
            name='payment_month',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='payment_amount',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='total_cost',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cost', to='courses.course'),
        ),
        migrations.AlterField(
            model_name='course',
            name='total_cost',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_amount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='student_info',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.studentinfo'),
        ),
    ]
