import os
import sys
import json

import torch
import torch.nn as nn
from torchvision import transforms, datasets, utils
import matplotlib.pyplot as plt
import numpy as np
import torch.optim as optim
from tqdm import tqdm
import torch.optim as optim
from mymodel import MYnet



def main():
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    print("using {} device.".format(device))

    data_transform = {
        "train": transforms.Compose([transforms.RandomResizedCrop(224),
                                     transforms.RandomHorizontalFlip(),
                                     transforms.ToTensor(),
                                     transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))]),
        "val": transforms.Compose([transforms.Resize((224, 224)),  # cannot 224, must (224, 224)
                                   transforms.ToTensor(),
                                   transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])}

    train_dataset= datasets.ImageFolder('dataset\\train',data_transform["train"])
    train_num = len(train_dataset)
    flower_list = train_dataset.class_to_idx
    cla_dict = dict((val, key) for key, val in flower_list.items())
    # write dict into json file
    json_str = json.dumps(cla_dict, indent=4)
    with open('class_indices.json', 'w') as json_file:
        json_file.write(json_str)

    batch_size =16
    nw = 0
    print('Using {} dataloader workers every process'.format(nw))

    train_loader = torch.utils.data.DataLoader(train_dataset,
                                               batch_size=batch_size, shuffle=True,
                                               num_workers=nw)

    validate_dataset = datasets.ImageFolder('dataset\\val', data_transform["val"])
    val_num = len(validate_dataset)
    train_num = len(train_dataset)
    validate_loader = torch.utils.data.DataLoader(validate_dataset,
                                                  batch_size=4, shuffle=True,
                                                  num_workers=nw)

    print("using {} images for training, {} images for validation.".format(train_num,
                                                                           val_num))

    net=MYnet(clss_num=2)

    net.to(device)
    loss_function = nn.CrossEntropyLoss()
    # pata = list(net.parameters())
    optimizer = optim.Adam(net.parameters(), lr=0.0001)

    epochs = 30
    save_path = './MyNet.pth'
    best_acc = 0.0
    train_steps = len(train_loader)
    val_steps = len(validate_loader)
    Loss_list = []
    Val_acc = []
    Val_loss = []
    Train_acc=[]
    for epoch in range(epochs):
        # train
        net.train()
        running_loss = 0.0
        train_bar = tqdm(train_loader, file=sys.stdout)
        train_acc = 0.0
        for step, data in enumerate(train_bar):
            images, labels = data
            optimizer.zero_grad()
            outputs = net(images.to(device))
            predict_y = torch.max(outputs, dim=1)[1]
            train_acc += torch.eq(predict_y,labels.to(device)).sum().item()
            loss = loss_function(outputs, labels.to(device))
            loss.backward()
            optimizer.step()

            # print statistics
            running_loss += loss.item()

            train_bar.desc = "train epoch[{}/{}] loss:{:.3f}".format(epoch + 1,
                                                                     epochs,
                                                                     loss)

        # validate
        running_val_loss=0.0
        net.eval()
        acc = 0.0  # accumulate accurate number / epoch
        with torch.no_grad():
            val_bar = tqdm(validate_loader, file=sys.stdout)
            for val_data in val_bar:
                val_images, val_labels = val_data
                outputs = net(val_images.to(device))
                val_loss = loss_function(outputs,  val_labels.to(device))
                predict_y = torch.max(outputs, dim=1)[1]
                acc += torch.eq(predict_y, val_labels.to(device)).sum().item()
                running_val_loss += val_loss.item()

        val_accurate = acc / val_num
        train_accurate =train_acc / train_num
        print('[epoch %d] train_loss: %.3f  val_loss: %.3f  val_accuracy: %.3f train_accuracy: %.3f' %
              (epoch + 1, running_loss / train_steps,running_val_loss/val_steps,val_accurate,train_accurate))


        Loss_list.append(running_loss / train_steps)
        Val_acc.append(val_accurate)
        Val_loss.append(running_val_loss/val_steps)
        Train_acc.append(train_accurate)
        if val_accurate > best_acc:
            best_acc = val_accurate
            torch.save(net.state_dict(), save_path)

    print('Finished Training')
    print("开始绘制训练曲线：---------------------------")
    x1 = np.arange(1, len(Loss_list) + 1)
    y1 = Val_loss
    plt.plot(x1, y1, 'o-', color='blue', label='Val_loss')
    plt.plot(x1, Loss_list, '--', color='red', label='Train_loss')
    plt.title('comparison of model losses')
    plt.ylabel('Loss')
    plt.xlabel('epoch')
    plt.legend()
    plt.show()

    x1 = np.arange(1, len(Val_acc) + 1)
    y1 =Train_acc
    plt.plot(x1, y1, 'o-', color='blue', label='Train_acc')
    plt.plot(x1, Val_acc, '--', color='red', label='Val_acc')
    plt.title('comparison of model acc')
    plt.ylabel('acc')
    plt.xlabel('epoch')
    plt.legend()
    plt.show()



if __name__ == '__main__':
    main()