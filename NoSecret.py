#!/usr/bin/env python
from netmiko import ConnectHandler
import getpass

device = { 
    'device_type': 'cisco_ios',
    'ip': 'placeholder',
    'username': 'because',
    'password': 'idkhow2use',
    'secret': 'netmiko',
} 
write_file = open('WriteConfirm.txt', 'w')

devicelist = open('WriteConf.txt', 'r')
print('Oh shoot it is a script!')
device['username'] = input('Gimmie dat user: ')
device['password'] = getpass.getpass()   #input('And pass cause I cant get GetPass to work')
#device['secret'] = getpass.getpass()        #input('And I guess the enable pass idk')

for host in devicelist:
    device['ip'] = host.strip('\n')
    net_connect = ConnectHandler(**device)
    net_connect.enable() 	#Passes the enable secret and drops you into conf t
    config_cmds = ['do wr']  
    output = net_connect.send_config_set(config_cmds)
    print(output)
    write_file.write(output)