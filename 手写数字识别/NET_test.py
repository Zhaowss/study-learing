import torch
from torch import nn
import torch
import torchvision
import torch.utils.data as Data
from torch import nn
import matplotlib as matplotlib
import matplotlib # 注意这个也要import一次
import matplotlib.pyplot as plt
from d2l import torch as d2l
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
        self.conv3 = nn.Sequential(
            nn.Conv2d(64, 64, 3, 1, 1),
            nn.ReLU(),
            nn.MaxPool2d(2, 2)
        )

        self.fc = nn.Sequential(
            nn.Linear(576, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU()
        )

        self.out = nn.Linear(64, 10)

    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)
        x= self.conv3(x)
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
##########################用于训练画图###################################################################
def evaluate_accuracy_gpu(net, data_iter, device=None): #@save
    if isinstance(net, nn.Module):
        net.eval()  # 设置为评估模式
        if not device:
            device = next(iter(net.parameters())).device
    # 正确预测的数量，总预测的数量
    metric = d2l.Accumulator(2)
    with torch.no_grad():
        for X, y in data_iter:
            if isinstance(X, list):
                # BERT微调所需的（之后将介绍）
                X = [x.to(device) for x in X]
            else:
                X = X.to(device)
            y = y.to(device)
            metric.add(d2l.accuracy(net(X), y), y.numel())
    return metric[0] / metric[1]

def train_ch6(net, train_iter, test_iter, num_epochs, lr, device):
    def init_weights(m):
        if type(m) == nn.Linear or type(m) == nn.Conv2d:
            nn.init.xavier_uniform_(m.weight)
    net.apply(init_weights)
    print('training on', device)
    net.to(device)
    optimizer = torch.optim.SGD(net.parameters(), lr=lr)
    loss = nn.CrossEntropyLoss()
    animator = d2l.Animator(xlabel='epoch', xlim=[1, num_epochs],
                            legend=['train loss', 'train acc', 'test acc'])
    timer, num_batches = d2l.Timer(), len(train_iter)
    for epoch in range(num_epochs):
        # 训练损失之和，训练准确率之和，样本数
        metric = d2l.Accumulator(3)
        net.train()
        for i, (X, y) in enumerate(train_iter):
            timer.start()
            optimizer.zero_grad()
            X, y = X.to(device), y.to(device)
            y_hat = net(X)
            l = loss(y_hat, y)
            l.backward()
            optimizer.step()
            with torch.no_grad():
                metric.add(l * X.shape[0], d2l.accuracy(y_hat, y), X.shape[0])
            timer.stop()
            train_l = metric[0] / metric[2]
            train_acc = metric[1] / metric[2]
            if (i + 1) % (num_batches // 5) == 0 or i == num_batches - 1:
                animator.add(epoch + (i + 1) / num_batches,
                             (train_l, train_acc, None))
        test_acc = evaluate_accuracy_gpu(net, test_iter)
        animator.add(epoch + 1, (None, None, test_acc))
    plt.show()
    print(f'loss {train_l:.3f}, train acc {train_acc:.3f}, '
          f'test acc {test_acc:.3f}')
    print(f'{metric[2] * num_epochs / timer.sum():.1f} examples/sec '
          f'on {str(device)}')
          
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

lr, num_epochs = 3e-4, 100
##########################用于训练画图###################################################################
train_ch6(Conv_Net1, train_loader,test_loader, num_epochs, lr,device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu"))        
##########################用于训练画图###################################################################

###########################自定义训练##################################################################

EPOCH = 10
for epoch in range(EPOCH):
        train(epoch)
###################################################################################################