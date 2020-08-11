import copy

nodes = []

homename = 'yhome%01d'
nodename = 'y%03d'

#for number in xrange(1, 4):
#	nodes.append(homename % number)

#for number in xrange(101,201):
#	nodes.append(nodename % number)

for number in xrange(201,230):
	nodes.append(nodename % number)

script = open("/etc/hostname",'r').read()

for node in nodes :

	try :
		f = open("/nfsroot/%s/etc/hostname" %node,'w')
		newscript = copy.deepcopy(script)
		newscript = newscript.replace("gpucluster", "%s" %node)
		f.write(newscript)
		f.close()
	except Exception as err :
		print err
		pass
