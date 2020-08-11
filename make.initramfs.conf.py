import copy

nodes = []
homename = 'yhome%01d'
nodename = 'y%03d'

for number in xrange(1, 4):
	nodes.append(homename % number)

for number in xrange(101,200):
	nodes.append(nodename % number)

for number in xrange(201,230):
	nodes.append(nodename % number)

serverip = '192.168.100.1'
spath = '/etc/initramfs-tools/initramfs.conf'
fpath = '/tftpboot/initramfs-pxe.node/%s/initramfs.conf'

script = open(spath, 'r').read()

for node in nodes:
	f = open(fpath % node, 'w')
	newscript = copy.deepcopy(script)
	newscript = newscript.replace('MODULES=most', 'MODULES=netboot\nBOOT=nfs')
	newscript = newscript.replace('DEVICE=', 'DEVICE=')
	newscript = newscript.replace('NFSROOT=auto', ('NFSROOT=%s:/nfsroot/%s' % (serverip, node)))
	f.write(newscript)
	f.close()
