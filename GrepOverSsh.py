#! /usr/bin/env/python

import subprocess
import sys

print("Enter list of ips (comma separated)")
hosts = input().split(",")
print("Enter search string")
query = input()
command="grep \"" + query + "\" /home/kompuser/log/changenotify.log"

for host in hosts:
	print(1, host)
	ssh = subprocess.Popen(["ssh", "%s" % host, command],
						   shell=False,
						   stdout=subprocess.PIPE,
						   stderr=subprocess.PIPE)
	print(2, host)
	result = ssh.stdout.readlines()
	print(3, host)
	if result == []:
		error = ssh.stderr.readlines()
		print("Empty", error)
	else:
		print(result)
