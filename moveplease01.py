#!/usr/bin/env python3
import shutil
######importing shutil
import os
######importing the OS
os.chdir('/home/student/mycode/')
######Starts Python in the home directory of Mycode
shutil.move('raynor.obj', 'ceph_storage/')
######Moves the raynor file from mycode folder to ceph storage
xname = input('What is the new name for kerrigan.obj? ')
######Asking user what they want to rename the kerrigan file to
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)
######renaming it to the input provided by the user
