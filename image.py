import cv2
import numpy as np
black=np.zeros([600,600])
black[350:400,369:400]=255
cv2.imshow("dot",black)
cv2.waitKey(0)