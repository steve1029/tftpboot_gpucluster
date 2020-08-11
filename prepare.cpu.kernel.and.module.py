import os, copy

cpunodes = []
homes = []

homename = 'yhome%01d'
nodename = 'y%03d'

#for number in xrange(1, 4):
#	homes.append(homename % number)

for number in range(120,121):
	cpunodes.append(nodename % number)

##############################################################
###################### Prepare pxe boot ######################
##############################################################
os.system("cp /usr/lib/PXELINUX/pxelinux.0 /tftpboot")
os.system("cp /usr/lib/syslinux/modules/bios/ldlinux.c32 /tftpboot")

#----------------- Make config.pxelinux.node ----------------#

serverip = '192.168.100.1'
node_pxe_config = '/tftpboot/config.pxelinux.%s'

config = \
"""default node
label node
	kernel vmlinuz.%s
	append root=/dev/nfs initrd=initrd.img.%s nfsroot=%s:/nfsroot/%s ip=dhcp rw vga=0x318
"""

for cpunode in cpunodes:
	f = open(node_pxe_config % cpunode, 'w')
	f.write(config % (cpunode, cpunode, serverip, cpunode))
	f.close()

##############################################################
################### Prepare kernel module ####################
##############################################################

if not os.path.exists("/tftpboot/initramfs-pxe.cpunode"):
	os.system("mkdir /tftpboot/initramfs-pxe.cpunode")

uname = '4.15.0-29-generic'

# You must copy vmlinuz and initramfs-modules from /boot and /etc !!

#os.system("cp -a /boot/vmlinuz-%s /tftpboot/vmlinuz-%s.cpunode" %uname)
#os.system("cp -a /etc/initramfs-tools /tftpboot/initramfs-tools-%s.cpunode" %uname)

copied_server_kernel        = '/tftpboot/vmlinuz-%s.cpunode' %uname
copied_server_kernel_module = '/tftpboot/initramfs-tools-%s.cpunode' %uname
copied_server_module_config = '/tftpboot/initramfs-tools-%s.cpunode/initramfs.conf' %uname

node_kernel_path          = '/tftpboot/vmlinuz.%s'
node_kernel_module_path   = '/tftpboot/initramfs-pxe.cpunode/%s'
node_kernel_module_config = '/tftpboot/initramfs-pxe.cpunode/%s/initramfs.conf'
node_module_image_path    = '/tftpboot/initrd.img.%s'

#----------- make kernel module for all cpunodes ------------#
for cpunode in cpunodes:
	nkm_path = node_kernel_module_path % cpunode
	command = 'cp -a %s %s' % (copied_server_kernel_module, nkm_path)
	os.system(command)

#---------- Edit configuration file for all cpunodes --------#
server_config = open(copied_server_module_config, 'r').read()

for cpunode in cpunodes:
	f = open(node_kernel_module_config % cpunode, 'w')

	node_config = copy.deepcopy(server_config)
	node_config = node_config.replace('MODULES=most', 'MODULES=netboot\nBOOT=nfs')
	node_config = node_config.replace('DEVICE=', 'DEVICE=')
	node_config = node_config.replace('NFSROOT=auto', ('NFSROOT=%s:/nfsroot/%s' % (serverip, cpunode)))

	f.write(node_config)
	f.close()

#--- Prepare kernel and kernel module image for cpunodes ----#

for cpunode in cpunodes:
	print('making image of initramfs: %s' % cpunode)

	nk_path  = node_kernel_path        % cpunode	
	nkm_path = node_kernel_module_path % cpunode
	nmi_path = node_module_image_path  % cpunode	

	make_initrd = 'mkinitramfs -d %s -o %s %s' % (nkm_path, nmi_path, uname)
	copy_kernel = 'cp -a %s %s' % (copied_server_kernel, nk_path)

	os.system(make_initrd)
	os.system(copy_kernel)

os.system("chmod 755 /tftpboot")
os.system("chmod 644 /tftpboot/vmlinuz.*")
