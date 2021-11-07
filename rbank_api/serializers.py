from  rest_framework import serializers
from .models import Member
from .models import Account

class MemberSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Member
    fields = ('id','first_name', 'last_name', 'birthday', 'ssn', 'address_one', 'address_two', 'city', 'state', 'zip_code')

class AccountSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Account
    fields = ('id','open_date', 'close_date', 'activity_date', 'member_id')