import gevent.monkey
import time
gevent.monkey.patch_all()



def acker(m, n, s="%s"):

    if m == 0:
        return n + 1
    if n == 0:
        return acker(m - 1, 1, s)
    n2 = acker(m, n - 1, s % ("(%d,%%s)" % (m - 1)))
    return acker(m - 1, n2, s)

def slowfunction(count):

    print('Starting job #: %i' % count)

    for j in range(int(5e3)):
        acker(3, 3)
        gevent.sleep(0)

    print('Done with job #: %i' % count)





x = 1
while True:

    if x%5 == 0:
        gevent.spawn(slowfunction,x)




    print('Loop count: %i ' % x)
    time.sleep(1)
    x += 1


