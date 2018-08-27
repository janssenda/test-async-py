import gevent.monkey
import time
import shutil
import cv2
import os

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


filename = "data.txt"
gevent.monkey.patch_all(writeout)

while True:

                print("Before:\t" + str(time.clock()))
                gevent.spawn(writeout,filename)
                gevent.sleep(0)
                print("After:\t" + str(time.clock()))
                time.sleep(1)

