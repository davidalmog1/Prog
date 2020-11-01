#!/usr/bin/env python3

# Author: David Almog
# Version: 1.0

import time
from scapy.all import *
from sys import exit
from time import sleep

pktState = {"First":"00",
            "Transfer":"01",
            "Last":"10",
            "OkCheck":"11" }
mvc = 80 #can be change [ x < 1024 ]
class Main:
    #constructor
    def __init__(self):
    #variables
        filePath = 'file.txt'#input("Please enter file path to send: ")
        filename = filePath.split('/')[-1] if filePath.find('/') != -1 else filePath
        dstIP = '192.168.199.135'#input("Please enter your destination (IP):" )
        frames = self.splitFileToFrames(filePath,mvc)
        countFramesSent = len(frames)
    #sending first pkt to let the server know about the dtat we what to send
        print("[#] Starts sending...\n")
        pkt = Ether()/IP(dst=dstIP)/ICMP()/Padding(load=self.pktSiginitrue(pktState["First"],len(frames),filename,''))
        sendp(pkt)
    #Sending data file
        for x in range(countFramesSent-1):
            pkt = Ether()/IP(dst=dstIP)/ICMP()/Padding(load=self.pktSiginitrue(pktState["Transfer"],len(frames),filename,frames[x]))
            sendp(pkt)
            time.sleep(2)
    #Sending Last pkt
        pkt = Ether()/IP(dst=dstIP)/ICMP()/Padding(load=self.pktSiginitrue(pktState["Last"],len(frames),filename,frames[len(frames)-1]))
        sendp(pkt)
    #Finish sending
        print("\nFinished Sending\n")
        exit(0)

    def splitFileToFrames(self,filename,mvc):
        frames = []
        with open(filename, 'rb') as reader:
            num = reader.read()
        length = len(num)
        counter = 0 
        if length > mvc:
            while (counter+mvc) < length:
                frames.append(num[counter:counter+mvc])
                counter +=mvc
        frames.append(num[counter:])
        return frames
    
    def pktSiginitrue(self, pktStatus ,frames='',fileName='',data=''):
        if pktStatus == '00': # Start Sending (without any data just filenmae & amount of frames)
            return 'D|'+str(pktStatus)+'|'+'OK|'+str(fileName)+'|'+str(frames)+'|'
        elif pktStatus == '01': #Transfer state 
            return 'D|'+str(pktStatus)+'|'+str(data)+'|'
        elif pktStatus == '10': # the Last pkt the client will sent
            return 'D|'+str(pktStatus)+'|'+str(data)+'|'
        else:
            return "Error"

    def pkt_analysis(self, pkt):
        print("[!] New Packet: {src} -> {dst}".format(src= pkt[IP].src,dst=pkt[IP].dst))


            


########### Main ###########
Main()


