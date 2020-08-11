import subprocess as sp
import os
import sys

nodes = ['testing']
homename = 'yhome%01d'
nodename = 'y%03d'

sshcmd = 'ssh %s %s'

cmd = ' '.join(sys.argv[1:])

#for number in xrange(1, 4):
#	nodes.append(homename % number)

#for number in xrange(101,171):
#	nodes.append(nodename % number)

for number in xrange(208,214):
	nodes.append(nodename % number)

for node in nodes:
    os.system(sshcmd % (node, cmd))
