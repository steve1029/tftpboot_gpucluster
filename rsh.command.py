import subprocess as sp
import sys
import os

nodes = []
homename = 'yhome%01d'
nodename = 'y%03d'

#for number in xrange(1, 4):
#    nodes.append(homename % number)

for number in xrange(101,180):
    nodes.append(nodename % number)

for number in xrange(207,213):
    nodes.append(nodename % number)

def ext_exec_wait(cmd):
    out, err = sp.Popen(cmd.split(), stdout=sp.PIPE, stderr=sp.PIPE).communicate()
    if err != '': print err
    return out

def ext_exec_list(cmd_list):
    out, err = sp.Popen(cmd_list, stdout=sp.PIPE, stderr=sp.PIPE).communicate()
    if err != '': print err
    return out

#cmdl = ["rsh", "", ""]

rshcmd = "rsh %s %s"
cmd = " ".join(sys.argv[1:])

for node in nodes:
	nodecmd = rshcmd % (node, cmd)
	print nodecmd
	os.system(nodecmd)
#    cmdl[1] = str(node)
#    print ext_exec_list(cmdl)
