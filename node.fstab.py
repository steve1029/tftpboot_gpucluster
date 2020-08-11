import os
import subprocess as sp

homename = 'yhome%01d'
nodename = 'y%03d'

nodes = []

nodes.append('jessie.default')
nodes.append('jessie.gpunode')
nodes.append('jessie.cpunode')
nodes.append('jessie.trial')

for i in range(1,4):
	nodes.append(homename % i)

for i in range(101,200):
	nodes.append(nodename % i)

for i in range(201,230):
	nodes.append(nodename % i)

line1 = "\nproc	/proc	proc	defaults	0	0\n"
line2 = "none	/tmp	tmpfs	defaults	0	0\n"
line3 = "192.168.100.1:/root	/root	nfs	defaults,async,nosuid,nodev,intr,nfsvers=3,rsize=32768,wsize=32768	0	0"

for i in nodes:
	
	try : 
		f = open("/nfsroot/%s/etc/fstab" % i, 'a')
		f.write(line1)
		f.write(line2)
		f.write(line3)
		f.close()
	except Exception as err :
		print err
		pass
