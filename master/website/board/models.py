from django.db import models


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
class BCo(models.Model):  # 법인
    co_cd = models.CharField(max_length=50, blank=True, null=True)
    co_nm = models.CharField(max_length=50, blank=True, null=True)
    co_shnm = models.CharField(max_length=50, blank=True, null=True)
    rpr = models.CharField(max_length=20, blank=True, null=True)
    co_type = models.CharField(max_length=20, blank=True, null=True)
    co_div = models.CharField(max_length=20, blank=True, null=True)
    co_estdt = models.DateTimeField(blank=True, null=True)
    co_strdt = models.DateTimeField(blank=True, null=True)
    sttl_dt = models.IntegerField(blank=True, null=True)
    cn_cd = models.CharField(max_length=20, blank=True, null=True)
    cur_cd = models.CharField(max_length=20, blank=True, null=True)
    insrt_id = models.CharField(max_length=50, blank=True, null=True)
    insrt_dt = models.DateTimeField(blank=True, null=True)
    updt_user = models.CharField(max_length=50, blank=True, null=True)
    updt_dt = models.DateTimeField(blank=True, null=True)
    usage_fg = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'b_co'

class BBizarea(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    bizarea_cd = models.CharField(max_length=50, blank=True, null=True)
    co_id = models.ForeignKey(BCo,on_delete=models.CASCADE)
    bizarea_nm = models.CharField(max_length=50, blank=True, null=True)
    bizarea_shnm = models.CharField(max_length=20, blank=True, null=True)
    biz_no = models.CharField(max_length=50, blank=True, null=True)
    biz_rpr = models.CharField(max_length=50, blank=True, null=True)
    str_dt = models.DateTimeField(blank=True, null=True)
    cn_cd = models.CharField(max_length=20, blank=True, null=True)
    cur_cd = models.CharField(max_length=20, blank=True, null=True)
    insrt_id = models.IntegerField(blank=True, null=True)
    insrt_dt = models.DateTimeField(blank=True, null=True)
    updt_user = models.CharField(max_length=50, blank=True, null=True)
    updt_dt = models.DateTimeField(blank=True, null=True)
    usage_fg = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'b_bizarea'

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




class BBizpartner(models.Model):  # 거래처
    id = models.IntegerField(primary_key=True)
    bizpartner_cd = models.CharField(max_length=50)
    co_id = models.IntegerField(blank=True, null=True)
    bizpartner_type = models.CharField(max_length=20, blank=True, null=True)
    biz_nm = models.CharField(max_length=50, blank=True, null=True)
    bizpartner_nm = models.CharField(max_length=50, blank=True, null=True)
    cn_cd = models.CharField(max_length=20, blank=True, null=True)
    cur_cd = models.CharField(max_length=20, blank=True, null=True)
    bizpartner_stat = models.CharField(max_length=20, blank=True, null=True)
    insrt_id = models.CharField(max_length=50, blank=True, null=True)
    insrt_dt = models.DateTimeField(blank=True, null=True)
    updt_user = models.CharField(max_length=50, blank=True, null=True)
    updt_dt = models.DateTimeField(blank=True, null=True)
    usage_fg = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'b_bizpartner'


class BBizunit(models.Model):  # 사업부
    bizunit_cd = models.CharField(max_length=50)
    bizunit_nm = models.CharField(max_length=50, blank=True, null=True)
    bizunit_rmrk = models.CharField(max_length=50, blank=True, null=True)
    insrt_id = models.CharField(max_length=50, blank=True, null=True)
    insrt_dt = models.DateTimeField(blank=True, null=True)
    updt_user = models.CharField(max_length=50, blank=True, null=True)
    updt_dt = models.DateTimeField(blank=True, null=True)
    usage_fg = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'b_bizunit'




class BFactory(models.Model):  # 공장
    factory_cd = models.CharField(max_length=20, blank=True, null=True)
    factory_nm = models.CharField(max_length=50, blank=True, null=True)
    factory_rmrk = models.CharField(max_length=50, blank=True, null=True)
    insrt_id = models.CharField(max_length=50, blank=True, null=True)
    insrt_dt = models.DateTimeField(blank=True, null=True)
    updt_user = models.CharField(max_length=50, blank=True, null=True)
    updt_dt = models.DateTimeField(blank=True, null=True)
    usage_fg = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'b_factory'


class BItem(models.Model):  # 품목마스터
    itemaccnt_id = models.IntegerField(blank=True, null=True)
    factory_id = models.IntegerField(blank=True, null=True)
    itemgrp_id = models.IntegerField(blank=True, null=True)
    unit_id = models.IntegerField(blank=True, null=True)
    item_cd = models.CharField(max_length=50)
    item_nm = models.CharField(max_length=50, blank=True, null=True)
    item_spec = models.CharField(max_length=50, blank=True, null=True)
    phantom_div = models.CharField(max_length=1, blank=True, null=True)
    insrt_id = models.CharField(max_length=50, blank=True, null=True)
    insrt_dt = models.DateTimeField(blank=True, null=True)
    updt_user = models.CharField(max_length=50, blank=True, null=True)
    updt_dt = models.DateTimeField(blank=True, null=True)
    usage_fg = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'b_item'


class BItemaccnt(models.Model):  # 품목계정
    id = models.IntegerField(primary_key=True)
    itemaccnt_cd = models.CharField(max_length=50)
    itemaccnt_nm = models.CharField(max_length=50, blank=True, null=True)
    insrt_id = models.CharField(max_length=50, blank=True, null=True)
    insrt_dt = models.DateTimeField(blank=True, null=True)
    updt_user = models.CharField(max_length=50, blank=True, null=True)
    updt_dt = models.DateTimeField(blank=True, null=True)
    usage_fg = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'b_itemaccnt'


class BItemgrp(models.Model):  # 품목그룹
    itemgrp_cd = models.CharField(max_length=50, blank=True, null=True)
    itemgrp_nm = models.CharField(max_length=50, blank=True, null=True)
    insrt_id = models.CharField(max_length=50, blank=True, null=True)
    insrt_dt = models.DateTimeField(blank=True, null=True)
    updt_user = models.CharField(max_length=50, blank=True, null=True)
    updt_dt = models.DateTimeField(blank=True, null=True)
    usage_fg = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'b_itemgrp'


class BUser(models.Model):  # 사용자관리
    user_id = models.CharField(max_length=50, blank=True, null=True)
    user_nm = models.CharField(max_length=50, blank=True, null=True)
    psswd = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    phoneno = models.IntegerField(blank=True, null=True)
    insrt_id = models.CharField(max_length=50, blank=True, null=True)
    insrt_dt = models.DateTimeField(blank=True, null=True)
    updt_user = models.CharField(max_length=50, blank=True, null=True)
    updt_dt = models.DateTimeField(blank=True, null=True)
    usage_fg = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'b_user'


class BWorkcenter(models.Model):  # 작업장
    workcenter_cd = models.CharField(max_length=50, blank=True, null=True)
    workcenter_nm = models.CharField(max_length=50, blank=True, null=True)
    cc_id = models.CharField(max_length=50, blank=True, null=True)
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


class BomHdr(models.Model):  # BOM 헤더
    item_nm = models.CharField(max_length=50, blank=True, null=True)
    standard = models.CharField(max_length=50, blank=True, null=True)
    invt_asset = models.IntegerField(blank=True, null=True)
    item_bigdiv = models.CharField(max_length=50, blank=True, null=True)
    ip_unit = models.CharField(max_length=20, blank=True, null=True)
    req = models.CharField(max_length=50, blank=True, null=True)
    loss = models.FloatField(blank=True, null=True)
    ip_div = models.CharField(max_length=50, blank=True, null=True)
    fair = models.CharField(max_length=50, blank=True, null=True)
    apply_strdt = models.DateTimeField(blank=True, null=True)
    apply_enddt = models.DateTimeField(blank=True, null=True)
    eco_no = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bom_hdr'


class CbCodeDtl(models.Model):  # 코드 디테일
    type_cd = models.CharField(max_length=20, blank=True, null=True)
    code_cd = models.CharField(max_length=20, blank=True, null=True)
    cd_nm = models.CharField(max_length=50, blank=True, null=True)
    cd_nmen = models.CharField(max_length=50, blank=True, null=True)
    insrt_id = models.IntegerField(blank=True, null=True)
    updt_dt = models.DateTimeField(blank=True, null=True)
    insrt_dt = models.DateTimeField(blank=True, null=True)
    usage_fg = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cb_code_dtl'


class CbCodeHdr(models.Model):  # 코드 헤더
    type_cd = models.CharField(max_length=20, blank=True, null=True)
    type_nm = models.CharField(max_length=50, blank=True, null=True)
    type_nmen = models.CharField(max_length=50, blank=True, null=True)
    insrt_id = models.IntegerField(blank=True, null=True)
    updt_dt = models.DateTimeField(blank=True, null=True)
    insrt_dt = models.DateTimeField(blank=True, null=True)
    usage_fg = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cb_code_hdr'


class CbCostCenter(models.Model):
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


# Create your models here.

# class Corporation(models.Model):
#     name = models.CharField(verbose_name='NAME', max_length=50)
#     description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text.')
#     content = models.TextField('CONTENT')
#     create_dt = models.DateTimeField('CREATE DATE', auto_now_add=True)
#     modify_dt = models.DateTimeField('MODIFY DATE', auto_now=True)
#
#     class Establishment(models.Model):
#         name = models.CharField(verbose_name='NAME', max_length=50)
#         description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text.')
#         content = models.TextField('CONTENT')
#         create_dt = models.DateTimeField('CREATE DATE', auto_now_add=True)
#         modify_dt = models.DateTimeField('MODIFY DATE', auto_now=True)
#
#     class Department(models.Model):
#         name = models.CharField(verbose_name='NAME', max_length=50)
#         description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text.')
#         content = models.TextField('CONTENT')
#         create_dt = models.DateTimeField('CREATE DATE', auto_now_add=True)
#         modify_dt = models.DateTimeField('MODIFY DATE', auto_now=True)
#
#     class Factory(models.Model):
#         name = models.CharField(verbose_name='NAME', max_length=50)
#         description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text.')
#         content = models.TextField('CONTENT')
#         create_dt = models.DateTimeField('CREATE DATE', auto_now_add=True)
#         modify_dt = models.DateTimeField('MODIFY DATE', auto_now=True)
#
#     class Workshop(models.Model):
#         name = models.CharField(verbose_name='NAME', max_length=50)
#         description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text.')
#         content = models.TextField('CONTENT')
#         create_dt = models.DateTimeField('CREATE DATE', auto_now_add=True)
#         modify_dt = models.DateTimeField('MODIFY DATE', auto_now=True)
#
#     class Item(models.Model):
#         name = models.CharField(verbose_name='NAME', max_length=50)
#         description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text.')
#         content = models.TextField('CONTENT')
#         create_dt = models.DateTimeField('CREATE DATE', auto_now_add=True)
#         modify_dt = models.DateTimeField('MODIFY DATE', auto_now=True)
#
#     class CostCenter(models.Model):
#         name = models.CharField(verbose_name='NAME', max_length=50)
#         description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text.')
#         content = models.TextField('CONTENT')
#         create_dt = models.DateTimeField('CREATE DATE', auto_now_add=True)
#         modify_dt = models.DateTimeField('MODIFY DATE', auto_now=True)
#
#     class CostElementAccount(models.Model):
#         name = models.CharField(verbose_name='NAME', max_length=50)
#         description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text.')
#         content = models.TextField('CONTENT')
#         create_dt = models.DateTimeField('CREATE DATE', auto_now_add=True)
#         modify_dt = models.DateTimeField('MODIFY DATE', auto_now=True)
#
#     class Client(models.Model):
#         name = models.CharField(verbose_name='NAME', max_length=50)
#         description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text.')
#         content = models.TextField('CONTENT')
#         create_dt = models.DateTimeField('CREATE DATE', auto_now_add=True)
#         modify_dt = models.DateTimeField('MODIFY DATE', auto_now=True)
#
#     class BOM(models.Model):
#         name = models.CharField(verbose_name='NAME', max_length=50)
#         description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text.')
#         content = models.TextField('CONTENT')
#         create_dt = models.DateTimeField('CREATE DATE', auto_now_add=True)
#         modify_dt = models.DateTimeField('MODIFY DATE', auto_now=True)
#
#     class Meta:
#         ordering = ('create_dt',)
#
#     def __str__(self):
#         return self.title


#####

