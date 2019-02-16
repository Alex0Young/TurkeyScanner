#!/bin/bash
echo -e "\033[34;49;1m[+] File Access scan \033[39;49;0m"
echo -e "------------------------------------"
#re ip -> grep -o "[0-9]\{1,3\}[.][0,9]\{1,3\}[.][0-9]\{1,3\}[.][0-9]\{1,3\}[.:][0-9]\{1,5\}" file
touch ./script/output/fileaccess
touch ./script/output/fileresult
echo "start scan file Permission! ..."
printf "%-60s\033[32;49;1m%10s\n\033[39;49;0m" "  - ALL Rights Resvered!" "[OK]"
echo "[OK]" 1> ./script/output/fileresult

echo "start scan /etc ... "
_fileN640_=$(find /etc ! -perm 640 ! -perm 600 ! -perm 644 -type f -exec ls -l {} \; 2>/dev/null)
fileN640=$(echo "${_fileN640_}" | awk '{ print "[-]"$9 ": " $1 "\n     perms recommanded to be 640!"}')
echo "${fileN640}" 1 > ./script/output/fileaccess
printf "%-60s\033[32;49;1m%10s\n\033[39;49;0m" "  - etc scan finfished!" "[OK]"
echo "[OK]" 1>> ./script/output/fileresult

echo "start scan /root ... "
_fileN640_=$(find /etc ! -perm 640 ! -perm 600 ! -perm 644 -type f -exec ls -l {} \; 2>/dev/null)
fileN640=$(echo "${_fileN640_}" | awk '{ print "[-]"$9 ": " $1 "\n     perms recommanded to be 640!"}')
echo "${fileN640}" 1>> ./script/output/fileaccess
printf "%-60s\033[32;49;1m%10s\n\033[39;49;0m" "  - root scan finished!" "[OK]"
echo "[OK]" 1>> ./script/output/fileresult

echo "start scan /usr ... "
_fileN640_=$(find /usr/lib /usr/lib32 /usr/libx32 /usr/src ! -perm 640 ! -perm 600 ! -perm 644 -type f -exec ls -l {} \; 2>/dev/null)
fileN640=$(echo "${_fileN640_}" | awk '{ print "[-]"$9 ": " $1 "\n     perms recommanded to be 640!"}')
echo "${fileN640}" 1> ./script/output/fileaccess
printf "%-60s\033[32;49;1m%10s\n\033[39;49;0m" "  - usr scan finfished!" "[OK]"
echo "[OK]" 1>> ./script/output/fileresult

echo "start scan log | pem | crt | key | file  ... "
_filePem_=$(find /proc -type f ! -perm 444 ! -perm 440 -path /proc/sys/net/* -exec ls -l {} \; 2>/dev/null | grep -E -i '*.log$|*.pem$|*.key$|*.crt$')
filePem=$(echo "${_filePem_}" | awk '{ print "[-]"$9 ": " $1 "\n     perms recommended to be 444 or 440" }')
echo "${filePem}"
_filePem_=$(find /proc/sys/net -type f ! -perm 644 ! -perm 640 ! -perm 600 ! -perm 444 ! -perm 440 -exec ls -l {} \; 2>/dev/null |grep -E -i '*.log$|*.pem$|*.key$|*.crt$')
filePem=$(echo "${_filePem_}" | awk '{ print "[-]"$9 ": " $1 "\n     perms recommende to be 640 or lower" }')
echo "${filePem}" 1> ./script/output/fileaccess
printf "%-60s\033[32;49;1m%10s\n\033[39;49;0m" "  - special file scan finished!" "[OK]"
echo "[OK]" 1>> ./script/output/fileresult
printf "%-60s\033[37;49;1m\n\033[39;49;0m" "    * The result is in the ./output/fileaccess"

echo -e "\n---------------------------------------------------------------------------------------------\n"