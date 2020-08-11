import subprocess as sp
import sys
import os

nodes = []
homes = []
homename = 'yhome%01d'
nodename = 'y%03d'

#for number in range(1, 4):
#	homes.append(homename % number)
#	nodes.append(homename % number)

for number in range(101,121):
	nodes.append(nodename % number)

#for number in range(201,230):
#	nodes.append(nodename % number)

def ext_exec_wait(cmd):
	out, err = sp.Popen(cmd.split(), stdout=sp.PIPE, stderr=sp.PIPE).communicate()
	if err != '': print(err)
	return out

rpath = '/nfsroot/%s'

cmd = sys.argv[1:]
for node in nodes:
	print(node)
	rpathn = rpath % node
	print(ext_exec_wait('cp /etc/group %s/etc/' % rpathn))
	print(ext_exec_wait('cp /etc/passwd %s/etc/' % rpathn))
	print(ext_exec_wait('cp /etc/shadow %s/etc/' % rpathn))
	print(ext_exec_wait('cp /etc/gshadow %s/etc/' % rpathn))

for home in homes:
	print (home)
	os.system('sshpass -p "0000" scp -r /etc/group %s:/etc/' % home)
	os.system('sshpass -p "0000" scp -r /etc/passwd %s:/etc/' % home)
	os.system('sshpass -p "0000" scp -r /etc/shadow %s:/etc/' % home)
	os.system('sshpass -p "0000" scp -r /etc/gshadow %s:/etc/' % home)
