import requests
from threading import Thread, BoundedSemaphore
from time import time
global_results = []

list_of_urls = ['http://24tv.ua', 'http://zik.ua', 'http://zaxid.net', 'https://github.com/openprocurement', 'https://www.youtube.com'] * 1000

lock = BoundedSemaphore(100)


class CustomThread(Thread):
    def __init__(self, name, start, end):
        super().__init__()
        self.name=name
        self.st=start
        self.en=end

    def run(self):
        #print(f'{self.name} is starting')
        with lock:
            #print(f'{self.name} is working')
            global global_results
            for url in list_of_urls[self.st:self.en]:
                result = requests.get(url)
                global_results.append(result.status_code)
        #print(f'{self.name} is done')

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time()
        func(*args, **kwargs)
        print(time() - start)
    return wrapper
@time_it
def main():
    threads = []
    for x in range(100):
        t = CustomThread(name='name '+ str(x), start=x*5, end=x*5+5)
        threads.append(t)
        t.start()
    res = [x.join() for x in threads]


for x in range(100, 0, -10):
    print(x)
    lock = BoundedSemaphore(x)
    main()
    global_results = []