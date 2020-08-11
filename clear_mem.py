import subprocess as sp
import sys

nodes = []
homename = 'yhome%01d'
nodename = 'y%03d'

for number in xrange(1, 4):
    nodes.append(homename % number)

for number in xrange(101,166):
    nodes.append(nodename % number)

for number in xrange(201,206):
    nodes.append(nodename % number)

def ext_exec_wait(cmd):
    out, err = sp.Popen(cmd.split(), stdout=sp.PIPE, stderr=sp.PIPE).communicate()
    if err != '': print err
    return out

def ext_exec_list(cmd_list):
    out, err = sp.Popen(cmd_list, stdout=sp.PIPE, stderr=sp.PIPE).communicate()
    if err != '': print err
    return out

cmd  = "rsh %s '/bin/echo 3 > /proc/sys/vm/drop_caches'" 
cmdl = ["rsh", "", "/bin/echo 3 > /proc/sys/vm/drop_caches"]

for node in nodes:
    print "Memory of %s has been cleared" %(node)
    cmdl[1] = node
    print ext_exec_list(cmdl)
