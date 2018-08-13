from django.contrib import admin
from .models import UserProfile, UserAccounts, SwiftCode, TransactionLog, Enquiry

admin.site.register([UserProfile, UserAccounts, SwiftCode, TransactionLog, Enquiry])
