#!/usr/bin/env python3
# Author: David Almog
# Version: 1.0
import multiprocessing
from sys import path
import collections
import time
import xml.etree.ElementTree as ET
from netmiko import ConnectHandler

#New Data Type named Machine that stores [ip, type(mds,gw.mgmt...), username,psssword,validations(basic,advanced,other),status(0,1,2)]
Machine = collections.namedtuple('Machine',['ip','type','user','ps','validations','status'])



class main:
    
    def __init__(self,filepath):
        machines = self.getMachinesFromFile(filepath) #machie.xml file
        if machines != None:
            for i in range(len(machines)):
                machines[i]._replace(status = self.runCommandOnMachine(machines[i], "cat /opt/passwd"))


    def getMachinesFromFile(self,filename):
        # parse an xml file by name
        try:
            tree = ET.parse(filename)
            root = tree.getroot()
        except:
            print(f"Failed where: parseing the file {filename}")
            return None
        fileElements = [] # all the <machine name="?">
        for elem in root:
            fileElements.append(elem)
        machines  = []
        for child in fileElements:
            data = []
            for cc in child:
                data.append(cc.text)
            data.append(None)
            data.append(None)
            machines.append(Machine._make(data))
        return machines

    def runCommandOnMachine(self,machine :Machine, command) -> str:
        iosv_l2 = {
            'device_type': 'linux',
            'ip':machine.ip,
            'username':machine.user,
            'password': machine.ps,
        }
        try:
            net_connect = ConnectHandler(**iosv_l2)
            output = net_connect.send_command(command)
            machine._replace(status = 2)
        except:
            print(f"Failed connect to {machine.ip}")
            output = none
        return output

    def runScriptOnMachine(self,script :file) -> str:
    
    

main('machine.xml')