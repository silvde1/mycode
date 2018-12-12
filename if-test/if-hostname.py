#!/usr/bin/env python3

prompt_hostname_msg = "What is the hostname?"  ####Asking the user what the hostname is
hostname = (input (prompt_hostname_msg))  #####Gathering the user input
hostname = hostname.upper()  ######Adjusting the user input to all caps
if hostname == 'MTG':  ####If then statement for MTG response
    print('The hostname was found to be mtg')  ####Confirming the hostname is MTG
    print('The hostname matches expected config')  ####Confirming hostname meets expectations

print('Exiting the script.') #####Exiting the script