# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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
    first_name = models.CharField(max_length=30)
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


class Comments(models.Model):
    commentid = models.AutoField(db_column='CommentID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    theaterid = models.ForeignKey('Theaters', models.DO_NOTHING, db_column='TheaterID')  # Field name made lowercase.
    content = models.CharField(db_column='Content', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reply = models.CharField(db_column='Reply', max_length=255, blank=True, null=True)  # Field name made lowercase.
    likes = models.IntegerField(db_column='Likes', blank=True, null=True)  # Field name made lowercase.
    image = models.TextField(db_column='Image', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'comments'


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


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Theaters(models.Model):
    theaterid = models.AutoField(db_column='TheaterID', primary_key=True)  # Field name made lowercase.
    theatername = models.CharField(db_column='TheaterName', max_length=50)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=50)  # Field name made lowercase.
    period = models.CharField(db_column='Period', max_length=50)  # Field name made lowercase.
    place = models.CharField(db_column='Place', max_length=50)  # Field name made lowercase.
    openingday = models.DateField(db_column='OpeningDay')  # Field name made lowercase.
    closingday = models.DateField(db_column='ClosingDay', blank=True, null=True)  # Field name made lowercase.
    openrun = models.CharField(db_column='OpenRun', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'theaters'


class TheatersDetails(models.Model):
    theaterid = models.OneToOneField(Theaters, models.DO_NOTHING, db_column='TheaterID', primary_key=True)  # Field name made lowercase.
    viewingage = models.CharField(db_column='ViewingAge', max_length=50, blank=True, null=True)  # Field name made lowercase.
    performancetime = models.CharField(db_column='PerformanceTime', max_length=50, blank=True, null=True)  # Field name made lowercase.
    descriptions = models.CharField(db_column='Descriptions', max_length=255, blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=7, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    shoptitle = models.CharField(db_column='ShopTitle', max_length=50, blank=True, null=True)  # Field name made lowercase.
    shoplink = models.TextField(db_column='ShopLink', blank=True, null=True)  # Field name made lowercase.
    image = models.CharField(db_column='Image', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'theaters_details'


class Users(models.Model):
    userid = models.AutoField(db_column='UserID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users'
