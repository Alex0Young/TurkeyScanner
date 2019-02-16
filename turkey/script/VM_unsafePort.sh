touch ./script/output/portresult
touch ./script/suggestion/portsuggestion
n=`netstat -tunlp | egrep "20" | awk '{ print $4}'`
if [ "${n##*:}" = "20" ]; then
	printf "%-60s\033[32;49;1m%10s\n\033[39;49;0m" "  - Ftp Data Port 20:" "[Found]" 
	echo "[Found]" 1> ./script/output/portresult
else
	printf "%-60s\033[37;49;1m%10s\n\033[39;49;0m" "  - Ftp Data Port 20:" "[Not Found]" 
	echo "[Not Found]" 1> ./script/output/portresult
fi

n=`netstat -tunlp | egrep "21" | awk '{ print $4}'`
if [ "${n##*:}" = "21" ]; then
	printf "%-60s\033[32;49;1m%10s\n\033[39;49;0m" "  - Ftp Port 21:" "[Found]"
	echo "[Found]" 1>> ./script/output/portresult
else
	printf "%-60s\033[37;49;1m%10s\n\033[39;49;0m" "  - Ftp Port 21:" "[Not Found]"
	echo "[Not Found]" 1>> ./script/output/portresult
fi

n=`netstat -tunlp | egrep "22" | awk '{ print $4}'`
if [ "${n##*:}" = "22" ]; then
	printf "%-60s\033[32;49;1m%10s\n\033[39;49;0m" "  - SSH Port 22:" "[Found]" 
	echo "[Found]" 1>> ./script/output/portresult
else
	printf "%-60s\033[37;49;1m%10s\n\033[39;49;0m" "  - SSH Port 22:" "[Not Found]" 
	echo "[Not Found]" 1>> ./script/output/portresult
fi

n=`netstat -tunlp | egrep "25" | awk '{ print $4}'`
if [ "${n##*:}" = "25" ]; then
	printf "%-60s\033[32;49;1m%10s\n\033[39;49;0m" "  - Smtp Port 25:" "[Found]"
	echo "[Found]" 1>> ./script/output/portresult
else
	printf "%-60s\033[37;49;1m%10s\n\033[39;49;0m" "  - Smtp Port 25:" "[Not Found]"
	echo "[Not Found]" 1>> ./script/output/portresult
fi

n=`netstat -tunlp | egrep "53" |egrep -v "5353" | awk '{ print $4}'`
for i in ${n}
do 
	d=${n##*:}
	if [ "$d" = "53" ]; then
		printf "%-60s\033[32;49;1m%10s\n\033[39;49;0m" "  - Domain Port 53:" "[Found]"
		echo "[Found]" 1>> ./script/output/portresult		
		break
	else
		printf "%-60s\033[37;49;1m%10s\n\033[39;49;0m" "  - Domain Port 53:" "[Not Found]"
		echo "[Not Found]" 1>> ./script/output/portresult
	fi
done

n=`netstat -tunlp | egrep "80" | awk '{ print $4}'`
if [ "${n##*:}" = "80" ]; then
	printf "%-60s\033[32;49;1m%10s\n\033[39;49;0m" "  - Http Port 80:" "[Found]"
	echo "[Found]" 1>> ./script/output/portresult
else
	printf "%-60s\033[37;49;1m%10s\n\033[39;49;0m" "  - Http Port 80:" "[Not Found]"
	echo "[Not Found]" 1>> ./script/output/portresult
fi

n=`netstat -tunlp | egrep "109" | awk '{ print $4}'`
if [ "${n##*:}" = "109" ]; then
	printf "%-60s\033[32;49;1m%10s\n\033[39;49;0m" "  - Pop2 Port 109:" "[Found]"
	echo "[Found]" 1>> ./script/output/portresult
else
	printf "%-60s\033[37;49;1m%10s\n\033[39;49;0m" "  - Pop2 Port 109 :" "[Not Found]"
	echo "[Not Found]" 1>> ./script/output/portresult
fi

n=`netstat -tunlp | egrep "143" | awk '{ print $4}'`
if [ "${n##*:}" = "143" ]; then
	printf "%-60s\033[32;49;1m%10s\n\033[39;49;0m" "  - Imap Port 143:" "[Found]"
	echo "[Found]" 1>> ./script/output/portresult
else
	printf "%-60s\033[37;49;1m%10s\n\033[39;49;0m" "  - Imap Port 143:" "[Not Found]"
	echo "[Not Found]" 1>> ./script/output/portresult
fi

n=`netstat -tunlp | egrep "161" | awk '{ print $4}'`
if [ "${n##*:}" = "161" ]; then
	printf "%-60s\033[32;49;1m%10s\n\033[39;49;0m" "  - Snmp Port 161:" "[Found]"
	echo "[Found]" 1>> ./script/output/portresult
else
	printf "%-60s\033[37;49;1m%10s\n\033[39;49;0m" "  - Snmap Port 161:" "[Not Found]"
	echo "[Not Found]" 1>> ./script/output/portresult
fi

#n=`netstat -tunlp | egrep -v "Local" | awk '{ print $4}'`
#a="1024"
#for i in ${n}
#do 
#	d=${i##*:}
#	if [ $d -gt $a ];then
#		printf "%-60s\033[31;49;1m%10s\n\033[39;49;0m" "  - Port more than 1024:" "[Found]"
#		printf "%-60s\033[31;49;1m%10s\n\033[39;49;0m" "   * ${i}"
#		printf "%-40s%10s\n" "Port more than 1024:${i}" "[Found]" 1>> ./script/output/portresult	
#		b=1		
#	fi
#done

#if [ "$b" = "1" ];then
#	echo "port Suggestion:" 1> ./script/suggestion/portsuggestion
#	echo "  *请检查大于1024的端口" 1>> ./script/suggestion/portsuggestion
#fi				


