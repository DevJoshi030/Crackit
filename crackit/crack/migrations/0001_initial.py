# Generated by Django 3.1.6 on 2021-02-10 12:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=55)),
                ('email', models.EmailField(max_length=255)),
                ('phone_no', models.IntegerField(blank=True, null=True, validators=[django.core.validators.RegexValidator('^0?[5-9]{1}\\d{9}$')])),
                ('website', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('message', models.TextField()),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
    ]
