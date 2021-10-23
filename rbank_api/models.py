from django.db import models
from datetime import date
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db.models.deletion import CASCADE

# Create your models here.
class Member(models.Model):
  STATES = [
    ('ALABAMA', 'AL'),
    ('ALASKA', 'AK'),
    ('AMERICAN SAMOA', 'AS'),
    ('ARIZONA', 'AZ'),
    ('ARKANSAS', 'AR'),
    ('CALIFORNIA', 'CA'),
    ('COLORADO', 'CO'),
    ('CONNECTICUT', 'CT'),
    ('DELAWARE', 'DE'),
    ('DISTRICT OF COLUMBIA', 'DC'),
    ('FLORIDA', 'FL'),
    ('GEORGIA', 'GA'),
    ('GUAM', 'GU'),
    ('HAWAII', 'HI'),
    ('IDAHO', 'ID'),
    ('ILLINOIS', 'IL'),
    ('INDIANA', 'IN'),
    ('IOWA', 'IA'),
    ('KANSAS', 'KS'),
    ('KENTUCKY', 'KY'),
    ('LOUISIANA', 'LA'),
    ('MAINE', 'ME'),
    ('MARYLAND', 'MD'),
    ('MASSACHUSETTS', 'MA'),
    ('MICHIGAN', 'MI'),
    ('MINNESOTA', 'MN'),
    ('MISSISSIPPI', 'MS'),
    ('MISSOURI', 'MO'),
    ('MONTANA', 'MT'),
    ('NEBRASKA', 'NE'),
    ('NEVADA', 'NV'),
    ('NEW HAMPSHIRE', 'NH'),
    ('NEW JERSEY', 'NJ'),
    ('NEW MEXICO', 'NM'),
    ('NEW YORK', 'NY'),
    ('NORTH CAROLINA', 'NC'),
    ('NORTH DAKOTA', 'ND'),
    ('NORTHERN MARIANA IS', 'MP'),
    ('OHIO', 'OH'),
    ('OKLAHOMA', 'OK'),
    ('OREGON', 'OR'),
    ('PENNSYLVANIA', 'PA'),
    ('PUERTO RICO', 'PR'),
    ('RHODE ISLAND', 'RI'),
    ('SOUTH CAROLINA', 'SC'),
    ('SOUTH DAKOTA', 'SD'),
    ('TENNESSEE', 'TN'),
    ('TEXAS', 'TX'),
    ('UTAH', 'UT'),
    ('VERMONT', 'VT'),
    ('VIRGINIA', 'VA'),
    ('VIRGIN ISLANDS', 'VI'),
    ('WASHINGTON', 'WA'),
    ('WEST VIRGINIA', 'WV'),
    ('WISCONSIN', 'WI'),
    ('WYOMING', 'WY'),
  ]
  first_name = models.CharField(max_length=40)
  last_name = models.CharField(max_length=60)
  birthday = models.DateField(blank=False,default=date.today)
  ssn = models.CharField(default='000000000', max_length=9, validators=[MaxLengthValidator(9), MinLengthValidator(9)])
  address_one = models.CharField(max_length=60)
  address_two = models.CharField(blank=True, max_length=60)
  city = models.CharField(max_length=60)
  state = models.CharField(max_length=30, choices=STATES)
  zip_code = models.CharField(max_length=15)

  def __str__(self):
    member = f'{self.id} - {self.first_name} {self.last_name}'
    return member

class Account(models.Model):
  open_date = models.DateField(blank=False, default=date.today)
  close_date = models.DateField(blank=True, null=True)
  activity_date = models.DateField(auto_now=True)
  member_id = models.ForeignKey(Member, on_delete=models.CASCADE, default='0000000000')

  def __str__(self):
    return f'{self.id} - {self.member_id}'

class Share(models.Model):
  SHARE_TYPES = [
    ('001', 'Checking'),
    ('002', 'Savings')
  ]
  acct_id = models.ForeignKey(Account, on_delete=models.CASCADE)
  open_date = models.DateField(blank=False, default=date.today)
  balance = models.DecimalField(max_digits=30, decimal_places=2)
  close_date = models.DateField(blank=True, null=True)
  share_type = models.CharField(max_length=30, choices=SHARE_TYPES)
  def __str__(self):
    return f'{self.acct_id} - {self.share_type}'

class Transaction(models.Model):
  TRANSACTION_TYPE = [
    ('C', 'Credit'),
    ('D', 'Debit'),
    ('T', 'Transfer')
  ]
  share_id = models.ForeignKey(Share, on_delete=models.CASCADE)
  originator = models.CharField(max_length=80)
  amount = models.DecimalField(max_digits=30, decimal_places=2)
  transaction_type = models.CharField(max_length=30, choices=TRANSACTION_TYPE)

  def __str__(self):
    return f'{self.originator} - {self.amount} - {self.share_id}'