# Generated by Django 5.1.6 on 2025-02-19 17:49
from django.db import migrations
class Migration(migrations.Migration):
    dependencies = [
        ('complaints', '0003_complaint_image_complaint_ip_address_and_more'),
    ]
    operations = [
        migrations.RemoveField(
            model_name='complaint',
            name='ip_address',
        ),
        migrations.RemoveField(
            model_name='complaint',
            name='location',
        ),
        migrations.RemoveField(
            model_name='complaint',
            name='resolution',
        ),
    ]
