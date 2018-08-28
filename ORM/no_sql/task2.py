from time import time, sleep

import requests
import redis
import multiprocessing

redis_server = redis.StrictRedis(host='192.168.99.100',
                                 port=6379,
                                 charset='utf-8',
                                 decode_responses=True,
                                 db=0)


class Producer(multiprocessing.Process):

    def run(self):
        for _ in range(10):
            response = requests.get('http://24tv.ua')
            redis_server.set(time(), response.content)
            sleep(10)


class Consumer(multiprocessing.Process):

    def run(self):
        with open('results.txt', 'a') as target_file:
            for _ in range(11):
                for key in redis_server.keys():
                    target_file.write(redis_server.get(key))
                    redis_server.delete(key)
                sleep(22)


if __name__ == '__main__':
    p1 = Producer()
    p2 = Consumer()
    p1.start()
    p2.start()
    p1.join()
    p2.join()
