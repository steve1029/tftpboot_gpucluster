import subprocess as sp

nodes = []
homename = 'yhome%01d'
nodename = 'y%03d'

for number in xrange(1, 4):
	nodes.append(homename % number)

for number in xrange(101,201):
	nodes.append(nodename % number)

for number in xrange(201,214):
	nodes.append(nodename % number)

serverip = '192.168.100.1'
fpath = '/tftpboot/initramfs-pxe.node/%s'
opath = '/tftpboot/initrd.img.%s'
vpath = '/tftpboot/vmlinuz.%s'
uname = '4.3.0-1-amd64'

def ext_exec_wait(cmd):
	out, err = sp.Popen(cmd.split(), stdout=sp.PIPE, stderr=sp.PIPE).communicate()
	if err != '': print err
	return out

for node in nodes:
	print 'making image of initramfs: %s' % node
	nfpath = fpath % node
	nopath = opath % node	
	nvpath = vpath % node	
	command = 'mkinitramfs -d %s -o %s %s' % (nfpath, nopath, uname)
	command = 'cp -a /boot/vmlinuz-%s %s' % (uname, nvpath)
	ext_exec_wait(command)
