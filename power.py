#! /bin/python
import os
ip_map={
        # 3:70,
        # 4:140,
        #5:160,
        #6:150,
        7:160,
        8:160
        }

for k in ip_map:
    pre = k 
    suffix = ip_map.get(k)
    for i in range(0,suffix):
        ip = '6.16.'+str(pre)+'.' + str(i+1)
        try:
            print ip
            power_on_cmd = "ipmitool -I lanplus -H %s -U admin -P admin power off" % ip
            os.popen(power_on_cmd)
        except Exception as e:
            print e


