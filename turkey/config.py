#!/usr/bin/python
# -*- coding: utf-8 -*-

logo = (
    ' /—————————/  /-/      /-/  //————//   /-/ /-/     //——————/  \-\  /-/     \n'
    '/___   ___/  / /      / /  //____//   / / / /     //           \ \/ /      \n'
    '   / /      / /      / /  //\ \      / /-/ /     //——————/     /   /       \n'
    '  / /      / /______/ /  //  \ \    / /  \ \    //            /   /        \n'
    ' /_/      /__________/  //    \_\  /_/    \_\  //——————/     /___/         \n')

information = (
    '[*] functions keys:\n'
    '    p : port scan\n'
    '    w : Weak password check\n'
    '    s : system config check\n'
    '    m : memory information check\n'
    '    d : system detection\n'
    '    f : file permission check and firewall check\n'
    '    a : Do all detections\n'
    '[*] hot keys:\n'
    '    i : show information\n'
    '    q : quit the process\n'
    '[**] format:\n'
    '    (1)please input a space(or ,) between two commends(p m...)\n'
    '    (2)you can only input one type of keys one time\n'
    '    (3)you can only input one hot key one time\n')

wrongtime_prompt = ("[*] Unknown commend, please input again\n"
                    "-----------------------------------------")

wrong_much_key_prompt = ("[*] too much type of keys, please input again\n"
                         "-----------------------------------------")

wrong_much_hk_prompt = ("[*] too much hot keys, please input again\n"
                        "-----------------------------------------")

commends_list = ['p', 'w', 's', 'm', 'f', 'a', 'i', 'q','d']
functions_list = ['p', 'w', 's', 'm', 'f', 'a','d']
hot_keys_list = ['i', 'q']