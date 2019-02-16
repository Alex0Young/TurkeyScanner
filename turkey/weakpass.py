# -*- coding: utf-8 -*-

import crypt   ##导入Linux口令加密库
def testPass(cryptPass):
    salt=cryptPass[cryptPass.find("$"):cryptPass.rfind("$")]  ##获得盐值，包含$id部分
    dictFile=open('key.txt','r')
    for word in dictFile.readlines():
        word=word.strip("\n")
        cryptWord=crypt.crypt(word,salt)                   ##将密码字典中的值和盐值一起加密
        if (cryptWord==cryptPass):                           ##判断加密后的数据和密码字段是否相等
            print "[+]发现弱密钥："+word+"\n"       ##如果相等则打印出来
            return 
    print "[-] 未发现弱密钥。\n"
    return 
 
def main():
    passFile=open('/etc/shadow')
    for line in passFile.readlines():      ##读取文件中的所有内容
        if ":" in line:
            user=line.split(":")[0]                     ##获得用户名
            cryptPass=line.split(":")[1].strip(' ')   ##获得密码字段
            print "[*] 检查用户"+user+"的弱密钥："
            testPass(cryptPass)
main()
 


