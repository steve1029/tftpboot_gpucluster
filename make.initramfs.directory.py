import subprocess as sp

nodes = []
homename = 'yhome%01d'
nodename = 'y%03d'

for number in xrange(1, 4):
	nodes.append(homename % number)

for number in xrange(101,200):
	nodes.append(nodename % number)

for number in xrange(201,230):
	nodes.append(nodename % number)

spath = '/etc/initramfs-tools'
fpath0= '/tftpboot/initramfs-pxe.node'
fpath = '/tftpboot/initramfs-pxe.node/%s'

def ext_exec_wait(cmd):
	out, err = sp.Popen(cmd.split(), stdout=sp.PIPE, stderr=sp.PIPE).communicate()
	if err != '': print err
	return out

#ext_exec_wait('rm -r %s/*' % fpath0)

for node in nodes:
	nfpath = fpath % node
	command = 'cp -a %s %s' % (spath, nfpath)
	ext_exec_wait(command)
	
