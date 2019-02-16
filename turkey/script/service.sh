    echo -e "\033[34;49;1m[+] Service Scan\033[39;49;0m"
echo -e "------------------------------------"
    touch ./script/output/service
    touch ./script/output/serresult
  
    centosVersion=8
    if [[ $centosVersion > 7 ]];then
        conf=$(systemctl list-unit-files --type=service --state=enabled --no-pager | grep "enabled")
        process=$(systemctl list-units --type=service --state=running --no-pager | grep ".service")
        #报表信息
        report_SelfInitiatedService="$(echo "$conf" | wc -l)"       #自启动服务数量
        report_RuningService="$(echo "$process" | wc -l)"           #运行中服务数量
    else
        conf=$(/sbin/chkconfig | grep -E ":on|:启用")
        process=$(/sbin/service --status-all 2>/dev/null | grep -E "is running|正在运行")
        #报表信息
        report_SelfInitiatedService="$(echo "$conf" | wc -l)"       #自启动服务数量
        report_RuningService="$(echo "$process" | wc -l)"           #运行中服务数量
    fi
	
    if [ $? -eq 0 ]; then
    	printf "%-60s\033[32;49;1m%10s\n\033[39;49;0m" "  - Service Config scan:" "[OK]"
	printf "%-60s\033[37;49;1m\n\033[39;49;0m" "    * The result is in the ./output/service" 
	echo "[OK]" 1> ./script/output/serresult
   	# echo -e "  - Contain Open Shell Debug:\033[31;49;1m\t\t\t\t\t\t[Found]\033[39;49;0m"
    else
    	printf "%-60s\033[31;49;1m%10s\n\033[39;49;0m" "  - Service Config scan:" "[No]"
	echo "[NO]" 1> ./script/output/serresult
    	#echo -e "  - Contain Open Shell Debug:\033[32;49;1m\t\t\t\t\t\t[No]\033[39;49;0m"
    fi

    echo "服务配置" 1> ./script/output/service
    echo "--------" 1>> ./script/output/service
    echo "$conf"  | column -t 1>> ./script/output/service
    echo "" 1>> ./script/output/service
    echo "正在运行的服务" 1>> ./script/output/service
    echo "--------------" 1>> ./script/output/service
    echo "$process" 1 >> ./script/output/service
echo -e "\n---------------------------------------------------------------------------------------------\n"
