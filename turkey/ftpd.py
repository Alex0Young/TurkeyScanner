import os, sys, re, socket, time
from ftplib import FTP
import ftplib

def usage():
    print ('+' + '-' * 50 + '+')
    print ('\t   FTP Weak Password Detection Tool')
    print ('+' + '-' * 50 + '+')

def Login(warning, host, username, password):
    ftp = FTP()

    try:
        ftp.connect(host, 2121, 1)
        ftp.login(username, password)
        ftp.retrlines('LIST')
        ftp.quit()
        inn = 'user:' + username + '，pass:' + password + '\n'
        nin = '发现弱口令，建议及时更改密码以保证系统安全！\n'
        fw = open('script/suggestion/ftpsuggestion', 'w')
        fw.write("FTP:\n"+nin + '\n' + inn)
        fw.close()
        print('[-] Weak password.\n')
        warning += 1
#        exit()
        return warning
    except ftplib.all_errors:
        pass
    print('[+] Congratulations! No Weak Password.\n')
#    exit()
    return warning


def main():
    usage()
    warning = 0
    host = "127.0.0.1"
    userlist = [i.rstrip() for i in open("initial/user.txt")]
    passlist = [j.rstrip() for j in open("initial/pass.txt")]
    for x in userlist:
        for j in passlist:
            warning = Login(warning,host, x, j)
    fw = open('script/output/ftpresult', 'w')
    if warning > 0:
        out = '[Warning]\n'
    else:
        out = '[OK]\n'
    fw.write(out)
    fw.close()
