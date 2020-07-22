import cv2
import numpy

def click_event(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,y)
        font = cv2.FONT_HERSHEY_PLAIN
        txt = str(x) + ", " + str(y)
        cv2.putText(img,txt,(x,y),font,1,(255,255,255),1,cv2.LINE_AA)
        cv2.imshow("flash",img)
    
    if event == cv2.EVENT_RBUTTONDOWN:              #   for pick the color
        blue =  img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]
        font = cv2.FONT_HERSHEY_COMPLEX_SMALL
        txt = str(blue) + ", " + str(green) + ", " + str(red)
        cv2.putText(img,txt,(x,y),font,1,(0,0,0),1,cv2.LINE_AA)
        cv2.imshow("flash",img)
#img = numpy.zeros((512,512,3),numpy.uint8)
img = cv2.imread("colourPicker.jpg")
img = cv2.resize(img,(600,600))
cv2.imshow("flash",img)
cv2.setMouseCallback("flash",click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
