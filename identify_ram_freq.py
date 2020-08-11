import subprocess as sp

nodes = []
homename = 'yhome%01d'
nodename = 'y%03d'

#for number in xrange(1, 4):
#	nodes.append(homename % number)

#for number in xrange(101,166):
#	nodes.append(nodename % number)

#for number in xrange(201,207):
#	nodes.append(nodename % number)

for number in xrange(151,166):
	nodes.append(nodename % number)


def ext_exec_wait(cmd):
	out, err = sp.Popen(cmd.split(), stdout=sp.PIPE, stderr=sp.PIPE).communicate()
	if err != '': print err
	return out

f = file('./raminfo.txt', 'w')

for node in nodes:
	str_node = '%s: identifying ram freq...' % node
	command = "rsh %s /usr/sbin/dmidecode | grep \"Speed\"" % node
	out = ext_exec_wait(command)
	f.write('%s\n' % str_node)
	f.write('%s\n' % out)
	print str_node
	print out
f.close()

