import subprocess as sp
import sys

nodes = []
homes = []
homename = 'yhome%01d'
nodename = 'y%03d'

for number in xrange(1, 4):
	homes.append(homename % number)

for number in xrange(101,200):
	nodes.append(nodename % number)

for number in xrange(201,230):
	nodes.append(nodename % number)

def ext_exec_wait(cmd):
	out, err = sp.Popen(cmd.split(), stdout=sp.PIPE, stderr=sp.PIPE).communicate()
	if err != '': print err
	return out

default= '/nfsroot/default/'
testing= '/nfsroot/testing/'
jessie_default= '/nfsroot/jessie.default/'
jessie_gpunode= '/nfsroot/jessie.gpunode/'

rpath = '/nfsroot/%s/'

ext_exec_wait('mount %s/proc' % default)
ext_exec_wait('mount %s/dev/pts' % default)

ext_exec_wait('mount %s/proc' % testing)
ext_exec_wait('mount %s/dev/pts' % testing)

ext_exec_wait('mount %s/proc' % jessie_default)
ext_exec_wait('mount %s/dev/pts' % jessie_default)

ext_exec_wait('mount %s/proc' % jessie_gpunode)
ext_exec_wait('mount %s/dev/pts' % jessie_gpunode)

for node in nodes:
	print node
	rpathn = rpath % node
	ext_exec_wait('mount %s/proc' % rpathn)
	ext_exec_wait('mount %s/dev/pts' % rpathn)

for home in homes:
	print home
	rpathn = rpath % home
	ext_exec_wait('mount %s/proc' % rpathn)
	ext_exec_wait('mount %s/dev/pts' % rpathn)

