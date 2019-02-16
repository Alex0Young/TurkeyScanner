import socket
import time
import _thread

class Port(object):
    def __init__(self):
        pass

    def __getitem__(self, item):
        pass

    def __setitem__(self, key, value):
        pass

    def Field(self,port,status,service,warning_class):
        try:
            assert type(port) is int, "the port should be int!"
            assert type(status) is str, "the status should be string!"
            assert type(service) is str, "the service should be string!"
            assert type(warning_class) is str, "the warning_class should be string!"
            self.port = port
            self.status = status
            self.service = service
            self.warning_class = warning_class
            return True
        except Exception as error:
            print(error)
            return False


class PortScanner(object):
    lock = _thread.allocate_lock()
    socket.setdefaulttimeout(3)

    def __init__(self):
        self.single_port = 0
        self.target_start_port = 0
        self.target_end_port = 65534
        self.target_ip = ''
        self.black_dict = {31 : ['Trojan - Master Paradise or Hackers Paradise','high'],
                           5554 : ['worm.Sasser病毒','high'],
                           7626 : ['冰河病毒','high'],
                           8011 : ['WAY2.4病毒','high'],
                           7306 : ['Netspy3.0病毒','high'],
                           1024 : ['YAI病毒','middle']

                           }
        self.port_dict = {'0' : 'Reserved',
                          '1' : 'tcpmux',
                          '7' : 'Echo',
                          '19' : 'Character Generator',
                          '21' : 'Ftp',
                          '22' : 'Ssh',
                          '23' : 'Telnet',
                          # '24' : 'Private mail-system',
                          '25' : 'SMTP',
                          '31' : 'MSG Authentication',
                          # '33' : 'Display Support Protocol',
                          # '35' : 'Private printer server',
                          # '37' : 'Time',
                          # '38' : 'Route Access Protocol',
                          # '39' : 'Resource Location Protocol',
                          # '41' : 'Graphics',
                          '42' : 'WINS Replication',
                          # '43' : 'Who is',
                          # '44' : 'MPM FLAGS Protocol',
                          # '45' : 'Message Processing Module',
                          # '46' : 'MPM-snd',
                          # '47' : 'ni-ftp',
                          # '48' : 'Digital Audit Daemon',
                          # '49' : 'Login Host Protocol',
                          # '50' : 'Remote Mail Checking Protocol',
                          # '51' : 'IMP Logical Address Maintenance',
                          '53' : 'Domain Name Server（DNS）',
                          '57' : 'Private terminal access',
                          '59' : 'Private file service',
                          '61' : 'NI Mail',

                          '67' : 'Bootstrap Protocol Server',
                          '69' : 'Trival File Transfer',
                          '79' : 'Finger Server',
                          '80' : 'HTTP',
                          '99' : 'Metagram Relay',
                          '102' : 'Message transfer agent(MTA)-X.400 over TCP/IP',
                          '109' : 'Post Office Protocol -Version3',
                          '110' : 'SUN公司的RPC服务所有端口',
                          '113' : 'Authentication Service',
                          '119' : 'Network News Transfer Protocol',
                          '135' : 'Location Service',
                          '137' : 'NETBIOS Name Service',
                          '138' : 'NETBIOS Name Service',
                          '139' : 'NETBIOS Name Service',
                          '143' : 'Interim Mail Access Protocol v2',
                          '161' : 'SNMP',
                          '177' : 'X Display Manager Control Protocol',
                          '389' : 'LDAP、ILS',
                          '443' : 'Https',
                          '456' : '[NULL]',
                          '513' : 'Login,remote login',
                          '544' : 'kerberos kshell',
                          '548' : 'Macintosh,File Services(AFP/IP)',
                          '553' : 'CORBA IIOP （UDP）',
                          '555' : 'DSF',
                          '568' : 'Membership DPA',
                          '569' : 'Membership MSN',
                          '635' : 'mountd',
                          '636' : 'LDAP',
                          '666' : 'Doom Id Software',
                          '993' : 'IMAP',
                          # '1001' : '[NULL]',
                          # '1011' : '[NULL]',
                          '1024' : 'Reserved',
                          '1025' : 'network blackjack',
                          # '1033' : '[NULL]',
                          '1080' : 'SOCKS',
                          # '1170' : '[NULL]',
                          # '1234' : '[NULL]',
                          # '1243' : '[NULL]',
                          # '6776' : '[NULL]',
                          # '6711' : '[NULL]',
                          # '1245' : '[NULL]',
                          '1433' : 'SQL',
                          '1492' : 'stone-design-1',
                          '1500' : 'RPC client fixed port session queries',
                          '1503' : 'NetMeeting T.120',
                          '1524' : 'ingress',
                          '1600' : 'issd',
                          '1720' : 'NetMeeting',
                          '1731' : 'NetMeeting Audio Call Control',
                          '1807' : '***warning*** (SpySender)',
                          '1981' : '***warning*** (ShockRave)',
                          '1999' : 'cisco identification port',
                          '2000' : '***warning*** (GirlFriend 1.3,Millenium 1.0)',
                          '2001' : '***warning*** (Millenium 1.0、Trojan Cow)',
                          '2023' : '***warning*** (Pass Ripper)'
                          ''

                            }

    def get_host_ip(self):
        """
        查询本机ip地址
        :return: ip
        """
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            ip = s.getsockname()[0]
        finally:
            s.close()

        return ip
    #-------------------------------------------------------------------------------------------
    def Ports_Inital(self,ip,start_port,end_port):    #初始化目标ip地址，起始端口和终止端口。默认为0-65534
        try:
            if isinstance(ip,str):
                self.target_ip = str(ip)
            if isinstance(start_port,int) and int(start_port) >= 0:
                self.target_start_port = int(start_port)
            if isinstance(end_port,int) and int(end_port) <= 65534:
                self.target_end_port = int(end_port)
            return True

        except Exception as error:
            print(error)
            return False

    def socket_port(self, ip, port):
        """
        输入IP和端口号，扫描判断端口是否开放
        """
        try:
            print("now the port is: " + str(port))
            if port >= 65535:
                print("端口扫描结束")
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = s.connect_ex((ip, port))
            if result == 0:
                self.lock.acquire()
                print(ip, u':', port, u'端口开放')
                self.lock.release()
            s.close()
        except Exception as error:
            print("端口扫描异常:" + str(error))

    def Ports_Scan(self):
        """
        输入IP，扫描IP的0-65534端口情况
        """
        try:
            print(u'开始扫描 %s' % self.target_ip)
            start_time = time.time()
            for i in range(self.target_start_port,self.target_end_port):
                _thread.start_new_thread(self.socket_port, (self.target_ip, int(i)))
                time.sleep(0.001)
            time.sleep(3)
            print(u'扫描端口完成，总共用时 ：%.2f' % (time.time() - start_time))
            return True
        except Exception as error:
            print(error)
            return False

    #-------------------------------------------------------------------------------------------

    def Port_Initial(self,ip):
        try:
            if isinstance(ip,str):
                self.target_ip = ip
            return True

        except Exception as error:
            print(error)
            return False

    def Port_Scan(self,single_port=0):
        if isinstance(single_port, int) and single_port in range(0, 65535):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = s.connect_ex((self.target_ip, single_port))
            if result == 0:
                print(self.target_ip, u':', single_port, u'端口开放')

    #------------------------------------------------------------------------------------------




#
# ps = PortScanner()
# a = ps.Ports_Inital(ip="10.8.173,145",start_port=0,end_port=1000)
# d = ps.Ports_Scan()

# b = ps.Port_Initial(ip="127.0.0.1")
# c = ps.Port_Scan(631)

# p = Port()
# m = p.Field(port=22,status="open",service="unknown",warning_class="high")
# if m:
#     print(p.port)








