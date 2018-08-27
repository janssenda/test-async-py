import gevent.monkey
import time


def slowfunction(count):
    print('Starting job #: %i' % count)
    time.sleep(5)
    print('Done with job #: %i' % count)




gevent.monkey.patch_all(slowfunction)
x = 1
while True:

    if x%5 == 0:
        gevent.spawn(slowfunction,x)
        gevent.sleep(0)


    print('Loop count: %i ' % x)
    time.sleep(1)
    x += 1

