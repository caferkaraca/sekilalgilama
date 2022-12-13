import cv2
import numpy as np
img=cv2.imread("sekil.png")
#cv2.imshow("resim",img)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
Canny=cv2.Canny(gray,100,200)
#cv2.imshow("Canny",Canny)

contours,_=cv2.findContours(Canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

for cnt in contours:
    area=cv2.contourArea(cnt)
    if area>500:
        approx=cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
        cornerCount=len(approx)
        x,y,w,h=cv2.boundingRect(approx)
        if(cornerCount==3):
            cv2.putText(img,"ucgen",(x-10,y-10),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0))
            cv2.drawContours(img, [cnt],0,(164 ,0 ,0),-1)
        elif(cornerCount==4):
            print(w,"genişlik",h,"yükseklik")
            if abs(w-h) <= 3:
                cv2.putText(img,"kare",(x-10,y-10),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0))
                cv2.drawContours(img, [cnt],0,(255 ,185 ,15),-1)
            else:
                cv2.putText(img,"dikdortgen",(x-10,y-10),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0))
                cv2.drawContours(img, [cnt],0,(0 ,205, 0),-1)
        elif(cornerCount==5):
            cv2.putText(img,"besgen",(x-10,y-10),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0))
            cv2.drawContours(img, [cnt],0,(67,205,128),-1)
        elif(cornerCount==6):
            cv2.putText(img,"altigen",(x-10,y-10),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0))
            cv2.drawContours(img, [cnt],0,(100,205,128),-1)
        elif(cornerCount==8):
            cv2.putText(img,"sekizgen",(x-10,y-10),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0))
            cv2.drawContours(img, [cnt],0,(100,205,200),-1)
        elif(cornerCount>10 and cornerCount<14):
            cv2.putText(img,"elips",(x-10,y-10),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0))
            cv2.drawContours(img, [cnt],0,(238,207,161),-1)
        elif(cornerCount>14):
            cv2.putText(img,"daire",(x-10,y-10),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0))
            cv2.drawContours(img, [cnt],0,(15,105,150),-1)
cv2.imshow("sekil tespit ve renklendirme",img)
cv2.waitKey(0)
cv2.destroyAllWindows
