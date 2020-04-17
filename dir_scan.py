import requests,re,threading,file_operation,os
class dir_scanner:
    def __init__(self, urll, positionn, thread_num):
        self.url = urll
        self.judge_url = re.match(r'http://|https://', self.url)
        self.file = open(positionn, 'r')
        self.responsecode = []
        self.url_list = []

        if not thread_num:
            self.thread_num=10
        else:
            self.thread_num = thread_num
        self.head = \
            {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:72.0) Gecko/20100101 Firefox/72.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
                'Accept-Encoding': 'gzip, deflate, br'
            }


        self.lock = threading.Semaphore(self.thread_num)

    def get_result(self, urlll=None):
        self.lock.acquire()
        response_code = str(requests.get(urlll, headers=self.head).status_code)
        reason = requests.get(urlll, headers=self.head).reason
        self.url_list.append(urlll)
        self.responsecode.append(response_code)
        if response_code =='200':
            print(urlll+' -----> '+response_code + '  ' + reason)
        self.lock.release()


    def run(self):
        list_thread=[]
        if self.judge_url is not None:
            for i in self.file:
                if i[0:1] != '#':
                    ii = i.strip('\n')
                    url = self.url + ii
                    t = threading.Thread(target=self.get_result,kwargs={"urlll":url})
                    list_thread.append(t)


        else:
            print('\033[1;36;40m[-]Please use "http://" or "https://" at the beginning of the url.\033[0m')
        for i in list_thread:
            try:
                i.start()
            except:
                pass

        for i in list_thread:
            i.join(10)

    def output(self):
        domain1 = str(self.url)
        domain1 = domain1.strip('http://').strip('https://')
        file_operation.file_operate(domain1, self.url_list, self.responsecode, 'dir_search')
        # print(len(self.url_list))
        # print(len(self.responsecode))

# domain = 'https://www.baidu.com'
# pwd = str(os.getcwd())
# pwd = pwd + '/_dict/345.txt'
# thread_numb = 30
#
# execute = dir_scanner(domain, pwd, thread_numb)
# execute.run()
# execute.output()