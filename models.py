# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Abog(models.Model):
    id_abog = models.AutoField(db_column='Id_abog', primary_key=True)  # Field name made lowercase.
    id_usu_sist = models.ForeignKey('UsuSist', models.DO_NOTHING, db_column='Id_Usu_sist', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Abog'


class AuditoriaCambios(models.Model):
    id_auditoria = models.AutoField(db_column='Id_Auditoria', primary_key=True)  # Field name made lowercase.
    tabla = models.CharField(db_column='Tabla', max_length=100, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fecha_oper = models.DateTimeField(db_column='Fecha_oper', blank=True, null=True)  # Field name made lowercase.
    tipo_oper = models.CharField(db_column='Tipo_oper', max_length=50, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    datos_anti = models.TextField(db_column='Datos_anti', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    datos_nuev = models.TextField(db_column='Datos_nuev', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=100, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    datos = models.TextField(db_column='Datos', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Auditoria_Cambios'


class Caso(models.Model):
    id_caso = models.AutoField(db_column='Id_caso', primary_key=True)  # Field name made lowercase.
    fec_asig = models.DateTimeField(db_column='Fec_Asig')  # Field name made lowercase.
    deta = models.TextField(db_column='Deta', db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    id_esta = models.ForeignKey('Est', models.DO_NOTHING, db_column='Id_esta', blank=True, null=True)  # Field name made lowercase.
    id_abog = models.ForeignKey(Abog, models.DO_NOTHING, db_column='Id_abog', blank=True, null=True)  # Field name made lowercase.
    id_tip_ayu = models.ForeignKey('TipAyu', models.DO_NOTHING, db_column='Id_tip_ayu', blank=True, null=True)  # Field name made lowercase.
    id_hecho = models.ForeignKey('Hecho', models.DO_NOTHING, db_column='Id_hecho', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Caso'


class DatVic(models.Model):
    id_dat_vic = models.AutoField(db_column='ID_Dat_Vic', primary_key=True)  # Field name made lowercase.
    fe_naci = models.DateField(db_column='Fe_naci')  # Field name made lowercase.
    id_depar_naci = models.ForeignKey('Depar', models.DO_NOTHING, db_column='Id_Depar_Naci', blank=True, null=True)  # Field name made lowercase.
    id_depar_resi = models.ForeignKey('Depar', models.DO_NOTHING, db_column='Id_Depar_Resi', related_name='datvic_id_depar_resi_set', blank=True, null=True)  # Field name made lowercase.
    id_gp_etni = models.ForeignKey('GpEtni', models.DO_NOTHING, db_column='Id_gp_etni', blank=True, null=True)  # Field name made lowercase.
    id_tip_ayu = models.ForeignKey('TipAyu', models.DO_NOTHING, db_column='Id_tip_ayu', blank=True, null=True)  # Field name made lowercase.
    id_gen = models.ForeignKey('Gene', models.DO_NOTHING, db_column='Id_Gen', blank=True, null=True)  # Field name made lowercase.
    id_usu_sist = models.ForeignKey('UsuSist', models.DO_NOTHING, db_column='Id_Usu_sist', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Dat_Vic'


class Depar(models.Model):
    id_dep = models.AutoField(db_column='Id_dep', primary_key=True)  # Field name made lowercase.
    nom_dep = models.TextField(db_column='Nom_dep', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Depar'


class Descotrogen(models.Model):
    id_desc = models.AutoField(db_column='Id_Desc', primary_key=True)  # Field name made lowercase.
    descripcion = models.TextField(db_column='Descripcion', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    id_gen = models.ForeignKey('Gene', models.DO_NOTHING, db_column='Id_Gen', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DescOtroGen'


class Docu(models.Model):
    id_docu = models.AutoField(db_column='Id_docu', primary_key=True)  # Field name made lowercase.
    escri_terre = models.BinaryField(db_column='Escri_terre')  # Field name made lowercase.
    car_dema = models.BinaryField(db_column='Car_dema')  # Field name made lowercase.
    fot_cedu = models.BinaryField(db_column='Fot_cedu')  # Field name made lowercase.
    id_dat_vic = models.ForeignKey(DatVic, models.DO_NOTHING, db_column='ID_Dat_Vic', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Docu'


class Est(models.Model):
    id_esta = models.AutoField(db_column='Id_esta', primary_key=True)  # Field name made lowercase.
    tip_esta = models.CharField(db_column='Tip_esta', max_length=255, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Est'


class Gene(models.Model):
    id_gen = models.AutoField(db_column='Id_Gen', primary_key=True)  # Field name made lowercase.
    tp_gen = models.TextField(db_column='Tp_Gen', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Gene'


class GpEtni(models.Model):
    id_gp_etni = models.AutoField(db_column='Id_gp_etni', primary_key=True)  # Field name made lowercase.
    nom_gp_etni = models.TextField(db_column='Nom_Gp_etni', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Gp_etni'


class Hecho(models.Model):
    id_hecho = models.AutoField(db_column='Id_hecho', primary_key=True)  # Field name made lowercase.
    rela_hecho = models.BinaryField(db_column='Rela_hecho')  # Field name made lowercase.
    rela_hecho_testi = models.BinaryField(db_column='Rela_hecho_testi')  # Field name made lowercase.
    lugar_terre = models.BinaryField(db_column='Lugar_Terre')  # Field name made lowercase.
    id_dep = models.ForeignKey(Depar, models.DO_NOTHING, db_column='Id_dep', blank=True, null=True)  # Field name made lowercase.
    id_docu = models.ForeignKey(Docu, models.DO_NOTHING, db_column='Id_docu', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Hecho'


class PartiAyu(models.Model):
    id_parti_ayu = models.AutoField(db_column='Id_parti_ayu', primary_key=True)  # Field name made lowercase.
    fecha_ini = models.DateTimeField(db_column='Fecha_ini')  # Field name made lowercase.
    fecha_fina = models.DateTimeField(db_column='Fecha_fina')  # Field name made lowercase.
    id_esta = models.ForeignKey(Est, models.DO_NOTHING, db_column='Id_esta', blank=True, null=True)  # Field name made lowercase.
    id_dat_vic = models.ForeignKey(DatVic, models.DO_NOTHING, db_column='ID_Dat_Vic', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Parti_Ayu'


class Rol(models.Model):
    id_rol = models.AutoField(db_column='Id_Rol', primary_key=True)  # Field name made lowercase.
    nom_rol = models.CharField(db_column='Nom_Rol', max_length=50, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Rol'


class SegCasoVic(models.Model):
    id_seg_caso_vic = models.AutoField(db_column='Id_Seg_caso_vic', primary_key=True)  # Field name made lowercase.
    id_abog = models.ForeignKey(Abog, models.DO_NOTHING, db_column='ID_abog', blank=True, null=True)  # Field name made lowercase.
    id_esta = models.ForeignKey(Est, models.DO_NOTHING, db_column='Id_esta', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Seg_caso_vic'


class TipAyu(models.Model):
    id_tip_ayu = models.AutoField(db_column='Id_tip_ayu', primary_key=True)  # Field name made lowercase.
    nom_tip_ayu = models.CharField(db_column='Nom_tip_ayu', max_length=255, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    id_esta = models.ForeignKey(Est, models.DO_NOTHING, db_column='Id_esta', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tip_ayu'


class TpDocident(models.Model):
    id_tpdoc_ident = models.AutoField(db_column='Id_TpDoc_Ident', primary_key=True)  # Field name made lowercase.
    nom_doc_ident = models.CharField(db_column='Nom_Doc_Ident', max_length=50, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tp_DocIdent'


class UsuLog(models.Model):
    id_usu_log = models.AutoField(db_column='Id_Usu_log', primary_key=True)  # Field name made lowercase.
    corr = models.CharField(db_column='Corr', max_length=255, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    contra = models.CharField(db_column='Contra', max_length=255, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    id_usu_sist = models.ForeignKey('UsuSist', models.DO_NOTHING, db_column='Id_Usu_sist', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Usu_log'


class UsuSist(models.Model):
    id_usu_sist = models.AutoField(db_column='Id_Usu_sist', primary_key=True)  # Field name made lowercase.
    p_nom = models.TextField(db_column='P_Nom', db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    s_nom = models.TextField(db_column='S_Nom', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    p_apell = models.TextField(db_column='P_Apell', db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    s_apell = models.TextField(db_column='S_Apell', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    num_ident = models.BigIntegerField(db_column='Num_Ident')  # Field name made lowercase.
    direc = models.CharField(db_column='Direc', max_length=30, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    num_tel1 = models.BigIntegerField(db_column='Num_Tel1')  # Field name made lowercase.
    num_tel2 = models.BigIntegerField(db_column='Num_Tel2', blank=True, null=True)  # Field name made lowercase.
    corr = models.CharField(db_column='Corr', max_length=255, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    contra = models.CharField(db_column='Contra', max_length=255, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    id_rol = models.ForeignKey(Rol, models.DO_NOTHING, db_column='Id_Rol', blank=True, null=True)  # Field name made lowercase.
    id_tpdoc_ident = models.ForeignKey(TpDocident, models.DO_NOTHING, db_column='Id_TpDoc_Ident', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Usu_sist'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, db_collation='Modern_Spanish_CI_AS')

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


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, db_collation='Modern_Spanish_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, db_collation='Modern_Spanish_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, db_collation='Modern_Spanish_CI_AS')
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, db_collation='Modern_Spanish_CI_AS')
    first_name = models.CharField(max_length=150, db_collation='Modern_Spanish_CI_AS')
    last_name = models.CharField(max_length=150, db_collation='Modern_Spanish_CI_AS')
    email = models.CharField(max_length=254, db_collation='Modern_Spanish_CI_AS')
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    object_repr = models.CharField(max_length=200, db_collation='Modern_Spanish_CI_AS')
    action_flag = models.SmallIntegerField()
    change_message = models.TextField(db_collation='Modern_Spanish_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, db_collation='Modern_Spanish_CI_AS')
    model = models.CharField(max_length=100, db_collation='Modern_Spanish_CI_AS')

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, db_collation='Modern_Spanish_CI_AS')
    name = models.CharField(max_length=255, db_collation='Modern_Spanish_CI_AS')
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40, db_collation='Modern_Spanish_CI_AS')
    session_data = models.TextField(db_collation='Modern_Spanish_CI_AS')
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


#class Solicitud(models.Model):
   # id_sol = models.AutoField(primary_key=True)
    #fec_sol = models.DateTimeField()
    #est_sol = models.CharField(max_length=30)
    #id_docu = models.ForeignKey(Docu, models.DO_NOTHING)

   
   # class Meta:
    #    managed = False  # Le indica a Django que no intente crear/migrar esta "tabla"
     #   db_table = 'vw_solicitudes'  # El nombre exacto de la vista en tu base de datos