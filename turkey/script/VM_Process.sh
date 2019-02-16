echo -e "\033[34;49;1m[+] Process Detection \033[39;49;0m"
echo -e "------------------------------------"
touch ./script/output/process
touch ./script/output/proresult
ps -ef | egrep -v  '[[0-9]*]| pts/' |grep 'root ' 1> ./script/output/process
if [ $? -eq 0 ]; then
    printf "%-60s\033[31;49;1m%10s\n\033[39;49;0m" "  - The access of Process on root:" "[Found]"
    printf "[Found]\n" 1> ./script/output/proresult
    printf "%-60s\033[37;49;1m\n\033[39;49;0m" "    * The result is in the ./process" 
    echo "Process Suggestion:" >> ./script/suggestion/suggestion
    echo "  *请按照检查结果排查权限过大的进程" >> ./script/suggestion/suggestion
   # echo -e "  - Contain Open Shell Debug:\033[31;49;1m\t\t\t\t\t\t[Found]\033[39;49;0m"
else
    printf "%-60s\033[32;49;1m%10s\n\033[39;49;0m" "  - Contain Open Shell Debug Files:" "[No]"
    echo "[No]" 1> ./script/output/proresult
    #echo -e "  - Contain Open Shell Debug:\033[32;49;1m\t\t\t\t\t\t[No]\033[39;49;0m"
fi

    if [ $(ps -ef | grep defunct | grep -v grep | wc -l) -ge 1 ];then
        echo ""
        echo "僵尸进程";
        echo "--------"
        ps -ef | head -n1
        ps -ef | grep defunct | grep -v grep
        printf "%-60s\033[31;49;1m%10s\n\033[39;49;0m" "  - Defunct Process:" "[Found]"
	echo "[Found]" 1>> ./script/output/proresult
    else
	printf "%-60s\033[32;49;1m%10s\n\033[39;49;0m" "  - Defunct Process:" "[Not Found]"
	echo "[Not Found]" 1>> ./script/output/proresult
    fi
    
    echo ""
    echo "  - 内存占用TOP10" | tee -a ./script/output/process
    echo "-------------" | tee -a ./script/output/process
    echo -e "  PID %MEM RSS COMMAND
    $(ps aux | awk '{print $2, $4, $6, $11 }' | sort -k3rn | head -n 10 )"| column -t | tee -a ./script/output/process
    echo ""
    echo "  - CPU占用TOP10" | tee -a ./script/output/process
    echo "------------"
    top b -n1 | head -17 | tail -11 | tee -a ./script/output/process

echo -e "\n---------------------------------------------------------------------------------------------\n"
