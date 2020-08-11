import subprocess as sp
import sys

path1 = sys.argv[1]
path2 = sys.argv[2]

nodes = []
homes = []
homename = 'yhome%01d'
nodename = 'y%03d'

#nodes.append("gpunode")
#nodes.append("gpunode.no.ana")
#nodes.append("gpunode.ana")
#nodes.append("gpunode.ana.cuda")
#nodes.append("gpunode.ana.cuda.ompi-dev")
#nodes.append("gpunode.ana.cuda.ompi-dev.mpi4py")

#for number in xrange(1, 4):
#	nodes.append(homename % number)
#	homes.append(homename % number)

#for number in xrange(101,180):
#	nodes.append(nodename % number)

for number in xrange(201,214):
	nodes.append(nodename % number)

def ext_exec_wait(cmd):
	out, err = sp.Popen(cmd.split(), stdout=sp.PIPE, stderr=sp.PIPE).communicate()
	if err != '': print err
	return out

rpath = '/nfsroot/%s'

cmd = sys.argv[1:]
for node in nodes:
	print node
	rpathn = rpath % node
	print ext_exec_wait('cp -a %s %s%s' % (path1, rpathn, path2))

#for home in homes:
#	print home
#	rpathn = rpath % home
#	print ext_exec_wait('sshpass -p "dusrntlf*2nol" scp -r %s %s:%s' % (path1, home, path2))

