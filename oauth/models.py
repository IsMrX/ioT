from django.db import models

# Create your models here.

class OAuthUser(models.Model):
    name = models.CharField(max_length=10)
    passw = models.CharField(db_column="password", max_length=16)

    class Meta:
        db_table = 'oauth_user'

class OAuthCode(models.Model):
    code = models.CharField(max_length=10)
    url = models.CharField(max_length=255,default="")
    ClientId = models.CharField(db_column="client_id", max_length=255,default="")
    scope = models.CharField(max_length=255,default="")
    time = models.IntegerField()

    class Meta:
        db_table = 'oauth_code'

class OAuthClient(models.Model):
    client = models.CharField(max_length=16)
    secret = models.CharField(max_length=100)
    annotation = models.CharField(max_length=255)

    class Meta:
        db_table = 'oauth_client'

class OAuthToken(models.Model):
    access = models.CharField(max_length=16)
    refresh = models.CharField(max_length=16)
    scope = models.CharField(max_length=255,default="")
    client = models.CharField(max_length=16,default="")
    time = models.IntegerField()

    class Meta:
        db_table = 'oauth_token'
