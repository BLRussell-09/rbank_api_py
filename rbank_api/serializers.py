from  rest_framework import serializers
from .models import Member

class MemberSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Member
    fields = ('id','first_name', 'last_name', 'birthday', 'ssn', 'address_one', 'address_two', 'city', 'state', 'zip_code')