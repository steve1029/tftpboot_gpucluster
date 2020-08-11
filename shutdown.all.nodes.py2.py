import subprocess as sp

homes = []
nodes = []
homename = 'yhome%01d'
nodename = 'y%03d'

for number in xrange(1, 4):
    homes.append(homename % number)

for number in xrange(101,180):
    nodes.append(nodename % number)

#for number in xrange(151,169):
#    nodes.append(nodename % number)

for number in xrange(201,214):
    nodes.append(nodename % number)

def ext_exec_wait(cmd):
    out, err = sp.Popen(cmd.split(), stdout=sp.PIPE, stderr=sp.PIPE).communicate()
    if err != '': print err
    return out

def ext_exec_nowait(cmd):
    sp.Popen(cmd.split(), stdout=sp.PIPE, stderr=sp.PIPE)

for node in nodes:
    print node
    command = 'rsh %s /sbin/shutdown -P -h now' % node
    ext_exec_wait(command)

for home in homes:
    print home 
    command = 'rsh %s /sbin/shutdown -P -h now' % home
    ext_exec_wait(command)
