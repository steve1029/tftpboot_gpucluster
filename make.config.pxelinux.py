nodes = []
homename = 'yhome%01d'
nodename = 'y%03d'

for number in xrange(1,4):
	nodes.append(homename % number)

for number in xrange(101,200):
	nodes.append(nodename % number)

for number in xrange(201,230):
	nodes.append(nodename % number)

serverip = '192.168.100.1'
fpath = '/tftpboot/config.pxelinux.%s'

script = \
"""default node
label node
	kernel vmlinuz.%s
	append root=/dev/nfs initrd=initrd.img.%s nfsroot=%s:/nfsroot/%s ip=dhcp rw vga=0x318
"""

for node in nodes:
	f = open(fpath % node, 'w')
	f.write(script % (node, node, serverip, node))
	f.close()
