# Generated by Django 2.1 on 2018-08-10 22:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userControl', '0004_auto_20180810_1032'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bankname', models.CharField(max_length=200)),
                ('benEmail', models.EmailField(max_length=254)),
                ('benAccNum', models.CharField(max_length=256)),
                ('swiftcode', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('referenceNum', models.CharField(max_length=20)),
                ('created_at', models.IntegerField(default=1533940856)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='swiftcode',
            name='created_at',
            field=models.IntegerField(default=1533940856),
        ),
        migrations.AlterField(
            model_name='useraccounts',
            name='created_at',
            field=models.IntegerField(default=1533940856),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='account_number',
            field=models.CharField(default=0, max_length=256),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='created_at',
            field=models.IntegerField(default=1533940856),
        ),
    ]
