import torch
import torchvision.transforms as transforms
from PIL import Image
from  model import LeNet

transform=transforms.Compose(
            [transforms.Resize((32,32)),
             transforms.ToTensor()
            ])
#transfoerm 是图像的预处理的方法
classes=('001','002','003','004','005')
net=LeNet()
net.load_state_dict(torch.load('D:/zhuomian/deeplearning-work/class_1/Lenet.pth'))

im=Image.open('D:/zhuomian/GaitSet-master(2)/GaitSet-master/001-bg-01-000-001.jpg')

im=transform(im)  #bwc
#cbw

im=torch.unsqueeze(im,dim=0) #[N,C,B,W]

with torch.no_grad():
    output=net(im)
    data_test=torch.max(output,dim=1)
    predict=torch.max(output,dim=1)[1].data.numpy()

print(int(predict))
print(classes[int(predict)])