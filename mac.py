#! /bin/python
import os

with open('M6B.csv', 'a') as f:
    for i in range(0,160):
        ip = '6.16.8.' + str(i+1)
        power_on_cmd = "ipmitool -I lanplus -H %s -U admin -P admin power on" % ip
        os.popen(power_on_cmd)

        sn_cmd = "ipmitool -I lanplus -H %s -U admin -P admin fru | grep 'Product Serial' |awk -F ':' '{print $2}'|uniq" % ip
        sn = os.popen(sn_cmd).read().strip()
        
        mac1_cmd = "ipmitool -I lanplus -H %s -U admin -P admin raw 0x3a 0x02 0x04 0x00 0x00" % ip
        output = os.popen(mac1_cmd).read()
        mac1 = ':'.join(output.split()[5:11])

        mac2_cmd = "ipmitool -I lanplus -H %s -U admin -P admin raw 0x3a 0x02 0x04 0x01 0x01" % ip
        output = os.popen(mac2_cmd).read()
        mac2 = ':'.join(output.split()[5:11])
        
        power_off_cmd = "ipmitool -I lanplus -H %s -U admin -P admin power off" % ip
        os.popen(power_off_cmd)

        print sn, mac1, mac2
        
        f.write(sn+','+mac1+','+mac2+'\n')
