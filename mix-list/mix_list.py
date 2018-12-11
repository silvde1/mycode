#!/usr/bin/env python3
###########Shebang to run Python3
my_list = [ "192.168.0.5", 5060, "UP" ]
###########Creating list of different object types, float, integer etc.
print("The first item in the list (IP): " + my_list[0] )
########Line 5 is printing the first number from the list
print("The second item in the list (port): " + str(my_list[1]) )
########Line 7 is printing the second number from the list
print("The last item in the list (state): " + my_list[2] )
########Line 9 is printing the third item from the list
new_list = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]
print("When I " + new_list[5] + " into Ip addresses " + new_list[3] + " or " + new_list[4] + " I am unable to ping ports " + str(new_list[0]) + ",  " + new_list[1] + " or " + str(new_list[2] ) + "." )