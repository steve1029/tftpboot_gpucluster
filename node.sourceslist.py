import os

nodes = []
homename = 'yhome%01d'
nodename = 'y%03d'

nodes.append('defaults')

#for number in xrange(1, 4):
#	nodes.append(homename % number)

#for number in xrange(101,201):
#	nodes.append(nodename % number)

for number in xrange(201,230):
	nodes.append(nodename % number)

spath = '/etc/apt/sources.list'
fpath = '/nfsroot/%s/etc/apt/sources.list'

for node in nodes:

	node_sources_list = fpath %node
	os.system("cp %s %s" %(spath, node_sources_list))
