from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    account_number = models.CharField(default=000000, max_length=256)
    secret_key = models.CharField(blank=False, max_length=256, default=0)
    status = models.BooleanField(default=False)
    created_at = models.IntegerField(default=int(datetime.now().timestamp()))

    def __str__(self):
        return self.user.username

class UserAccounts(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    royaleAVB = models.FloatField(default=0.0, blank=True, null=True)
    checkingAVB = models.FloatField(default=0.0, blank=True, null=True)
    royalePNB = models.FloatField(default=0.0, blank=True, null=True)
    checkingPNB = models.FloatField(default=0.0, blank=True, null=True)
    created_at = models.IntegerField(default=int(datetime.now().timestamp()))

    def __str__(self):
        return self.user.username

class SwiftCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(default="", max_length=20)
    created_at = models.IntegerField(default=int(datetime.now().timestamp()))

    def __str__(self):
        return self.user.username

class TransactionLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.CharField(default="0.0", max_length=200)
    bankname = models.CharField(max_length=200)
    benEmail = models.EmailField()
    benAccNum = models.CharField(max_length=256)
    code = models.CharField(max_length=20)
    country = models.CharField(max_length=500)
    referenceNum = models.CharField(max_length=20)
    htmlTemplate = models.TextField(default="")
    created_at = models.IntegerField(default=int(datetime.now().timestamp()))

    def __str__(self):
        return self.user.username+" - "+self.referenceNum