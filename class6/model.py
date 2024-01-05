#mobilenet V1 V2 V3
#mobilenet V2 的实现
#designer :zws
#2023 4 8


import torch.nn as nn
import torch.nn.functional as F
import torch
#首先定义一些我们基础的网络的模块的部分
from torchvision.models.mobilenet import _make_divisible


class ConvBnReLu(nn.Sequential):
    #继承自我们的nn.sequential容器我们创建一个组合层
    def __init__(self,in_channel,out_channel,kernel_size,stride=1,groups=1):
        padding=(kernel_size-1)//2
        super(ConvBnReLu,self).__init__(
        nn.Conv2d(in_channel,out_channel,kernel_size,stride,padding,groups=groups,bias=False),
        nn.BatchNorm2d(out_channel),
        nn.ReLU(inplace=True)
        )
class InverResidual(nn.Module):
     def __init__(self,in_channel,out_channel,stride,expand_rate):
         super(InverResidual, self).__init__()
         hidden_channel=in_channel*expand_rate
         self.use_shotcut= stride==1 and in_channel==out_channel
#定义的布尔变量看是否使用短链的操作
         layers=[]
         #定义一个层的列表
         if expand_rate!=1:
             #1x1的卷积层
             layers.append(ConvBnReLu(in_channel,hidden_channel,kernel_size=1))

         layers.extend(
             [
            ConvBnReLu(hidden_channel,hidden_channel,stride=stride,kernel_size=3,groups=hidden_channel),
            nn.Conv2d(hidden_channel,out_channel,kernel_size=1,bias=False),
            nn.BatchNorm2d(out_channel),
             ]
         )
         self.conv=nn.Sequential(*layers)

     def forward(self,x):
           if  self.use_shotcut:
                return x+self.conv(x)
           else:
                return self.conv(x)

class MobilenetV2(nn.Module):
    def __init__(self,num_class=1000,alpha=1.0,round_nearest=8):
        super(MobilenetV2, self).__init__()
        block=InverResidual
        #引入我们的倒残差结构定义的类将其复制给我门的block
        #_make_divisible将其调整为我们输入的参数的整数倍，更好的调用我们的底层设备
        #这个传入的参数，主要就是将其传入到我们通道数比如328alpha调整倒我们的round_nearest的整数倍
        input_channnel=_make_divisible(32*alpha,round_nearest)
        last_channel=_make_divisible(1280*alpha,round_nearest)
        inverted_residual_setting=[
            #t,c,n,s
            [1,16,1,1],
            [6,24,2,2],
            [6,32,3,2],
            [6,64,4,2],
            [6,96,3,1],
            [6,160,3,2],
            [6,320,1,1],
        ]
        features=[]
        features.append(ConvBnReLu(3,input_channnel,1,stride=2))
        for t,c,n,s in inverted_residual_setting:
            output_channel=_make_divisible(c*alpha,round_nearest)
            for i in range(n):
                stride=s if i==0 else 1
                features.append(block(input_channnel,output_channel,stride,expand_rate=t))
                input_channnel=output_channel
        features.append(ConvBnReLu(input_channnel,last_channel,1))
        self.features=nn.Sequential(*features)

        #build classifier
        self.avgpool=nn.AdaptiveAvgPool2d((1,1))
        self.classifier=nn.Sequential(
            nn.Dropout(0.2),
            nn.Linear(last_channel,num_class)
        )

        #权重的初始化
        for m in self.modules():
            if isinstance(m,nn.Conv2d):
                nn.init.kaiming_normal_(m.weight,mode='fan_out')
                if m.bias is not None:
                    nn.init.zeros_(m.bias)
            if isinstance(m,nn.BatchNorm2d):
                nn.init.ones_(m.weight)
                nn.init.zeros_(m.bias)
    def forward(self,x):
        x=self.features(x)
        x=self.avgpool(x)
        x=torch.flatten(x,start_dim=1)
        x=self.classifier(x)
        return x

