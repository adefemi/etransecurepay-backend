from django.contrib import admin
from .models import UserProfile, UserAccounts, SwiftCode, TransactionLog

admin.site.register([UserProfile, UserAccounts, SwiftCode, TransactionLog])
