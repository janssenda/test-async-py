
import time
import threading
import random

import shutil
import cv2
import os

# def acker(m, n, s="%s"):
#     if m == 0:
#         return n + 1
#     if n == 0:
#         return acker(m - 1, 1, s)
#     n2 = acker(m, n - 1, s % ("(%d,%%s)" % (m - 1)))
#     return acker(m - 1, n2, s)
    # for j in range(int(5e3)):
    #     acker(3, 3)


def writeout(filename):

    BufferCopy = ["a", "b", "c", "c"]
    out = cv2.VideoWriter(os.getcwd(), cv2.VideoWriter_fourcc('X', 'V', 'I', 'D'), 5, (400, 400))

    print("Inside Before:\t" + str(time.clock()))
    logger = open(os.getcwd() +"\\" + filename, "w")

    logger.write("T-\tN\tArea\tPerim\tMax\tAvg\tA/N\tM/A\tAvgN\tTime\n")
    for entry in BufferCopy:
        logger.write(entry)

    logger.close()
    shutil.move(os.getcwd() +"\\" + filename, os.getcwd() +"\\" + "new_" + filename )
    time.sleep(5)
    print("Inside After:\t" + str(time.clock()))

def slowfunction(count):

    duration = random.uniform(0.5,10)
    print('Starting job # %i with duration of %1.2f seconds' % (count, duration))

    time.sleep(duration)
    print('Done with job #: %i' % count)


def main():

    for i in range(1,100):
        print('Loop count: %i ' % i)
        if i%5 == 0:
            threading.Thread(target=slowfunction,args=[i]).start()
            #threading.Thread(target=writeout, args=["data"+str(i)+".txt"]).start()
        time.sleep(1)

main()