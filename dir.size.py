import os,sys

number = sys.argv[1]

os.system("du -hsx * | sort -rh | head -n %s" %number)
