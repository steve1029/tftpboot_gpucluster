import os
import subprocess as sp

homename = 'yhome%01d'
nodename = 'y%03d'

homes = []
nodes = []

for i in range(1,4):
	homes.append(homename % i)

for i in range(113,119):
	nodes.append(nodename % i)

#print homes
#print nodes

line = "IgnoreRhosts no"

for i in nodes:
	
	f = open("/nfsroot/%s/etc/ssh/sshd_config" % i, 'a')
	f.write(line)
	f.close()
