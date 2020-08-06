# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=128)
    student_size = models.IntegerField(blank=True, null=True)
    avg_net_price = models.IntegerField(blank=True, null=True)
    median_earnings = models.IntegerField(blank=True, null=True)
    predominant = models.CharField(max_length=128, blank=True, null=True)
    ddsdd = models.CharField(max_length=12)

    class Meta:
        managed = True
        db_table = 'test'

class College(models.Model):
    college_name = models.CharField(max_length=128, db_column='college', unique=True)
    state = models.CharField(max_length=32, blank=True, null=True)
    city = models.CharField(max_length=32, blank=True, null=True)
    cost = models.FloatField(blank=True, null=True)
    student_size = models.IntegerField(blank=True, null=True)
    avg_price = models.FloatField(blank=True, null=True)
    percent_greater_than_25k = models.FloatField(blank=True, null=True)
    predominant = models.CharField(max_length=64, blank=True, null=True)
    consumer_rate = models.FloatField(blank=True, null=True)
    type = models.CharField(max_length=32, blank=True, null=True)
    position = models.CharField(max_length=32, blank=True, null=True)

    def __str__(self):
        return self.college_name

    class Meta:
        db_table = 'college'
        unique_together = (('id', 'college_name'),)


class CollegeDetail(models.Model):
    college_name = models.ForeignKey(College, models.DO_NOTHING, to_field='college_name', db_column='college')
    year = models.CharField(max_length=16)
    acceptance_rate = models.FloatField(blank=True, null=True)
    student_count = models.IntegerField(blank=True, null=True)
    sat_math = models.CharField(max_length=16, blank=True, null=True)
    sat_critical_reading = models.CharField(max_length=16, blank=True, null=True)
    sat_writing = models.CharField(max_length=16, blank=True, null=True)
    act_math = models.CharField(max_length=16, blank=True, null=True)
    act_writing = models.CharField(max_length=16, blank=True, null=True)
    act_cumulative = models.CharField(max_length=16, blank=True, null=True)
    act_english = models.CharField(max_length=16, blank=True, null=True)
    full_time = models.FloatField(blank=True, null=True)
    part_time = models.FloatField(blank=True, null=True)

    def __str__(self):
        return ':'.join([self.year, self.college_name.college_name])

    class Meta:
        db_table = 'college_detail'
        unique_together = (('year', 'college_name'),)


class Major(models.Model):
    college_name = models.ForeignKey(College, models.DO_NOTHING, to_field='college_name', db_column='college')
    year = models.CharField(max_length=16)
    major = models.CharField(max_length=128)
    credential = models.CharField(max_length=64, blank=True, null=True)
    graduates_count = models.IntegerField(blank=True, null=True)
    avg_earning = models.CharField(max_length=32, blank=True, null=True)

    def __str__(self):
        return ':'.join([self.year, self.major])

    class Meta:
        db_table = 'major'


class PayAllBachelors(models.Model):
    rank = models.IntegerField()
    college_name = models.CharField(max_length=64, db_column='college')
    type = models.CharField(max_length=64, blank=True, null=True)
    early_career_pay = models.CharField(max_length=64, blank=True, null=True)
    mid_career_pay = models.CharField(max_length=64, blank=True, null=True)
    high_meaning = models.CharField(max_length=16, blank=True, null=True)
    stem_degrees = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'pay_all_bachelors'
        unique_together = (('id', 'rank'),)


class PayBachelors(models.Model):
    rank = models.IntegerField()
    college_name = models.CharField(max_length=64, db_column='college')
    type = models.CharField(max_length=64, blank=True, null=True)
    early_career_pay = models.CharField(max_length=64, blank=True, null=True)
    mid_career_pay = models.CharField(max_length=64, blank=True, null=True)
    high_meaning = models.CharField(max_length=16, blank=True, null=True)
    stem_degrees = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'pay_bachelors'
        unique_together = (('id', 'rank'),)


class PayCity(models.Model):
    state = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    pay = models.CharField(max_length=64, blank=True, null=True)
    hourly_pay = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'pay_city'

