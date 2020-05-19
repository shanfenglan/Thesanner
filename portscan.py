import netaddr,file_operation
import socket
from scapy.all import *

def port_s(ip,port):

    class receive_package(object):
        def __init__(self, l_ip, d_ip, o_p_l, c_p_l, c_port=None, nameee = None):
            self.port = c_port
            self.open_port_list1 = o_p_l
            self.close_port_list1 = c_p_l
            self.local_ip1 = l_ip
            self.destination_ip1 = d_ip
            self.all_port = []
            self.all_status = []
            self.namee = nameee

        def prn(self, pkt):
            flags = pkt.sprintf("%TCP.flags%")
            final_port = pkt.sprintf("%IP.src%:%IP.sport%")
            pppport = pkt.sprintf("%IP.sport%")
            if flags == 'SA':
                print(pkt.sprintf("[=====]%IP.src%:%IP.sport% opend"))
                self.open_port_list1.append(final_port)
            else:
                print(pkt.sprintf("[=====]%IP.src%:%IP.sport% closed"))
                self.close_port_list1.append(final_port)
            # self.port.remove(pppport)

        def run(self):
            tmo = len(self.destination_ip1) * (1/20) * len(self.port)

            # print(tmo)
            sniff(
                lfilter=lambda x: x.haslayer(TCP) and x[IP].dst == self.local_ip1 and x[IP].src in self.destination_ip1 and x[
                    TCP].flags == 'SA'
                                  or
                                  x.haslayer(TCP) and x[IP].dst == self.local_ip1 and x[IP].src in self.destination_ip1 and x[
                                      TCP].flags == 'RA'
                , prn=self.prn, timeout=tmo)

        def output(self):

            print('\n\n[+]The follow is "Port Scan" report for \'{0}\' :'.format(self.namee))

            print('\n[+]The opend port:')
            if not self.open_port_list1:
                print('None')
            for p in self.open_port_list1:
                print('--->'+str(p) + ' opend')
                self.all_port.append(p)
                self.all_status.append('opend')
            print('[+]The closed port:')
            if not self.close_port_list1:
                print('None')
            for p in self.close_port_list1:
                print('--->'+str(p) + ' closed')
                self.all_port.append(p)
                self.all_status.append('closed')


            # # print(self.open_port_list1)
            # for i in self.open_port_list1:
            #     if i in self.port:
            #         self.port.remove(i)
            # # print(port)
            # for i in self.close_port_list1:
            #     if i in self.port:
            #         self.port.remove(i)
            # print('[+]The filtered port:')
            # if not self.port:
            #     print('None')
            # # print(port)
            # for p in self.port:
            #     print('--->'+str(p) + ' filtered')
            #     self.all_port.append(p)
            #     self.all_status.append('filtered')

    def get_host_ip():
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            ip = s.getsockname()[0]
        finally:
            s.close()

        return ip



    final_port = []
    final_state = []

    _ip = ip
    # print(_ip)
    # print(type(_ip))
    port1 = []


    try:
        if len(port) == 1 and '-' in port[0]:
            g = int(port[0][0:1])
            c = int(port[0][2:]) + 1
            for i in range(g,c):
                port1.append(i)
        elif  port:
            for i in port:
                port1.append(int(i))
        else:
            port1 = [22, 80, 443, 445, 21, 23 ,8080, 3389, 1433, 3306]
    except:
        pass
    # print(port1)
    # port1 = [22, 80, 443, 445, 21, 23, 8080, 3389, 1433, 3306]

    local_ip = get_host_ip()
    ipArray = []
    open_port_list = []
    close_port_list = []
    portArray = [port1[i:i + 3] for i in range(0, len(port1), 3)]
    # portArray = port1
    # print(portArray)
    port2 = []
    for i in port1:
        port2.append(str(i))

    for i in _ip:   # data processing
        ipArray.extend([str(i) for i in netaddr.IPNetwork(i)])
    # print(ipArray)
    for i in ipArray:   # send package
        # print(i)
        for j in portArray:
            send(IP(dst=i)/TCP(dport=j, flags=2), verbose=False)

    demo = receive_package(l_ip=local_ip, d_ip=ipArray, o_p_l=open_port_list, c_p_l=close_port_list, c_port=port2,nameee = _ip)
    demo.run()
    demo.output()
    final_port.extend(demo.all_port)
    final_state.extend(demo.all_status)
    _ip = '$'+str(_ip)
    _ip = _ip.replace('/','\\')
    file_operation.file_operate(_ip,final_port,final_state,'port')


# port_s(['39.156.66.14/24'],['80'])
# port_s(['39.156.66.14','39.156.66.14','39.156.66.14','39.156.66.14','39.156.66.14','39.156.66.14','39.156.66.14'],['80'])
# port_s(['32.156.66.14'],['80'])
