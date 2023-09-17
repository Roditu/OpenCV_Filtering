import cv2
import numpy as np
import time

defimg = cv2.imread("noised.jpg", 0)

start = time.time()

result = cv2.boxFilter(defimg, -1, (7,7))

end = time.time()
exe = end - start

print(f"Execution time : {exe} seconds")

cv2.imshow("Noise", result)
cv2.waitKey(0)
cv2.destroyAllWindows()

