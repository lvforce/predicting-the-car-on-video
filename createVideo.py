from PIL import Image
import cv2


def createVideo(predictedClass, accuracy):
	point = (0,0)
	counter = 0
	font = cv2.FONT_HERSHEY_SIMPLEX
	org = (5, 20)
	fontScale = 1
	color = (255, 0, 0)
	thickness = 2
	newFrame = 0
	imgArray = []

	video = cv2.VideoCapture('/home/roman/projects/9.mp4')
	while(video.isOpened()):
		ret, frame = video.read()
		if ret == True:
			prediction = accuracy[newFrame] if predictedClass[newFrame] == 'car' else 0
			#frame = cv2.resize(frame, (1280,720),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)
			cv2.putText(frame, 'Car'+': '+str(prediction)+'%', org, font, fontScale, color, thickness,  cv2.LINE_AA)
			cv2.imwrite('newFrame/frame'+str(newFrame)+'.jpg', frame)
			newFrame += 1
		else:
			break

	for i in range(0, newFrame):
		img = cv2.imread('newFrame/frame'+str(i)+'.jpg')
		height, width, layers = img.shape
		size = (width, height)
		imgArray.append(img)

	newVideo=cv2.VideoWriter('video10.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15,size)
	for j in range(len(imgArray)):
		newVideo.write(imgArray[j])

	newVideo.release()

