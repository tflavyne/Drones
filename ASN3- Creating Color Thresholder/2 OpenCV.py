import numpy
import scipy.signal
import cv2


#step2.1
img = cv2.imread('Frame0064.png', 0)

print (img)

cv2.imshow('image', img)
cv2.waitKey(10000)
cv2.destroyAllWindows()


#step2.2
Ig_array = numpy.asarray(img)
Kx = numpy.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
Gx = scipy.signal.convolve2d(Ig_array, Kx)
print(f"Gx magnitude: \n{numpy.absolute(Gx)}")
print()

Ky = numpy.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
Gy = scipy.signal.convolve2d(Ig_array, Ky)
print(f"Gy magnitude: \n{numpy.absolute(Gy)}")

G = numpy.sqrt(numpy.add(Gx*Gx, Gy*Gy))
print(f"G: \n{G}")

