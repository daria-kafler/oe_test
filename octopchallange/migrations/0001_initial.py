# Generated by Django 4.2.5 on 2023-09-17 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mpan', models.IntegerField()),
                ('meter_id', models.CharField(max_length=10)),
                ('meter_register', models.CharField(max_length=2)),
                ('reading_date_time', models.DateTimeField()),
                ('register_reading', models.DecimalField(decimal_places=1, max_digits=10)),
            ],
        ),
    ]
