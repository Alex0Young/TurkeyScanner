echo -e "\033[34;49;1m[+] Bash or Shell Debug Modle \033[39;49;0m"
echo -e "------------------------------------"

touch ./script/output/debugModel
touch ./script/output/deresult
touch ./script/suggestion/suggestion
echo "---   System Suggestions:   ---" 1> ./script/suggestion/suggestion
find / \
-path /proc -prune -o \
-path /tmp -prune -o \
-path /boot -prune -o \
-path /run/user/1000 -prune -o \
-type f -name "*.sh" | xargs egrep -i -n 'bash[[:blank:]]*-[a-zA-Z]*x|set[[:blank:]]*-[a-zA-Z]*x' | egrep -v "bash_history|Binary file|containerScan|vmSecureScan|/devicemapper/mnt"  2>/dev/null 1> ./script/output/debugModel

if [ $? -eq 0 ]; then
    printf "%-60s\033[31;49;1m%10s\n\033[39;49;0m" "  - Contain Open Shell Debug Files:" "[Found]"
    printf "%-60s\033[37;49;1m\n\033[39;49;0m" "    * The result is in the ./output/debugmodel" 
    echo "[Found]" 1> ./script/output/deresult
    echo "Sh Debug Model Suggestion:" >> ./script/suggestion/suggestion
    echo "  *开启Sh Debug 模式会暴露过多的系统信息，请注意" >> ./script/suggestion/suggestion
   # echo -e "  - Contain Open Shell Debug:\033[31;49;1m\t\t\t\t\t\t[Found]\033[39;49;0m"
else
    printf "%-60s\033[32;49;1m%10s\n\033[39;49;0m" "  - Contain Open Shell Debug Files:" "[No]"
    echo "[NO]" 1> ./script/output/deresult
    #echo -e "  - Contain Open Shell Debug:\033[32;49;1m\t\t\t\t\t\t[No]\033[39;49;0m"
fi

find / \
-path /proc -prune -o \
-path /tmp -prune -o \
-path /boot -prune -o \
-path /run/user/1000 -prune -o \
-type f -name "*.py" | xargs egrep -i -n 'bash[[:blank:]]*-[a-zA-Z]*x|set[[:blank:]]*-[a-zA-Z]*x' | egrep -v "bash_history|Binary file|containerScan|vmSecureScan|/devicemapper/mnt" 2>/dev/null 1>> ./script/output/debugModel

if [ $? -eq 0 ]; then
    printf "%-60s\033[31;49;1m%10s\n\033[39;49;0m" "  - Contain Open Bash Debug Files:" "[Found]"
    echo "[Found]" 1>> ./script/output/deresult
    echo "Bash Debug Model Suggestion:" >> ./script/suggestion/suggestion
    echo "  *开启Bash Debug 模式会暴露过多的系统信息，请注意" >> ./script/suggestion/suggestion
   # echo -e "  - Contain Open Bash Debug123456789132456:\033[31;49;1m\t\t\t\t\t[Found]\033[39;49;0m"
else
    printf "%-60s\033[32;49;1m%10s\n\033[39;49;0m" "  - Contain Open Bash Debug Files:" "[No]"
    echo "[No]" 1>> ./script/output/deresult
    # echo -e "  - Contain Open Bash Debug File:\033[32;49;1m\t\t\t\t\t[No]\033[39;49;0m"
fi
echo -e "\n---------------------------------------------------------------------------------------------\n"
