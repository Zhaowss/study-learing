import torch.nn as nn
import torch.nn.functional as F
import torch
import numpy as np
import matplotlib.pyplot as plt
#传入的cfg 是一个配置变量，
def get_feature(module, input, output):
    feature = output.cpu().detach().numpy()
    for feature_map in feature[0:3]:
        # [N, C, H, W] -> [C, H, W]
        im = np.squeeze(feature_map)
        # [C, H, W] -> [H, W, C]
        im = np.transpose(im, [1, 2, 0])

        # show top 12 feature maps
        plt.figure()
        for i in range(12):
            ax = plt.subplot(3, 4, i + 1)
            # [H, W, C]
            plt.imshow(im[:, :, i])
        plt.show()

class GoogleNet(nn.Module):
       #是否使用辅助分类器
       def __init__(self,clss_num=1000,aux_logits=True,init_weights=False):
           super(GoogleNet,self).__init__()
           self.aux_logits=aux_logits
           if init_weights:
               self._initialize_weights()

           self.conv1=BasicConv2d(3,64,kernel_size=7,stride=2,padding=3)
           self.maxpool1=nn.MaxPool2d(3,stride=2,ceil_mode=True)  #cell_mode=True 池化后的尺度选择向上取整
           self.conv2=BasicConv2d(64,64,kernel_size=1)
           self.conv3=BasicConv2d(64,192,kernel_size=3,padding=1)
           self.maxpool2=nn.MaxPool2d(3,stride=2,ceil_mode=True)

           self.inception3a=Inception(192,64,96,128,16,32,32)
           self.inception3b=Inception(256,128,128,192,32,96,64)
           self.maxpool3=nn.MaxPool2d(3,stride=2,ceil_mode=True)

           self.inception4a = Inception(480,192,96,208,16,48,64)
           self.inception4b = Inception(512, 160, 112, 224, 24, 64, 64)
           self.inception4c = Inception(512, 128, 128, 256, 24, 64, 64)
           self.inception4d = Inception(512, 112, 144, 288, 32, 64, 64)
           self.inception4e = Inception(528, 256, 160, 320, 32, 128, 128)
           self.maxpool4 = nn.MaxPool2d(2,stride=2,ceil_mode=True)

           self.inception5a=Inception(832,256,160,320,32,128,128)
           self.inception5b=Inception(832,384,192,384,48,128,128)

           if self.aux_logits:
               self.aux1=InceptionAux(512,num_classes=clss_num)
               self.aux2=InceptionAux(528,num_classes=clss_num)
           self.avgpool=nn.AdaptiveAvgPool2d((1,1))
           self.dropout=nn.Dropout(0.4)
           #权重丢失的比列为百分之四十
           self.fc=nn.Linear(1024,clss_num)
           if init_weights:
               self._initialize_weights()
       # 定义我们的正向传播的过程
       def forward(self,x):
           x=self.conv1(x)

           x=self.maxpool1(x)

           x=self.conv2(x)
           x=self.conv3(x)

           x=self.maxpool2(x)


           x=self.inception3a(x)
           x=self.inception3b(x)
           x=self.maxpool3(x)
           x=self.inception4a(x)
           if self.training and self.aux_logits:
               aux1=self.aux1(x)
           x=self.inception4b(x)
           x=self.inception4c(x)
           x=self.inception4d(x)

           if self.training and self.aux_logits:
               aux2=self.aux2(x)

           x=self.inception4e(x)
           x=self.maxpool4(x)
           x=self.inception5a(x)
           x=self.inception5b(x)

           x=self.avgpool(x)
           x=torch.flatten(x , start_dim=1)
           x=self.dropout(x)

           x=self.fc(x)

           if self.training and self.aux_logits:
              return x, aux1 , aux2

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
#定义我们的inception的结构
class Inception(nn.Module):
    def __init__(self,in_channels,ch1X1,ch3X3red,ch3X3,ch5x5red,ch5X5,pool_proj):
        super(Inception, self).__init__()
        self.branch1=BasicConv2d(in_channels,ch1X1,kernel_size=1)

        self.branch2=nn.Sequential(
            BasicConv2d(in_channels,ch3X3red,kernel_size=1),
            BasicConv2d(ch3X3red,ch3X3,kernel_size=3,padding=1)
        )
        self.branch3 = nn.Sequential(
            BasicConv2d(in_channels, ch5x5red, kernel_size=1),
            BasicConv2d(ch5x5red,ch5X5, kernel_size=5, padding=2)
        )
        self.branch4 = nn.Sequential(
            nn.MaxPool2d(kernel_size=3,stride=1,padding=1),
            BasicConv2d(in_channels,pool_proj, kernel_size=1)
        )
    def forward(self,x):
        branch1=self.branch1(x)
        branch2 = self.branch2(x)
        branch3= self.branch3(x)
        branch4 = self.branch4(x)
        outputs=[branch1,branch2,branch3,branch4]
        return torch.cat(outputs,dim=1)






#定义辅助分类器
class InceptionAux(nn.Module):
    def __init__(self,in_channels,num_classes):
        super(InceptionAux, self).__init__()
        self.averagePool=nn.AvgPool2d(kernel_size=5,stride=3)
        self.conv=BasicConv2d(in_channels,128,kernel_size=1)

        self.fc1=nn.Linear(2048,1024)
        self.fc2=nn.Linear(1024,num_classes)
    def forward(self,x):
        x=self.averagePool(x)
        x=self.conv(x)
        x=torch.flatten(x,start_dim=1)
        x=F.dropout(x,0.5,training=self.training)
        x=F.relu(self.fc1(x),inplace=True)
        x=F.dropout(x,0.5,training=self.training)
        x=self.fc2(x)
        return x

class BasicConv2d(nn.Module):
    #初始化传入三个参数，输入的深度，输出特征矩阵的深度
    def __init__(self,in_channels,out_channels,**kwargs):
        super(BasicConv2d,self).__init__()
        self.conv=nn.Conv2d(in_channels=in_channels,out_channels=out_channels,**kwargs)
        self.relu=nn.ReLU(inplace=True)

    def forward(self,x):
        x=self.conv(x)
        x=self.relu(x)
        return x

input1=torch.rand([32,3,224,224])
model=GoogleNet(clss_num=5,aux_logits=False,init_weights=True)

# 注册钩子
handle = model.inception3a.register_forward_hook(get_feature)

# 前向传递
output = model(input1)


handle.remove()


