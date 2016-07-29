# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Products3', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('orderId', models.CharField(max_length=15)),
                ('orderPlacedDate', models.DateTimeField(auto_now=True)),
                ('deliveryDate', models.DateField(null=True)),
                ('orderDelivered', models.BooleanField(default=False)),
                ('orderCancelled', models.BooleanField(default=False)),
                ('isBasicAddress', models.BooleanField(default=True)),
                ('orderAmount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='orderDeliveryDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone', models.CharField(default=b'', max_length=12)),
                ('street_address', models.CharField(max_length=100, null=True, blank=True)),
                ('city', models.CharField(max_length=20, null=True, blank=True)),
                ('pincode', models.CharField(default=b'0000000', max_length=8)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='isNotBasicAddress',
            field=models.ForeignKey(blank=True, to='orders.orderDeliveryDetails', null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='productCode',
            field=models.ForeignKey(to='Products3.Product'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
