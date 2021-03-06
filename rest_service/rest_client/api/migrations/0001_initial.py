# Generated by Django 3.2.8 on 2022-05-03 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=40)),
                ('vin', models.CharField(max_length=40)),
                ('state', models.CharField(choices=[('U', 'in use'), ('S', 'in_service'), ('M', 'maintanance'), ('D', 'disabled')], default='D', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('state', models.CharField(choices=[('P', 'pending'), ('I', 'in progress'), ('R', 'resolved'), ('D', 'declined')], default='P', max_length=1)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.vehicle')),
            ],
        ),
    ]
