import cv2 
import numpy as np 
from PIL import Image, ImageDraw, ImageFont

def frame_car():
  video = cv2.VideoCapture('/home/roman/projects/2.mp4') 
  point = (0,0)

  if (video.isOpened()== False):  
    print("Error opening video  file") 

  new_frame = 0  
  frames = []

  while(video.isOpened()): 
        
    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (5, 20)
    fontScale = 1
    color = (255, 0, 0)
    thickness = 2
    ret, frame = video.read()

    if ret == True: 
      width  = video.get(cv2.CAP_PROP_FRAME_WIDTH)   
      height = video.get(cv2.CAP_PROP_FRAME_HEIGHT) 
      ren = cv2.rectangle(frame,point,(100, 50),(60, 255, 0),0)
      cv2.putText(frame, 'Car', org, font, fontScale, color, thickness,  cv2.LINE_AA)
      cv2.imshow('Frame', frame) 
      cv2.imwrite('frame/frame'+str(new_frame)+'.jpg',ren)
      frames.append(frame)
      new_frame += 1

      if cv2.waitKey(25) & 0xFF == ord('q'): 
        break
    else:  
      break

  cv2.destroyAllWindows() 


frame_car()