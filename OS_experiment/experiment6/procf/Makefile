CONFIG_MODULE_SIG=n
obj-m := procfs_example.o
KDIR := /usr/src/linux-headers-$(shell uname -r )
PWD := $(shell pwd)
all:
	make -C $(KDIR) M=$(PWD) modules
clean:
	make -C $(KDIR) M=$(PWD) clean