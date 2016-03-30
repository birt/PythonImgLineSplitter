import numpy as np
import cv2
#import cv2.cv as cv

# python reimplementation of:
#
# http://stackoverflow.com/questions/34981144/split-text-lines-in-scanned-document/35014061
#

print cv2.__version__

img = cv2.imread('Afbeelding 2.png')

cv2.imshow('image',img)
#cv2.waitKey(0)
bin = (255 - img)
bin = cv2.cvtColor(bin,cv2.COLOR_BGR2GRAY)
pts = cv2.findNonZero(bin)

#box = cv2.minAreaRect(pts)

horProj = cv2.reduce(bin, 1, cv2.REDUCE_AVG)

horProj[horProj<=5.0] = 0

ycoords = []
y=0
count=0
isSpace=False

for i in xrange(0,horProj.size):
         if (not isSpace):
            if (not horProj[i]):
                isSpace=True
                count=1
                y=i
         else:
             if horProj[i]:
                 isSpace=False
                 ycoords.append(y/count)
             else:
                 y += i
                 count = count + 1


cv2.imshow('img2',bin)


result = cv2.cvtColor(bin, cv2.COLOR_GRAY2BGR)
(rows,cols,somthing) = result.shape

for i in xrange(0,len(ycoords)):
    # C++ version
    # line(result, Point(0, ycoords[i]), Point(result.cols, ycoords[i]), Scalar(0, 255, 0));
    cv2.line(result,(0,ycoords[i]),(cols,ycoords[i]),(0,255,0),1)

cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()