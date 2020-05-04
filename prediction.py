from nn import *
from dataset import *
from train import train
from workingWithVideo import frame
from PIL import Image
import cv2 
import torch


loader = transforms.Compose([transforms.Resize((32, 32)),
                                transforms.ToTensor(),
                                transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

def prediction():

	net = train()
	frames = frame()
	counter = 0

	while (counter != len(frames)):
		with Image.open('frame/frame'+str(counter)+'.jpg') as image:
			net.eval()
			image = loader(image).float()
			image = image.unsqueeze(0)
			output = net(image)
			conf, predicted = torch.max(output.data, 1)
			print(classes[predicted.item()], "confidence: ", conf.item())
			counter += 1


prediction()



