
echo -e "\033[34;49;1m[+] SSH Detection \033[39;49;0m"
echo -e "------------------------------------"
touch ./script/output/sshresult
if ps -ef | grep ssh | egrep -v "grep" 1> ./script/output/sshtest ;then
	printf "%-60s\033[32;49;1m%10s\n\033[39;49;0m" "  - SSH Server:" "[Found]"
	echo "[Found]" 1> ./script/output/sshresult
else
	printf "%-60s\033[37;49;1m%10s\n\033[39;49;0m" "  - SSH Server:" "[Not Found]"
	echo "[Not Found]" 1> ./script/output/sshresult
fi


if find /etc/ssh/ssh_config 1> ./script/output/sshtest ; then
	printf "%-60s\033[32;49;1m%10s\n\033[39;49;0m" "  - SSH Configuration:" "[Found]"
	echo "[Found]" 1>> ./script/output/sshresult
else
	printf "%-60s\033[31;49;1m%10s\n\033[39;49;0m" "  - SSH Configuration:" "[Not Found]"
	echo "[Not Found]" 1>> ./script/output/sshresult
	echo "SSH Configuration Suggestion:" >> ./script/suggestion/suggestion
	echo "  *你必须设置SSH Config文件" >> ./script/suggestion/suggestion
fi

curport=`grep Port /etc/ssh/ssh_config | awk -F'=' '{print $1}' | awk '{ print $3 }'`
if [ "${curport}" = "22" ]; then
	printf "%-60s\033[31;49;1m%10s\n\033[39;49;0m" "  - SSH Port is 22:" "[Warning]"
	echo "[Warning]" 1>> ./script/output/sshresult
	echo "SSH Port Suggestion:" >> ./script/suggestion/suggestion
	echo "  *将SSH端口设置为非22且大于1024的端口，可降低被扫描器扫描的几率" >> ./script/suggestion/suggestion
else
	printf "%-60s\033[32;49;1m%10s\n\033[39;49;0m" "  - SSH Port is not 22:" "[OK]"
	echo "[Ok]" 1>> ./script/output/sshresult
fi

curpro=`grep Protocol /etc/ssh/ssh_config | awk -F'=' '{print $1}' | awk '{ print $3 }'`
if [ "${curpro}" = "2" ]; then
	printf "%-60s\033[32;49;1m%10s\n\033[39;49;0m" "  - SSH Protocol is 2:" "[OK]"
	echo "[Ok]" 1>> ./script/output/sshresult
else 
	printf "%-60s\033[31;49;1m%10s\n\033[39;49;0m" "  - SSH Protocol is not 2:" "[Warning]"
	echo "[Warning]" 1>> ./script/output/sshresult
	echo "SSH Protocol Suggestion:" >> ./script/suggestion/suggestion
	echo "  *使用SSH2协议更加安全，SSH1协议会被攻击" >> ./script/suggestion/suggestion
fi

curper=`grep PermintRootLogin /etc/ssh/ssh_config | awk -F'=' '{print $1}' | awk '{ print $3 }'`

if [ "$curper" = "yes" ]; then
	printf "%-60s\033[34;49;1m%10s\n\033[39;49;0m" "  - SSH Permit Root Login:" "[Suggestion]"
	echo "[Suggestion]" 1>> ./script/output/sshresult
	echo "SSH Permition Suggestion:" >> ./script/suggestion/suggestion
	echo "  *不允许root用户登录，可以防止非法登录造成不必要的风险" >> ./script/suggestion/suggestion
elif [ "$curper" = "no" ];then
	printf "%-60s\033[32;49;1m%10s\n\033[39;49;0m" "  - SSH Not Permit Root Login:" "[OK]"
	echo "[Ok]" 1>> ./script/output/sshresult
else
	printf "%-60s\033[37;49;1m%10s\n\033[39;49;0m" "  - SSH Permit Root Login:" "[Not Found]"
	echo "[Not Found]" 1>> ./script/output/sshresult
fi

curban=`grep Banner /etc/ssh/ssh_config | awk -F'=' '{print $1}' | awk '{ print $1 }'`
curban1=`grep Banner /etc/ssh/ssh_config | awk -F'=' '{print $1}' | awk '{ print $2 }'`
if [ "$curban" = "#" ]; then
	printf "%-60s\033[34;49;1m%10s\n\033[39;49;0m" "  - SSH Banner is close:" "[Suggestion]"
	echo "[Suggestion]" 1>> ./script/output/sshresult
	echo "SSH Banner Suggestion:" >> ./script/suggestion/suggestion
	echo "  *让任何连接到你SSH服务的用户看到一条特殊的消息,可显示注意信息" >> ./script/suggestion/suggestion
elif [ "$curban1" = "Banner" ]; then
	printf "%-60s\033[32;49;1m%10s\n\033[39;49;0m" "  - SSH Banner is open:" "[OK]"
	echo "[OK]" 1>> ./script/output/sshresult
else
	printf "%-60s\033[37;49;1m%10s\n\033[39;49;0m" "  - SSH Banner not find:" "[Not Found]"
	echo "[Not Found]" 1>> ./script/output/sshresult
fi

curpub=`grep RSAAuthentication /etc/ssh/ssh_config | awk '{print $1$2}' | egrep -v "RhostsRSAAuthentication"`
curpub1=`grep RSAAuthentication /etc/ssh/ssh_config | awk '{print $2}' | egrep -v "RhostsRSAAuthentication"`

if [ "$curpub" = "#RSAAuthentication" ]; then
	printf "%-60s\033[34;49;1m%10s\n\033[39;49;0m" "  - SSH RSAAuthentication is close:" "[Suggestion]"
	echo "[Suggestion]" 1>> ./script/output/sshresult
	echo "SSH RSAAuthentication Suggestion:" >> ./script/suggestion/suggestion
	echo "  *公钥认证登录，可以防止字典攻击弱密钥" >> ./script/suggestion/suggestion
elif [ "$curpub1" = "RSAAuthentication" ]; then
	printf "%-60s\033[32;49;1m%10s\n\033[39;49;0m" "  - SSH RSAAuthentication is open:" "[OK]"
	echo "[OK]" 1>> ./script/output/sshresult
else
	printf "%-60s\033[37;49;1m%10s\n\033[39;49;0m" "  - SSH RSAAuthentication not find:" "[Not Found]"
	echo "[Not Found]" 1>> ./script/output/sshresult
fi

curdeny=`grep "sshd: ALL" /etc/hosts.deny | awk '{print $1$2}'`
curallow=`grep sshd: /etc/hosts.allow | awk '{print $1$2}'`

if [ -z $curdeny ]; then
	printf "%-60s\033[34;49;1m%10s\n\033[39;49;0m" "  - SSH TCP Wrappers is close:" "[Suggestion]"
	echo "[Suggestion]" 1>> ./script/output/sshresult
	echo "SSH TCP Wrappers Suggestion:" >> ./script/suggestion/suggestion
	echo "  *仅允许特定ip登录，防止非法IP登录" >> ./script/suggestion/suggestion
else
	printf "%-60s\033[32;49;1m%10s\n\033[39;49;0m" "  - SSH TCP Wrappers is open:" "[OK]"
	echo "[Ok]" 1>> ./script/output/sshresult
fi

echo -e "\n---------------------------------------------------------------------------------------------\n"






