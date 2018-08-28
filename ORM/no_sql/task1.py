import redis

redis_server = redis.StrictRedis(host='localhost',
                                 port=6379,
                                 charset='utf-8',
                                 decode_responses=True,
                                 db=0)


def task1():
    redis_server.set('stork', 'storch')
    redis_server.set('hawk', 'falke')
    redis_server.set('woodpecker', 'specht')
    redis_server.set('owl', 'eule')
    redis_server.set('duck', 'ente')
    redis_server.set('chicken', 'duchchicken')

    keys = redis_server.keys()
    values = []
    for key in keys:
        values.append(redis_server.get(key))
        redis_server.delete(key)

    print(redis_server.get('owl'))
    print(keys)
    print(values)
    print(f'After deleting all keys {redis_server.keys()}')


if __name__ == '__main__':
    task1()
