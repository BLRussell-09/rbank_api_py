from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MemberSerializer, AccountSerializer
from .models import Member, Account
# Create your views here.

class MemberViewSet(viewsets.ModelViewSet):
  queryset = Member.objects.all().order_by('first_name')
  serializer_class = MemberSerializer

class AccountViewSet(viewsets.ModelViewSet):
  serializer_class = AccountSerializer

  def get_queryset(self):
    queryset = Account.objects.all()
    member_num = self.request.query_params.get('member_num')
    if member_num is not None:
      queryset = queryset.filter(member_id=member_num)
    return queryset
