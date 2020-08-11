import subprocess as sp
import sys

nodes = ['default']
homename = 'yhome%01d'
nodename = 'y%03d'

for number in xrange(1, 4):
	nodes.append(homename % number)

for number in xrange(101,166):
	nodes.append(nodename % number)

for number in xrange(201,214):
	nodes.append(nodename % number)

def ext_exec_wait(cmd):
	out, err = sp.Popen(cmd.split(), stdout=sp.PIPE, stderr=sp.PIPE).communicate()
	if err != '': print err
	return out

rpath = '/nfsroot/%s'

cmd = sys.argv[1:]
for node in nodes:
	print node
	rpathn = rpath % node
	print ext_exec_wait('ln -sf /home/smsmsms/lib/KEMP %s/usr/lib/python2.7/dist-packages/KEMP' % rpathn)

