import os

procname = "python"
#cmd = "ps -elf | grep '%s' | awk '{print $4}' | xargs kill"

cmd = "killall -9 %s"

os.system(cmd % procname)
