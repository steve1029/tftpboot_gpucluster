import os

nodes = ['default']
homename = 'yhome%01d'
nodename = 'y%03d'

for number in xrange(1, 4):
	nodes.append(homename % number)

for number in xrange(101,201):
	nodes.append(nodename % number)

for number in xrange(201,230):
	nodes.append(nodename % number)

os.system("cp /root/.vimrc /home/ldg/.vimrc")

for node in nodes:
	
	try :
		os.system("cp /root/.vimrc /nfsroot/%s/root/.vimrc" %node)
		os.system("cp /root/.vimrc /nfsroot/%s/home/ldg/.vimrc" %node)
	except Exception as err :
		print err
		pass
