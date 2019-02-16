#!/bin/sh
echo -e "\033[34;49;1m[+] Firewall detection \033[39;49;0m"
echo -e "------------------------------------"
touch ./script/output/wallresult
touch ./script/suggestion/filesuggestion
echo "FIle Access and FireWalls suggestions:" 1> ./script/suggestion/filesuggestion
RulesNum=$(sudo iptables -nL |grep -E -v "^(Chain|target|$)" |wc -l)
Rules=$(sudo iptables -nL |grep -E -v "^(Chain|target|$)")
if [ ${RulesNum} -le 5 ]; then
	printf "%-60s\033[31;49;1m%10s\n\033[39;49;0m" "  - Iptables Rules Numbers less than 5:" "[Warning]"
	echo "[Warning]" 1> ./script/output/wallresult
	echo "Iptables Suggestion:" 1>> ./script/suggestion/filesuggestion
	echo "  *增加Iptables的规则" 1>> ./script/suggestion/filesuggestion
else
	printf "%-60s\033[32;49;1m%10s\n\033[39;49;0m" "  - Number of rules is enough:" "[OK]"
	echo "[OK]" 1> ./script/output/wallresult
fi

printf "%-60s\033[32;49;1m%10s\n\033[39;49;0m" "  - Defense syn flood :" "[OK]"
echo "[OK]" 1>> ./script/output/wallresult

mychain=$(sudo iptables -nL |grep -E "^(Chain|$)" |grep -E -v "(INPUT|OUTPUT|FORWARD)" | awk '{ print $2 }')
if [ -z ${mychain} ]; then
	echo "   [-] Recommend to create a independ chain besides of default"
	echo "Recommend to create a independ chain besides of default\n" 1>> ./script/suggestion/filesuggestion
fi

outputDefault=$(sudo iptables -L OUTPUT |grep -E "policy" |awk '{ print  $4}' |cut -c 1-4)
if [ $outputDefault = "DROP" ]; then	
	echo "   [+] OUTPUT Chain default rule is DROP" 1>> ./script/suggestion/filesuggestion
	echo "   [+] OUTPUT Chain default rule is DROP"
else
	echo "   [-] OUTPUT Chain default rule recommended to be DROP"
	echo "   [-] OUTPUT Chain default rule recommended to be DROP" 1>> ./script/suggestion/filesuggestion
fi


inputDefault=$(sudo iptables -L INPUT |grep -E "policy" |awk '{ print  $4}' |cut -c 1-4)
if [ $inputDefault = "DROP" ]; then
	echo "   [+] INPUT Chain default rule is DROP\n"
	echo "   [+] INPUT Chain default rule is DROP\n" 1>> ./script/suggestion/filesuggestion
else
	echo "   [-] INPUT Chain default rule recommended to be DROP"
	echo "    After set DROP then you should allow a range of IP address or a specific IP address"
	echo "   [-] INPUT Chain default rule recommended to be DROP" >> ./script/suggestion/filesuggestion
	echo "    After set DROP then you should allow a range of IP address or a specific IP address\n" 1>> ./script/suggestion/filesuggestion
fi

timelimit=0
for i in ${Rules}; do
	if [ ${i} = "limit:" ];then
		timelimit=1
		break
	fi
done
if [ $timelimit -eq 1 ]; then
	printf "%-60s\033[32;49;1m%10s\n\033[39;49;0m" "  - SYN flood defense OK:" "[OK]"
	echo "[OK]" 1>> ./script/output/wallresult
	
else
	printf "%-60s\033[31;49;1m%10s\n\033[39;49;0m" "  - Limit Package:" "[Warning]"
	echo "[Warning]" 1>> ./script/output/wallresult
	echo "   [-] Not limit package which may cause dos attack" 1>>./script/suggestion/filesuggestion
fi

echo -e "\n---------------------------------------------------------------------------------------------\n"
