# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-29 15:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('asset', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name=b'ad\xe8\xb4\xa6\xe5\x8f\xb7')),
                ('cn_name', models.CharField(max_length=50, null=True, verbose_name=b'\xe5\xa7\x93\xe5\x90\x8d')),
                ('phone', models.CharField(max_length=50, null=True, verbose_name=b'\xe8\x81\x94\xe7\xb3\xbb\xe7\x94\xb5\xe8\xaf\x9d')),
                ('mail', models.EmailField(max_length=254, null=True, verbose_name=b'\xe8\x81\x94\xe7\xb3\xbb\xe9\x82\xae\xe7\xae\xb1')),
            ],
            options={
                'verbose_name': '\u8054\u7cfb\u4eba',
                'verbose_name_plural': '\u8054\u7cfb\u4eba',
            },
        ),
        migrations.CreateModel(
            name='HostInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(blank=True, max_length=255, verbose_name='\u7269\u7406\u4e3b\u673a\u540d')),
                ('ip', models.GenericIPAddressField(verbose_name='\u7269\u7406\u4e3b\u673aIP\u5730\u5740')),
                ('manage_ip', models.GenericIPAddressField(blank=True, null=True, verbose_name=b'\xe8\xbf\x9c\xe6\x8e\xa7\xe5\x8d\xa1IP')),
                ('app_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='\u4e3b\u673a\u5e94\u7528\u540d\u79f0')),
                ('app_description', models.CharField(blank=True, max_length=100, null=True, verbose_name='\u4e3b\u673a\u5e94\u7528\u63cf\u8ff0')),
                ('Cabinet', models.CharField(blank=True, max_length=10, null=True, verbose_name='\u673a\u67dc\u4f4d\u7f6e')),
                ('OS', models.CharField(blank=True, choices=[('Microsoft Windows', 'Microsoft Windows'), ('Linux', 'Linux'), ('VMware ESX Server', 'VMware ESX Server')], max_length=50, null=True, verbose_name='\u64cd\u4f5c\u7cfb\u7edf')),
                ('OsVersion', models.CharField(blank=True, choices=[('CentOS 5_x64', 'CentOS 5 (64\u4f4d)'), ('CentOS 5.8_x64', 'CentOS 5.8 (64\u4f4d)'), ('CentOS 7_x64', 'CentOS 7 (64\u4f4d)'), ('CentOS 6.5_x64', 'CentOS 6.5 (64\u4f4d)'), ('CentOS 6.7_x64', 'CentOS 6.7 (64\u4f4d)'), ('Linux\u5b9a\u5236', 'Linux\u5b9a\u5236'), ('Microsoft Windows 7', 'Microsoft Windows 7'), ('Microsoft Windows Server 2003', 'Microsoft Windows Server 2003'), ('Microsoft Windows Server 2008', 'Microsoft Windows Server 2008'), ('Microsoft Windows Server 2008 R2', 'Microsoft Windows Server 2008 R2'), ('Microsoft Windows XP Professional', 'Microsoft Windows XP Professional'), ('RHEL 6.5_x64', 'RHEL 6.5_x64'), ('RHEL 5.4_x64', 'RHEL 5.4_x64'), ('Ubuntu 12_x64', 'Ubuntu 12_x64'), ('Ubuntu Linux_x64', 'Ubuntu Linux_x64'), ('ESXI 5.0', 'ESXI 5.0'), ('ESXI 5.1 U3', 'ESXI 5.1 U3'), ('Ubuntu Linux_x64', 'Ubuntu Linux_x64'), ('Win 8.1_x64', 'Win 8.1_x64')], max_length=50, null=True, verbose_name='\u64cd\u4f5c\u7cfb\u7edf\u7248\u672c\u53f7')),
                ('Cluster', models.NullBooleanField(default=False, verbose_name='\u96c6\u7fa4')),
                ('TotalHardDisk', models.CharField(blank=True, max_length=10, null=True, verbose_name='\u603b\u786c\u76d8\u5bb9\u91cf')),
                ('CPU', models.CharField(blank=True, max_length=10, null=True, verbose_name='CPU\u6838\u5fc3\u6570\u91cf')),
                ('CpuMainFrequency', models.CharField(blank=True, max_length=10, null=True, verbose_name='CPU\u4e3b\u9891')),
                ('mem', models.IntegerField(blank=True, null=True, verbose_name='\u5185\u5b58')),
                ('Raid', models.CharField(blank=True, choices=[('1', 'raid1'), ('2', 'raid2'), ('5', 'raid5'), ('0', 'raid0'), ('0+1', 'raid0+1')], max_length=10, null=True, verbose_name='\u78c1\u76d8\u9635\u5217\u4fe1\u606f')),
                ('fibrechannelhbacards', models.NullBooleanField(default=False, verbose_name='\u5149\u7ea4\u901a\u9053\u5361')),
                ('fiberswitchport', models.CharField(blank=True, max_length=30, null=True, verbose_name='\u5149\u7ea4\u4ea4\u6362\u673a\u7aef\u53e3')),
                ('Domain', models.CharField(blank=True, choices=[('addom.xinaogroup.com', 'addom.xinaogroup.com'), ('adlab.xinaogroup.com', 'adlab.xinaogroup.com'), ('test.xinaogroup.com', 'test.xinaogroup.com')], max_length=20, null=True, verbose_name='\u57df\u4fe1\u606f')),
                ('dmz', models.NullBooleanField(default=False, verbose_name='DMZ')),
                ('type', models.CharField(blank=True, choices=[('\u751f\u4ea7', '\u751f\u4ea7'), ('\u5f00\u53d1\u6d4b\u8bd5', '\u5f00\u53d1\u6d4b\u8bd5'), ('\u5b9e\u9a8c', '\u5b9e\u9a8c')], max_length=10, verbose_name='\u5e94\u7528\u670d\u52a1\u7c7b\u522b')),
                ('delivery_time', models.DateField(blank=True, null=True, verbose_name='\u8d44\u6e90\u4ea4\u4ed8\u65f6\u95f4')),
                ('datacenter_address', models.CharField(blank=True, max_length=10, null=True, verbose_name='\u4f4d\u7f6e')),
                ('born_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='\u4e0a\u6b21\u4fee\u6539\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u7269\u7406\u4e3b\u673a',
                'verbose_name_plural': '\u7269\u7406\u4e3b\u673a',
            },
        ),
        migrations.CreateModel(
            name='NetworkDeviceInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sn', models.CharField(blank=True, max_length=50, null=True, verbose_name=b'SN\xe5\x8f\xb7')),
                ('company_name', models.CharField(blank=True, max_length=50, null=True, verbose_name=b'\xe4\xbc\x81\xe4\xb8\x9a\xe5\x90\x8d\xe7\xa7\xb0')),
                ('dc_location', models.NullBooleanField(max_length=50, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe6\x95\xb0\xe6\x8d\xae\xe4\xb8\xad\xe5\xbf\x83')),
                ('industry_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='asset.IndustryGroup')),
                ('network_device', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='asset.NetworkDevice', verbose_name=b'\xe6\x8c\x82\xe8\xbd\xbd\xe8\xae\xbe\xe5\xa4\x87')),
            ],
        ),
        migrations.CreateModel(
            name='VMServer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=255, null=True, unique=True, verbose_name='\u4e3b\u673a\u540d')),
                ('ip', models.GenericIPAddressField(verbose_name='IP\u5730\u5740')),
                ('app_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='\u5e94\u7528\u540d\u79f0')),
                ('app_role', models.CharField(blank=True, max_length=30, null=True, verbose_name='\u5e94\u7528\u89d2\u8272')),
                ('app_description', models.CharField(blank=True, max_length=100, null=True, verbose_name='\u5e94\u7528\u63cf\u8ff0')),
                ('type', models.CharField(blank=True, choices=[('\u751f\u4ea7', '\u751f\u4ea7'), ('\u5f00\u53d1\u6d4b\u8bd5', '\u5f00\u53d1\u6d4b\u8bd5'), ('\u5b9e\u9a8c', '\u5b9e\u9a8c')], max_length=10, null=True, verbose_name='\u7c7b\u522b')),
                ('os', models.CharField(blank=True, choices=[('Microsoft Windows', 'Microsoft Windows'), ('Linux', 'Linux'), ('VMware ESX Server', 'VMware ESX Server')], max_length=50, null=True, verbose_name='\u64cd\u4f5c\u7cfb\u7edf')),
                ('os_version', models.CharField(blank=True, choices=[('CentOS 5_x64', 'CentOS 5 (64\u4f4d)'), ('CentOS 5.8_x64', 'CentOS 5.8 (64\u4f4d)'), ('CentOS 7_x64', 'CentOS 7 (64\u4f4d)'), ('CentOS 6.5_x64', 'CentOS 6.5 (64\u4f4d)'), ('CentOS 6.7_x64', 'CentOS 6.7 (64\u4f4d)'), ('Linux\u5b9a\u5236', 'Linux\u5b9a\u5236'), ('Microsoft Windows 7', 'Microsoft Windows 7'), ('Microsoft Windows Server 2003', 'Microsoft Windows Server 2003'), ('Microsoft Windows Server 2008', 'Microsoft Windows Server 2008'), ('Microsoft Windows Server 2008 R2', 'Microsoft Windows Server 2008 R2'), ('Microsoft Windows XP Professional', 'Microsoft Windows XP Professional'), ('RHEL 6.5_x64', 'RHEL 6.5_x64'), ('RHEL 5.4_x64', 'RHEL 5.4_x64'), ('Ubuntu 12_x64', 'Ubuntu 12_x64'), ('Ubuntu Linux_x64', 'Ubuntu Linux_x64'), ('ESXI 5.0', 'ESXI 5.0'), ('ESXI 5.1 U3', 'ESXI 5.1 U3'), ('Ubuntu Linux_x64', 'Ubuntu Linux_x64'), ('Win 8.1_x64', 'Win 8.1_x64')], max_length=50, null=True, verbose_name='\u64cd\u4f5c\u7cfb\u7edf\u7248\u672c\u53f7')),
                ('cluster', models.NullBooleanField(default=False, verbose_name='\u96c6\u7fa4')),
                ('hard_disk', models.CharField(blank=True, max_length=10, null=True, verbose_name='\u786c\u76d8\u5bb9\u91cf')),
                ('total_hard_disk', models.CharField(blank=True, max_length=10, null=True, verbose_name='\u603b\u786c\u76d8\u5bb9\u91cf')),
                ('cpu', models.IntegerField(blank=True, null=True, verbose_name='CPU\u6838\u5fc3\u6570\u91cf')),
                ('mem', models.CharField(blank=True, max_length=5, null=True, verbose_name='\u5185\u5b58')),
                ('domain', models.CharField(blank=True, choices=[('addom.xinaogroup.com', 'addom.xinaogroup.com'), ('adlab.xinaogroup.com', 'adlab.xinaogroup.com'), ('test.xinaogroup.com', 'test.xinaogroup.com')], max_length=20, null=True, verbose_name='\u57df\u4fe1\u606f')),
                ('create_time', models.DateField(max_length=20, null=True, verbose_name='\u8d44\u6e90\u4ea4\u4ed8\u65f6\u95f4')),
                ('delete_time', models.DateField(blank=True, max_length=20, null=True, verbose_name='\u8d44\u6e90\u5220\u9664\u65f6\u95f4')),
                ('born_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='\u4e0a\u6b21\u4fee\u6539\u65f6\u95f4')),
                ('admin_con', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ops.Contact', to_field=b'name', verbose_name=b'\xe7\xae\xa1\xe7\x90\x86\xe5\x91\x98')),
                ('industry_groupName', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='asset.IndustryGroup', to_field=b'name', verbose_name=b'\xe8\xae\xa1\xe8\xb4\xb9\xe7\xbb\x84')),
            ],
            options={
                'verbose_name': '\u865a\u62df\u4e3b\u673a',
                'verbose_name_plural': '\u865a\u62df\u4e3b\u673a',
            },
        ),
        migrations.CreateModel(
            name='VspherePool',
            fields=[
                ('pool_name', models.CharField(max_length=20, unique=True, verbose_name='\u8d44\u6e90\u6c60')),
                ('pool_id', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True, verbose_name='\u8d44\u6e90\u6c60ID')),
                ('pool_desc', models.CharField(max_length=20, null=True, verbose_name='\u63cf\u8ff0')),
                ('born_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='\u4e0a\u6b21\u4fee\u6539\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u8d44\u6e90\u6c60',
                'verbose_name_plural': '\u8d44\u6e90\u6c60',
            },
        ),
        migrations.AddField(
            model_name='vmserver',
            name='pool_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ops.VspherePool', verbose_name=b'\xe8\xb5\x84\xe6\xba\x90\xe6\xb1\xa0'),
        ),
        migrations.AddField(
            model_name='hostinfo',
            name='pool',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ops.VspherePool', verbose_name=b'\xe8\xb5\x84\xe6\xba\x90\xe6\xb1\xa0'),
        ),
        migrations.AddField(
            model_name='hostinfo',
            name='sn',
            field=models.ForeignKey(db_column=b'sn', on_delete=django.db.models.deletion.CASCADE, to='asset.Host', to_field=b'sn', verbose_name=b'SN\xe5\x8f\xb7'),
        ),
    ]
