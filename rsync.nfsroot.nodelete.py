import subprocess as sp

nodes = []
homename = 'yhome%01d'
nodename = 'y%03d'

for number in xrange(1, 4):
	nodes.append(homename % number)

for number in xrange(101,166):
	nodes.append(nodename % number)

#for number in xrange(201,207):
#	nodes.append(nodename % number)

rpath0= '/nfsroot/default/'
rpath = '/nfsroot/%s'
option = '-a -H -v'

def ext_exec_wait(cmd):
	out, err = sp.Popen(cmd.split(), stdout=sp.PIPE, stderr=sp.PIPE).communicate()
	if err != '': print err
	return out

ext_exec_wait('umount %s/proc' % rpath0)
ext_exec_wait('umount %s/dev/pts' % rpath0)

for node in nodes:
	print 'syncing nfs root file system: %s to %s' % (rpath0, (rpath % node))
	command = 'rsync %s %s %s' % (option, rpath0, (rpath % node))
	print ext_exec_wait(command)

ext_exec_wait('mount %s/proc' % rpath0)
ext_exec_wait('mount %s/dev/pts' % rpath0)
