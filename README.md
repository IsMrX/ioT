# ioT
MQTT 接入到天猫精灵
1.带完整oauth2认证
2.访问api接口,可自定义添加多种物联网设备

依赖:
    python版本: 3.5  django版本: 2.2.2  mysqlclient: 1.4.2  paho-mqtt: 1.4.0
# 操作方式
一.服务端oauth2部分配置

二.django的服务的常用安装

三.数据库里添加用户

    oauth_client  client:oauth2的clientId  secret:oauth2的secret  annotation:备注

    oauth_user  oauth的用户账号密码

四.天猫精灵开放平台配置

五.天猫精灵控制台添加技能

六.服务设置处配置:

    账户授权连接：https://域名/oauth/code

    Client Id: 填入(一.2) 里oauth_client的client内容

    Client Secret: 填入(一.2) 里oauth_client的secret内容

    Access Token URL: https://域名/oauth/token

    开发者网关地址:此处为开发者的网关接口地址,本项目的地址为:https://域名/iMrX/code

七.测试验证:

    开启测试

    新窗打开

    账户配置

    填入(一.2) 里oauth_user的账户名与密码

到此oauth2验证部分结束,稍后天猫精灵会自动调用网关接口获取设备列表

注意:天猫精灵要求oauth2的响应请求url必须为https