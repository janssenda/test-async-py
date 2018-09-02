


import threading
import cv2
import numpy as np

def sub(obj, ROI):
    np.copyto(ROI[:,:,0],obj.apply(ROI, None, -1))

fgbg = cv2.createBackgroundSubtractorKNN(100, 500, False)

threadcount = 10
threads = []
data = []

for x in range(threadcount):
    data.append((255 * np.random.rand(320, 200, 1)).astype(dtype="uint8"))
    threads.append(threading.Thread(target=sub, args=[fgbg, data[x]]))

# Start them all
for thread in threads:
    thread.start()

# Wait for all to complete
for thread in threads:
    thread.join()

print()


