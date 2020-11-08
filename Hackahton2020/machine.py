#!/usr/bin/env python3
# Author: David Almog
# Version: 1.0
import collections
from netmiko import ConnectHandler

Machine = collections.namedtuple('Machine',['ip','type','user','ps','validations','status'])
machine = Machine._make(['192.168.199.135','Ubntu','rio','zubur1',None,None])

iosv_l2 = {
    'device_type': 'linux',
    'ip':machine.ip,
    'username':machine.user,
    'password': machine.ps,
}
try:
    net_connect = ConnectHandler(**iosv_l2)
    output = net_connect.send_command('ip a | grep "ens33" | grep "inet" | cut -d " " -f 6')
    machine._replace(status = 2)
    print(f"output = {output}")
except:
    machine._replace(status = 0)
    print(f"Failed connect to {machine.ip}")
print(machine)