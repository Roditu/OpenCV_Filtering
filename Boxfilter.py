import cv2
import numpy as np
import time

start = time.time()

defimg = cv2.imread("noised.jpg", 0)

result = cv2.boxFilter(defimg, -1, (7,7))

end = time.time()
exe = end - start

print(f"Execution time : {exe} seconds")

cv2.imshow("Noise", result)
cv2.waitKey(0)
cv2.destroyAllWindows()

