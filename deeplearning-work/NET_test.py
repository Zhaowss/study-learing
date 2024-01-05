import torch
from torch import nn
import torch
import torchvision
import torch.utils.data as Data
from torch import nn
import matplotlib as matplotlib
import matplotlib # 注意这个也要import一次
import matplotlib.pyplot as plt
#下载mnist手写数据集
train_data=torchvision.datasets.MNIST(
    root='./data/',   #用于存放数据，放置在当前的位置
    train=True ,      #指定是用于训练的数据，false是指用于测试的数据
    transform=torchvision.transforms.ToTensor(), #将数据转换为tensor的格式
    download=True
)
test_data=torchvision.datasets.MNIST(
    root='./data/',   #用于存放数据，放置在当前的位置
    train=False ,      #指定是用于训练的数据，false是指用于测试的数据
    transform=torchvision.transforms.ToTensor(), #将数据转换为tensor的格式
    download=True
)
#批训练数据，50，1，28，28
#torch中的Dataloader是用来包装数据的工具，帮助我们快速的迭代数据，来实现批训练
train_loader=Data.DataLoader(
    dataset=train_data,
    batch_size=50,
    shuffle=True
)
test_loader=Data.DataLoader(
    dataset=test_data,
    batch_size=50,
    shuffle=False
)


#构建模型

class Conv_Net(nn.Module):
    def __init__(self):
        super(Conv_Net, self).__init__()

        self.conv1 = nn.Sequential(
            nn.Conv2d(1, 32, 3, 1, 1),
            nn.ReLU(),
            nn.AvgPool2d(2, 2)
        )

        self.conv2 = nn.Sequential(
            nn.Conv2d(32, 64, 3, 1, 1),
            nn.ReLU(),
            nn.MaxPool2d(2, 2)
        )

        self.fc = nn.Sequential(
            nn.Linear(64 * 7 * 7, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU()
        )

        self.out = nn.Linear(64, 10)

    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)
        x = x.view(x.size(0), -1)
        x = self.fc(x)
        output = self.out(x)
        return output

#创建优化器
# 获取优化器和损失函数
Conv_Net1 = Conv_Net()
optimizer = torch.optim.Adam(Conv_Net1.parameters(), lr=3e-4)
loss_func = nn.CrossEntropyLoss()
log_step_interval = 100  # 记录的步数间隔
print(Conv_Net1)


def train(epoch):
    running_loss = 0.0  # 这整个epoch的loss清零
    running_total = 0
    running_correct = 0
    for step, data in enumerate(train_loader, 0):
        inputs, target = data
        optimizer.zero_grad()
        # forward + backward + update
        outputs =Conv_Net1(inputs)
        loss = loss_func(outputs, target)
        loss.backward()
        optimizer.step()
        # 把运行中的loss累加起来，为了下面300次一除
        running_loss += loss.item()
        # 把运行中的准确率acc算出来
        _, predicted = torch.max(outputs.data, dim=1)
        running_total += inputs.shape[0]
        running_correct += (predicted == target).sum().item()
        if step %50 ==0:
           correct = 0
           total = 0
           with torch.no_grad():  # 测试集不用算梯度
              for data in test_loader:
                images, labels = data
                outputs = Conv_Net1(images)
                _, predicted = torch.max(outputs.data, dim=1)  # dim = 1 列是第0个维度，行是第1个维度，沿着行(第1个维度)去找1.最大值和2.最大值的下标
                total += labels.size(0)  # 张量之间的比较运算
                correct += (predicted == labels).sum().item()
           acc = correct / total
           print('[%d / %d]: Accuracy on test set: %.1f %% ' % (epoch+1, EPOCH, 100 * acc))  # 求测试的准确率，正确数/总数

EPOCH = 10
for epoch in range(EPOCH):
        train(epoch)

        
