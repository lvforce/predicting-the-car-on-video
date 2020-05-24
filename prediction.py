from nn import *
from dataset import *
from train import train
from workingWithVideo import frame
from createVideo import createVideo
from PIL import Image
import cv2 
import torch


loader = transforms.Compose([transforms.Resize((32, 32)),
                                transforms.ToTensor(),
                                transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

def prediction():

	frames = frame()
	net = train()
	counter = 0
	predictedClass = []
	accuracy = []


	while (counter != len(frames)):
		with Image.open('frame/frame'+str(counter)+'.jpg') as image:
			net.eval()
			image = loader(image).float()
			image = image.unsqueeze(0)
			output = net(image)
			conf, predicted = torch.max(output.data, 1)
			print(classes[predicted.item()], "confidence: ", conf.item())
			predictedClass.append(classes[predicted.item()])
			accuracy.append(float("{0:.1f}".format(conf.item())))
			counter += 1

	createVideo(predictedClass, accuracy)

prediction()



