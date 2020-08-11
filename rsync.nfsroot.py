import subprocess as sp
import os

nodes = []
homename = 'yhome%01d'
nodename = 'y%03d'


#for number in xrange(1, 4):
#	nodes.append(homename % number)
#
#for number in xrange(101,171):
#	nodes.append(nodename % number)

#for number in range(201,205):
#	nodes.append(nodename % number)

#for number in range(206,214):
#	nodes.append(nodename % number)

#nodes.append('gpunode')
nodes.append('y205')

rpath0= '/nfsroot/gpunode/'
rpath = '/nfsroot/%s'
option = '-aH --delete'

def ext_exec_wait(cmd):
    out, err = sp.Popen(cmd.split(), stdout=sp.PIPE, stderr=sp.PIPE).communicate()
    if err != '': print(err)
    return out

ext_exec_wait('umount %s/proc' % rpath0[:-1])
ext_exec_wait('umount %s/dev/pts' % rpath0[:-1])

for node in nodes:
    ext_exec_wait('umount %s/proc' % (rpath % node))
    ext_exec_wait('umount %s/dev/pts' % (rpath % node))
    print('synchronizng nfs root file system: %s to %s' % (rpath0, (rpath % node)))
    command = 'rsync %s %s %s' % (option, rpath0, (rpath % node))
    print(ext_exec_wait(command))
    ext_exec_wait('mount %s/proc' % (rpath % node))
    ext_exec_wait('mount %s/dev/pts' % (rpath % node))

ext_exec_wait('mount %s/proc' % rpath0[:-1])
ext_exec_wait('mount %s/dev/pts' % rpath0[:-1])

#os.system("python3 /tftpboot/node.hostname.py")
#os.system("python3 /tftpboot/copy.ids.py")
