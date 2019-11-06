from django.db import models

class IotDevice(models.Model):
    name = models.CharField(max_length=150)
    deviceid = models.CharField(max_length=10,default="0")
    type = models.IntegerField()
    typealias = models.CharField(max_length=20)
    CmdTopic = models.CharField(db_column="cmdtopic",max_length=255,default="0")
    StateTopic = models.CharField(db_column="statetopic",max_length=255, default="ismrx/iot/#", null=True, blank=True)
    state = models.CharField(max_length=10,default="0",null=True,blank=True)
    args = models.CharField(max_length=255,default="0",null=True,blank=True)

    class Meta:
        db_table = 'iot_device'

class IotDeviceType(models.Model):
    typealias = models.CharField(max_length=20)
    icon = models.TextField()
    properties = models.TextField()
    actions = models.TextField()
    extensions = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'iot_device_type'
