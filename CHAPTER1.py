import cv2
print("package is installed")

#Read an image and show

#img = cv2.imread("RESOURCES/Instagram Lately _ MrsCasual.jpg")

#Read a video and display it 
#cv2.imshow("Read Image", img)
#cv2.waitKey(0)


#Read a webcam and display it

#cap = cv2.VideoCapture("RESOURCES/Snapchat-1597268298.mp4")

#display the video
#while True:
    #success, img = cap.read()
    #cv2.imshow("Video", img)

    #if cv2.waitKey(1) & 0xFF == ord('q'):
        #break

#Read a webcam and display it 
#webcam = cv2.VideoCapture(0)

#define the width and the height 
#3 = width, 4 = height

#webcam.set(3,640)
#webcam.set(4,480)

#display the webcam
#while True:
    #success, img = webcam.read()
    #cv2.imshow("wwbcam", img)

    #if cv2.waitKey(1) & 0xFF == ord('q'):
        #break

#converting an image to grey scale
img = cv2.imread("RESOURCES/Instagram Lately _ MrsCasual.jpg")

cv2.imshow("Read image", img)

imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Grey image", imgGrey)

cv2.waitKey(0)

