result = []

try:
    import pymysql
except ImportError:
    print ('\n[!] MySQLdb module import error')
    exit()


def usage():
    print ('+' + '-' * 50 + '+')
    print ('\t   MySQL Weak Password Detection Tool')
    print ('+' + '-' * 50 + '+')


def mysql_brute(user, password):
    host = "127.0.0.1"
    # print("1234")
    db = None
    try:
        # print "user:", user, "password:", password
        db = pymysql.connect(host=host, user=user, passwd=password, db="mysql", port=3306)
        # print '[-] Weak password：', user, password
        result.append('user：' + user + "\tpass：" + password)
    except KeyboardInterrupt:
        print ('exit')
        exit()
    except pymysql.Error:
        pass
    finally:
        if db:
            db.close()


def main():
    usage()
    inn = None
    userlist = [i.rstrip() for i in open("initial/user.txt")]
    passlist = [j.rstrip() for j in open("initial/pass.txt")]

    for x in userlist:
        for j in passlist:
            mysql_brute(x, j)
    if len(result) != 0:
        print('[-] Weak password.\n')
        fw = open("script/output/mysqlresult", 'w')
        fw.write('[Warning]\n')
        fw.close()
        inn = 'Mysql:\n'+'发现弱口令，建议及时更改密码以保证系统安全！\n'
        fw = open("script/suggestion/mysqlsuggestion", 'w')
        fw.write(inn)
        for x in {}.fromkeys(result).keys():
            out = x + '\n'
            #	print out
            fw = open("script/suggestion/mysqlsuggestion", 'a+')
            fw.write(out)
            fw.close()
        fw.close()
    else:
        print('[+] Congratulations. No weak password.\n')
        fw = open("script/output/mysqlresult", 'w')
        fw.write("[OK]\n")
        fw.close()
