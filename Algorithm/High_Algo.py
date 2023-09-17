import cv2
import numpy as np 
import time

start = time.time()

def Convolusi(f,w):
    row = f.shape[0]
    column = f.shape[1]
    dkernel = w.shape[0]
    rkernel= np.int32(np.floor(dkernel/2)) 

    g =np.zeros((row,column))
    for y in range(row):
        for x in range(column):
            g[y,x] = 0 
            for i in range(dkernel):
                yy =y+i-rkernel
                if (yy<0)|(yy>=row-1):
                    continue 
                for j in range(dkernel):
                    xx =x+j - rkernel
                    if (xx<0)|(xx>=column-1): 
                        continue 
                    g[y,x]=g[y,x]+f[yy,xx]*w[i,j]
    g= np.uint8(np.floor(g))
    return g

    
# Membaca File Citra
default = cv2.imread("noised.jpg", 0)
cv2.imshow('Citra Asli', default)

filter = np.array([ 
    [0, -1, 0],
    [-1, 5.5, -1],
    [0, -1, 0]
])
result= Convolusi(default,filter)
cv2.imshow('Highpass Filter', result)

end = time.time()
exe = end - start

print(f"Execution time : {exe} seconds")

cv2.waitKey(0)
cv2.destroyAllWindows()
 