echo -e "\033[34;49;1m[+] Login Status \033[39;49;0m"
echo -e "------------------------------------"
touch ./script/output/loginf
touch ./script/output/logstaresult
loginf=$(last | head | awk '{ print $1 }'  )
wh=$(who)
for i in $loginf
do 
    if [ "$i"!="$wh" ]; then
       echo "$i" 1> ./script/output/loginf
       a=1
    fi
done
if [ "$a"==1 ];then
   printf "%-60s\033[31;49;1m%10s\n\033[39;49;0m" "  - Login Status:" "[Warning]"
   echo "[Warning]" 1> ./script/output/logstaresult
   printf "%-60s\033[37;49;1m\n\033[39;49;0m" "    * The result is in the ./loginf" 
   echo "Login Status Suggestion:" >> ./script/suggestion/suggestion
   echo "  *登录状态中，含有非当前用户登录状态，请检查登录异常报告" >> ./script/suggestion/suggestion
else
   printf "%-60s\033[32;49;1m%10s\n\033[39;49;0m" "  - Login Status:" "[OK]"
   echo "[OK]" 1> ./script/output/logstaresult
fi
echo -e "\n---------------------------------------------------------------------------------------------\n"