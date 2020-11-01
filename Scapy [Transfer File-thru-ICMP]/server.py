#!/usr/bin/env python3

# Author: David Almog
# Version: 1.0

import binascii
from scapy.all import *
from os import path

error_state = -1 
deff_value = 0 # like none
pktState = {"First":"00",
            "Transfer":"01",
            "Last":"10",
            "OkCheck":"11" }

class Main:
    #Variables
    filename = deff_value
    framesNumber = deff_value #int
    countDataAccept = deff_value #int
    status = deff_value
    clientIP = deff_value

    def __init__(self,runfor = 5):# 1 minutes from now  
        print("[*] Start sniffing...")
        sniff(filter="icmp", count=1, prn=self.pkt_analysis)
        if self.status == pktState["First"]:
            sniff(filter="icmp and host "+str(self.clientIP), count=(self.framesNumber*2)-2, prn=self.pkt_analysis)
        else:
            print("\n [X] Wrong Format \n")    
        print("\nFinish")
        exit(0)    
        
    def pkt_analysis(self, pkt):
        print(" [!] New Packet: {src} -> {dst} ".format(src= pkt[IP].src, dst=pkt[IP].dst))
        print(pkt[Padding])
        pktData = str(pkt[Padding]).split('|')
        print(f"\t[$]\t{pktData[0]} ")
        pktData[0] = pktData[0][2:]
        if pktData[0] == 'D':
            if pktData[1] == pktState['First']:
                # Example for D|00|OK|FileName|10|
                self.status = pktData[1] 
                self.clientIP = pkt[IP].src
                self.filename = pktData[3]
                self.framesNumber = int(pktData[4])
                self.countDataAccept = int(pktData[4])
            elif pktData[1] == pktState['Transfer'] or pktData[1] == pktState['Last']:
                # Example for D|01|Data|  or  Example for D|10|Data|
                self.status = pktData[1] 
                data = str(pktData[2])[2:]
                if str(data)[0] == '\'':
                    data = data[1:]
                if str(data)[-1] == '\'':
                    data = data[:-1]
                print(f"\n [{ self.countDataAccept}] Data: {data}")
                self.reBuildFile(data)
                self.countDataAccept = self.countDataAccept-1
            else:
                print("\n [X] Error State, pksState Wrong (is not: 00 or 01 or 10)\n")
        else:
            ignore = "b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'"
            if pktData[0] == ignore:
                pass
            else:
                print("\n [X] Error State, Wrong Format \n")

    def reBuildFile(self,data):
        file_state = 'a' if path.exists(self.filename) else 'w'
        with open(self.filename,file_state) as file:
            file.write(data+"\n")   
 
########### Main ###########

Main()

