# Generated by Django 2.2.10 on 2020-06-21 02:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shared_schedule', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.CharField(blank=True, max_length=2, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='event',
            name='allDay',
        ),
        migrations.RemoveField(
            model_name='event',
            name='editable',
        ),
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.CharField(blank=True, max_length=99, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='start',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(blank=True, max_length=99, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='resourceId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shared_schedule.Resource'),
        ),
    ]
