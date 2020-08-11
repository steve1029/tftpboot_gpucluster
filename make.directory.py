import os

nodes = []
homename = 'yhome%01d'
nodename = 'y%03d'

#for number in xrange(1, 4):
#	nodes.append(homename % number)

for number in xrange(101,201):
	nodes.append(nodename % number)

#for number in xrange(201,214):
#	nodes.append(nodename % number)

path = '/tftpboot/initramfs-pxe.node/%s'

for node in nodes :
	if os.path.exists(path % node) == False :

		os.mkdir(path % node)

	else : 
		pass
