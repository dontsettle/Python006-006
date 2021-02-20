import redis

client = redis.Redis(host='localhost', password='')
def counter(video_id):
    client.set(video_id, '0', nx=True)
    count_number = client.incr(video_id)
    return count_number
print(counter(1000))
print(counter(1001))
print(counter(1002))
# 下面可以完善成和上面的一样吗？
def counter(video_id):
    client.lpush('counter','video_id')
    cou_number=client.llen('counter')
    print(cou_number)
counter(1000)
def counter1(video_id):
    client.lpush('counter1','video_id')
    cou_number=client.llen('counter1')
    print(cou_number)
counter1(1001)
