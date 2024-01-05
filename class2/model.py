import torch.nn as nn
import torch.nn.functional as F
import torch
#relu           diyici
#dropout

class AlexNet(nn.Module):
    def __init__(self,num_classes=5,init_weithts=False):
        super(AlexNet,self).__init__()
        self.features=nn.Sequential(
            nn.Conv2d(3,48,kernel_size=11,stride=4,padding=2),   #input[3,224,224]    out=[48,55,55]
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3,stride=2),                #input[48,55,55]     out=[48,27,27]
            nn.Conv2d(48, 128, kernel_size=5, padding=2),  # input[48,27,27]    out=[128,27,27]
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3,stride=2),#input[128,27,27]     out=[128,13,13]
            nn.Conv2d(128,192,kernel_size=3,padding=1) ,#input[128,13,13]     out=[192,13,13]
            nn.ReLU(inplace=True),
            nn.Conv2d(192, 192, kernel_size=3, padding=1),  # input[192,13,13]     out=[192,13,13]
            nn.ReLU(inplace=True),
            nn.Conv2d(192, 128, kernel_size=3, padding=1),  # input[192,13,13]     out=[128,13,13]
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3,stride=2),          #input=[128,13,13]  output=[128,6,6]
        )
    #初始化一些定义得类别
    #全连接层一般需要放置权重丢失的层，防止产生过拟合

        self.classifier=nn.Sequential(
            nn.Dropout(p=0.5),
            nn.Linear(128*6*6,2048),         #input=[192*6*6]  op=[2048]
            nn.ReLU(inplace=True),
            nn.Dropout(p=0.5),
            nn.Linear(2048,2048),              #input=[2048]  op=[2048]
            nn.ReLU(inplace=True),
            nn.Linear(2048,num_classes)     #input=[2048]  op=[num_classes]
        )

    #是否初始化我们的权重
        if init_weithts:
            self._initialize_weights()

    #定义前向传播的网络
    def forward(self,x):
        x=self.features(x)   #特征提取层
        x=torch.flatten(x,start_dim=1)   #展开层
        x=self.classifier(x) #分类层
        return x

    #初始化我们的权重
    def _initialize_weights(self):
        for m in self.modules():
            if isinstance(m,nn.Conv2d):
                nn.init.kaiming_normal_(m.weight,mode='fan_out')
                if m.bias is not None:
                    nn.init.constant_(m.bias,0)
            elif isinstance(m,nn.Linear):
                nn.init.normal_(m.weight,0,0.01)
                nn.init.normal_(m.bias,0)

