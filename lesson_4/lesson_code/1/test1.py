import numpy as np
# p=[np.random.randint(1,10,10),np.random.randint(1,10,10)]
# print(p[0])
# print(p[1])
# m=np.square(p[0])+np.square(p[1])
# print(np.sqrt(m))
np.random.seed(1)
d=np.random.uniform(0,1,10)
print(d)
print(np.where(d<0.1))
print(np.where(d<0.1)[0].shape[0])

import cv2
from MahalSdk import MahalSdk
img=MahalSdk.read("老虎.jpg")
cv2.imshow("tiger",img)
cv2.waitKey(0)