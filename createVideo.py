from PIL import Image
import cv2
import numpy as np


def createVideo(predictedClass, accuracy):
	point = (0,0)
	counter = 0
	font = cv2.FONT_HERSHEY_SIMPLEX
	orgCar = (50, 100)
	orgShip = (50, 200)
	fontScale = 2
	thickness = 10
	newFrame = 0
	imgArray = []


	video = cv2.VideoCapture('/home/roman/Desktop/videoNN/.mp4')
	while(video.isOpened()):
		ret, frame = video.read()
		if ret == True:
			color = (0, 0, 255) if accuracy[newFrame] >= 10 else (255, 0, 0)
			if (predictedClass[newFrame] == 'car'): 
				cv2.putText(frame, 'Car'+': '+str(accuracy[newFrame])+'%', orgCar, font, fontScale, color, thickness,  cv2.LINE_AA)
				cv2.putText(frame, 'Ship'+': '+'0%', orgShip, font, fontScale, (255, 0, 0), thickness,  cv2.LINE_AA)
			elif (predictedClass[newFrame] == 'ship'):
				cv2.putText(frame, 'Car'+': '+'0%', orgCar, font, fontScale, (255, 0, 0), thickness,  cv2.LINE_AA)
				cv2.putText(frame, 'Ship'+': '+str(accuracy[newFrame])+'%', orgShip, font, fontScale, color, thickness,  cv2.LINE_AA)
			else:
				cv2.putText(frame, 'Car'+': '+'0%', orgCar, font, fontScale, (255, 0, 0), thickness,  cv2.LINE_AA)
				cv2.putText(frame, 'Ship'+': '+'0%', orgShip, font, fontScale, (255, 0, 0), thickness,  cv2.LINE_AA)
			cv2.imwrite('newFrame/frame'+str(newFrame)+'.jpg', frame)
			newFrame += 1
		else:
			break

	for i in range(0, newFrame):
		img = cv2.imread('newFrame/frame'+str(i)+'.jpg')
		height, width, layers = img.shape
		size = (width, height)
		imgArray.append(img)

	newVideo=cv2.VideoWriter('video8.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15,size)
	for j in range(len(imgArray)):
		newVideo.write(imgArray[j])

	newVideo.release()

