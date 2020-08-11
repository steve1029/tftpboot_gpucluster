import os, copy

nodes = []
homename = 'yhome%01d'
nodename = 'y%03d'

nodes.append("default")
nodes.append("jessie.default")
nodes.append("jessie.gpunode")
nodes.append("jessie.cpunode")

for number in xrange(1, 4):
	nodes.append(homename % number)

for number in xrange(101,200):
	nodes.append(nodename % number)

for number in xrange(201,230):
	nodes.append(nodename % number)

f = open("/etc/exports",'a')

script = "/nfsroot/%s\t192.168.100.0/24(rw,no_root_squash,no_subtree_check,async)\n"

for node in nodes :
	nscript = script % node
	f.write(nscript)

f.close()
