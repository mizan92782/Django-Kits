# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models





class MyappAddress(models.Model):
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'myapp_address'


class MyappCustomer(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.CharField(max_length=20)
    address = models.ForeignKey(MyappAddress, models.DO_NOTHING)
    user = models.OneToOneField('MyappUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'myapp_customer'


class MyappPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField()
    user = models.ForeignKey('MyappUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'myapp_post'


class MyappUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    email = models.CharField(unique=True, max_length=254)
    is_active = models.BooleanField()
    is_staff = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'myapp_user'


class MyappUserGroups(models.Model):
    user = models.ForeignKey(MyappUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'myapp_user_groups'
        unique_together = (('user', 'group'),)

        