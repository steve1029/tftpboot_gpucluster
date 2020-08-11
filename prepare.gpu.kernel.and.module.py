import os, copy

gpunodes = []
homes = []

homename = 'yhome%01d'
nodename = 'y%03d'

#for number in xrange(1, 4):
#	homes.append(homename % number)

for number in xrange(205,216):
	gpunodes.append(nodename % number)

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

for gpunode in gpunodes:
	f = open(node_pxe_config % gpunode, 'w')
	f.write(config % (gpunode, gpunode, serverip, gpunode))
	f.close()

##############################################################
################### Prepare kernel module ####################
##############################################################

if not os.path.exists("/tftpboot/initramfs-pxe.gpunode"):
	os.system("mkdir /tftpboot/initramfs-pxe.gpunode")

uname = '4.4.0-87-generic'

copied_server_kernel        = '/tftpboot/vmlinuz-%s.gpunode' %uname
copied_server_kernel_module = '/tftpboot/initramfs-tools-%s.gpunode' %uname
copied_server_module_config = '/tftpboot/initramfs-tools-%s.gpunode/initramfs.conf' %uname

node_kernel_path          = '/tftpboot/vmlinuz.%s'
node_kernel_module_path   = '/tftpboot/initramfs-pxe.gpunode/%s'
node_kernel_module_config = '/tftpboot/initramfs-pxe.gpunode/%s/initramfs.conf'
node_module_image_path    = '/tftpboot/initrd.img.%s'

#----------- make kernel module for all gpunodes ------------#
for gpunode in gpunodes:
	nkm_path = node_kernel_module_path % gpunode
	command = 'cp -a %s %s' % (copied_server_kernel_module, nkm_path)
	os.system(command)

#---------- Edit configuration file for all gpunodes --------#
server_config = open(copied_server_module_config, 'r').read()

for gpunode in gpunodes:
	f = open(node_kernel_module_config % gpunode, 'w')

	node_config = copy.deepcopy(server_config)
	node_config = node_config.replace('MODULES=most', 'MODULES=netboot\nBOOT=nfs')
	node_config = node_config.replace('DEVICE=', 'DEVICE=')
	node_config = node_config.replace('NFSROOT=auto', ('NFSROOT=%s:/nfsroot/%s' % (serverip, gpunode)))

	f.write(node_config)
	f.close()

#--- Prepare kernel and kernel module image for gpunodes ----#

for gpunode in gpunodes:
	print 'making image of initramfs: %s' % gpunode

	nk_path  = node_kernel_path        % gpunode	
	nkm_path = node_kernel_module_path % gpunode
	nmi_path = node_module_image_path  % gpunode	

	make_initrd = 'mkinitramfs -d %s -o %s %s' % (nkm_path, nmi_path, uname)
	copy_kernel = 'cp -a %s %s' % (copied_server_kernel, nk_path)

	os.system(make_initrd)
	os.system(copy_kernel)

os.system("chmod 755 /tftpboot")
os.system("chmod 644 /tftpboot/vmlinuz.*")
