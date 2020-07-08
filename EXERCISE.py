import cv2
#print("Installed Successfuly")
import numpy as np
"""The cv2.line() takes the following parameters: where, start coordinates,
 end coordinates, color (bgr), line thickness."""
#drawing on an image

#img = cv2.imread("RESOURCES/Instagram Lately _ MrsCasual.jpg", cv2.IMREAD_COLOR)
#Diagonal line
#cv2.line(img,(0,0),(150,150),(255,255,255),15)

#cv2.imshow('image',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#rectangle
"""The parameters here are the image, the top left coordinate,
 bottom right coordinate, color, and line thickness."""
#cv2.rectangle(img,(15,25),(200,150),(0,0,255),15)
#cv2.imshow('image',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#CIRCLE
"""The parameters here are the image/frame,
 the center of the circle, the radius, color,
  and then thickness. Notice we have a -1 for thickness. 
  This means the object will actually be filled in, 
  so we will get a filled in circle."""
#img = cv2.imread("RESOURCES/Instagram Lately _ MrsCasual.jpg", cv2.IMREAD_COLOR)

#cv2.circle(img,(100,63), 55, (0,255,0), -1)
#cv2.imshow('image',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


#WRITING ON AN IMAGE
img = cv2.imread("RESOURCES/Instagram Lately _ MrsCasual.jpg", cv2.IMREAD_COLOR)
#font = cv2.FONT_ITALIC
#cv2.putText(img,'AWSOME STYLE',(0,30), font, 1, (200,255,155),2, cv2.LINE_AA )
#cv2.imshow('image',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#ALL OF THEM TOGETHER
import numpy as np
import cv2

img = cv2.imread("RESOURCES/Instagram Lately _ MrsCasual.jpg", cv2.IMREAD_COLOR)
cv2.line(img,(0,0),(200,300),(255,255,255),50)
cv2.rectangle(img,(500,250),(1000,500),(0,0,255),15)
cv2.circle(img,(447,63), 63, (0,255,0), -1)
pts = np.array([[100,50],[200,300],[700,200],[500,100]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], True, (0,255,255), 3)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'GLAM',(10,500), font, 6, (200,255,155), 13, cv2.LINE_AA)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
