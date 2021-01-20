from django.db import models
from . import *


# Create your models here.

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CbCodeHdr(models.Model):  # 코드 헤더
    id = models.AutoField(db_column='id', primary_key=True)
    type_cd = models.CharField(db_column='type_cd', max_length=20)
    type_nm = models.CharField(db_column='type_nm', max_length=50)
    type_nmen = models.CharField(db_column='type_nmen', max_length=50)
    updt_dt = models.DateTimeField(db_column='updt_dt', auto_now=True)
    insrt_dt = models.DateTimeField(db_column='insrt_dt', auto_now_add=True)
    usage_fg = models.CharField(db_column='usage_fg', max_length=1, default='Y')
    insrt_id = models.IntegerField(db_column='insrt_id')
    updt_id = models.IntegerField(db_column='updt_id')

    class Meta:
        managed = False
        db_table = 'cb_code_hdr'


class CbCodeDtl(models.Model):  # 코드 detail
    id = models.AutoField(db_column='id', primary_key=True)
    type_cd = models.CharField(db_column='type_cd', max_length=20)
    code_cd = models.CharField(db_column='code_cd', max_length=20)
    cd_nm = models.CharField(db_column='cd_nm', max_length=50)
    cd_nmen = models.CharField(db_column='cd_nmen', max_length=50)
    updt_dt = models.DateTimeField(db_column='updt_dt', auto_now=True)
    insrt_dt = models.DateTimeField(db_column='insrt_dt', auto_now_add=True)
    usage_fg = models.CharField(db_column='usage_fg', max_length=1, default='Y')
    insrt_id = models.IntegerField(db_column='insrt_id')
    updt_id = models.IntegerField(db_column='updt_id')

    class Meta:
        managed = False
        db_table = 'cb_code_dtl'


class BCo(models.Model):  # 법인
    id = models.IntegerField(primary_key=True)
    co_cd = models.CharField(max_length=50, blank=True, null=True)
    co_nm = models.CharField(max_length=50, blank=True, null=True)
    co_shnm = models.CharField(max_length=50, blank=True, null=True)
    co_rpr = models.CharField(max_length=20, blank=True, null=True)
    co_type = models.CharField(max_length=20, blank=True, null=True)
    co_div = models.CharField(max_length=20, blank=True, null=True)
    co_estdt = models.DateTimeField(blank=True, null=True)
    co_strdt = models.DateTimeField(blank=True, null=True)
    sttl_dt = models.IntegerField(blank=True, null=True)
    # cn_cd = models.CharField(max_length=20, blank=True, null=True)
    # cur_cd = models.CharField(max_length=20, blank=True, null=True)
    # insrt_id = models.CharField(max_length=50, blank=True, null=True)
    # insrt_dt = models.DateTimeField(blank=True, null=True)
    # updt_user = models.CharField(max_length=50, blank=True, null=True)
    # updt_dt = models.DateTimeField(blank=True, null=True)
    usage_fg = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'b_co'


lass BBizarea(models.Model):  # 사업장 현준
    id = models.AutoField(db_column='id', primary_key=True)
    bizarea_cd = models.CharField(db_column='bizarea_cd', max_length=50, blank=True, null=True)
    co = models.ForeignKey(BCo, on_delete=models.CASCADE)
    bizarea_nm = models.CharField(db_column='bizarea_nm', max_length=50, blank=True, null=True)
    bizarea_shnm = models.CharField(db_column='bizarea_shnm', max_length=20, blank=True, null=True)
    biz_no = models.CharField(db_column='biz_no', max_length=50, blank=True, null=True)
    biz_rpr = models.CharField(db_column='biz_rpr', max_length=50, blank=True, null=True)
    str_dt = models.DateTimeField(db_column='str_dt', blank=True, null=True)
    unitcur= models.ForeignKey(CbCodeDtl, related_name='+', on_delete=models.CASCADE)
    unitcn= models.ForeignKey(CbCodeDtl, related_name='+', on_delete=models.CASCADE)
    usage_fg = models.CharField(db_column='usage_fg', max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'b_bizarea'


class BBizunit(models.Model):  # 사업부 현준
    id = models.AutoField(db_column='id', primary_key=True)
    bizunit_cd = models.CharField(db_column='bizunit_cd', max_length=50)
    bizunit_nm = models.CharField(db_column='bizunit_nm', max_length=50, blank=True, null=True)
    bizunit_rmrk = models.CharField(db_column='bizunit_rmrk', max_length=50, blank=True, null=True)
    insrt_id = models.IntegerField(db_column='insrt_id', max_length=50, blank=True, null=True)
    insrt_dt = models.DateTimeField(db_column='insrt_dt', auto_now_add=True, blank=True, null=True)
    updt_id = models.IntegerField(db_column='updt_id', max_length=50, blank=True, null=True)
    updt_dt = models.DateTimeField(db_column='updt_dt', auto_now=True, blank=True, null=True)
    usage_fg = models.CharField(db_column='usage_fg', max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'b_bizunit'


class BBizpartner(models.Model):  # 거래처
    id = models.AutoField(db_column='id', primary_key=True)
    bizpartner_cd = models.CharField(db_column='bizpartner_cd', max_length=50)
    # foreignkey연결 필요.
    co_id = models.IntegerField(db_column='co_id', max_length=50)
    bizpartner_type = models.CharField(db_column='bizpartner_type', max_length=20, blank=True, null=True)
    biz_nm = models.CharField(db_column='biz_nm', max_length=50, blank=True, null=True)
    bizpartner_nm = models.CharField(db_column='bizpartner_nm', max_length=50, blank=True, null=True)
    cn_cd = models.CharField(db_column='cn_cd', max_length=20, blank=True, null=True)
    cur_cd = models.CharField(db_column='cur_cd', max_length=20, blank=True, null=True)
    bizpartner_stat = models.CharField(db_column='bizpartner_stat', max_length=20, blank=True, null=True)
    insrt_id = models.IntegerField(db_column='insrt_id', max_length=50, blank=True, null=True)
    insrt_dt = models.DateTimeField(db_column='insrt_dt', blank=True, null=True, auto_now_add=True)
    updt_id = models.IntegerField(db_column='updt_id', max_length=50, blank=True, null=True)
    updt_dt = models.DateTimeField(db_column='updt_dt', blank=True, null=True, auto_now=True)
    usage_fg = models.CharField(db_column='usage_fg', max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'b_bizpartner'


class BFactory(models.Model):  # 공장
    id = models.AutoField(db_column='id', primary_key=True)
    factory_cd = models.CharField(max_length=20, blank=True, null=True)
    factory_nm = models.CharField(max_length=50, blank=True, null=True)
    factory_rmrk = models.CharField(max_length=50, blank=True, null=True)
    insrt_dt = models.DateTimeField(db_column='insrt_dt', blank=True, null=True, auto_now_add=True)
    updt_dt = models.DateTimeField(blank=True, null=True, auto_now=True)
    usage_fg = models.CharField(db_column='usage_fg', max_length=1, default='Y')
    user_id = models.IntegerField(db_column='user_id')

    class Meta:
        managed = False
        db_table = 'b_factory'


class BItemaccnt(models.Model):  # 품목계정
    id = models.IntegerField(db_column='id', primary_key=True)
    itemaccnt_cd = models.CharField(db_column='itemaccnt_cd', max_length=50)
    itemaccnt_nm = models.CharField(db_column='itemaccnt_nm', max_length=50, blank=True, null=True)
    insrt_dt = models.DateTimeField(db_column='insrt_dt', blank=True, null=True, auto_now_add=True)
    updt_dt = models.DateTimeField(db_column='updt_dt', blank=True, null=True, auto_now=True)
    usage_fg = models.CharField(db_column='usage_fg', max_length=1, default='Y')
    user_id = models.IntegerField(db_column='user_id')

    class Meta:
        managed = False
        db_table = 'b_itemaccnt'


class BItemgrp(models.Model):  # 품목그룹
    id = models.IntegerField(db_column='id', primary_key=True)
    itemgrp_cd = models.CharField(db_column='itemgrp_cd', max_length=50, blank=True, null=True)
    itemgrp_nm = models.CharField(db_column='itemgrp_nm', max_length=50, blank=True, null=True)
    insrt_dt = models.DateTimeField(db_column='insrt_dt', blank=True, null=True, auto_now_add=True)
    updt_dt = models.DateTimeField(db_column='updt_dt', blank=True, null=True, auto_now=True)
    usage_fg = models.CharField(db_column='usage_fg', max_length=1, default='Y')
    user_id = models.IntegerField(db_column='user_id')

    class Meta:
        managed = False
        db_table = 'b_itemgrp'


class BItem(models.Model):  # 품목마스터
    id = models.AutoField(db_column='id', primary_key=True)
    itemaccnt = models.ForeignKey(BItemaccnt, on_delete=models.CASCADE)
    factory = models.ForeignKey(BFactory, on_delete=models.CASCADE)
    itemgrp = models.ForeignKey(BItemgrp, on_delete=models.CASCADE)
    item_cd = models.CharField(db_column='item_cd', max_length=50)
    item_nm = models.CharField(db_column='item_nm', max_length=50, blank=True, null=True)
    item_spec = models.CharField(db_column='item_spec', max_length=50, blank=True, null=True)
    phantom_div = models.CharField(db_column='phantom_div', max_length=1, blank=True, null=True)
    insrt_dt = models.DateTimeField(db_column='insrt_dt', blank=True, null=True, auto_now_add=True)
    updt_dt = models.DateTimeField(db_column='updt_dt', blank=True, null=True, auto_now=True)
    usage_fg = models.CharField(db_column='usage_fg', max_length=1, default='Y')
    unit_id = models.IntegerField(db_column='unit_id', default=0)
    user_id = models.IntegerField(db_column='user_id')
    bom_fg = models.CharField(db_column='bom_fg', max_length=8, default='0')


    class Meta:
        managed = False
        db_table = 'b_item'


class BUser(models.Model):  # 사용자관리
    id = models.AutoField(db_column='id', primary_key=True)
    user_id = models.CharField(db_column='user_id', max_length=50)
    user_nm = models.CharField(db_column='user_nm', max_length=50, blank=True, null=True)
    psswd = models.CharField(db_column='psswd', max_length=255)
    email = models.CharField(db_column='email', max_length=255, blank=True, null=True)
    phoneno = models.CharField(db_column='phoneno', max_length=20, blank=True, null=True)
    insrt_id = models.IntegerField(db_column='insrt_id', max_length=11, blank=True, null=True)
    insrt_dt = models.DateTimeField(db_column='insrt_dt', blank=True, null=True, auto_now_add=True)
    updt_id = models.IntegerField(db_column='updt_id', max_length=11, blank=True, null=True)
    updt_dt = models.DateTimeField(db_column='updt_dt', blank=True, null=True, auto_now=True)
    usage_fg = models.CharField(db_column='usage_fg', max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'b_user'


class BWorkcenter(models.Model):  # 작업장
    workcenter_cd = models.CharField(max_length=50, blank=True, null=True)
    workcenter_nm = models.CharField(max_length=50, blank=True, null=True)
    cstctr_id = models.CharField(max_length=50, blank=True, null=True)
    insrt_id = models.CharField(max_length=50, blank=True, null=True)
    insrt_dt = models.DateTimeField(blank=True, null=True)
    updt_user = models.CharField(max_length=50, blank=True, null=True)
    updt_dt = models.DateTimeField(blank=True, null=True)
    usage_fg = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'b_workcenter'


class BomDtl(models.Model):  # BOM 디테일
    invt_asset = models.CharField(max_length=20, blank=True, null=True)
    item_div1 = models.CharField(max_length=50, blank=True, null=True)
    revision = models.CharField(max_length=20, blank=True, null=True)
    ip_unit = models.CharField(max_length=50, blank=True, null=True)
    ip_am = models.IntegerField(blank=True, null=True)
    loss = models.IntegerField(blank=True, null=True)
    ip_div = models.CharField(max_length=50, blank=True, null=True)
    fair = models.CharField(max_length=50, blank=True, null=True)
    apply_strdt = models.DateTimeField(blank=True, null=True)
    apply_enddt = models.DateTimeField(blank=True, null=True)
    rmrk = models.CharField(max_length=50, blank=True, null=True)
    cnt = models.CharField(max_length=50, blank=True, null=True)
    crtdt = models.DateTimeField(blank=True, null=True)
    updt_user = models.CharField(max_length=50, blank=True, null=True)
    udt_dt = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bom_dtl'


class BBom(models.Model):  # BOM 메인
    id = models.AutoField(db_column='id', primary_key=True)
    bom_type = models.CharField(db_column='bom_type', max_length=20)
    item = models.ForeignKey(BItem, on_delete=models.DO_NOTHING)
    parent_id = models.IntegerField(db_column='parent_id', default=0)
    top_id = models.IntegerField(db_column='top_id', default=0)
    bom_order = models.IntegerField(db_column='bom_order', default=0)
    bom_level = models.IntegerField(db_column='bom_level', default=0)
    leaf_fg = models.CharField(db_column='leaf_fg', max_length=10, default='1')
    moitem_base = models.FloatField(db_column='moitem_base', default=0.0)
    jaitem_base = models.FloatField(db_column='jaitem_base', default=0.0)
    unit_product = models.CharField(db_column='unit_product', max_length=50)
    free_fg = models.CharField(db_column='free_fg', max_length=10, default='1')
    loss_product = models.FloatField(db_column='loss_product', default=0.0)
    demand_amt = models.FloatField(db_column='demand_amt', default=0.0)
    start_dt = models.CharField(db_column='start_dt', max_length=8)
    end_dt = models.CharField(db_column='end_dt', max_length=8)
    register_dt = models.DateTimeField(db_column='register_dt', )
    usage_fg = models.CharField(db_column='usage_fg', max_length=10, default='1')

    class Meta:
        managed = False
        db_table = 'b_bom'

    def __str__(self):
        return "BOM id : " + str(self.id) + " Type : " + self.bom_type


class CbCostCenter(models.Model):  # 코스트센터
    id = models.IntegerField(primary_key=True)
    cstctr_cd = models.CharField(max_length=50, blank=True, null=True)
    cstctr_nm = models.CharField(max_length=50, blank=True, null=True)
    bizarea_id = models.IntegerField(blank=True, null=True)
    bizunit_id = models.IntegerField(blank=True, null=True)
    factory_id = models.IntegerField(blank=True, null=True)
    cstctr_type = models.CharField(max_length=50, blank=True, null=True)
    cstctr_dir_div = models.CharField(max_length=50, blank=True, null=True)
    insrt_id = models.IntegerField(blank=True, null=True)
    updt_dt = models.DateTimeField(blank=True, null=True)
    insrt_dt = models.DateTimeField(blank=True, null=True)
    usage_fg = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cb_cost_center'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'
