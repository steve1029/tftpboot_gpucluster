import subprocess as sp
import sys

nodes = []
homename = 'yhome%01d'
nodename = 'y%03d'

#for number in xrange(1, 4):
#	nodes.append(homename % number)

#for number in xrange(101,200):
#	nodes.append(nodename % number)

for number in range(101,102):
	nodes.append(nodename % number)

def ext_exec_wait(cmd):
	out, err = sp.Popen(cmd.split(), stdout=sp.PIPE, stderr=sp.PIPE).communicate()
	if err != '': print(err)
	return out

default = '/nfsroot/default/'
cpunode = '/nfsroot/cpunode/'
testing = '/nfsroot/testing/'
rpath   = '/nfsroot/%s'

jessie_default  = '/nfsroot/jessie.default/'
jessie_gpunode  = '/nfsroot/jessie.gpunode/'

#cmd = sys.argv[1:]

#comm = ''
#for ch in cmd:
#	comm += ch
#	comm += ' '
#comm = comm.rstrip(' ')

print('default')
#ext_exec_wait('mount %s/proc' % rpath0)
#ext_exec_wait('mount %s/dev/pts' % rpath0)
#print ext_exec_wait('chroot %s %s' % (rpath0, comm))
#print ext_exec_wait('chroot %s %s' % (rpath1, comm))
ext_exec_wait('umount %s/proc' % default)
ext_exec_wait('umount %s/dev/pts' % default)

ext_exec_wait('umount %s/proc' % cpunode)
ext_exec_wait('umount %s/dev/pts' % cpunode)

ext_exec_wait('umount %s/proc' % testing)
ext_exec_wait('umount %s/dev/pts' % testing)

ext_exec_wait('umount %s/proc' % jessie_default)
ext_exec_wait('umount %s/dev/pts' % jessie_default)

ext_exec_wait('umount %s/proc' % jessie_gpunode)
ext_exec_wait('umount %s/dev/pts' % jessie_gpunode)

for node in nodes:
	print(node)
	rpathn = rpath % node
	ext_exec_wait('umount %s/proc' % rpathn)
	ext_exec_wait('umount %s/dev/pts' % rpathn)
