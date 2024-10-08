# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthAssignment(models.Model):
    item_name = models.CharField(primary_key=True, max_length=64, db_collation='utf8mb3_uca1400_ai_ci')  # The composite primary key (item_name, user_id) found, that is not supported. The first column is selected.
    user_id = models.CharField(max_length=64, db_collation='utf8mb3_uca1400_ai_ci')
    created_at = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_assignment'
        unique_together = (('item_name', 'user_id'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthItem(models.Model):
    name = models.CharField(primary_key=True, max_length=64, db_collation='utf8mb3_uca1400_ai_ci')
    type = models.SmallIntegerField()
    description = models.TextField(db_collation='utf8mb3_uca1400_ai_ci', blank=True, null=True)
    rule_name = models.CharField(max_length=64, db_collation='utf8mb3_uca1400_ai_ci', blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    created_at = models.IntegerField(blank=True, null=True)
    updated_at = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_item'


class AuthItemChild(models.Model):
    parent = models.CharField(primary_key=True, max_length=64, db_collation='utf8mb3_uca1400_ai_ci')  # The composite primary key (parent, child) found, that is not supported. The first column is selected.
    child = models.CharField(max_length=64, db_collation='utf8mb3_uca1400_ai_ci')

    class Meta:
        managed = False
        db_table = 'auth_item_child'
        unique_together = (('parent', 'child'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthRule(models.Model):
    name = models.CharField(primary_key=True, max_length=64, db_collation='utf8mb3_uca1400_ai_ci')
    data = models.TextField(blank=True, null=True)
    created_at = models.IntegerField(blank=True, null=True)
    updated_at = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_rule'


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
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CexAdsFormat(models.Model):
    name = models.CharField(max_length=80)
    width = models.CharField(max_length=4)
    height = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'cex_ads_format'


class CexAdsImage(models.Model):
    advertisement = models.ForeignKey('CexAdvertisement', models.DO_NOTHING)
    url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cex_ads_image'


class CexAdvertisement(models.Model):
    place = models.TextField(db_collation='utf8mb3_unicode_ci', blank=True, null=True, db_comment='(DC2Type:json_array)')
    position = models.TextField(db_collation='utf8mb3_unicode_ci', blank=True, null=True, db_comment='(DC2Type:json_array)')
    user_id = models.CharField(max_length=255)
    ads_format = models.ForeignKey(CexAdsFormat, models.DO_NOTHING, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    impressions_numbers = models.IntegerField(blank=True, null=True)
    impressions_count = models.IntegerField(blank=True, null=True)
    click_count = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=80)
    active = models.IntegerField(blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cex_advertisement'


class CexAliances(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    image_url = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    slug = models.CharField(unique=True, max_length=255)
    seo_id = models.IntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 'cex_aliances'
        db_table_comment = 'Gestión de alianzas'


class CexBanner(models.Model):
    name = models.CharField(unique=True, max_length=128)
    visible = models.TextField()  # This field type is a guess.
    speed = models.IntegerField()
    transition = models.CharField(max_length=64)
    pause = models.IntegerField()
    css = models.TextField()  # This field type is a guess.
    images_count = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    url_link = models.TextField(blank=True, null=True, db_comment='Incluida para agregar links')
    banner_adv = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cex_banner'


class CexBannerImg(models.Model):
    route = models.CharField(max_length=250)
    url = models.CharField(max_length=250, blank=True, null=True)
    text = models.CharField(max_length=250, blank=True, null=True)
    banner_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cex_banner_img'
        unique_together = (('id', 'route'),)


class CexBuildWith(models.Model):
    build_date = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=80)
    email = models.CharField(max_length=80)
    phone = models.CharField(max_length=80)
    province = models.IntegerField()
    q1 = models.CharField(max_length=80)
    q2 = models.CharField(max_length=80)
    q3 = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'cex_build_with'


class CexBuilderTypes(models.Model):
    name = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'cex_builder_types'


class CexCatalog(models.Model):
    stand_id = models.IntegerField()
    category_id = models.IntegerField(blank=True, null=True)
    seo_id = models.IntegerField()
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    img_pdf = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=150, blank=True, null=True)
    hits = models.IntegerField(blank=True, null=True)
    slug = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'cex_catalog'


class CexCategory(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    short_description = models.CharField(max_length=255, blank=True, null=True, db_comment='Descripción corta para SEO')
    description = models.TextField(blank=True, null=True)
    img = models.CharField(max_length=100, blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    level = models.IntegerField()
    slug = models.CharField(unique=True, max_length=255)
    type = models.CharField(max_length=20, db_comment='producto «product» o servicio «service»')
    credits = models.FloatField(blank=True, null=True, db_comment='Creitos solo para terce nivel')
    def_type = models.CharField(max_length=5)
    def_price = models.FloatField()
    do_related = models.TextField()  # This field type is a guess.
    coins_coefficient = models.FloatField(blank=True, null=True)
    min_coins = models.IntegerField(blank=True, null=True)
    max_coins = models.IntegerField(blank=True, null=True)
    industry_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cex_category'


class CexClientCrm(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=255)
    city = models.CharField(max_length=255, blank=True, null=True)
    province = models.IntegerField(blank=True, null=True)
    enterprise = models.CharField(max_length=255, blank=True, null=True)
    ruc = models.CharField(max_length=45, blank=True, null=True)
    created_by = models.IntegerField()
    has_transport = models.IntegerField(blank=True, null=True)
    delivered_place = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cex_client_crm'


class CexCoinsLog(models.Model):
    stand_id = models.IntegerField()
    stand_name = models.CharField(max_length=255)
    date = models.DateField()
    coins_before = models.IntegerField()
    coins_after = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cex_coins_log'


class CexCommentsLog(models.Model):
    stand_id = models.IntegerField()
    date = models.DateTimeField()
    comment = models.TextField()

    class Meta:
        managed = False
        db_table = 'cex_comments_log'


class CexCountry(models.Model):
    iso = models.CharField(max_length=45, blank=True, null=True)
    name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cex_country'


class CexCredit(models.Model):
    credit_date = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=80)
    email = models.CharField(max_length=80)
    phone = models.CharField(max_length=80)
    province = models.IntegerField()
    credit = models.CharField(max_length=80)
    how_to_use = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'cex_credit'


class CexExhibition(models.Model):
    stand_id = models.IntegerField()
    url_image = models.CharField(max_length=250)
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField()
    code = models.TextField(blank=True, null=True)
    date_final = models.DateField(blank=True, null=True)
    slug = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'cex_exhibition'


class CexGalley(models.Model):
    file_type = models.CharField(max_length=45)
    file_name = models.CharField(max_length=150)
    url = models.CharField(max_length=45)
    type = models.CharField(max_length=5)
    profile_user_id = models.IntegerField(blank=True, null=True)
    stand_id = models.IntegerField(blank=True, null=True)
    service_product_id = models.IntegerField(blank=True, null=True)
    catalog_id = models.IntegerField(blank=True, null=True)
    aliances_id = models.IntegerField(blank=True, null=True)
    seo_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cex_galley'


class CexHighlight(models.Model):
    id_serv_prod = models.IntegerField()
    start_date = models.DateTimeField()
    n_days = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cex_highlight'


class CexInbox(models.Model):
    name = models.CharField(max_length=80, blank=True, null=True)
    phone = models.CharField(max_length=80, blank=True, null=True)
    email = models.CharField(max_length=120, blank=True, null=True)
    organization = models.CharField(max_length=80, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=45)
    from_field = models.CharField(db_column='from', max_length=120, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    to = models.CharField(max_length=120, blank=True, null=True)
    stand_name = models.CharField(max_length=120, blank=True, null=True)
    mailed_it = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cex_inbox'


class CexLandingPages(models.Model):
    seo_title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    seo_description = models.CharField(max_length=255)
    front_block = models.TextField(blank=True, null=True)
    seo_keywords = models.CharField(max_length=255)
    has_slider_revolution = models.IntegerField()
    slider_revolution_file = models.CharField(max_length=255)
    slider_revolution_date = models.DateTimeField(blank=True, null=True)
    slider_id = models.IntegerField(blank=True, null=True)
    tour_switch = models.IntegerField()
    tour_virtual_code = models.TextField(blank=True, null=True)
    foot_bar = models.IntegerField()
    image_url = models.CharField(max_length=255, blank=True, null=True)
    promo_title = models.TextField(blank=True, null=True)
    spaces_public = models.IntegerField()
    is_public = models.IntegerField()
    adsense_enabled = models.IntegerField()
    adsense_code = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cex_landing_pages'


class CexLandingPagesAdv(models.Model):
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    impressions_numbers = models.IntegerField(blank=True, null=True)
    impressions_count = models.IntegerField(blank=True, null=True)
    slider_id = models.IntegerField(blank=True, null=True)
    has_slider_revolution = models.IntegerField()
    slider_revolution_file = models.CharField(max_length=255)
    slider_revolution_url = models.CharField(max_length=250, blank=True, null=True)
    click_count = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=80)
    active = models.IntegerField(blank=True, null=True)
    landing_pages_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cex_landing_pages_adv'


class CexLicitation(models.Model):
    stand_id = models.IntegerField(db_comment='Id Exhibidor')
    name = models.CharField(max_length=255, db_comment='Nombre Licitación')
    slug = models.CharField(max_length=255, db_comment='Slug Licitación')
    status = models.CharField(max_length=255, blank=True, null=True, db_comment='Estado Licitación')
    manager_name = models.CharField(max_length=255, db_comment='Nombre Gerente de Compras')
    country_id = models.IntegerField(blank=True, null=True, db_comment='Id Pais')
    province_id = models.IntegerField(blank=True, null=True, db_comment='Id Provincia')
    city = models.CharField(max_length=255, blank=True, null=True, db_comment='Ciudad')
    start_date = models.DateTimeField(db_comment='Fecha publicación «inicio Licitación»')
    end_date = models.DateTimeField(db_comment='Fecha cierre Licitación')
    date_time_range = models.CharField(max_length=255)
    estimated_value = models.FloatField(blank=True, null=True, db_comment='Valor estimado Licitación')
    description = models.TextField(db_comment='Descripción')
    url_file = models.CharField(max_length=255, blank=True, null=True, db_comment='Url Archivo Adjunto')
    licitation_value = models.FloatField(blank=True, null=True, db_comment='Valor de Licitación')
    admin_comments = models.TextField(blank=True, null=True, db_comment='Comentarios del Administrador')
    created_at = models.IntegerField(blank=True, null=True, db_comment='Creado el')
    updated_at = models.IntegerField(blank=True, null=True, db_comment='Actualizado en')
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    admin_pub_comments = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cex_licitation'
        db_table_comment = 'Gestión de Licitaciones'


class CexLicitationMessages(models.Model):
    licitation = models.ForeignKey(CexLicitation, models.DO_NOTHING, db_comment='Id Licitación')
    sender_id = models.IntegerField(db_comment='Id emisor')
    receiver_id = models.IntegerField(db_comment='Id de receptor')
    created_at = models.IntegerField(blank=True, null=True, db_comment='Creado el')
    updated_at = models.IntegerField(blank=True, null=True, db_comment='Actualizado el')
    date_time = models.DateTimeField(db_comment='Fecha y hora mensaje')
    message = models.TextField(db_comment='Mensaje')

    class Meta:
        managed = False
        db_table = 'cex_licitation_messages'


class CexLicitationProducts(models.Model):
    licitation = models.ForeignKey(CexLicitation, models.DO_NOTHING, db_comment='Id Licitación')
    type = models.CharField(max_length=255, db_comment='Tipo de producto/servicio')
    cat_n1_id = models.IntegerField(db_comment='Id Categoría Nivel 1')
    cat_n2_id = models.IntegerField(db_comment='Id Categoría Nivel 2')
    cat_n3_id = models.IntegerField(db_comment='Id Categoría Nivel 2')
    short_description = models.TextField(blank=True, null=True, db_comment='Descripción Corta')
    unit_type = models.CharField(max_length=255, blank=True, null=True, db_comment='Tipo Unidad')
    amount = models.IntegerField(blank=True, null=True, db_comment='Cantidad')
    unit_value = models.FloatField(blank=True, null=True, db_comment='Valor unitario')

    class Meta:
        managed = False
        db_table = 'cex_licitation_products'


class CexLicitationStandPayments(models.Model):
    stand_id = models.IntegerField(db_comment='Id Exhibidor')
    licitation_id = models.IntegerField(db_comment='id licitación')
    end_date = models.DateTimeField(blank=True, null=True, db_comment='Fecha de cierre de la Licitación')

    class Meta:
        managed = False
        db_table = 'cex_licitation_stand_payments'
        db_table_comment = 'Control de apertura de licitaciones'


class CexLinks(models.Model):
    menus_id = models.IntegerField()
    order = models.IntegerField(blank=True, null=True, db_comment='Permite asignar orden')
    name = models.CharField(max_length=45)
    url = models.CharField(max_length=100)
    parent_id = models.IntegerField()
    target = models.CharField(max_length=7, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=40, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    enabled = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cex_links'


class CexLocal(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    phone = models.CharField(max_length=32, blank=True, null=True)
    web = models.CharField(max_length=255, blank=True, null=True)
    lat_lng = models.TextField(blank=True, null=True)
    hits = models.CharField(max_length=45, blank=True, null=True)
    slug = models.CharField(unique=True, max_length=45)
    seo_id = models.IntegerField()
    stand_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cex_local'


class CexMenus(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cex_menus'


class CexNotification(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    creation_date = models.DateTimeField()
    sent = models.IntegerField()
    sent_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cex_notification'


class CexNotificationLog(models.Model):
    stand_id = models.IntegerField()
    notification_id = models.IntegerField()
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cex_notification_log'


class CexOptimizationData(models.Model):
    name = models.CharField(max_length=50)
    value = models.TextField(db_collation='utf8mb3_unicode_ci', blank=True, null=True, db_comment='(DC2Type:json_array)')
    creation_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cex_optimization_data'


class CexOrderComment(models.Model):
    order_id = models.IntegerField()
    status = models.IntegerField()
    date = models.DateTimeField()
    comment = models.TextField()

    class Meta:
        managed = False
        db_table = 'cex_order_comment'


class CexOrderStand(models.Model):
    order_id = models.IntegerField()
    stand_id = models.IntegerField()
    status = models.IntegerField()
    tracking_number = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'cex_order_stand'


class CexPages(models.Model):
    seo_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True, null=True)
    static = models.IntegerField(db_comment='Es página estática? O funcional\n')
    slug = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'cex_pages'
        db_table_comment = 'Tabla para manejo de Páginas Estáticas'


class CexPaypalPlan(models.Model):
    id_paypal = models.CharField(max_length=255)
    product_id = models.CharField(max_length=255)
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    interval_unit = models.CharField(max_length=255)
    cycles = models.IntegerField()
    price = models.FloatField()
    price_currency = models.CharField(max_length=3)
    fee = models.FloatField()
    fee_currency = models.CharField(max_length=3)
    tax = models.FloatField()
    pro = models.IntegerField()
    tax_inclusive = models.IntegerField()
    create_time = models.CharField(max_length=50)
    update_time = models.CharField(max_length=50)
    stand_type_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cex_paypal_plan'


class CexPaypalProduct(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=255)
    type = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    image_url = models.CharField(max_length=255)
    home_url = models.CharField(max_length=255)
    id_paypal = models.CharField(max_length=255)
    create_time = models.CharField(max_length=50)
    update_time = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cex_paypal_product'


class CexPaypalSubscription(models.Model):
    id_paypal = models.CharField(max_length=255)
    stand_id = models.IntegerField()
    plan_id = models.IntegerField()
    create_time = models.DateTimeField()
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cex_paypal_subscription'


class CexPlan(models.Model):
    name = models.CharField(max_length=150, db_comment='Nombre del Plan')
    description = models.CharField(max_length=250, db_comment='Descripción del Plan')
    description_pro = models.CharField(max_length=250, blank=True, null=True, db_comment='Descripción del Plan profesional')
    payment_description = models.CharField(max_length=255, blank=True, null=True)
    payment_description_pro = models.CharField(max_length=255, blank=True, null=True)
    features = models.TextField(blank=True, null=True)
    features_pro = models.TextField(blank=True, null=True)
    slug = models.CharField(max_length=45, blank=True, null=True, db_comment='Slug del Plan')
    active = models.BooleanField(db_comment='Activo/Inactivo')  # Cambiado a BooleanField
    plan_type = models.CharField(max_length=45, db_comment='Tipo del Plan')
    valid_for_days = models.IntegerField(db_comment='Validez del plan en días')
    monthly_cost = models.FloatField(db_comment='Costo del plan en valor mensual')
    monthly_cost_pro = models.FloatField(blank=True, null=True, db_comment='Costo del plan en valor mensual - profesional')
    annual_discount = models.FloatField(blank=True, null=True, db_comment='Descuento en el plan, en caso de pago anualizado')
    annual_discount_pro = models.FloatField(blank=True, null=True, db_comment='Descuento en el plan, en caso de pago anualizado - profesional')
    catalogs = models.IntegerField(db_comment='Número de catálogos para el plan')
    catalogs_pro = models.IntegerField(blank=True, null=True, db_comment='Número de catálogos para el plan profesional')
    branding_index = models.BooleanField(db_comment='Permite modificar landing page exhibidor')  # Cambiado a BooleanField
    branding_index_pro = models.BooleanField(blank=True, null=True, db_comment='Permite modificar landing page exhibidor - profesional')  # Cambiado a BooleanField
    video_stand = models.BooleanField(db_comment='Se permite colocar videos en el exhibidor')  # Cambiado a BooleanField
    video_stand_pro = models.BooleanField(blank=True, null=True, db_comment='Se permite colocar videos en el exhibidor - profesional')  # Cambiado a BooleanField
    slider_pro_stand = models.BooleanField(db_comment='Permite la inclusión de sliders pro')  # Cambiado a BooleanField
    slider_pro_stand_pro = models.BooleanField(blank=True, null=True, db_comment='Permite la inclusión de sliders pro - profesional')  # Cambiado a BooleanField
    tour_virtual_stand = models.BooleanField(db_comment='Permite incluir Tour virtual')  # Cambiado a BooleanField
    tour_virtual_stand_pro = models.BooleanField(blank=True, null=True, db_comment='Permite incluir Tour virtual - profesional')  # Cambiado a BooleanField
    featured_product_index = models.IntegerField(db_comment='Número de productos destacados en página principal')
    featured_product_index_pro = models.IntegerField(blank=True, null=True, db_comment='Número de productos destacados en página principal - profesional')
    featured_product_category = models.IntegerField(db_comment='Número de productos destacados en categorías')
    featured_product_category_pro = models.IntegerField(blank=True, null=True, db_comment='Número de productos destacados en categorías - profesional')
    featured_catalog_index = models.IntegerField(db_comment='Número de catálogos')
    featured_catalog_index_pro = models.IntegerField(blank=True, null=True, db_comment='Número de catálogos - profesional')
    featured_catalog_category = models.IntegerField(db_comment='Número de catálogos promocionados en categoría')
    featured_catalog_category_pro = models.IntegerField(blank=True, null=True, db_comment='Número de catálogos promocionados en categoría - profesional')
    banner_index = models.IntegerField(db_comment='Número de imágenes por banner')
    banner_index_pro = models.IntegerField(blank=True, null=True, db_comment='Número de imágenes por banner - profesional')
    credits = models.IntegerField(db_comment='Créditos para el plan')
    credits_pro = models.IntegerField(blank=True, null=True, db_comment='Créditos para el plan profesional')
    tour_virtual_stand_arq = models.BooleanField(db_comment='Permite incluir Tour virtual Arquitectura')  # Cambiado a BooleanField
    tour_virtual_stand_fer = models.BooleanField(db_comment='Permite incluir Tour virtual Ferretería')  # Cambiado a BooleanField
    slider_pro_stand_arq = models.IntegerField(blank=True, null=True, db_comment='Permite la inclusión de sliders pro arquitectura')
    slider_pro_stand_fer = models.IntegerField(blank=True, null=True, db_comment='Permite la inclusión de sliders pro ferretería')
    description_arq = models.CharField(max_length=250, blank=True, null=True, db_comment='Descripción del Plan Arquitectura')
    description_fer = models.CharField(max_length=250, blank=True, null=True, db_comment='Descripción del Plan Ferretería')
    monthly_cost_arq = models.FloatField(blank=True, null=True, db_comment='Costo del plan en valor mensual - Arquitectura')
    monthly_cost_fer = models.FloatField(blank=True, null=True, db_comment='Costo del plan en valor mensual - Ferretería')
    payment_description_arq = models.CharField(max_length=255, blank=True, null=True)
    payment_description_fer = models.CharField(max_length=255, blank=True, null=True)
    features_arq = models.TextField(blank=True, null=True)
    features_fer = models.TextField(blank=True, null=True)
    annual_discount_arq = models.FloatField(blank=True, null=True, db_comment='Descuento en el plan, en caso de pago anualizado - Arquitectura')
    annual_discount_fer = models.FloatField(blank=True, null=True, db_comment='Descuento en el plan, en caso de pago anualizado - Ferretería')
    catalogs_arq = models.IntegerField(blank=True, null=True, db_comment='Número de catálogos para el plan Arquitectura')
    catalogs_fer = models.IntegerField(blank=True, null=True, db_comment='Número de catálogos para el plan Ferretería')
    branding_index_arq = models.BooleanField(blank=True, null=True, db_comment='Permite modificar landing page exhibidor - Arquitectura')  # Cambiado a BooleanField
    branding_index_fer = models.BooleanField(blank=True, null=True, db_comment='Permite modificar landing page exhibidor - Ferretería')  # Cambiado a BooleanField
    video_stand_arq = models.BooleanField(blank=True, null=True, db_comment='Se permite colocar videos en el exhibidor - Arquitectura')  # Cambiado a BooleanField
    video_stand_fer = models.BooleanField(blank=True, null=True, db_comment='Se permite colocar videos en el exhibidor - Ferretería')  # Cambiado a BooleanField
    featured_product_index_arq = models.IntegerField(blank=True, null=True, db_comment='Número de productos destacados en página principal - Arquitectura')
    featured_product_index_fer = models.IntegerField(blank=True, null=True, db_comment='Número de productos destacados en página principal - Ferretería')
    featured_product_category_arq = models.IntegerField(blank=True, null=True, db_comment='Número de productos destacados en categorías - Arquitectura')
    featured_product_category_fer = models.IntegerField(blank=True, null=True, db_comment='Número de productos destacados en categorías - Ferretería')
    featured_catalog_index_arq = models.IntegerField(blank=True, null=True, db_comment='Número de catálogos - Arquitectura')
    featured_catalog_index_fer = models.IntegerField(blank=True, null=True, db_comment='Número de catálogos - Ferretería')
    featured_catalog_category_arq = models.IntegerField(blank=True, null=True, db_comment='Número de catálogos promocionados en categoría - Arquitectura')
    featured_catalog_category_fer = models.IntegerField(blank=True, null=True, db_comment='Número de catálogos promocionados en categoría - Ferretería')
    banner_index_arq = models.IntegerField(blank=True, null=True, db_comment='Número de imágenes por banner - Arquitectura')
    banner_index_fer = models.IntegerField(blank=True, null=True, db_comment='Número de imágenes por banner - Ferretería')
    credits_arq = models.IntegerField(blank=True, null=True, db_comment='Créditos para el plan Arquitectura')
    credits_fer = models.IntegerField(blank=True, null=True, db_comment='Créditos para el plan Ferretería')
    promotion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cex_plan'



class CexPreforma(models.Model):
    service_product_id = models.IntegerField()
    quotes_id = models.IntegerField()
    client_crm_id = models.IntegerField()
    price_public_sale = models.FloatField()
    price = models.FloatField()
    price_countruex = models.FloatField()
    description = models.TextField(blank=True, null=True)
    items_amount = models.IntegerField()
    imagen_remove = models.IntegerField(blank=True, null=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cex_preforma'


class CexPreformaPdf(models.Model):
    pdf_url = models.CharField(max_length=250, blank=True, null=True)
    quotes_id = models.IntegerField()
    created = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cex_preforma_pdf'


class CexProductsTags(models.Model):
    service_product_id = models.IntegerField(primary_key=True)  # The composite primary key (service_product_id, tag_id) found, that is not supported. The first column is selected.
    tag_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cex_products_tags'
        unique_together = (('service_product_id', 'tag_id'),)


class CexProfessionalTypes(models.Model):
    name = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'cex_professional_types'


class CexPromoted(models.Model):
    id_serv_prod = models.IntegerField()
    start_date = models.DateTimeField()
    n_days = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cex_promoted'


class CexProvince(models.Model):
    id = models.IntegerField(primary_key=True)
    country_id = models.IntegerField()
    name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cex_province'


class CexQuotes(models.Model):
    stand_id = models.IntegerField()
    service_product_id = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=32)
    ispaid = models.IntegerField(db_column='isPaid')  # Field name made lowercase.
    quoted_by = models.CharField(max_length=255)
    quoted_on = models.DateTimeField()
    quote_email = models.CharField(max_length=150, blank=True, null=True)
    quote_phone = models.CharField(max_length=45, blank=True, null=True)
    quote_notes = models.TextField(blank=True, null=True)
    quote_preferred_contact = models.CharField(max_length=8)
    quote_time_of_contact = models.CharField(max_length=100, blank=True, null=True)
    service_product_no_of_items = models.IntegerField()
    quote_place_of_contact = models.CharField(max_length=255, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    quote_price = models.FloatField(db_comment='Precio del ítem')
    quote_c1 = models.IntegerField(blank=True, null=True, db_comment='Categoría 1')
    quote_c2 = models.IntegerField(blank=True, null=True, db_comment='Categoría 2')
    quote_c3 = models.IntegerField(blank=True, null=True, db_comment='Categoría 3')
    quote_country = models.IntegerField()
    quote_province = models.IntegerField()
    quote_created = models.DateTimeField()
    quote_opened = models.DateTimeField(blank=True, null=True)
    quote_edited = models.DateTimeField(blank=True, null=True)
    quote_closed = models.DateTimeField(blank=True, null=True)
    number_coins = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    quote_type = models.CharField(max_length=8)
    payed = models.IntegerField()
    latitud = models.CharField(max_length=30, blank=True, null=True)
    longitud = models.CharField(max_length=30, blank=True, null=True)
    project_advance = models.CharField(max_length=25, blank=True, null=True)
    project_type = models.CharField(max_length=33, blank=True, null=True)
    project_finance_status = models.CharField(max_length=26, blank=True, null=True)
    project_value = models.CharField(max_length=17, blank=True, null=True)
    project_name = models.CharField(max_length=50, blank=True, null=True)
    has_budget = models.IntegerField(blank=True, null=True)
    budget = models.FloatField(blank=True, null=True)
    project_responsable = models.CharField(max_length=50, blank=True, null=True)
    project_email = models.CharField(max_length=50, blank=True, null=True)
    project_phone = models.IntegerField(blank=True, null=True)
    project_qualification = models.IntegerField(blank=True, null=True)
    comerce = models.IntegerField(blank=True, null=True)
    qualification_description = models.TextField(blank=True, null=True)
    qualification_status = models.CharField(max_length=16, blank=True, null=True)
    qualification_date = models.DateField(blank=True, null=True)
    manual_admin_quote = models.IntegerField(blank=True, null=True)
    install_time = models.CharField(max_length=250, blank=True, null=True)
    pay_form = models.CharField(max_length=250, blank=True, null=True)
    same_client_address = models.IntegerField(blank=True, null=True)
    delivered_place = models.CharField(max_length=255, blank=True, null=True)
    has_transport = models.IntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    cex_client_crm_id = models.IntegerField(blank=True, null=True)
    created_by_stand = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cex_quotes'
        db_table_comment = 'gestión de cotizaciones'


class CexSeo(models.Model):
    page_title = models.CharField(max_length=60, db_comment='Primary Keyword - Secondary Keyword | Brand Name\n8-foot Green Widgets - Widgets & Tools | Widget World\n50-60 characters\nhttps://moz.com/learn/seo/title-tag')
    page_description = models.CharField(max_length=255, db_comment='160 characters')
    page_keywords = models.CharField(max_length=120, blank=True, null=True)
    og_title = models.CharField(max_length=255, blank=True, null=True)
    og_image = models.CharField(max_length=255, blank=True, null=True)
    og_url = models.CharField(max_length=255, blank=True, null=True)
    og_description = models.CharField(max_length=255, blank=True, null=True)
    twitter_card = models.CharField(max_length=255, blank=True, null=True)
    twitter_url = models.CharField(max_length=255, blank=True, null=True)
    twitter_title = models.CharField(max_length=255, blank=True, null=True)
    twitter_description = models.CharField(max_length=255, blank=True, null=True)
    twitter_image = models.CharField(max_length=255, blank=True, null=True)
    robots = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cex_seo'


class CexServiceProduct(models.Model):
    stand_id = models.IntegerField()
    category_id = models.IntegerField()
    seo_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    brand = models.CharField(max_length=255, blank=True, null=True)
    origin = models.CharField(max_length=45, blank=True, null=True)
    specifications = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=20, db_comment='producto «product» o servicio «service»')
    active = models.TextField()  # This field type is a guess.
    upc = models.CharField(max_length=120)
    price = models.FloatField()
    item_type = models.CharField(max_length=5, blank=True, null=True)
    creation_date = models.DateTimeField()
    image = models.CharField(max_length=255, blank=True, null=True)
    images = models.TextField(blank=True, null=True)
    url_web = models.CharField(max_length=150, blank=True, null=True)
    slug = models.CharField(max_length=45)
    counter = models.IntegerField(db_comment='Contador de accesos\n')
    promoted = models.TextField(db_comment='Produto es promovido')  # This field type is a guess.
    highlight = models.TextField()  # This field type is a guess.
    delivery_to = models.CharField(max_length=255, blank=True, null=True)
    tour_switch = models.IntegerField(db_comment='Switch tour virtual ')
    bnb_switch_switch = models.IntegerField(db_comment='Switch código bnb')
    vr_tour = models.TextField(db_comment='Código tour virtual')
    bnb_code = models.TextField(db_comment='Código bnb')
    position = models.IntegerField(db_comment='Posición del producto')
    discount = models.FloatField()
    has_discount = models.IntegerField()
    delivery_cost = models.FloatField()
    inventory = models.IntegerField()
    can_sell = models.IntegerField()
    price_contruex = models.FloatField()
    price_public_sale = models.FloatField()
    fixed = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cex_service_product'


class CexSettings(models.Model):
    setting_name = models.CharField(primary_key=True, max_length=60)
    setting_value = models.TextField()

    class Meta:
        managed = False
        db_table = 'cex_settings'


class CexShoppingOrder(models.Model):
    user_id = models.CharField(max_length=255)
    date = models.DateTimeField()
    authorization_code = models.CharField(max_length=255)
    tracking_number = models.CharField(max_length=255)
    payment_status = models.IntegerField()
    transaction_id = models.CharField(max_length=255, blank=True, null=True)
    payment_type = models.IntegerField(blank=True, null=True)
    delivery_type = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=255)
    completed = models.IntegerField()
    notes = models.CharField(max_length=255)
    date_delivered = models.DateTimeField(blank=True, null=True)
    total = models.FloatField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cex_shopping_order'


class CexShoppingProduct(models.Model):
    order_id = models.IntegerField()
    product_id = models.IntegerField()
    amount = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cex_shopping_product'


class CexStand(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    stand_type_id = models.IntegerField()
    seo_id = models.IntegerField()
    stand_name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    ruc = models.CharField(max_length=13, blank=True, null=True)
    img = models.CharField(max_length=255, blank=True, null=True)
    hits = models.IntegerField(blank=True, null=True)
    slug = models.CharField(unique=True, max_length=255)
    tour_virtual_code = models.TextField(blank=True, null=True)
    tour_virtual_active = models.TextField()  # This field type is a guess.
    isdeleted = models.TextField(db_column='isDeleted', db_comment='Útil para borrado lógico')  # Field name made lowercase. This field type is a guess.
    isactive = models.TextField(db_column='isActive', db_comment='Útil para uso de activo/inactivo\n')  # Field name made lowercase. This field type is a guess.
    credits_total = models.FloatField(db_comment='Valor de créditos dados por el plan')
    credits_extra = models.FloatField(db_comment='Valor de créditos adquiridos')
    issleep = models.TextField(db_column='isSleep', db_comment='Verificador de Estado Dormido')  # Field name made lowercase. This field type is a guess.
    pro_switch = models.TextField()  # This field type is a guess.
    pro_slide_image = models.CharField(max_length=255)
    pro_body = models.TextField(blank=True, null=True)
    pro_products = models.TextField()
    pro_services = models.TextField()
    pro_faq = models.TextField()
    pro_products_switch = models.TextField()  # This field type is a guess.
    pro_services_switch = models.TextField()  # This field type is a guess.
    pro_hv_switch = models.TextField(db_comment='switch horizontal,vertical')  # This field type is a guess.
    video_code = models.TextField(blank=True, null=True, db_comment='Video del Stand')
    email_manager = models.TextField(blank=True, null=True)
    email_quotes = models.TextField()  # This field type is a guess.
    do_related = models.TextField()  # This field type is a guess.
    can_sell = models.IntegerField()
    switch_store = models.IntegerField()
    store_code = models.TextField(blank=True, null=True)
    professional_type_id = models.IntegerField(blank=True, null=True)
    builder_type_id = models.IntegerField(blank=True, null=True)
    renewal_date = models.DateField(blank=True, null=True)
    state_1 = models.TextField()  # This field type is a guess.
    state_2 = models.TextField()  # This field type is a guess.
    state_3 = models.TextField()  # This field type is a guess.
    state_4 = models.TextField()  # This field type is a guess.
    state_5 = models.TextField()  # This field type is a guess.
    state_6 = models.TextField()  # This field type is a guess.
    state_7 = models.TextField()  # This field type is a guess.
    state_8 = models.TextField()  # This field type is a guess.
    state_9 = models.TextField()  # This field type is a guess.
    state_10 = models.TextField()  # This field type is a guess.
    date_activate_shopping = models.DateTimeField(blank=True, null=True)
    delivery_cost = models.FloatField()
    url = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=30)
    industry_id = models.IntegerField(blank=True, null=True)
    adsense_code = models.TextField(blank=True, null=True)
    adsense_enabled = models.IntegerField()
    cex_whatsapp_phone = models.CharField(max_length=30, blank=True, null=True)
    cex_whatsapp_start_date = models.DateField(blank=True, null=True)
    cex_whatsapp_end_date = models.DateField(blank=True, null=True)
    cex_whatsapp_enabled = models.IntegerField()
    show_map = models.IntegerField(blank=True, null=True)
    manual_end_date_whatsapp = models.IntegerField(blank=True, null=True)
    show_product_price = models.IntegerField(blank=True, null=True)
    percent_price_contruex = models.FloatField()
    percent_price_public_sale = models.FloatField()
    enable_quotes_crm = models.IntegerField(blank=True, null=True)
    cex_manage_crm_start_date = models.DateField(blank=True, null=True)
    cex_manage_crm_end_date = models.DateField(blank=True, null=True)
    manage_crm = models.IntegerField(blank=True, null=True)
    manage_client_quotes_crm = models.IntegerField(blank=True, null=True)
    cex_manage_client_quotes_crm_start_date = models.DateField(blank=True, null=True)
    cex_manage_client_quotes_crm_end_date = models.DateField(blank=True, null=True)
    dealers = models.TextField(db_collation='utf8mb3_unicode_ci', blank=True, null=True, db_comment='(DC2Type:json_array)')
    enable_client_quotes_form = models.IntegerField(blank=True, null=True)
    enable_client_advisory_distributors_form = models.IntegerField(blank=True, null=True)
    other_trans_emails = models.TextField(db_collation='utf8mb3_unicode_ci', blank=True, null=True, db_comment='(DC2Type:json_array)')
    other_users = models.TextField(db_collation='utf8mb3_unicode_ci', blank=True, null=True, db_comment='(DC2Type:json_array)')
    enable_quote_direct = models.IntegerField(blank=True, null=True)
    enable_super_stand = models.IntegerField(blank=True, null=True)
    date_activate_super_stand = models.DateTimeField(blank=True, null=True)
    super_stand_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cex_stand'


class CexStandExpenses(models.Model):
    stand_id = models.IntegerField()
    type = models.CharField(max_length=30)
    amount = models.IntegerField()
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'cex_stand_expenses'


class CexStandIndustry(models.Model):
    stand_id = models.IntegerField()
    industry_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cex_stand_industry'


class CexStandTypes(models.Model):
    type = models.CharField(max_length=120)
    new_profile = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cex_stand_types'


class CexSubscription(models.Model):
    creation_date = models.CharField(max_length=45)
    active = models.IntegerField(blank=True, null=True)
    stand_id = models.IntegerField()
    plan_id = models.IntegerField()
    plan_valid_for = models.IntegerField()
    note = models.CharField(max_length=250, blank=True, null=True)
    edit_user = models.IntegerField(blank=True, null=True)
    months = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cex_subscription'
        db_table_comment = 'Gestion de suscripciones construex'


class CexTag(models.Model):
    frequency = models.IntegerField()
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'cex_tag'


class CexUserQuotes(models.Model):
    user_id = models.IntegerField()
    quotes_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cex_user_quotes'


class CexVirtualTour(models.Model):
    stand_id = models.IntegerField()
    name = models.CharField(unique=True, max_length=255)
    description = models.TextField(blank=True, null=True)
    code = models.TextField(blank=True, null=True)
    slug = models.CharField(unique=True, max_length=255)
    img = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'cex_virtual_tour'


class CexWallet(models.Model):
    date = models.CharField(max_length=255, blank=True, null=True)
    action = models.CharField(max_length=2, db_comment='Acción realizada')
    amount = models.FloatField(blank=True, null=True)
    balance = models.FloatField(blank=True, null=True)
    cex_stand_id = models.IntegerField()
    log_usr = models.IntegerField()
    transaction_detail = models.TextField()
    plan_credits = models.FloatField(blank=True, null=True, db_comment='control de créditos del plan')
    purchased_credits = models.FloatField(blank=True, null=True, db_comment='control de créditos adquiridos')

    class Meta:
        managed = False
        db_table = 'cex_wallet'


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
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Migration(models.Model):
    version = models.CharField(primary_key=True, max_length=180)
    apply_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'migration'


class Profile(models.Model):
    user_id = models.IntegerField(primary_key=True, db_comment='dektrium')
    name = models.CharField(max_length=255, db_collation='utf8mb3_uca1400_ai_ci', blank=True, null=True, db_comment='dektrium')
    public_email = models.CharField(max_length=255, db_collation='utf8mb3_uca1400_ai_ci', blank=True, null=True, db_comment='dektrium')
    gravatar_email = models.CharField(max_length=255, db_collation='utf8mb3_uca1400_ai_ci', blank=True, null=True, db_comment='dektrium')
    gravatar_id = models.CharField(max_length=32, db_collation='utf8mb3_uca1400_ai_ci', blank=True, null=True, db_comment='dektrium')
    location = models.CharField(max_length=255, db_collation='utf8mb3_uca1400_ai_ci', blank=True, null=True, db_comment='localidad lat,lng')
    website = models.CharField(max_length=255, db_collation='utf8mb3_uca1400_ai_ci', blank=True, null=True, db_comment='Sitio web')
    bio = models.TextField(db_collation='utf8mb3_uca1400_ai_ci', blank=True, null=True, db_comment='Biografía')
    timezone = models.CharField(max_length=40, db_collation='utf8mb3_uca1400_ai_ci', blank=True, null=True, db_comment='Zona horaria')
    cex_first_name = models.CharField(max_length=100, db_collation='utf8mb3_uca1400_ai_ci', blank=True, null=True)
    cex_last_name = models.CharField(max_length=100, db_collation='utf8mb3_uca1400_ai_ci', blank=True, null=True, db_comment='Apellido')
    cex_contact_phone = models.CharField(max_length=45, db_collation='utf8mb3_uca1400_ai_ci', blank=True, null=True, db_comment='Teléfono de contacto')
    cex_newsfeed_subscription = models.TextField(blank=True, null=True, db_comment='Subscripción a noticias')  # This field type is a guess.
    cex_city = models.CharField(max_length=45, db_collation='utf8mb3_uca1400_ai_ci', blank=True, null=True, db_comment='Ciudad')
    cex_country_id = models.IntegerField(blank=True, null=True, db_comment='Pais Id')
    cex_province_id = models.IntegerField(blank=True, null=True)
    cex_status = models.CharField(max_length=25, db_comment='Status del usuario')
    cex_comments = models.TextField(blank=True, null=True)
    cex_home_address = models.CharField(max_length=255, blank=True, null=True)
    cex_billing_address = models.CharField(max_length=255, blank=True, null=True)
    cex_ruc = models.CharField(max_length=13, blank=True, null=True)
    cex_contact_home_phone = models.CharField(max_length=45)
    email_visitor_sent = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'profile'


class SocialAccount(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    provider = models.CharField(max_length=255, db_collation='utf8mb3_uca1400_ai_ci')
    client_id = models.CharField(max_length=255, db_collation='utf8mb3_uca1400_ai_ci')
    data = models.TextField(db_collation='utf8mb3_uca1400_ai_ci', blank=True, null=True)
    code = models.CharField(unique=True, max_length=32, db_collation='utf8mb3_uca1400_ai_ci', blank=True, null=True)
    created_at = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=255, db_collation='utf8mb3_uca1400_ai_ci', blank=True, null=True)
    username = models.CharField(max_length=255, db_collation='utf8mb3_uca1400_ai_ci', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'social_account'
        unique_together = (('provider', 'client_id'),)


class Token(models.Model):
    user_id = models.IntegerField()
    code = models.CharField(max_length=32, db_collation='utf8mb3_uca1400_ai_ci')
    created_at = models.IntegerField()
    type = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'token'


class User(models.Model):
    username = models.CharField(unique=True, max_length=255, db_collation='utf8mb3_uca1400_ai_ci')
    email = models.CharField(unique=True, max_length=255, db_collation='utf8mb3_uca1400_ai_ci')
    password_hash = models.CharField(max_length=60, db_collation='utf8mb3_uca1400_ai_ci')
    auth_key = models.CharField(max_length=32, db_collation='utf8mb3_uca1400_ai_ci')
    confirmed_at = models.IntegerField(blank=True, null=True)
    unconfirmed_email = models.CharField(max_length=255, db_collation='utf8mb3_uca1400_ai_ci', blank=True, null=True)
    blocked_at = models.IntegerField(blank=True, null=True)
    registration_ip = models.CharField(max_length=45, db_collation='utf8mb3_uca1400_ai_ci', blank=True, null=True)
    created_at = models.IntegerField()
    updated_at = models.IntegerField()
    flags = models.IntegerField(blank=True, null=True)
    last_login_at = models.IntegerField(blank=True, null=True)
    stand_id = models.IntegerField(blank=True, null=True)
    terms_and_conditions = models.BooleanField(db_comment='Términos y condiciones aceptados o no aceptados')
    stand_assign = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
