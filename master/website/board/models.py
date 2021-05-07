from django.db import models


# Create your models here.


class BUser(models.Model):  # 사용자관리
    id = models.AutoField(db_column='id', primary_key=True)
    user_id = models.CharField(db_column='user_id', max_length=50)
    user_nm = models.CharField(db_column='user_nm', max_length=50, blank=True, null=True)
    psswd = models.CharField(db_column='psswd', max_length=255)
    email = models.CharField(db_column='email', max_length=255, blank=True, null=True)
    phoneno = models.CharField(db_column='phoneno', max_length=20, blank=True, null=True)
    insrt_id = models.IntegerField(db_column='insrt_id', blank=True, null=True)
    insrt_dt = models.DateTimeField(db_column='insrt_dt', blank=True, null=True, auto_now_add=True)
    updt_id = models.IntegerField(db_column='updt_id', blank=True, null=True)
    updt_dt = models.DateTimeField(db_column='updt_dt', blank=True, null=True, auto_now=True)
    usage_fg = models.CharField(db_column='usage_fg', max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'b_user'


class CbCodeHdr(models.Model):  # 코드 헤더
    id = models.AutoField(db_column='id', primary_key=True)
    type_cd = models.CharField(db_column='type_cd', max_length=20)
    type_nm = models.CharField(db_column='type_nm', max_length=50)
    type_nmen = models.CharField(db_column='type_nmen', max_length=50)
    updt_dt = models.DateTimeField(db_column='updt_dt', auto_now=True)
    insrt_dt = models.DateTimeField(db_column='insrt_dt', auto_now_add=True)
    usage_fg = models.CharField(db_column='usage_fg', max_length=1, default='Y')
    insrt = models.ForeignKey(BUser, related_name='+', on_delete=models.CASCADE)
    updt = models.ForeignKey(BUser, related_name='+', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'cb_code_hdr'


class CbCodeDtl(models.Model):  # 코드 detail
    id = models.AutoField(db_column='id', primary_key=True)
    type_cd = models.CharField(db_column='type_cd', max_length=20)
    code_cd = models.CharField(db_column='code_cd', max_length=20)
    cd_nm = models.CharField(db_column='cd_nm', max_length=50)
    updt_dt = models.DateTimeField(db_column='updt_dt', auto_now=True)
    insrt_dt = models.DateTimeField(db_column='insrt_dt', auto_now_add=True)
    usage_fg = models.CharField(db_column='usage_fg', max_length=1, default='Y')
    insrt = models.ForeignKey(BUser, related_name='+', on_delete=models.CASCADE)
    updt = models.ForeignKey(BUser, related_name='+', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'cb_code_dtl'


class BCo(models.Model):  # 법인정보
    id = models.AutoField(db_column='id', primary_key=True)
    co_cd = models.CharField(db_column='co_cd', max_length=50, blank=True, null=True)
    co_nm = models.CharField(db_column='co_nm', max_length=50, blank=True, null=True)
    co_shnm = models.CharField(db_column='co_shnm', max_length=50, blank=True, null=True)
    co_rpr = models.CharField(db_column='co_rpr', max_length=20, blank=True, null=True)
    co_type = models.CharField(db_column='co_type', max_length=20, blank=True, null=True)
    co_div = models.CharField(db_column='co_div', max_length=20, blank=True, null=True)
    co_estdt = models.DateTimeField(db_column='co_estdt', blank=True, null=True)
    co_strdt = models.DateTimeField(db_column='co_strdt', blank=True, null=True)
    unitcur = models.ForeignKey(CbCodeDtl, related_name='+', on_delete=models.CASCADE)
    unitcn = models.ForeignKey(CbCodeDtl, related_name='+', on_delete=models.CASCADE)
    updt_dt = models.DateTimeField(db_column='updt_dt', auto_now=True)
    insrt_dt = models.DateTimeField(db_column='insrt_dt', auto_now_add=True)
    insrt = models.ForeignKey(BUser, related_name='+', on_delete=models.CASCADE)
    updt = models.ForeignKey(BUser, related_name='+', on_delete=models.CASCADE)
    usage_fg = models.CharField(db_column='usage_fg', max_length=1, default='Y')

    class Meta:
        managed = False
        db_table = 'b_co'


class BBizarea(models.Model):  # 사업장
    id = models.AutoField(db_column='id', primary_key=True)
    bizarea_cd = models.CharField(db_column='bizarea_cd', max_length=50, blank=True, null=True)
    co = models.ForeignKey(BCo, on_delete=models.CASCADE)
    bizarea_nm = models.CharField(db_column='bizarea_nm', max_length=50, blank=True, null=True)
    bizarea_shnm = models.CharField(db_column='bizarea_shnm', max_length=20, blank=True, null=True)
    biz_no = models.CharField(db_column='biz_no', max_length=50, blank=True, null=True)
    biz_rpr = models.CharField(db_column='biz_rpr', max_length=50, blank=True, null=True)
    str_dt = models.DateTimeField(db_column='str_dt', blank=True, null=True)
    unitcur = models.ForeignKey(CbCodeDtl, related_name='+', on_delete=models.CASCADE)
    unitcn = models.ForeignKey(CbCodeDtl, related_name='+', on_delete=models.CASCADE)
    usage_fg = models.CharField(db_column='usage_fg', max_length=1, blank=True, null=True)
    insrt = models.ForeignKey(BUser, related_name='+', on_delete=models.CASCADE)
    updt = models.ForeignKey(BUser, related_name='+', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'b_bizarea'


class BBizunit(models.Model):  # 사업부
    id = models.AutoField(db_column='id', primary_key=True)
    bizunit_cd = models.CharField(db_column='bizunit_cd', max_length=50)
    bizunit_nm = models.CharField(db_column='bizunit_nm', max_length=50, blank=True, null=True)
    bizunit_rmrk = models.CharField(db_column='bizunit_rmrk', max_length=50, blank=True, null=True)
    insrt_dt = models.DateTimeField(db_column='insrt_dt', auto_now_add=True, blank=True, null=True)
    updt_dt = models.DateTimeField(db_column='updt_dt', auto_now=True, blank=True, null=True)
    usage_fg = models.CharField(db_column='usage_fg', max_length=1, blank=True, null=True)
    insrt = models.ForeignKey(BUser, related_name='+', on_delete=models.CASCADE)
    updt = models.ForeignKey(BUser, related_name='+', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'b_bizunit'


class BBizpartner(models.Model):  # 거래처
    id = models.AutoField(db_column='id', primary_key=True)
    bizpartner_cd = models.CharField(db_column='bizpartner_cd', max_length=50)
    co_id = models.IntegerField(db_column='co_id')
    bizpartner_type = models.CharField(db_column='bizpartner_type', max_length=20, blank=True, null=True)
    biz_nm = models.CharField(db_column='biz_nm', max_length=50, blank=True, null=True)
    bizpartner_nm = models.CharField(db_column='bizpartner_nm', max_length=50, blank=True, null=True)
    unitcur = models.ForeignKey(CbCodeDtl, related_name='+', on_delete=models.CASCADE)
    unitcn = models.ForeignKey(CbCodeDtl, related_name='+', on_delete=models.CASCADE)
    bizpartner_stat = models.CharField(db_column='bizpartner_stat', max_length=20, blank=True, null=True)
    insrt_dt = models.DateTimeField(db_column='insrt_dt', blank=True, null=True, auto_now_add=True)
    updt_dt = models.DateTimeField(db_column='updt_dt', blank=True, null=True, auto_now=True)
    usage_fg = models.CharField(db_column='usage_fg', max_length=1, blank=True, null=True)
    insrt = models.ForeignKey(BUser, related_name='+', on_delete=models.CASCADE)
    updt = models.ForeignKey(BUser, related_name='+', on_delete=models.CASCADE)

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
    insrt = models.ForeignKey(BUser, related_name='+', on_delete=models.CASCADE)
    updt = models.ForeignKey(BUser, related_name='+', on_delete=models.CASCADE)

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
    insrt = models.ForeignKey(BUser, related_name='+', on_delete=models.CASCADE)
    updt = models.ForeignKey(BUser, related_name='+', on_delete=models.CASCADE)

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
    insrt = models.ForeignKey(BUser, related_name='+', on_delete=models.CASCADE)
    updt = models.ForeignKey(BUser, related_name='+', on_delete=models.CASCADE)

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
    bom_fg = models.CharField(db_column='bom_fg', max_length=8, default='0')
    insrt = models.ForeignKey(BUser, related_name='+', on_delete=models.CASCADE)
    updt = models.ForeignKey(BUser, related_name='+', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'b_item'


class CbCostCenter(models.Model):  # 코스트센터
    id = models.AutoField(db_column='id', primary_key=True)
    cstctr_cd = models.CharField(max_length=50, blank=True, null=True)
    cstctr_nm = models.CharField(max_length=50, blank=True, null=True)
    bizarea_id = models.IntegerField(blank=True, null=True)
    bizunit_id = models.IntegerField(blank=True, null=True)
    factory_id = models.IntegerField(blank=True, null=True)
    cstctr_type = models.CharField(max_length=50, blank=True, null=True)
    cstctr_dir_div = models.CharField(max_length=50, blank=True, null=True)
    updt_dt = models.DateTimeField(blank=True, null=True)
    insrt_dt = models.DateTimeField(blank=True, null=True)
    usage_fg = models.CharField(max_length=1, blank=True, null=True)
    insrt = models.ForeignKey(BUser, related_name='+', on_delete=models.CASCADE)
    updt = models.ForeignKey(BUser, related_name='+', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'cb_cost_center'


class BWorkcenter(models.Model):  # 작업장
    id = models.AutoField(db_column='id', primary_key=True)
    workcenter_cd = models.CharField(max_length=50, blank=True, null=True)
    workcenter_nm = models.CharField(max_length=50, blank=True, null=True)
    cstctr = models.ForeignKey(CbCostCenter, related_name='+', on_delete=models.CASCADE)
    insrt_dt = models.DateTimeField(blank=True, null=True)
    updt_dt = models.DateTimeField(blank=True, null=True)
    usage_fg = models.CharField(max_length=1, blank=True, null=True)
    insrt = models.ForeignKey(BUser, related_name='+', on_delete=models.CASCADE)
    updt = models.ForeignKey(BUser, related_name='+', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'b_workcenter'


class BCosteleaccnt(models.Model):  #원가요소계정
    id = models.AutoField(db_column='id', primary_key=True)
    #itemaccnt = models.ForeignKey(BItemaccnt, blank=True, null=True, on_delete=models.CASCADE)
    accnt_cd = models.CharField(db_column='accnt_cd', max_length=50, blank=True, null=True)
    accnt_nm = models.CharField(db_column='accnt_nm',max_length=50, blank=True, null=True)
    placcnt_cd = models.CharField(db_column='placcnt_cd', max_length=50, blank=True, null=True)
    placcnt_nm = models.CharField(db_column='placcnt_nm', max_length=50, blank=True, null=True)
    fv_div = models.CharField(db_column='fv_div', max_length=1, blank=True, null=True)
    costeleaccnt_rmrk = models.CharField(db_column='costeleaccnt_rmrk', max_length=255, blank=True, null=True)
    #updt_dt = models.DateTimeField(blank=True, null=True)
    #insrt_dt = models.DateTimeField(blank=True, null=True)
    usage_fg = models.CharField(max_length=1, blank=True, null=True, default='Y')
    #insrt = models.ForeignKey(BUser, related_name='+', on_delete=models.CASCADE)
    #updt = models.ForeignKey(BUser, related_name='+', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'b_costeleaccnt'



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
    insrt = models.ForeignKey(BUser, related_name='+', on_delete=models.CASCADE)
    updt = models.ForeignKey(BUser, related_name='+', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'bom_dtl'


class BBom(models.Model):  # BOM 메인
    id = models.AutoField(db_column='id', primary_key=True)
    bom_type = models.CharField(db_column='bom_type', max_length=20)
    item_cd = models.CharField(db_column='item_cd', max_length=50)
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
    insrt = models.ForeignKey(BUser, related_name='+', on_delete=models.CASCADE)
    updt = models.ForeignKey(BUser, related_name='+', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'b_bom'

    def __str__(self):
        return "BOM id : " + str(self.id) + " Type : " + self.bom_type


class BVersion(models.Model):
    id = models.IntegerField(primary_key=True)
    #insrt = models.ForeignKey(BUser, related_name='+', on_delete=models.CASCADE)
    version_cd = models.CharField(max_length=50, blank=True, null=True)
    version_dt = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'b_version'


class CcManucostIf(models.Model):  # 제조비용
    id = models.AutoField(db_column='id', primary_key=True)
    co = models.ForeignKey(BCo, on_delete=models.CASCADE)
    costeleaccnt = models.ForeignKey(BCosteleaccnt, on_delete=models.CASCADE)
    periodym_cd = models.CharField(db_column='periodym_cd', max_length=6)
    cstctr = models.ForeignKey(CbCostCenter, on_delete=models.CASCADE)
    manucost_price = models.IntegerField(db_column='manucost_price', default=0)
    mngmt_1 = models.CharField(db_column='mngmt_1', max_length=50, default='0')
    version = models.ForeignKey(BVersion, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'cc_manucost_if'


class CcMaterialcostIf(models.Model):  # 제료비용
    id = models.AutoField(db_column='id', primary_key=True)
    factory = models.ForeignKey(BFactory, on_delete=models.CASCADE)
    co = models.ForeignKey(BCo, on_delete=models.CASCADE)
    periodym_cd = models.CharField(db_column='periodym_cd', max_length=6)
    version = models.ForeignKey(BVersion, on_delete=models.CASCADE)
    workcenter = models.ForeignKey(BWorkcenter, on_delete=models.CASCADE)
    mc_amount = models.IntegerField(db_column='mc_amount', default=0)
    mc_price = models.IntegerField(db_column='mc_price', default=0)
    costeleaccnt = models.ForeignKey(BCosteleaccnt, on_delete=models.CASCADE)
    bom = models.ForeignKey(BBom, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'cc_materialcost_if'


class CcItempermanucostIf(models.Model):  # 품목별제조비용
    id = models.AutoField(db_column='id', primary_key=True)
    co = models.ForeignKey(BCo, on_delete=models.CASCADE)
    version = models.ForeignKey(BVersion, on_delete=models.CASCADE)
    costeleaccnt = models.ForeignKey(BCosteleaccnt, on_delete=models.CASCADE)
    bom = models.ForeignKey(BBom, on_delete=models.CASCADE)
    ipmc_ym = models.CharField(db_column='ipmc_ym', max_length=6)
    ipmc_cost = models.IntegerField(db_column='ipmc_cost', default=0)

    class Meta:
        managed = False
        db_table = 'cc_itempermanucost_if'


class CcProductcostpaymentIf(models.Model):  # 제품원가수불
    id = models.AutoField(db_column='id', primary_key=True)
    factory = models.ForeignKey(BFactory, on_delete=models.CASCADE)
    bom = models.ForeignKey(BBom, on_delete=models.CASCADE)
    costeleaccnt = models.ForeignKey(BCosteleaccnt, on_delete=models.CASCADE)
    version = models.ForeignKey(BVersion, on_delete=models.CASCADE)
    basicicstoc_amt = models.IntegerField(db_column='basicicstoc_amt', default=0)
    basicicstoc_price = models.IntegerField(db_column='basicicstoc_price', default=0)
    productionreceipt_amt = models.IntegerField(db_column='productionreceipt_amt', default=0)
    productionreceipt_price = models.IntegerField(db_column='productionreceipt_price', default=0)
    sell_amt = models.IntegerField(db_column='sell_amt', default=0)
    sell_cost = models.IntegerField(db_column='sell_cost', default=0)
    loss_amt = models.IntegerField(db_column='loss_amt', default=0)
    loss_cost = models.IntegerField(db_column='loss_cost', default=0)
    development_amt = models.IntegerField(db_column='development_amt', default=0)
    development_cost = models.IntegerField(db_column='development_cost', default=0)
    endingstock_amt = models.IntegerField(db_column='endingstock_amt', default=0)
    endingstock_cost = models.IntegerField(db_column='endingstock_cost', default=0)
    pcp_dt = models.CharField(db_column='pcp_dt', max_length=6)

    class Meta:
        managed = False
        db_table = 'cc_productcostpayment_if'




class CcCostbill1(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    version_id = models.IntegerField(db_column='version_id', default=0)
    itemplan_id = models.IntegerField(db_column='itemplan_id', default=0)
    ic_idlc = models.IntegerField(db_column='ic_idlc', default=0)
    ic_dlfc = models.IntegerField(db_column='ic_dlfc', default=0)
    ic_dlvc = models.IntegerField(db_column='ic_dlvc', default=0)
    ic_idohc = models.IntegerField(db_column='ic_idohc', default=0)
    ic_ohdfe = models.IntegerField(db_column='ic_ohdfe', default=0)
    ic_ohdfd = models.IntegerField(db_column='ic_ohdfd', default=0)
    ic_ohdvc = models.IntegerField(db_column='ic_ohdvc', default=0)
    proamt_unit = models.IntegerField(db_column='proamt_unit', default=0)
    proamt_acc = models.BigIntegerField(db_column='proamt_acc', default=0)
    proq = models.IntegerField(db_column='proq', default=0)


    class Meta:
        managed = False
        db_table = 'cc_costbill1'


class CcCostbill(models.Model):
    version_cd = models.CharField(db_column='version_cd', max_length=6, default=0)
    periodym_cd = models.IntegerField(db_column='periodym_cd', blank=True, null=True)
    item_cd = models.CharField(db_column='item_cd', max_length=50, default=0)
    bi_brm = models.IntegerField(db_column='bi_brm')
    ra_rm = models.IntegerField(db_column='ra_rm')
    ei_erm = models.IntegerField(db_column='ei_erm')
    ei_elc = models.IntegerField(db_column='ei_elc')
    ei_eoh = models.IntegerField(db_column='ei_eoh')
    ic_idlc = models.IntegerField(db_column='ic_idlc', default=0)
    ic_dlfc = models.IntegerField(db_column='ic_dlfc', default=0)
    ic_dlvc = models.IntegerField(db_column='ic_dlvc', default=0)
    ic_idohc = models.IntegerField(db_column='ic_idohc', default=0)
    ic_ohdfe = models.IntegerField(db_column='ic_ohdfe', default=0)
    ic_ohdfd = models.IntegerField(db_column='ic_ohdfd', default=0)
    ic_ohdvc = models.IntegerField(db_column='ic_ohdvc', default=0)
    ic_arm = models.IntegerField(db_column='ic_arm')
    proq = models.IntegerField(db_column='proq', default=0)
    proamt_unit = models.IntegerField(db_column='proamt_unit', default=0)
    uc_srw = models.IntegerField(db_column='uc_srw', default=0)
    uc_dlc = models.IntegerField(db_column='uc_dlc', default=0)
    uc_idlc = models.IntegerField(db_column='uc_idlc', default=0)
    uc_idohc = models.IntegerField(db_column='uc_idohc', default=0)
    uc_dohc = models.IntegerField(db_column='uc_dohc', default=0)



    class Meta:
        managed = False
        db_table = 'cc_costbill'

class DmPeriod(models.Model):   #기간테이블
    id = models.AutoField(db_column='id', primary_key=True)
    period_ym = models.IntegerField(blank=True, null=True)
    period_y = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dm_period'


class DmManucost(models.Model): #제조비용마트
    id = models.AutoField(db_column='id', primary_key=True)
    itemaccnt = models.ForeignKey(BItemaccnt, blank=True, null=True, on_delete=models.CASCADE)
    period = models.ForeignKey(DmPeriod, blank=True, null=True, on_delete=models.CASCADE)
    manucost_price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dm_manucost'