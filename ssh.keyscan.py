import subprocess as sp
import os

nodes = []
homes = []
homename = 'yhome%01d'
nodename = 'y%03d'

#for number in xrange(1, 4):
#	homes.append(homename % number)
#	nodes.append(homename % number)

for number in xrange(101,200):
	nodes.append(nodename % number)

for number in xrange(201,230):
	nodes.append(nodename % number)

nodes.append('default')
nodes.append('jessie.default')
nodes.append('jessie.gpunode')
nodes.append('jessie.cpunode')

fpath = '/etc/ssh/ssh_known_hosts'
opath = '/nfsroot/%s/etc/ssh/'

def ext_exec_wait(cmd):
	out, err = sp.Popen(cmd.split(), stdout=sp.PIPE, stderr=sp.PIPE).communicate()
	if err != '': print err
	return out

def ext_exec_wait_list(cmd):
	out, err = sp.Popen(cmd, stdout=sp.PIPE, stderr=sp.PIPE).communicate()
	if err != '': print err
	return out

#ssh_keyscan = "ssh-keyscan $(grep '192\.168\.100\.' /etc/hosts)"
#ssh_keys = ext_exec_wait_list(ssh_keyscan)
#print ssh_keys
#f = file(fpath, 'w')
#f.write(ssh_keys)
#f.close()

os.system("ssh-keyscan $(grep '192\.168\.100\.' /etc/hosts) | sort > /etc/ssh/ssh_known_hosts")
command = 'cp -a /etc/ssh/ssh_known_hosts /root/ssh_known_hosts'
ext_exec_wait(command)

for node in nodes:
	nopath = opath % node
	command = 'cp -a %s %s' % (fpath, nopath)
	ext_exec_wait(command)

cmd_scp = 'sshpass -p 0000 scp -r /etc/ssh/ssh_known_hosts %s:/etc/ssh/'

for home in homes:
	print home 
	os.system(cmd_scp % home)
