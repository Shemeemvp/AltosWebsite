# Generated by Django 4.1 on 2023-01-03 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery_img', models.FileField(upload_to='events')),
                ('img_cre_date', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
    ]
