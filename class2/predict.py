import torch
import torchvision.transforms as transforms
from PIL import Image
from  model import AlexNet
import json
import matplotlib.pyplot as plt


transform=transforms.Compose(
            [transforms.Resize(224,224),
            transforms.ToTensor(),
             transforms.Normalize((0.5,0.5,0.5),(0.5,0.5,0.5))
            ])

#transfoerm 是图像的预处理的方法
classes={'plane','car','bird','cat','deer','dog','frog','horse','ship','truck'}

net=AlexNet()
net.load_state_dict(torch.load('LeNet.pth'))

im=Image.open('1.jpeg')
plt.imshow(im)
im=transform(im)
im=torch.unsqueeze(im,dim=0)  #[N,C,B,W]
#进行升维度的操作
#扩充维度
try:
    json_file=open('./class_indices.json','r')
    class_index=json.load(json_file)
except Exception as e:
    print(e)
    exit(-1)

with torch.no_grad():
    output=torch.squeeze(net(im))
    #进行降维度的操作
    predict=torch.softmax(output,dim=0)
    predict_cla=torch.argmax(predict).numpy()
print(class_index[str(predict)],predict[predict_cla].item())
plt.show()