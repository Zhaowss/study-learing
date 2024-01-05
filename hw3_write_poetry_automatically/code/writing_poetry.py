#导入我们所需要的库
import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from model import PoetryModel
import matplotlib.pyplot as plt
#################################################################参数的设置#####################################################################：

Batch_size =32                                                    # batch size大小设置为32
learning_rate = 5e-3                                                     # learn rate
embedding_dim = 128                                                      # embedding layer dimension
hidden_dim = 512                                                        # hidden layer dimension
epochs =10                                                             # epochs to train
verbose = True                                                           # print training process
device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')  # 指定运行的设备
trained_model_path = 'model.pth'                                         # 模型保存的地址
start_words = '湖光秋月两相和'                                           # 给定的首句诗词
start_words_acrostic = '轻舟已过万重山'                                
max_gen_len = 128         


##################################################################数据的准备#####################################################################
# 加载我门给定的数据集
def prepareData():
    
    # Load Tang poetry data including 3 parts: data, ix2word, word2ix
    datas = np.load("tang.npz", allow_pickle=True)
    data = datas['data']
    ix2word = datas['ix2word'].item()
    word2ix = datas['word2ix'].item()
    
    # 将数据转换为tensor的格式，并通过dataloader将数据加载成我们可迭代训练的数据

    data = torch.from_numpy(data)
    print(data.shape) # [57580, 125]
    dataloader = DataLoader(data,
                         batch_size = Batch_size,
                         shuffle = True,
                         num_workers = 0)
    print(len(dataloader)) # 3599
    
    return dataloader, ix2word, word2ix

##################################################################数据的训练#####################################################################

def train(dataloader, ix2word, word2ix):
  

    # 初始化我们的模型：
    model = PoetryModel(len(word2ix), embedding_dim, hidden_dim)

    #将模型指定到我们的设备上
    model.to(device)
    
    #定义优化器和损失函数
    optimizer = torch.optim.Adam(model.parameters(), lr = learning_rate)
    criterion = nn.CrossEntropyLoss()

    # 开始训练
    Loss_list=[]
    for epoch in range(epochs):
        running_loss=0.0
        for batch_idx, data in enumerate(dataloader):
            data = data.long().transpose(1, 0).contiguous()
            data = data.to(device)
            input, target = data[:-1, :], data[1:, :]
            output, _ = model(input)
            loss = criterion(output, target.view(-1))
            running_loss += loss.item()
            
            if (batch_idx+1) % 899 == 0 & verbose:
                print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                    epoch+1, (batch_idx+1) * Batch_size, len(dataloader.dataset),
                    100. * (batch_idx+1) / len(dataloader), loss.item()))
                
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
        Loss_list.append(running_loss / len(dataloader))
    # 保存模型
    torch.save(model.state_dict(), 'model.pth')
    print('Finished Training')
    print("开始绘制训练曲线：---------------------------")
    x1 = np.arange(1, len(Loss_list) + 1)
    plt.plot(x1, Loss_list, '--', color='red', label='Train_loss')
    plt.title('model losses')
    plt.ylabel('Loss')
    plt.xlabel('epoch')
    plt.legend()
    plt.show()


##################################################################诗句生成#####################################################################
def generate(start_words, ix2word, word2ix):

    # 加载我们的模型：
    model = PoetryModel(len(word2ix), embedding_dim, hidden_dim)
    #加载训练好的模型的权重文件
    model.load_state_dict(torch.load(trained_model_path))
    #将模型指定到我们的设备中
    model.to(device)
    
    # 开始的句子
    results = list(start_words)
    start_word_len = len(start_words)
    
    input = torch.Tensor([word2ix['<START>']]).view(1, 1).long()
    input = input.to(device)
    hidden = None

    # 生成诗句小于最大的长度
    for i in range(max_gen_len):
        output, hidden = model(input, hidden)
    
        if i < start_word_len:
            w = results[i]
            input = input.data.new([word2ix[w]]).view(1, 1)

        else:
            top_index = output.data[0].topk(1)[1][0].item()
            w = ix2word[top_index]
            results.append(w)
            input = input.data.new([top_index]).view(1, 1)
    
        if w == '<EOP>':
            del results[-1]
            break
            
    return results


def gen_acrostic(start_words, ix2word, word2ix):

    model = PoetryModel(len(word2ix), embedding_dim, hidden_dim)
    model.load_state_dict(torch.load(trained_model_path))
    model.to(device)
    results = []
    start_word_len = len(start_words)
    input = (torch.Tensor([word2ix['<START>']]).view(1, 1).long())
    input = input.to(device)
    hidden = None

    index = 0  # index of the character in start_words
    pre_word = '<START>'  # pre_word

    for i in range(max_gen_len):
        output, hidden = model(input, hidden)
        top_index = output.data[0].topk(1)[1][0].item()
        w = ix2word[top_index]
        if (pre_word in {u'。', u'！', '<START>'}):

            if index == start_word_len:
                break

            else:
                w = start_words[index]
                index += 1
                input = (input.data.new([word2ix[w]])).view(1, 1)

        else:
            input = (input.data.new([word2ix[w]])).view(1, 1)

        results.append(w)
        pre_word = w

    return results




if __name__ == '__main__':
        dataloader, ix2word, word2ix = prepareData()
        train(dataloader, ix2word, word2ix)
        results = generate(start_words, ix2word, word2ix)
        print(results)
        print(len(results))
        results_acrostic = gen_acrostic(start_words_acrostic, ix2word, word2ix)
        print(results_acrostic)