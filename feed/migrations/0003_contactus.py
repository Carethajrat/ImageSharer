# Generated by Django 4.2 on 2023-04-21 07:00

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0002_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=140,null=False,blank=False)),
                ('mobile', phonenumber_field.modelfields.PhoneNumberField(max_length=13, region=None, unique=True)),
                ('message', models.TextField()),
            ],
        ),
    ]