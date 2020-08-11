import subprocess as sp
import sys

nodes = []
homename = 'yhome%01d'
nodename = 'y%03d'

for number in xrange(1, 4):
	nodes.append(homename % number)

for number in xrange(101,169):
	nodes.append(nodename % number)

for number in xrange(201,214):
	nodes.append(nodename % number)


def ext_exec_wait(cmd):
	out, err = sp.Popen(cmd.split(), stdout=sp.PIPE, stderr=sp.PIPE).communicate()
	if err != '': print err
	return out

rpath0= '/nfsroot/default/'
rpath1= '/nfsroot/testing_3.16/'
rpath = '/nfsroot/%s'

cmd = sys.argv[1:]

comm = ''
for ch in cmd:
	comm += ch
	comm += ' '
comm = comm.rstrip(' ')

print 'default'
ext_exec_wait('mount %s/proc' % rpath0)
ext_exec_wait('mount %s/dev/pts' % rpath0)
print ext_exec_wait('chroot %s %s' % (rpath0, comm))
ext_exec_wait('umount %s/proc' % rpath0)
ext_exec_wait('umount %s/dev/pts' % rpath0)

ext_exec_wait('mount %s/proc' % rpath1)
ext_exec_wait('mount %s/dev/pts' % rpath1)
print ext_exec_wait('chroot %s %s' % (rpath1, comm))
ext_exec_wait('umount %s/proc' % rpath1)
ext_exec_wait('umount %s/dev/pts' % rpath1)

for node in nodes:
	print node
	rpathn = rpath % node
	ext_exec_wait('mount %s/proc' % rpathn)
	ext_exec_wait('mount %s/dev/pts' % rpathn)
	print ext_exec_wait('chroot %s %s' % (rpathn, comm))
	ext_exec_wait('umount %s/proc' % rpathn)
	ext_exec_wait('umount %s/dev/pts' % rpathn)

