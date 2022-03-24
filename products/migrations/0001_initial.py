# Generated by Django 4.0.3 on 2022-03-24 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('product_image', models.ImageField(upload_to='')),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]
