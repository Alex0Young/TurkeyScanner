echo -e "\033[34;49;1m[+] Log Sensitive Detection \033[39;49;0m"
echo -e "------------------------------------"
touch ./script/output/certlog
touch ./script/output/logresult
key_words="(certificate|auth|session|token|key|ak|sk)(\s*:|\s*=|\"\s*(:|=)|\'\s*(:|=)).*[0-9a-zA-Z]{20,}"

find /var -name '*.dat' -type f | xargs file |grep -E 'text|XML|PC bitmap data'|awk '{print $1}'|sed 's/:$//g'|xargs grep -i -n -E -H "$key_words" | egrep -v 'bash_history|Binary file|containerScan|vmSecureScan|/devicemapper/mnt' 2>/dev/null 1> ./script/output/certlog
find /var -name '*.log' -type f | xargs file | grep -E 'text|XML|PC bitmap data'|awk '{print $1}'|sed 's/:$//g'|xargs grep -i -n -E -H "$key_words" | egrep -v 'bash_history|Binary file|containerScan|vmSecureScan|/devicemapper/mnt' 2>/dev/null 1>> ./script/output/certlog

if [ $? -eq 0 ]; then
    printf "%-60s\033[31;49;1m%10s\n\033[39;49;0m" "  - Sensitive informatin in Logs:" "[Found]"
    echo "[Found]" 1> ./script/output/logresult
    printf "%-60s\033[37;49;1m\n\033[39;49;0m" "    * The result is in the ./certlog" 
    echo "Process Suggestion:" 1>> ./script/suggestion/suggestion
    echo "  *日志中含有敏感信息，请排查" 1>> ./script/suggestion/suggestion
   # echo -e "  - Contain Open Shell Debug:\033[31;49;1m\t\t\t\t\t\t[Found]\033[39;49;0m"
else
    printf "%-60s\033[32;49;1m%10s\n\033[39;49;0m" "  - Sensitive informatin in Logs:" "[No]"
    echo "[No]" 1> ./script/output/logresult
    #echo -e "  - Contain Open Shell Debug:\033[32;49;1m\t\t\t\t\t\t[No]\033[39;49;0m"
fi
echo -e "\n---------------------------------------------------------------------------------------------\n"