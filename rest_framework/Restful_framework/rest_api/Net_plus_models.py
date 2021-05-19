# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cod100(models.Model):
    mjr_cd = models.CharField(primary_key=True, max_length=20)
    mnr_cd = models.CharField(max_length=20)
    nm = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'COD100'
        unique_together = (('mjr_cd', 'mnr_cd'),)
        app_label = 'Net_plus'


class Cop100(models.Model):
    id = models.AutoField(primary_key=True)
    co_cd = models.CharField(max_length=50, blank=True, null=True)
    cc_cd = models.CharField(max_length=50, blank=True, null=True)
    ver_cd = models.CharField(max_length=50, blank=True, null=True)
    acc_cd = models.CharField(max_length=50, blank=True, null=True)
    yyyymm = models.CharField(max_length=6, blank=True, null=True)
    amt = models.IntegerField(blank=True, null=True)
    mng = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'COP100'
        app_label = 'Net_plus'


class Cop200(models.Model):
    id = models.AutoField(primary_key=True)
    fac_cd = models.CharField(max_length=50, blank=True, null=True)
    co_cd = models.CharField(max_length=50, blank=True, null=True)
    acc_cd = models.CharField(max_length=50, blank=True, null=True)
    ver_cd = models.CharField(max_length=50, blank=True, null=True)
    biz_cd = models.CharField(max_length=50, blank=True, null=True)
    bom_cd = models.CharField(max_length=50, blank=True, null=True)
    yyyymm = models.CharField(max_length=6, blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)
    amt = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'COP200'
        app_label = 'Net_plus'


class Cop300(models.Model):
    id = models.AutoField(primary_key=True)
    co_cd = models.CharField(max_length=50, blank=True, null=True)
    bom_cd = models.CharField(max_length=50, blank=True, null=True)
    acc_cd = models.CharField(max_length=50, blank=True, null=True)
    ver_cd = models.CharField(max_length=50, blank=True, null=True)
    amt = models.IntegerField(blank=True, null=True)
    yyyymm = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'COP300'
        app_label = 'Net_plus'


class Cop400(models.Model):
    id = models.AutoField(primary_key=True)
    fac_cd = models.CharField(max_length=50, blank=True, null=True)
    ver_cd = models.CharField(max_length=50, blank=True, null=True)
    acc_cd = models.CharField(max_length=50, blank=True, null=True)
    itm_cd = models.CharField(max_length=50, blank=True, null=True)
    bas_qty = models.IntegerField(blank=True, null=True)
    bas_amt = models.IntegerField(blank=True, null=True)
    pro_in_qty = models.IntegerField(blank=True, null=True)
    pro_in_amt = models.IntegerField(blank=True, null=True)
    sal_out_qty = models.IntegerField(blank=True, null=True)
    sal_out_amt = models.IntegerField(blank=True, null=True)
    loss_out_qty = models.IntegerField(blank=True, null=True)
    loss_out_amt = models.IntegerField(blank=True, null=True)
    dev_out_qty = models.IntegerField(blank=True, null=True)
    dev_out_amt = models.IntegerField(blank=True, null=True)
    end_qty = models.IntegerField(blank=True, null=True)
    end_amt = models.IntegerField(blank=True, null=True)
    yyyymm = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'COP400'
        app_label = 'Net_plus'


class Test(models.Model):
    id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test'
        app_label = 'Net_plus'
