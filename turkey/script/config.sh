#!/bin/bash
#version 1.0
#author by 网服务



echo " ####################################################################### "

rm -rf ./script/output/Klog
rm -rf ./script/suggestion/out.txt
echo -e  "\n"
echo -e "[+] \033[1;34m Account policy \033[0m" 
echo "------------------------------------"
passmax=`cat /etc/login.defs | grep PASS_MAX_DAYS | grep -v ^# | awk '{print $2}'`
passmin=`cat /etc/login.defs | grep PASS_MIN_DAYS | grep -v ^# | awk '{print $2}'`
passlen=`cat /etc/login.defs | grep PASS_MIN_LEN | grep -v ^# | awk '{print $2}'`
passage=`cat /etc/login.defs | grep PASS_WARN_AGE | grep -v ^# | awk '{print $2}'`

echo "  - Checking password lifetime for password setting policy "
if [ $passmax -le 90 -a $passmax -gt 0 ];then
  echo -e "   [ \033[1;32m DONE \033[0m ]"
  echo "[ DONE ]" >> ./script/output/Klog
  echo "[ √ ] 口令生存周期为${passmax}天，符合要求" >> ./script/suggestion/out.txt
else
  echo -e "   [ \033[1;31m WARNING \033[0m ]"
  echo "[ WARNING ]" >> ./script/output/Klog
  echo "[ X ] 口令生存周期为${passmax}天，不符合要求,建议设置不大于90天" >> ./script/suggestion/out.txt
fi

echo "  - Checking the minimum time interval of password change "
if [ $passmin -le 6 ];then
  echo -e "   [ \033[1;31m WARNING \033[0m ]"
  echo "[ WARNING ]" >> ./script/output/Klog
  echo "[ X ] 口令更改最小时间间隔为${passmin}天，不符合要求，建议设置大于等于6天" >> ./script/suggestion/out.txt
else
  echo -e "   [ \033[1;32m DONE \033[0m ]"
  echo "[ DONE ]" >> ./script/output/Klog
  echo "[ √ ] 口令更改最小时间间隔为${passmin}天，符合要求" >> ./script/suggestion/out.txt
fi

echo "  - Checking the minimum password length "
if [[ "$passlen" -ge "8" ]];then
  echo -e "   [ \033[1;32m DONE \033[0m ]"
  echo "[ DONE ]" >> ./script/output/Klog
  echo "[ √ ] 口令最小长度为${passlen},符合要求" >> ./script/suggestion/out.txt
else
  if [ "$passlen" = "" ];then
    echo -e "   [ \033[1;31m WARNING \033[0m ]"
    echo "[ WARNING ]" >> ./script/output/Klog
    echo "[ X ] 没有设置口令最小长度,不符合要求，建议设置最小长度大于等于8" >> ./script/suggestion/out.txt
  else
    echo -e "   [ \033[1;31m WARNING \033[0m ] "
    echo "[ WARNING ]" >> ./script/output/Klog
    echo "[ X ] 口令最小长度为${passlen},不符合要求，建议设置最小长度大于等于8" >> ./script/suggestion/out.txt
  fi
fi

echo "  - Checking days of password expiration warning time "
if [ $passage -ge 30 -a $passage -lt $passmax ];then
  echo -e "   [ \033[1;32m DONE \033[0m ]"
  echo "[ DONE ]" >> ./script/output/Klog
  echo "[ √ ] 口令过期警告时间天数为${passage},符合要求" >> ./script/suggestion/out.tx
else
  echo -e "   [ \033[1;31m WARNING \033[0m ]"
  echo "[ WARNING ]" >> ./script/output/Klog
  echo "[ X ] 口令过期警告时间天数为${passage},不符合要求，建议设置大于等于30并小于口令生存周期" >> ./script/suggestion/out.txt
fi

echo -e "\n"
echo -e "[+] \033[1;34m Umask setting \033[0m" 
echo "------------------------------------"
echo "  - Checking umask setting in /etc/profile file "
if [ ! -f /etc/profile ];then
  echo -e "   [ NOT FOUND ]"
  echo "[ NOT FOUND ]" >> ./script/output/Klog
  echo "[ X ] etc/profile配置文件不存在" >> ./script/suggestion/out.txt
else
  umask1=`cat /etc/profile | grep umask | grep -v ^# | awk '{print $2}'`
  for i in $umask1
  do
    if [ $i = "027" ];then
      echo -e "   [ \033[1;32m DONE \033[0m ]"
      echo "[ DONE ]" >> ./script/output/Klog
      echo "[ √ ] /etc/profile文件中所设置的umask为${i},符合 要求" >> ./script/suggestion/out.txt
    else
      flags=1
    fi
  done
  if [[ "$flags"="1" ]];then
    echo -e "   [ \033[1;31m WARNING \033[0m ]"
    echo "[ WARNING ]" >> ./script/output/Klog
    echo "[ X ] /etc/profile文件中所所设置的umask为${i},不符合要求，建议设置为027" >> ./script/suggestion/out.txt
  fi 
fi

echo "  - Checking umask setting in /etc/csh.cshrc file "
flags=0
if [ ! -f /etc/csh.cshrc ];then
  echo -e "   [ NOT FOUND ]"
  echo "[ NOT FOUND ]" >> ./script/output/Klog
  echo "[ X ] etc/csh.cshrc配置文件不存在" >> ./script/suggestion/out.txt
else
  umask2=`cat /etc/csh.cshrc | grep umask | grep -v ^# | awk '{print $2}'`
  for i in $umask2
  do
    if [ $i = "027" ];then
      echo -e "   [ \033[1;32m DONE \033[0m ]"
      echo "[ DONE ]" >> ./script/output/Klog
      echo "[ √ ] /etc/csh.cshrc文件中所设置的umask为${i},符合 要求" >> ./script/suggestion/out.txt
    else
      flags=1
    fi
  done
  if [[ "$flags" -eq 1 ]];then
    echo -e "   [ \033[1;31m WARNING \033[0m ]"
    echo "[ WARNING ]" >> ./script/output/Klog
    echo "[ X ] /etc/csh.cshrc文件中所所设置的umask为${i},不符合要求，建议设置为027" >> ./script/suggestion/out.txt
  fi 
fi

echo "  - Checking umask setting in /etc/bashrc file "
flags=0
if [ ! -f /etc/csh.cshrc ];then
  echo -e "   [ NOT FOUND ]"
  echo "[ NOT FOUND ]" >> ./script/output/Klog
  echo "[ X ] etc/bashrc配置文件不存在" >> ./script/suggestion/out.txt
else
  umask3=`cat /etc/bashrc | grep umask | grep -v ^# | awk 'NR!=1{print $2}'`
  for i in $umask3
  do
    if [ $i = "027" ];then
      echo -e "   [ \033[1;32m DONE \033[0m ]"
      echo "[ DONE ]" >> ./script/output/Klog
      echo "[ √ ] /etc/bashrc文件中所设置的umask为${i},符合 要求" >> ./script/suggestion/out.txt
    else
      flags=1
    fi
  done
  if [[ "$flags" = "1" ]];then
    echo -e "   [ \033[1;31m WARNING \033[0m ]"
    echo "[ WARNING ]" >> ./script/output/Klog
    echo "[ X ] /etc/bashrc文件中所所设置的umask为${i},不符合要求，建议设置为027" >> ./script/suggestion/out.txt
  fi 
fi


echo -e "\n"
echo -e "[+] \033[1;34m Account cancellation \033[0m" 
echo "------------------------------------"
echo "  - Checking whether account will be cancelled automatically "
TMOUT=`cat /etc/profile | grep TMOUT | awk -F[=] '{print $2}'`
if [ ! $TMOUT ];then
  echo -e "   [ \033[1;31m WARNING \033[0m ]"
echo "[ WARNING ]" >> ./script/output/Klog
  echo "[ X ] 账号超时不存在自动注销,不符合要求，建议设置小于600秒" >> ./script/suggestion/out.txt
else
        if [ $TMOUT -le 600 -a $TMOUT -ge 10 ] ; then
          echo -e "   [ \033[1;32m DONE \033[0m ]"
          echo "[ DONE ]" >> ./script/output/Klog
          echo "[ √ ] 账号超时时间${TMOUT}秒,符合要求" >> ./script/suggestion/out.txt
        else
          echo -e "   [ \033[1;31m WARNING \033[0m ]"
          echo "[ WARNING ]" >> ./script/output/Klog
          echo "[ X ] 账号超时时间$TMOUT秒,不符合要求，建议设置小于600秒" >> ./script/suggestion/out.txt
        fi
fi 

echo -e "\n"
echo -e "[+] \033[1;34m Non root accounts with UID 0 \033[0m" 
echo "------------------------------------"
echo "  - Checking if there are non root accounts with UID 0 "
UIDS=`awk -F[:] 'NR!=1{print $3}' /etc/passwd`
for i in $UIDS
do
  if [ $i = 0 ];then
    echo -e "   [ \033[1;31m WARNING \033[0m ]"
    echo "[ WARNING ]" >> ./script/output/Klog
    echo "[ X ] 存在非root账号的账号UID为0，不符合要求" >> ./script/suggestion/out.txt
  else
    flag=1
  fi
done
if [ $flag = 1 ];then
  echo -e "   [ \033[1;32m DONE \033[0m ]"
  echo "[ DONE ]" >> ./script/output/Klog
  echo "[ √ ] 不存在非root账号的账号UID为0，符合要求" >> ./script/suggestion/out.txt
fi


echo -e "\n"
echo -e "[+] \033[1;34m Cipher code \033[0m" 
echo "------------------------------------"
echo "  - Checking GRUB cipher "
if [ ! -f /boot/etc/grub.conf ] ; then
   echo -e "   [ NOT FOUND ]"
   echo "[ NOT FOUND ]" >> ./script/output/Klog
   echo "[ X ] grub.conf配置文件不存在，系统可能不是通过GRUB引导" >> ./script/suggestion/out.txt
else
   grup_pwd=`cat /boot/etc/grub.conf | grep -v ^# | grep password 2> /dev/null`
       if [ $? -eq 0 ];then
               echo -e "   [ \033[1;32m DONE \033[0m ]"
               echo "[ DONE ]" >> ./script/output/Klog
               echo "[ √ ] 已设置grub密码,符合要求" >> ./script/suggestion/out.txt
       else
               echo -e "   [ \033[1;31m WARNING \033[0m ]"
               echo "[ WARNING ]" >> ./script/output/Klog
               echo "[ X ] 没有设置grub密码，不符合要求,建议设置lilo密码" >> ./script/suggestion/out.txt
       fi
fi

echo "  - Checking LILO cipher "
if [ ! -f /etc/lilo.conf ] ; then
   echo -e "   [ NOT FOUND ]"
   echo "[ NOT FOUND ]" >> ./script/output/Klog
   echo "[ √ ] lilo.conf配置文件不存在，系统可能不是通过LILO引导" >> ./script/suggestion/out.txt
else
   lilo_pwd=`cat /etc/lilo.conf | grep -v ^# | grep password &> /dev/null`
       if [ $? -eq 0 ];then
               echo -e "   [ \033[1;32m DONE \033[0m ]"
               echo "[ DONE ]" >> ./script/output/Klog
               echo "[ √ ] 已设置lilo密码,符合要求" >> ./script/suggestion/out.txt
       else
               echo -e "   [ \033[1;31m WARNING \033[0m ]"
               echo "[ WARNING ]" >> ./script/output/Klog
               echo "[ X ] 没有设置lilo密码，不符合要求,建议设置lilo密码" >> ./script/suggestion/out.txt
       fi
fi

echo -e "\n"
echo -e "[+] \033[1;34m Core dump \033[0m" 
echo "------------------------------------"
echo "  - Checking whether the system core dump meets the specifications "
cat /etc/security/limits.conf | grep -V ^# | grep core
if [ $? -eq 0 ];then
  soft=`cat /etc/security/limits.conf | grep -V ^# | grep core | awk {print $2}`
  for i in $soft
  do
    if [ $i = "soft" ];then
      echo "[ √ ] * soft core 0 已经设置" >> ./script/suggestion/out.txt
    fi
    if [ $i = "hard" ];then
      echo "[ √ ] * hard core 0 已经设置" >> ./script/suggestion/out.txt
    fi
  done
echo -e "   [ \033[1;32m DONE \033[0m ]"
echo "[ DONE ]" >> ./script/output/Klog
else 
  echo -e "   [ \033[1;31m WARNING \033[0m ]"
  echo "[ WARNING ]" >> ./script/output/Klog
  echo "[ X ] 没有设置core，建议在/etc/security/limits.conf中添加* soft core 0和* hard core 0" >> ./script/suggestion/out.txt
fi

echo -e "\n"
echo -e "[+] \033[1;34m Important document authority \033[0m" 
echo "------------------------------------"
file1=`ls -l /etc/passwd | awk '{print $1}'`
file2=`ls -l /etc/shadow | awk '{print $1}'`
file3=`ls -l /etc/group | awk '{print $1}'`
file4=`ls -l /etc/securetty | awk '{print $1}'`
file5=`ls -l /etc/services | awk '{print $1}'`
echo "  - Checking file /etc/passwd permissions "
if [ $file1 = "-rw-r--r--" ];then
  echo -e "   [ \033[1;32m DONE \033[0m ]"
  echo "[ DONE ]" >> ./script/output/Klog
  echo "[ √ ] /etc/passwd文件权限为644，符合要求" >> ./script/suggestion/out.txt
else
  echo -e "   [ \033[1;31m WARNING \033[0m ]"
  echo "[ WARNING ]" >> ./script/output/Klog
  echo "[ X ] /etc/passwd文件权限不为644，不符合要求，建议设置权限为644" >> ./script/suggestion/out.txt
fi

echo "  - Checking file /etc/shadow permissions "
if [ $file2 = "-r--------" ];then
  echo -e "   [ \033[1;32m DONE \033[0m ]"
  echo "[ DONE ]" >> ./script/output/Klog
  echo "[ √ ] /etc/shadow文件权限为400，符合要求" >> ./script/suggestion/out.txt
else
  echo -e "   [ \033[1;31m WARNING \033[0m ]"
  echo "[ WARNING ]" >> ./script/output/Klog
  echo "[ X ] /etc/shadow文件权限不为400，不符合要求，建议设置权限为400" >> ./script/suggestion/out.txt
fi

echo "  - Checking file /etc/group permissions "
if [ $file3 = "-rw-r--r--" ];then
  echo -e "   [ \033[1;32m DONE \033[0m ]"
  echo "[ DONE ]" >> ./script/output/Klog
  echo "[ √ ] /etc/group文件权限为644，符合要求" >> ./script/suggestion/out.txt
else
  echo -e "   [ \033[1;31m WARNING \033[0m ]"
  echo "[ WARNING ]" >> ./script/output/Klog
  echo "[ X ] /etc/group文件权限不为644，不符合要求，建议设置权限为644" >> ./script/suggestion/out.txt
fi

echo "  - Checking file /etc/security permissions "
if [ $file4 = "-rw-------" ];then
  echo -e "   [ \033[1;32m DONE \033[0m ]"
  echo "[ DONE ]" >> ./script/output/Klog
  echo "[ √ ] /etc/security文件权限为600，符合要求" >> ./script/suggestion/out.txt
else
  echo -e "   [ \033[1;31m WARNING \033[0m ]"
  echo "[ WARNING ]" >> ./script/output/Klog
  echo "[ X ] /etc/security文件权限不为600，不符合要求，建议设置权限为600" >> ./script/suggestion/out.txt
fi

echo "  - Checking file /etc/services permissions "
if [ $file5 = "-rw-r--r--" ];then
  echo -e "   [ \033[1;32m DONE \033[0m ]"
  echo "[ DONE ]" >> ./script/output/Klog
  echo "[ √ ] /etc/services文件权限为644，符合要求" >> ./script/suggestion/out.txt
else
  echo -e "   [ \033[1;31m WARNING \033[0m ]"
  echo "[ WARNING ]" >> ./script/output/Klog
  echo "[ X ] /etc/services文件权限不为644，不符合要求，建议设置权限为644" >> ./script/suggestion/out.txt
fi

echo "  - Checking file /etc/xinetd.conf permissions "
if [ ! -f /etc/xinted.conf ];then
  echo -e "   [ NOT FOUND ]"
  echo "[ NOT FOUND ]" >> ./script/output/Klog
  echo "[ X ] /etc/xinted.conf文件夹不存在" >> ./script/suggestion/out.txt
else
  file6=`ls -l /etc/xinetd.conf | awk '{print $1}'`
  if [ "$file6" = "-rw-------" ];then
    echo -e "   [ \033[1;32m DONE \033[0m ]"
    echo "[ DONE ]" >> ./script/output/Klog
    echo "[ √ ] /etc/xinetd.conf文件权限为600，符合要求" >> ./script/suggestion/out.txt
  else
    echo -e "   [ \033[1;31m WARNING \033[0m ]"
    echo "[ WARNING ]" >> ./script/output/Klog
    echo "[ X ] /etc/xinetd.conf文件权限不为600，不符合要求，建议设置权限为600" >> ./script/suggestion/out.txt
  fi
fi

echo "  - Checking file /etc/grub.conf permissions "
if [ ! -f /etc/grub.conf ];then
  echo -e "   [ NOT FOUND ]"
  echo "[ NOT FOUND ]" >> ./script/output/Klog
  echo "[ X ] /etc/grub.conf文件夹不存在" >> ./script/suggestion/out.txt
else
  file7=`ls -l /etc/grub.conf | awk '{print $1}'`
  if [ "$file7" = "-rw-------" ];then
    echo -e "   [ \033[1;32m DONE \033[0m ]"
    echo "[ DONE ]" >> ./script/output/Klog
    echo "[ √ ] /etc/grub.conf文件权限为600，符合要求" >> ./script/suggestion/out.txt
  else
    echo -e "   [ \033[1;31m WARNING \033[0m ]"
    echo "[ WARNING ]" >> ./script/output/Klog
    echo "[ X ] /etc/grub.conf文件权限不为600，不符合要求，建议设置权限为600" >> ./script/suggestion/out.txt
  fi
fi

echo "  - Checking file /etc/lilo.conf permissions "
if [ ! -f /etc/lilo.conf ];then
  echo -e "   [ NOT FOUND ]"
  echo "[ NOT FOUND ]" >> ./script/output/Klog
  echo "[ X ] /etc/lilo.conf文件夹不存在" >> ./script/suggestion/out.txt
else
  if [ $file8 = "-rw-------" ];then
    file7=`ls -l /etc/grub.conf | awk '{print $1}'`
file8=`ls -l /etc/lilo.conf | awk '{print $1}'`s
    echo -e "   [ \033[1;32m DONE \033[0m ]"
    echo "[ DONE ]" >> ./script/output/Klog
    echo "[ √ ] /etc/lilo.conf文件权限为600，符合要求" >> ./script/suggestion/out.txt
  else
    echo -e "   [ \033[1;31m WARNING \033[0m ]"
    echo "[ WARNING ]" >> ./script/output/Klog
    echo "[ X ] /etc/lilo.conf文件权限不为600，不符合要求，建议设置权限为600" >> ./script/suggestion/out.txt
  fi
fi

echo -e "\n"
echo -e "[+] \033[1;34m Telnet \033[0m" 
echo "------------------------------------"
echo "  - Checking whether the telnet service is open "
if [ ! -f /etc/xinetd.d/telnet ];then
  echo -e "   [ NOT FOUND ]"
  echo "[ NOT FOUND ]" >> ./script/output/Klog
  echo "[ X ] telnet配置文件不存在" >> ./script/suggestion/out.txt
else
  telnetd=`cat /etc/xinetd.d/telnet | grep disable | awk '{print $3}'`
  if [ "$telnetd" = "yes" ];then
    echo -e "   [ \033[1;31m WARNING \033[0m ]"
    echo "[ WARNING ]" >> ./script/output/Klog
    echo "[ X ] 检测到telnet服务开启，不符合要求，建议关闭telnet" >> ./script/suggestion/out.txt
  else
    echo -e "   [ \033[1;32m DONE \033[0m ]"
    echo "[ DONE ]" >> ./script/output/Klog
    echo "[ √ ] 未检测到telnet服务开启，符合要求" >> ./script/suggestion/out.txt
  fi
fi

echo -e "\n"
echo -e "[+] \033[1;34m Openssh security configuration \033[0m" 
echo "------------------------------------"
echo "  - Checking openssh security configuration "
if [ ! -f /etc/ssh/sshd_config ];then
  echo -e "   [ NOT FOUND ]"
  echo "[ NOT FOUND ]" >> ./script/output/Klog
  echo "[ X ] sshd_config配置文件不存在" >> ./script/suggestion/out.txt
else
  Protocol=`cat /etc/ssh/sshd_config | grep -v ^# | grep Protocol | awk '{print $2}'`
  if [ "$Protocol" = "2" ];then
    echo -e "   [ \033[1;32m DONE \033[0m ]"
    echo "[ DONE ]" >> ./script/output/Klog
    echo "[ √ ] openssh使用ssh2协议，符合要求" >> ./script/suggestion/out.txt
  fi
  if [ "$Protocol" = "1" ];then
    echo -e "   [ \033[1;31m WARNING \033[0m ]"
    echo "[ WARNING ]" >> ./script/output/Klog
    echo "[ X ] openssh使用ssh1协议，不符合要求" >> ./script/suggestion/out.txt
  fi
fi

echo -e "\n"
echo -e "[+] \033[1;34m History command \033[0m" 
echo "------------------------------------"
echo "  - Checking numbers of history command "
HISTSIZE=`cat /etc/profile|grep HISTSIZE|head -1|awk -F[=] '{print $2}'`
if [[ "$HISTSIZE" -eq "5" ]];then
  echo -e "   [ \033[1;32m DONE \033[0m ]"
  echo "[ DONE ]" >> ./script/output/Klog
  echo "[ √ ] 保留历时命令条数为$HISTSIZE,符合要求" >> ./script/suggestion/out.txt
else
  if [ "$HISTSIZE" = "" ];then
    echo -e "   [ \033[1;31m WARNING \033[0m ]"
    echo "[ WARNING ]" >> ./script/output/Klog
    echo "[ X ] 没有设置保留历史命令条数,不符合要求，建议/etc/profile的HISTSIZE设置为5" >> ./script/suggestion/out.txt
  else
    echo -e "   [ \033[1;31m WARNING \033[0m ]"
    echo "[ WARNING ]" >> ./script/output/Klog
    echo "[ X ] 保留历时命令条数为$HISTSIZE,不符合要求，建议/etc/profile的HISTSIZE设置为5" >> ./script/suggestion/out.txt
  fi
fi

echo -e "\n"
echo -e "[+] \033[1;34m SNMP default group password \033[0m" 
echo "------------------------------------"
echo "  - Checking SNMP default group password public "
if [ -f /etc/snmp/snmpd.conf ];then
  public=`cat /etc/snmp/snmpd.conf | grep public | grep -v ^# | awk '{print $4}'`
  private=`cat /etc/snmp/snmpd.conf | grep private | grep -v ^# | awk '{print $4}'`
  if [ $public = "public" ];then
    echo -e "   [ \033[1;31m WARNING \033[0m ]"
    echo "[ WARNING ]" >> ./script/output/Klog
    echo "[ X ] 发现snmp服务存在默认团体名public,不符合要求" >> ./script/suggestion/out.txt
  else
    echo -e "   [ NOT FOUND ]"
    echo "[ NOT FOUND ]" >> ./script/output/Klog
  fi
echo "  - Checking SNMP default group password private "
  if [[ $private = "private" ]];then
    echo -e "   [ \033[1;31m WARNING \033[0m ]"
    echo "[ WARNING ]" >> ./script/output/Klog
    echo "[ X ] 发现snmp服务存在默认团体名private,不符合要求" >> ./script/suggestion/out.txt
  else
    echo -e "   [ NOT FOUND ]"
    echo "[ NOT FOUND ]" >> ./script/output/Klog
  fi
else
  echo -e "   [ NOT FOUND ]"
  echo "[ NOT FOUND ]" >> ./script/output/Klog
  echo "[ √ ] snmp服务配置文件不存在，可能没有运行snmp服务" >> ./script/suggestion/out.txt 
fi

echo -e "\n"
echo -e "[+] \033[1;34m Disk dynamic space \033[0m" 
echo "------------------------------------"
echo "  - Checking Disk dynamic space "
space=`df -h | awk -F "[ %]+" 'NR!=1{print $5}'`
for i in $space
do
  if [ $i -ge 80 ];then
   flag=1
  else flag=0
  fi
done
if [ "$flag" = "1" ];then
echo -e "   [ \033[1;31m WARNING \033[0m ]"
echo "[ WARNING ]" >> ./script/output/Klog
echo "[ X ] 警告！磁盘存储容量大于80%,建议扩充磁盘容量或者删除垃圾文件" >> ./script/suggestion/out.txt 
else
echo -e "   [ \033[1;32m DONE \033[0m ]"
echo "[ DONE ]" >> ./script/output/Klog
echo "[ √ ] 磁盘存储容量小于80%,符合要求" >> ./script/suggestion/out.txt
fi

echo -e "\n"
echo " ####################################################################### " 


