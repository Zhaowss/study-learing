import torch.nn as nn
import torch.nn.functional as F
import torch
#首先我们需要定义网络的残差块
class BasicBlock(nn.Module):
    #18层和三十四层所对应的残差结构块
    #expansion这里主要是定义的看主分支上的卷积核的个数是否发生变化

    expansion=1
    #用于标记残差结构中的主分支上的这个有没有发生卷积核的个数的变化
    def __init__(self,in_channel,out_channel,stride=1,downsample=None):
        #定义初始化，传入响应的参数的个数
        #下采样的残差结构
        super(BasicBlock,self).__init__()
        self.conv1=nn.Conv2d(in_channels=in_channel,out_channels=out_channel,kernel_size=3,stride=stride,padding=1,bias=False)
        self.bn1=nn.BatchNorm2d(out_channel)
        self.relu=nn.ReLU()
        self.conv2=nn.Conv2d(in_channels=out_channel,out_channels=out_channel,kernel_size=3,stride=1,padding=1,bias=False)
        self.bn2=nn.BatchNorm2d(out_channel)
        self.downsample=downsample

    def forward(self,x):
        identity=x
        if self.downsample is not None:
            identity=self.downsample(x)
        out=self.conv1(x)
        out=self.bn1(out)
        out=self.relu(out)

        out=self.conv2(out)
        out=self.bn2(out)
        out+=identity
        #输出加上捷径的输出后再通过relu的激活函数
        out=self.relu(out)

        return out


class Bottleneck(nn.Module):
      expansion=4
      #这里定义为四是因为我们的残差模块中的第三层的卷积核的深度变为输入的四倍
      def __init__(self,in_channel,out_channel,stride=1,downsample=None):
          super(Bottleneck,self).__init__()


          self.conv1 = nn.Conv2d(in_channels=in_channel, out_channels=out_channel, kernel_size=1, stride=1,
                                  bias=False)
          self.bn1 = nn.BatchNorm2d(out_channel)
          self.relu = nn.ReLU(inplace=True)
          self.conv2 = nn.Conv2d(in_channels=out_channel, out_channels=out_channel, kernel_size=3, stride=stride, padding=1,
                                 bias=False)
          self.bn2 = nn.BatchNorm2d(out_channel)

          self.conv3=nn.Conv2d(in_channels=out_channel,out_channels=out_channel*self.expansion,kernel_size=1,stride=1,bias=False)
          self.bn3=nn.BatchNorm2d(out_channel*self.expansion)

          self.downsample = downsample

      def forward(self,x):
           identity=x
           if self.downsample is not None:
              identity=self.downsample(x)

           out=self.conv1(x)
           out=self.bn1(out)
           out=self.relu(out)

           out=self.conv2(out)
           out=self.bn2(out)
           out=self.relu(out)

           out=self.conv3(out)
           out=self.bn3(out)

           out+=identity
           out=self.relu(out)

           return out
class ResNet(nn.Module):
      def __init__(self,block,block_num,num_classes=1000,include_top=True):
           super(ResNet,self).__init__()
           self.include_top=include_top
           self.in_channel=64
           self.conv1=nn.Conv2d(3,self.in_channel,kernel_size=7,stride=2,padding=3,bias=False)
           self.bn1=nn.BatchNorm2d(self.in_channel)
           self.relu=nn.ReLU(inplace=True)
           self.maxpool=nn.MaxPool2d(kernel_size=3,stride=2,padding=1)
           self.layer=self._make_layer(block,64,block_num[0])
           self.layer1=self._make_layer(block,128,block_num[1],stride=2)
           self.layer2=self._make_layer(block,256,block_num[2],stride=2)
           self.layer3=self._make_layer(block,512,block_num[3],stride=2)
           if self.include_top:
               self.avgpool=nn.AdaptiveAvgPool2d((1,1))
               self.fc=nn.Linear(512*block.expansion,num_classes)

           for m in self.modules():
               if isinstance(m,nn.Conv2d):
                   #这里采用开明初始化的正态分布初始化，
                   nn.init.kaiming_normal_(m.weight,mode='fan_out',nonlinearity='leaky_relu')



      def _make_layer(self,block,channel,block_num,stride=1):
         #定义下采样u之为空
          downsample=None
          if stride !=1 or self.in_channel != channel*block.expansion:
              downsample=nn.Sequential(
                  nn.Conv2d(self.in_channel,channel*block.expansion,kernel_size=1,stride=stride,bias=False),
                  nn.BatchNorm2d(channel*block.expansion)
              )
         #判断生成我们的下采样的函数
          layers=[]
          layers.append(block(self.in_channel,channel,stride=stride,downsample=downsample))
          self.in_channel=channel*block.expansion

          for _ in range(1,block_num):
              layers.append(block(self.in_channel,channel))

          return nn.Sequential(*layers)

      def forward(self,x):
          x=self.conv1(x)
          x=self.bn1(x)
          x=self.relu(x)
          x=self.maxpool(x)
          x=self.layer(x)
          x=self.layer1(x)
          x=self.layer2(x)
          x=self.layer3(x)

          if self.include_top:
              x=self.avgpool(x)
              x=torch.flatten(x,1)
              x=self.fc(x)
          return x


def resnet18(num_classes=1000,include_top=True):
    return ResNet(BasicBlock,[2,2,2,2],num_classes=num_classes,include_top=include_top)




def resnet34(num_classes=1000,include_top=True):
    return ResNet(BasicBlock,[3,4,6,3],num_classes=num_classes,include_top=include_top)


def resnet101(num_classes=1000,include_top=True):
    return ResNet(Bottleneck,[3, 4, 23, 3],num_classes=num_classes,include_top=include_top)

def resnet50(num_classes=1000,include_top=True):
    return ResNet(Bottleneck,[3,4,6,3],num_classes=num_classes,include_top=include_top)


data_x=torch.rand((32,3,224,224))

model=resnet18()
#model1=resnet101()
pred=model(data_x)
#pred1=model1(data_x)
print(model)

print(pred.shape)
#print(pred1.shape)