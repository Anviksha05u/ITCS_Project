import cy2
import datetime
import time
import message 
cap=cv2.VideoCapture(0)
time.sleep(2)
fgbg=cv2.createBackgroundsSubtractorMDG2()
count=0
while true:
  ret, frame=cap.read()
  text="UNOCCUPIED"
  fgmask=fgbg.apply(frame)
  gray=cv2.GaussainBkue(fgmask, (101, 101), 0)
  ret, thresh=cv2.threshold(gray, 25, 255,cv2.THRESH_BINARY)
  contours, hierarchy=cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX.SIMPLE)
  if(len(contours)!=0 and count=<20):
    if count>10 and count<20:
      img="screen{}.png".format(count-10):
      cv2.imwrite(img, frame)
    if count==19:
      message.msg()
    count+=1
  for c in contours:
    if cv2.contourArea(c)<10000:
      continue 
    x, y, w, h=cv2.boundingRect(c)
cv2.rectangle(frame, (x,y), (x+w), (y+h), (0,0,255), 2)
text="OCCUPIED"
