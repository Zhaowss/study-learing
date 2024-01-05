import torch
import os
import torchvision
import torch.nn as nn
from model import LeNet
import torch.optim as optim
import  matplotlib.pyplot as plt
from torchvision  import transforms,datasets,utils
import numpy as np
import json
import time
#导入一些必须的库
def main():
        transform=transforms.Compose(
            [transforms.RandomResizedCrop(32),
             transforms.ToTensor(),
             transforms.Normalize((0.5,0.5,0.5),(0.5,0.5,0.5))
            ]
        )
        #transfoerm 是图像的预处理的方法
        #transform.Totensor ：Converts a PIL Image or numpy.ndarray (H x W x C) in the range [0, 255] to a torch.FloatTensor of shape (C x H x W) in the range [0.0, 1.0]
        #本质就是将读入的图片转换为tensor，并将原始的图像的维度由长乘以宽乘以通道数，变为通道数乘以长乘以宽
        #Normalize就是对数据进行标准化的处理

        data_root = "deeplearning-work"
        image_path = data_root + "/data_set/flower_data/"
        train_dataset = datasets.ImageFolder(root="D:/zhuomian/deeplearning-work/class_1/train",
                                             transform=transform
                                             )


        train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=36,
                                                   shuffle=True, num_workers=0)





        classes=('plane','car','bird','cat','deer','dog','frog','horse','ship','truck'
        )

        net=LeNet()
        #实例化我们的模型
        Loos_function=nn.CrossEntropyLoss()
        #定义我们的损失函数,adam
        optimizer=optim.Adam(net.parameters(),lr=1e-3)
        #定义我们自己的优化器
        for epoch in range(10):
            run_loss=0
            for step,data in  enumerate(train_loader,start=0):
                inputs,label=data
                #image
                optimizer.zero_grad()

                outputs=net(inputs)
                loss=Loos_function(outputs,label)
                loss.backward()
                optimizer.step()

                run_loss+=loss.item()



                print('[%d, %5d] train_loss: %.3f ' %
                               (epoch + 1, step + 1, run_loss / 500))


        print('Finished Training')

        save_path = './Lenet.pth'
        torch.save(net.state_dict(), save_path)

if __name__=='__main__':
    main()
