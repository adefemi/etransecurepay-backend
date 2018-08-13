from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('usersprofile', views.UserProfileViewSet)
router.register('useraccount', views.UserAccountViewSet)
router.register('swiftcode', views.SwiftCodeViewSet)
router.register('transaction', views.TransactionLogViewSet)
router.register('enquiry', views.EnquiryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('updatepassword/<pk>', views.ChangePasswordView.as_view()),
    path('updateadmin/<pk>', views.UpdateAdminView.as_view()),
]