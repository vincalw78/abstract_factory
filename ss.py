import requests
from threading import Thread, Condition
from queue import Queue

condition = Condition()
queue = Queue()


class ProducerThread(Thread):

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        response = requests.get(self.url)
        condition.acquire()
        queue.put(response)
        condition.notify()
        condition.release()


class ConsumerThread(Thread):

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        with open('results.txt', 'a') as fi:

            queue.put(response)