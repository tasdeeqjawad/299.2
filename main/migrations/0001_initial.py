# Generated by Django 4.2.7 on 2023-11-22 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.IntegerField(db_column='Customer_ID', primary_key=True, serialize=False)),
                ('fname', models.CharField(db_column='Fname', max_length=200)),
                ('lname', models.CharField(db_column='Lname', max_length=200)),
                ('email', models.CharField(blank=True, db_column='Email', max_length=200, null=True)),
                ('age', models.IntegerField(blank=True, db_column='Age', null=True)),
                ('gender', models.CharField(blank=True, db_column='Gender', max_length=200, null=True)),
                ('passwrd', models.CharField(db_column='Passwrd', max_length=200)),
            ],
            options={
                'db_table': 'customer',
                'managed': False,
            },
        ),
    ]