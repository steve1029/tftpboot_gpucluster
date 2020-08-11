import os
import subprocess as sp

homename = 'yhome%01d'
nodename = 'y%03d'

homes = []
nodes = ['default']

#for i in range(1,4):
#	homes.append(homename % i)

for i in range(101,200):
	nodes.append(nodename % i)

for i in range(201,230):
	nodes.append(nodename % i)

line1 = "\n/home	/etc/auto.home\n"
line2 = "\nldg	192.168.100.1:/home/ldg\n"
for i in nodes:
	
	try : 
		f1 = open("/nfsroot/%s/etc/auto.master" % i, 'a')
		f1.write(line1)
		f1.close()

		f2 = open("/nfsroot/%s/etc/auto.home" % i, 'a')
		f2.write(line2)
		f2.close()
	except Exception as err :
		print err
		pass
