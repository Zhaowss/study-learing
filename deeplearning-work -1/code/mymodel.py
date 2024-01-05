import torch.nn as nn
import torch.nn.functional as F
import torch

class ChannelAttention(nn.Module):
    def __init__(self, in_planes, ratio=8):
        super(ChannelAttention, self).__init__()
        self.avg_pool = nn.AdaptiveAvgPool2d(1)
        self.max_pool = nn.AdaptiveMaxPool2d(1)
        #通道注意力，这里主要是通过定义申明俩个最大池化和平均池化
        #利用1x1卷积代替全连接
        self.fc1   = nn.Conv2d(in_planes, in_planes // ratio, 1, bias=False)
        self.relu1 = nn.ReLU()
        self.fc2   = nn.Conv2d(in_planes // ratio, in_planes, 1, bias=False)

        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        avg_out = self.fc2(self.relu1(self.fc1(self.avg_pool(x))))
        max_out = self.fc2(self.relu1(self.fc1(self.max_pool(x))))
        out = avg_out + max_out
        return self.sigmoid(out)

class SpatialAttention(nn.Module):
    def __init__(self, kernel_size=7):
        super(SpatialAttention, self).__init__()

        assert kernel_size in (3, 7), 'kernel size must be 3 or 7'
        padding = 3 if kernel_size == 7 else 1
        self.conv1 = nn.Conv2d(2, 1, kernel_size, padding=padding, bias=False)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        avg_out = torch.mean(x, dim=1, keepdim=True)
        max_out, _ = torch.max(x, dim=1, keepdim=True)
        x = torch.cat([avg_out, max_out], dim=1)
        x = self.conv1(x)
        return self.sigmoid(x)

class cbam_block(nn.Module):
    def __init__(self, channel, ratio=8, kernel_size=3):
        super(cbam_block, self).__init__()
        self.channelattention = ChannelAttention(channel, ratio=ratio)
        self.spatialattention = SpatialAttention(kernel_size=kernel_size)

    def forward(self, x):
        x = x * self.channelattention(x)
        x = x * self.spatialattention(x)
        return x

class MYnet(nn.Module):
       def __init__(self,clss_num=2,init_weights=False):
           super(MYnet,self).__init__()
           self.features=nn.Sequential(
               nn.Conv2d(3,64,kernel_size=3,padding=1),
               nn.ReLU(inplace=True),
               nn.MaxPool2d(kernel_size=2,stride=2),
               nn.Conv2d(64, 128, kernel_size=3, padding=1),
               nn.ReLU(inplace=True),
               nn.MaxPool2d(kernel_size=2, stride=2),
               nn.Conv2d(128, 256, kernel_size=3, padding=1),
               nn.ReLU(inplace=True),
               nn.Conv2d(256, 256, kernel_size=3, padding=1),
               nn.ReLU(inplace=True),
               nn.MaxPool2d(kernel_size=2, stride=2),
               nn.Conv2d(256, 512, kernel_size=3, padding=1),
               nn.ReLU(inplace=True),
               nn.Conv2d(512,512, kernel_size=3, padding=1),
               nn.ReLU(inplace=True),
               nn.MaxPool2d(kernel_size=2, stride=2)
           )
           self.attention=cbam_block(512)
           self.features2=nn.Sequential(
               nn.Conv2d(512, 512, kernel_size=3, padding=1),
               nn.ReLU(inplace=True),
               nn.Conv2d(512, 512, kernel_size=3, padding=1),
               nn.ReLU(inplace=True),
               nn.MaxPool2d(kernel_size=2, stride=2))

           self.classifier=nn.Sequential(
               nn.Dropout(p=0.5),
               #随机失活百分之五十，减少过拟合
               nn.Linear(512*7*7,2048),
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
           x=self.attention(x)
           x=self.features2(x)
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




