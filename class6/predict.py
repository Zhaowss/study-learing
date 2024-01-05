import torch
import torchvision.transforms as transforms
from PIL import Image
from  model import MobilenetV2
import json
import matplotlib.pyplot as plt
transform=transforms.Compose(
            [transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
             transforms.Normalize((0.485,0.456,0.406),(0.229,0.224,0.225))
            ])
#transfoerm 是图像的预处理的方法

classes={'daisy','dandelion','roses','sunflowers','tuplips'}
net = MobilenetV2(num_class=5)
missing_keys,unexpected_keys=net.load_state_dict(torch.load('MobilenetV2finish.pth'),strict=False)
net.eval()
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