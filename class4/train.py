import torch
import os
import torchvision
import torch.nn as nn
from model import GoogleNet
import torch.optim as optim
import  matplotlib.pyplot as plt
from torchvision  import transforms,datasets,utils
import numpy as np
import json
import time
#导入一些必须的库

def main():
        device=torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        print(device)
        data_transform={
        "train": transforms.Compose(
            [transforms.RandomResizedCrop(224),
             transforms.RandomHorizontalFlip(),
             transforms.ToTensor(),
             transforms.Normalize((0.5,0.5,0.5),(0.5,0.5,0.5))
            ]
        ),
        #transfoerm 是图像的预处理的方法
        #transforms.RandomHorizontalFlip()
        #transform.Totensor ：Converts a PIL Image or numpy.ndarray (H x W x C) in the range [0, 255] to a torch.FloatTensor of shape (C x H x W) in the range [0.0, 1.0]
        #本质就是将读入的图片转换为tensor，并将原始的图像的维度由长乘以宽乘以通道数，变为通道数乘以长乘以宽
        #Normalize就是对数据进行标准化的处理
        "val": transforms.Compose(
                [
                 transforms.Resize((224,224)),
                 transforms.ToTensor(),
                 transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
                 ]
        )}
        #获取根目录
        data_root=os.path.abspath(os.path.join(os.getcwd(),"../.."))
        image_path=data_root+"/data_set/flower_data/"
        train_dataset=datasets.ImageFolder(root=image_path+"/train",
                                           transform=data_transform["train"]
                                           )
        train_num=len(train_dataset)
        flower_list=train_dataset.class_to_idx
        cla_dict=dict((val,key) for key,val in flower_list.items())
        json_str=json.dumps(cla_dict,indent=4)
        with open('class_indices.json','w') as json_file:
             json_file.write(json_str)
        batch_size=32
        train_loader=torch.utils.data.DataLoader(
            train_dataset,
            batch_size=batch_size,
            shuffle=True,
            num_workers=0
        )
        validate_dataset=datasets.ImageFolder(
            root=image_path+"/val",
            transform=data_transform["val"]
        )
        val_num=len(validate_dataset)
        validate_loader=torch.utils.data.DataLoader(
            validate_dataset,
            batch_size=4,
            shuffle=True,
            num_workers=0
        )

        #查看训练集和测试集的batch中的图片的信息和label的信息
        test_data_iter=iter(validate_loader)
        test_image,test_label=test_data_iter.next()
        # def imshow(img):
        #     img=img/2+0.5
        #     npimg=img.numpy()
        #     plt.imshow(np.transpose(npimg,(1,2,0)))
        #     plt.show()
        # print(' '.join('%5s' %cla_dict[test_label[j].item()] for j in range(4)))
        # imshow(utils.make_grid(test_image))



        net=GoogleNet(clss_num=5)
        #实例化我们的模型
        net.to(device)
        #将我们的网络移植到初始化的设备上，cpu 或者GPU版本
        Loos_function=nn.CrossEntropyLoss()
        #定义我们的损失函数
        optimizer=optim.Adam(net.parameters(),lr=1e-3)
        save_path='./Googlenet.pth'
        best_acc=0
        #定义最佳的模型。
        #定义我们自己的优化器
        for epoch in range(10):
            #此处调用这个可以在训练的过程中调用我门的dropoot方法

            net.train()
            running_loss=0
            t1=time.perf_counter()
            for step,data in  enumerate(train_loader,start=0):
                inputs,label=data
                optimizer.zero_grad()
                x,aux1,aux2=net(inputs).to(device)
                loss1=Loos_function(x,label.to(device))
                loss2 = Loos_function(aux1, label.to(device))
                loss3 = Loos_function(aux2, label.to(device))
                loss=loss1+loss2*0.3+loss3*0.3
                loss.backward()
                optimizer.step()

                running_loss+=loss.item()

                rate=(step+1)/len(train_loader)

                a="*"*int(rate*50)
                b="."*int((1-rate)*50)
                print("\rtrain loss:{:^3.0f}%[{}->{}]{:.3f}".format(int(rate*100),a,b,loss),end="")
            print(time.perf_counter()-t1)
            #测试GPU设备
            net.eval()
            acc=0
            #启动net.eval之后模型将开始关闭dropout的操作，防止继续进行模型的权重丢失的操作
            with torch.no_grad():
                #晴空梯度的信息
                outputs = net(test_image).to(device)
                predict_y = torch.max(outputs, dim=1)[1]
                acc+=(predict_y==test_label.to(device).sum().item())
            accurate_test=acc/val_num
            if accurate_test>best_acc:
                best_acc=accurate_test

                torch.save(net.state_dict(), save_path)
            print('[epoch %d] train_loss:%.3f    test_acc:%.3f'%(epoch+1,running_loss,acc/val_num))
        print("finished training!")




if __name__=='__main__':
    main()
