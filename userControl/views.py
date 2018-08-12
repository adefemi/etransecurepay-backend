from rest_framework import viewsets, response, permissions, status, generics
from .serializers import UserSerializer, UserProfileSerializer, UserAccountSerializer, ChangePasswordSerializer, UpdateAdminSerializer, SwiftCodeSerializer, TransactionLogSerializer
from .models import UserProfile, UserAccounts, SwiftCode, TransactionLog
from django.contrib.auth.models import User
from .sendEmail import SendMail

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

class UserAccountViewSet(viewsets.ModelViewSet):
    queryset = UserAccounts.objects.all()
    serializer_class = UserAccountSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class SwiftCodeViewSet(viewsets.ModelViewSet):
    queryset = SwiftCode.objects.all()
    serializer_class = SwiftCodeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    queryset = User.objects.all()
    model = User
    permission_classes = (permissions.IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return response.Response({"old_password": ["The old password provided is wrong"]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return response.Response("Success.", status=status.HTTP_200_OK)

        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateAdminView(generics.UpdateAPIView):
    serializer_class = UpdateAdminSerializer
    queryset = User.objects.all()
    model = User
    permission_classes = (permissions.IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            print(self.object.username)
            self.object.username = serializer.data.get("username")
            self.object.save()
            return response.Response("Success.", status=status.HTTP_200_OK)

        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TransactionLogViewSet(viewsets.ModelViewSet):
    queryset = TransactionLog.objects.all()
    serializer_class = TransactionLogSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            try:
                Log = serializer.save()
            except Exception as e:
                return response.Response(e, status=status.HTTP_400_BAD_REQUEST)

            SendMail(Log.user.email, Log.bankname, Log.benAccNum, str(Log.amount), Log.country, Log.referenceNum, Log.benEmail)

            return response.Response("message send", status=status.HTTP_200_OK)


        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






