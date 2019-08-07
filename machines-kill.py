#!/usr/bin/env python

import re

inputfile = open("tokill-list.txt", "r")
outputfile = open("machines.txt", "w")
in1 = iter(inputfile )

while True:
	#print("begining while")
	line1 = next(in1)
	match1 =  re.search("(.*)<RDP>(.*)-(.*)", line1)
	if match1:
		machinename = match1.group(2)
		print(machinename)
		outputfile.write(machinename)
outputfile.close()
