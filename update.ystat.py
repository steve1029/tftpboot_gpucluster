import subprocess as sp

nodes = ['default']
homename = 'yhome%01d'
nodename = 'y%03d'
for number in xrange(1, 4):
	nodes.append(homename % number)

for number in xrange(101,166):
	nodes.append(nodename % number)

for number in xrange(201,207):
	nodes.append(nodename % number)

fpath = '/tftpboot/%s'
opath = '/nfsroot/%s/usr/local/%s/'

def ext_exec_wait(cmd):
	out, err = sp.Popen(cmd.split(), stdout=sp.PIPE, stderr=sp.PIPE).communicate()
	if err != '': print err
	return out

def ext_exec_nowait(cmd):
	sp.Popen(cmd.split(), stdout=sp.PIPE, stderr=sp.PIPE)

for node in nodes:
	nfpath = fpath % 'ystat_daemon'
	nopath = opath % (node, 'sbin')
	command = 'cp -a %s %s' % (nfpath, nopath)
	ext_exec_wait(command)
	nfpath = fpath % 'ystat'
	nopath = opath % (node, 'bin')
	command = 'cp -a %s %s' % (nfpath, nopath)
	ext_exec_wait(command)
	nfpath = fpath % 'ymon'
	nopath = opath % (node, 'bin')
	command = 'cp -a %s %s' % (nfpath, nopath)
	ext_exec_wait(command)
'''
for node in nodes:
	command = 'rsh %s /usr/local/sbin/ystat_daemon'
	ext_exec_nowait(command)
'''
