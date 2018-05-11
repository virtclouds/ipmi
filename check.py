#! /bin/python
import os
import paramiko
with open('M6A_CHECK.csv','w') as f:
    f.write('SN,HOSTNAME\n')
    for i in range(0,160):
        ip = '6.19.7.' + str(i+1)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        sn=hostname=''
        try:
            ssh.connect(hostname=ip, port=22, username='root', password='I6_spur!')
            stdin, stdout, stderr = ssh.exec_command('dmidecode -s system-serial-number')
            sn = stdout.read().decode().strip()
            stdin, stdout, stderr = ssh.exec_command('hostname')
            hostname = stdout.read().decode().strip()
            print sn, hostname
        except Exception as e:
            print e
        finally:
            ssh.close()

        f.write(str(sn)+','+hostname+'\n')



