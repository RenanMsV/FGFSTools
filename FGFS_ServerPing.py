#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from subprocess import PIPE, Popen

pattern = "ping mpserver{:02d}.flightgear.org"
max_server_number = 51
results = []

def cmdline(command):
    process = Popen(
        args=command,
        stdout=PIPE,
        shell=True
    )
    return process.communicate()[0]

print("\nTesting FlightGear Servers Ping...")
print('='*60)
for x in range(0,max_server_number + 1):
	log_file = open('log', 'wb')
	print("Testing {}\n".format(pattern.format(x)))
	result = cmdline(pattern.format(x))
	log_file.write(result)
	log_file.close()
	result = open('log', 'rb').readlines()
	if(len(result)>10):
		result = result[11].strip()[-6:].decode('utf8').strip()
		results.append( [result[:-2], x] )
		print("Result: {}".format(result))
	else:
		results.append( ['9999', x])
		print("No response")
	print('='*60)

results = sorted(results)
for x in range(0,3):
	print("\n{}º best server is: {} with {} ms".format(x+1,"mpserver{:02d}.flightgear.org".format(results[x][1]),results[x][0]))
os.remove('log')