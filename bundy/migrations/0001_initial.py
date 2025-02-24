# Generated by Django 5.1.6 on 2025-02-24 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jacket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typ', models.CharField(choices=[('kabát', 'Kabát'), ('bunda', 'Bunda'), ('bomber', 'Bomber')], max_length=20)),
                ('color', models.CharField(default='#ffffff', max_length=7)),
            ],
        ),
    ]
