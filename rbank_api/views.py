from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MemberSerializer
from .models import Member
# Create your views here.

class MemberViewSet(viewsets.ModelViewSet):
  queryset = Member.objects.all().order_by('first_name')
  serializer_class = MemberSerializer