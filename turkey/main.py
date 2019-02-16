#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re
import time

from config import *

now_path = os.getcwd()

#生成html文件
def genhtml(html_name,html_message):
    #if os.path.exists(html_name):
        # 删除文件，可使用以下两种方法。
        #os.remove(html_name)
    try:
        f = open(html_name, 'w')
        message = html_message
        f.write(message)
        f.close()
        return True
    except Exception as error:
        print(error)
        return False

#赋予sh文件执行权限
def give_authetication():
    now_path = os.getcwd()

    for root, dirs, files in os.walk(now_path):
        for name in files:
            file_name = root+'/'+name
            if re.match('(.*)\.sh',file_name):
                os.system("chmod +x "+file_name)

# 主函数选择器
def user_choice(flag):
    while(flag):
        wrong_commend_list = []
        input_func_list = []
        input_hk_list = []

        ori_input = raw_input('Please input your choice:\n')
        # print ori_input
        commends = re.split('\W+', ori_input)

        #分开输入的类型：错误输入，热键输入，功能键输入
        for commend in commends:
            if commend not in commends_list:
                wrong_commend_list.append(commend)
            if commend in functions_list:
                input_func_list.append(commend)
            if commend in hot_keys_list:
                input_hk_list.append(commend)

        #判断分类长度，伪自动机
        if len(wrong_commend_list) == 0:
            if len(input_hk_list) > 0 and len(input_func_list)>0:
                print(wrong_much_key_prompt)

            elif len(input_hk_list) > 0 and len(input_func_list) == 0:
                if len(input_hk_list) == 1:
                    if input_hk_list[0] == 'i':
                        print(information)
                    elif input_hk_list[0] == 'q':
                        os._exit(0)
                elif len(input_hk_list) > 1:
                    print(wrong_much_hk_prompt)

            elif len(input_hk_list) == 0 and len(input_func_list) > 0:
                if 'a' in input_func_list:
                    commends = ['a']
                flag = 0
        else:
            print(wrongtime_prompt)

    return  commends


#系统开启端口检查
def portscanner():
    print("port_scanner")
    out = os.system(now_path+"/script/VM_unsafePort.sh")
    print(out)

#系统弱密钥检查
def weakpass_detect():
    print("weakpass_detect")
    import mysql_check
    mysql_check.main()

    import ftpd
    ftpd.main()

#系统关键文件配置检查
def sysconfig_check():
    print("sysconfig_check")
    out = os.system(now_path+"/script/config.sh")
    print(out)

#系统CPU等配置检查
def memory_check():
    print("memory_check")
    out = os.system(now_path+"/script/osinfo.sh")
    print(out)

# 系统其他项目检测
def system_detection():
    print("sys_detection")
    out1 = os.system(now_path + "/script/service.sh")
    print(out1)
    #out2 = os.system(now_path + "/script/VM_debugModel.sh")
    #print(out2)
    out3 = os.system(now_path + "/script/ssh.sh")
    print(out3)
    out4 = os.system(now_path + "/script/VM_Process.sh")
    print(out4)
    out5 = os.system(now_path + "/script/VM_CertificateInLog.sh")
    print(out5)
    out6 = os.system(now_path + "/script/loginstatus.sh")
    print(out6)

#文件权限&防火墙管理检查
def file_wall_check():
    print("file_wall_check")
    out1 = os.system(now_path+"/script/firewalls.sh")
    print(out1)
    out2 = os.system(now_path+"/script/bash1.sh")
    print(out2)




if __name__ == '__main__':

    flag = 1

############################################################################################

    print(logo)
    print(information)

    give_authetication() #给所有文件执行权限

    commends = user_choice(flag) #主函数选择循环

#------------------------------判断执行哪些sh文件-------------------------------------------------
    try:
        if 'a' in commends:
            portscanner()
            sysconfig_check()
            memory_check()
            system_detection()
            file_wall_check()
            weakpass_detect()

        if 'p' in commends:
            portscanner()

        if 's' in commends:
            sysconfig_check()

        if 'm' in commends:
            memory_check()

        if 'd' in commends:
            system_detection()

        if 'f' in commends:
            file_wall_check()

        if 'w' in commends:
            weakpass_detect()

    except Exception as error:
        print(error)

#-----------------------------判断生成哪些html文件------------------------------------------------
    port_scanner = "report/port_scanner.html"
    weak_check = "report/weak_check.html"
    file_check = "report/file_check.html"
    sys_config = "report/sys_config.html"
    system_check = "report/system_check.html"
    system_detect = "report/system_detect.html"

    import web_config

    try:
        if 'a' in commends:
            port_res = genhtml(port_scanner, web_config.port_scanner_demo)
            weak_res = genhtml(weak_check, web_config.weak_check_demo)
            file_res = genhtml(file_check, web_config.file_check_demo)
            config_res = genhtml(sys_config, web_config.sysconfig_check_demo)
            syscheck_res = genhtml(system_check, web_config.sys_check_demo)
            sysdetect_res = genhtml(system_detect, web_config.sys_detect_demo)
        else:
            if 'p' in commends:
                port_res = genhtml(port_scanner,web_config.port_scanner_demo)
                pass
            else:
                port_res = genhtml(port_scanner,web_config.port_none_demo)

            if 'w' in commends:
                weak_res = genhtml(weak_check, web_config.weak_check_demo)
                pass
            else:
                weak_res = genhtml(weak_check,web_config.weak_none_demo)

            if 's' in commends:
                config_res = genhtml(sys_config, web_config.sysconfig_check_demo)
            else:
                config_res = genhtml(sys_config,web_config.sysconfig_none_demo)

            if 'm' in commends:
                syscheck_res = genhtml(system_check, web_config.sys_check_demo)
            else:
                syscheck_res = genhtml(system_check, web_config.syscheck_none_demo)

            if 'd' in commends:
                sysdetect_res = genhtml(system_detect, web_config.sys_detect_demo)
            else:
                sysdetect_res = genhtml(system_detect, web_config.sysdetect_none_demo)

            if 'f' in commends:
                file_res = genhtml(file_check, web_config.file_check_demo)
            else:
                file_res = genhtml(file_check, web_config.file_none_demo)


    except Exception as genhtml_error:
        print(genhtml_error)


