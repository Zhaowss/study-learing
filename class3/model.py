import torch.nn as nn
import torch.nn.functional as F
import torch
#传入的cfg 是一个配置变量，

#小尺度的卷积的叠加和大尺度卷积具备相同感受野

class VGG(nn.Module):
       def __init__(self,features,clss_num=2,init_weights=False):
           super(VGG,self).__init__()
           self.features=features

           self.classifier=nn.Sequential(
               nn.Dropout(p=0.5),
               #随机失活百分之五十，减少过拟合
               nn.Linear(25088,2048),
               nn.ReLU(inplace=True),
               nn.Dropout(p=0.5),
               nn.Linear(2048,2048),
               nn.ReLU(inplace=True),
               nn.Linear(2048,clss_num)
           )
           if init_weights:
               self._initialize_weights()
       def forward(self,x):
           x=self.features(x)
           x=torch.flatten(x , start_dim=1)
           x=self.classifier(x)
           return x

       # 初始化我们的权重
       def _initialize_weights(self):
           for m in self.modules():
               if isinstance(m, nn.Conv2d):
                   #nn.init.kaiming_normal_(m.weight, mode='fan_out', )
                   nn.init.xavier_uniform_(m.weight)
                   if m.bias is not None:
                       nn.init.constant_(m.bias, 0)
               elif isinstance(m, nn.Linear):
                    nn.init.xavier_uniform_(m.weight)
                    nn.init.constant_(m.bias,0)




def make_features(cfg: list):
    layers=[]
    #定义一个空列表存储我们的定义的层结构
    in_channels=3

    for v in cfg:
        if v=="M":
            layers+=[nn.MaxPool2d(kernel_size=2,stride=2)]
        else:
            conv2d=nn.Conv2d(in_channels,v,kernel_size=3,padding=1)
            layers+=[conv2d,nn.ReLU(inplace=True)]
            in_channels=v
    return nn.Sequential(*layers)
#非关键参数的传入



#我们网络的配置结构列表。
cfgs={
    'vgg11':[64,'M',128,'M',256,256,'M',512,512,'M',512,512,'M'],
    'vgg13':[64,64,'M',128,128,'M',256,256,'M',512,512,'M',512,512,'M'],
    'vgg16':[64,64,'M',128,128,'M',256,256,256,'M',512,512,512,'M',512,512,512,'M'],
    'vgg19':[64,64,'M',128,128,'M',256,256,256,256,'M',512,512,512,512,'M',512,512,512,512,'M'],
}

def vgg(model_name="vgg16",**kwargs):
    try:
        cfg=cfgs[model_name]
    except:
        print("warning: model number {} not in cfgs dict:".format(model_name))
        exit(-1)

    model=VGG(make_features(cfg),**kwargs)
    #定义的可变长度的字典变量
    return model

import torch
input1=torch.rand([32,3,224,224])
vgg_model=vgg(model_name='vgg16')
print(vgg_model)
output=vgg_model(input1)
print(output)