# Before running this script, make sure that
# You have ssh-key. If you are not, generate ssh-key
# by commanding '$ ssh-keygen' command.

import subprocess as sp
import sys, os

nodes=[]
homes = []
homename = 'yhome%01d'
nodename = 'y%03d'

#for number in xrange(1, 4):
#	homes.append(homename % number)
#	nodes.append(homename % number)

#for number in xrange(101,200):
#	nodes.append(nodename % number)

for number in xrange(205,215):
	nodes.append(nodename % number)

#nodes.append("gpunode")
#nodes.append("gpunode.no.ana")
#nodes.append("gpunode.ana")
#nodes.append("gpunode.ana.cuda")
#nodes.append("gpunode.ana.cuda.ompi-dev")
#nodes.append("gpunode.ana.cuda.ompi-dev.mpi4py")

def ext_exec_wait(cmd):
	out, err = sp.Popen(cmd.split(), stdout=sp.PIPE, stderr=sp.PIPE).communicate()
	if err != '': print err
	return out

passwd = sys.argv[1]

for node in nodes:
	command = 'sshpass -p "{0}" ssh-copy-id {1}'.format(passwd,node)
	print(command)
	ext_exec_wait(command)
