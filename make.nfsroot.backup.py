import subprocess as sp
import os
import sys

from datetime import datetime as dtm

nodes = ['default', 'testing']
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

backup_dir = '/nfsroot/nfsroot-backup-%s' % (dtm.now().date())
os.makedirs(backup_dir)
os.chdir(backup_dir)

for node in nodes:
	ext_exec_wait('umount /nfsroot/%s/proc' % node)
	ext_exec_wait('umount /nfsroot/%s/dev/pts' % node)
	source_dir = '/nfsroot/%s' % node
	cmd = 'tar -zcf %s.tar.gz %s' % (node, source_dir)
	ext_exec_wait(cmd)

