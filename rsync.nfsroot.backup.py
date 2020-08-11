import subprocess as sp
from datetime import datetime as dt

now = dt.now()

rpath0= '/nfsroot/default/'
rpath = '/nfsroot/backup_%04d.%02d.%02d' % (now.year, now.month, now.day)
option = '-a -H -v --delete'

def ext_exec_wait(cmd):
	out, err = sp.Popen(cmd.split(), stdout=sp.PIPE, stderr=sp.PIPE).communicate()
	if err != '': print err
	return out

ext_exec_wait('umount %s/proc' % rpath0)
ext_exec_wait('umount %s/dev/pts' % rpath0)

command = 'rsync %s %s %s' % (option, rpath0, rpath)
print ext_exec_wait(command)

ext_exec_wait('mount %s/proc' % rpath0)
ext_exec_wait('mount %s/dev/pts' % rpath0)
