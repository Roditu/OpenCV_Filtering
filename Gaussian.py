import cv2
import numpy as np
from matplotlib import pyplot as plt
import time

defimg = cv2.imread("noised.jpg", 0)

start = time.time()

#Gaussian
result = cv2.GaussianBlur(defimg, (7,7), 1)

end = time.time()
exe = end - start

print(f"Execution time : {exe} seconds")

cv2.imshow("Default", defimg)
cv2.imshow("Gauss", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
