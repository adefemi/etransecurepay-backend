# Generated by Django 2.1 on 2018-08-15 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userControl', '0013_auto_20180813_0913'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactionlog',
            name='benName',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='transactionlog',
            name='sender',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='created_at',
            field=models.IntegerField(default=1534335495),
        ),
        migrations.AlterField(
            model_name='swiftcode',
            name='created_at',
            field=models.IntegerField(default=1534335495),
        ),
        migrations.AlterField(
            model_name='transactionlog',
            name='amount',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='transactionlog',
            name='bankname',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='transactionlog',
            name='benAccNum',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='transactionlog',
            name='benEmail',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='transactionlog',
            name='code',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='transactionlog',
            name='country',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='transactionlog',
            name='created_at',
            field=models.IntegerField(default=1534335495),
        ),
        migrations.AlterField(
            model_name='transactionlog',
            name='referenceNum',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='useraccounts',
            name='created_at',
            field=models.IntegerField(default=1534335495),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='created_at',
            field=models.IntegerField(default=1534335495),
        ),
    ]
