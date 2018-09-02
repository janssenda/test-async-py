


import threading
import cv2
import numpy as np

def sub(obj, ROI):
    print("Thread before\t" + str(ROI[0,0]))
    ROI.put(ROI,obj.apply(ROI, None, -1))
    print("Thread after\t" + str(ROI[0,0]))


fgbg = cv2.createBackgroundSubtractorKNN(100, 500, False)
ROI = (255*np.random.rand(320,200,1)).astype(dtype="uint8")

print("Main before\t" + str(ROI[0,0]))

t1 = threading.Thread(target=sub, args=[fgbg, ROI])
t1.start()
t1.join()

print("Main after\t" + str(ROI[0,0]))

