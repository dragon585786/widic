#!/usr/bin/python 

import os
import sys
import random
import subprocess

print (' __        __  ___               _   _        ')
print (' \ \      / / |_ _|           __| | (_)   ___ ')
print ('  \ \ /\ / /   | |   _____   / _` | | |  / __|')
print ('   \ V  V /    | |  |_____| | (_| | | | | (__ ')
print ('    \_/\_/    |___|          \__,_| |_|  \___| version: 1.0.1')
print ('            \n\t~Automated dictionary attack tool.....')
print ('                            ~# Jonathan James.')


def info(): 
    info='''
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*                                                                     *
*  [+]Author: Jonathan James.                                         *
*  [+]Youtube Channel: https://www.youtube.com/c/Anonymoushacker101   *
*  [+]like,share and subscribe for more Hacks.                        *
*                                                                     *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
'''
    return info

print info() 

print "-----------------------------------------------------------------"        
 
def opt(): 
    opt='''
# # # # # # # # # # # # # # #
#                           #
#  [+]1.Check tools.        #
#  [+]2.Show Hacking menu.  #
#  [+]3.Credits.            #
#  [+]4.Exit.               #
#                           #
# # # # # # # # # # # # # # #
'''
    return opt

print opt()

choice=input('\n[+]Enter your choice: ') 

if choice == 1:
    if os.path.isfile('usr/bin/aircrack-ng'):
        print "\n[+]Aicrack-ng  :OK";
        print "[+]Airmon-ng   :OK";
        print "[+]Airodump-ng :OK";
        print "[+]Aireplay-ng :OK";
        print "\n[+]All good."
        mnu=raw_input('\n[?]Return to main menu (y/n): ')
        if mnu == 'y':
            choice+=1
    else:
        print "\n[!]Error !!!";
        print "[!]Check your installation.";
        raw_input('\nPress enter to end.');

if choice == 2:

    while True:
        
        print "\n[+]1.Start Airmon-ng."
        print "[+]2.Show networks around you."
        print "[+]3.Create a .cap file."
        print "[+]4.Start Deauthentication process."
        print "[+]5.Start cracking wifi(Wordlist required)."
        
        choicea=input('\nEnter your choice: ')

        if choicea == 1:
            os.system("airmon-ng check kill");
            print "\nairmon-ng check kill started..."
            os.system("airmon-ng start wlan0")
            print "\nmonitor mode started..."
            hm=raw_input('\n[?]Hacking menu (y/n): ')
            if hm == 'y':
                choicea+=1
            if hm == 'n':
                print "\nexiting..."
                sys.exit(0)
                raw_input('\nHit enter to end')
                
        elif choicea == 2:
            print "\nshowing wait..."
            os.system("airodump-ng wlan0mon")
            hm=raw_input('\n[?]Hacking menu (y/n): ');
            if hm == 'y':
                choicea+=1
            if hm == 'n':
                print "exiting..."
                sys.exit(0)
                raw_input('Hit enter to end')

if choice == 3:
    print "\n[*]This tool is created by Jonathan James."
    print "[*]Subscribe my channel HERE : https://www.youtube.com/c/Anonymoushacker101"
    print "[*]Thnx to me for creating such a nice tool."
    print "[*]This tool saves 80% of our time."
    print "[*]BY using this tool even a kid can also hack wifi."
    print "[*]All credits goes to Jonathan James."
    print "[-] Exiting..."
        
    
elif choice == 4:
    print "Exiting..."
    sys.exit(0)
    raw_input('Hit enter to end')
    


    



    

