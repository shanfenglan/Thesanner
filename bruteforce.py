import dns.resolver
import threading
import file_operation
import os

def bruteforce(domain,position,thread_number):
    domain = domain
    domain_list=[]
    pwd = position
    final_ip_list = []
    final_name_list = []
    thread = thread_number
    lock = threading.Semaphore(thread)
    thread_list = []

    with open(pwd,'r') as temporary_file:
        for i in temporary_file:
            i = i.strip()
            i = i+'.'+domain
            domain_list.append(i)


    def run(i):
        try:
            temporary_ip_list = []
            lock.acquire()
            A = dns.resolver.query(i)
            final_name_list.append(i)
            for i in A.response.answer:
                for j in i.items:
                    if j.rdtype == 1:
                        # print(j.address)
                        aaa = ' < ' + str(j.address) + ' > '
                        temporary_ip_list.append(aaa)

            # print(len(temporary_ip_list))
            if len(temporary_ip_list) != 1:

                temporary_date = ','.join(temporary_ip_list)
                # print(temporary_date)
                # print(type(temporary_date))
            else:
                temporary_date = str(temporary_ip_list[0])
            final_ip_list.append(temporary_date)
            # print(final_ip_list)
            # final_name_list.append(i)
            # print(final_name_list)
            lock.release()
        except dns.resolver.NXDOMAIN:
            pass

    for i in domain_list:
        # print(i)
        t = threading.Thread(target=run, args=(i,))
        thread_list.append(t)

    for i in thread_list:
        try:
            i.start()
        except:
            pass

    for i in thread_list:
        i.join()

    for i in range(len(final_ip_list)):
        print(str(final_name_list[i])+' <----->'+str(final_ip_list[i]))

    file_operation.file_operate(domain,final_name_list,final_ip_list,'brute')




# domain = 'baidu.com'
# pwd = str(os.getcwd())
# pwd = pwd + '/_dict/222.txt'
# thread_numb = 30
# bruteforce(domain, pwd, thread_numb)