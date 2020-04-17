import netaddr,file_operation
import socket
from scapy.all import *

def port_s(ip,port):



    class receive_package(object):
        def __init__(self, l_ip, d_ip, o_p_l, c_p_l, c_port=None):
            self.port = c_port
            self.open_port_list1 = o_p_l
            self.close_port_list1 = c_p_l
            self.local_ip1 = l_ip
            self.destination_ip1 = d_ip
            self.all_port = []
            self.all_status = []

        def prn(self, pkt):
            flags = pkt.sprintf("%TCP.flags%")
            final_port = pkt.sprintf("%IP.sport%")
            if flags == 'SA':
                # print(pkt.sprintf("[+]%IP.src%:%IP.sport% opend"))
                self.open_port_list1.append(final_port)
            else:
                # print(pkt.sprintf("[-]%IP.src%:%IP.sport% closed"))
                self.close_port_list1.append(final_port)

        def run(self):
            sniff(
                lfilter=lambda x: x.haslayer(TCP) and x[IP].dst == self.local_ip1 and x[IP].src == self.destination_ip1 and x[
                    TCP].flags == 'SA'
                                  or
                                  x.haslayer(TCP) and x[IP].dst == self.local_ip1 and x[IP].src == self.destination_ip1 and x[
                                      TCP].flags == 'RA'
                , prn=self.prn, timeout=30)

        def output(self):

            print('[+]The follow is "Port Scan" report for \'{0}\' :'.format(self.destination_ip1))

            print('[+]The opend port:')
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

            for i in self.open_port_list1:
                if i in self.port:
                    self.port.remove(i)
            for i in self.close_port_list1:
                if i in self.port:
                    self.port.remove(i)
            print('[+]The filtered port:')
            if not self.port:
                print('None')
            for p in self.port:
                print('--->'+str(p) + ' filtered')
                self.all_port.append(p)
                self.all_status.append('filtered')

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
    port1 = []
    if  port:
        for i in port:
            port1.append(int(i))
    else:
        port1 = [22, 80, 443, 445, 21, 23 ,8080, 3389, 1433, 3306]
    local_ip = get_host_ip()
    ipArray = []
    open_port_list = []
    close_port_list = []
    # portArray = [port1[i:i + 3] for i in range(0, len(port1), 3)]
    portArray = port1
    print(portArray)

    for i in _ip:   # data processing
        ipArray.extend([str(i) for i in  netaddr.IPNetwork(i)])

    for i in ipArray:   # send package
        for j in portArray:
            send(IP(dst=i)/TCP(dport=j, flags=2), verbose=False)

    for i in _ip:
        demo = receive_package(l_ip=local_ip, d_ip=i, o_p_l=open_port_list, c_p_l=close_port_list, c_port=portArray)
        demo.run()
        demo.output()
        final_port.extend(demo.all_port)
        final_state.extend(demo.all_status)

    file_operation.file_operate(ip,final_port,final_state,'port')

# port_s(['39.156.66.14'],['80'])
