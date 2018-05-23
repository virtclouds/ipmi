# ipmi 指令集
## 设置临时PXE启动
ipmitool -I lanplus -H 6.16.5.42 -U admin -P admin power off
ipmitool -I lanplus -H 6.16.5.42 -U admin -P admin chassis bootdev pxe
ipmitool -I lanplus -H 6.16.5.42 -U admin -P admin power on

## 获取板载网卡MAC
ipmitool -I lanplus -H 6.16.5.42 -U admin -P admin power on
ipmitool -I lanplus -H 6.16.5.42 -U admin -P admin raw 0x3a 0x02 0x04 0x00 0x00
ipmitool -I lanplus -H 6.16.5.42 -U admin -P admin raw 0x3a 0x02 0x04 0x01 0x01

