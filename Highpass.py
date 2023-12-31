import cv2
import numpy as np
import time

start = time.time()

defimg = cv2.imread("noised.jpg", 0)

#High Filter
filterbox=np.array([
    [0, -1, 0],
    [-1, 5.5, -1],
    [0, -1, 0]
])

result = cv2.filter2D(defimg, ddepth = -1, kernel = filterbox)

cv2.imshow("Default", defimg)
cv2.imshow("Sharpen", result)

end = time.time()
exe = end - start

print(f"Execution time : {exe} seconds")

cv2.waitKey(0)
cv2.destroyAllWindows()

