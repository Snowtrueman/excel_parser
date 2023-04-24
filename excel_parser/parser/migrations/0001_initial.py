# Generated by Django 4.2 on 2023-04-23 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_id', models.IntegerField(verbose_name='ID компании')),
                ('company_name', models.CharField(max_length=255, verbose_name='Наименование компании')),
                ('date', models.DateField(verbose_name='Дата')),
                ('qliq', models.IntegerField(verbose_name='Qliq')),
                ('qoil', models.IntegerField(verbose_name='Qoil')),
                ('data_type', models.CharField(choices=[('0', 'fact'), ('1', 'forecast')], max_length=10, verbose_name='Тип данных')),
            ],
            options={
                'ordering': ['id'],
                'unique_together': {('company_id', 'date', 'data_type')},
            },
        ),
    ]
