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
from mymodel import TextCNN
import gensim
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
from collections import Counter
from torch.utils.data import TensorDataset, DataLoader


####################################构建词汇表并存储####################################
def build_word2id(save_to_path=None):
    """
    :param save_to_path: path to save word2id
    :return: word2id dictionary {word: id}
    """
    word2id = {'_PAD_': 0}
    path = ['./Dataset/train.txt', './Dataset/validation.txt']
    
    # write the index to word2id[word]
    for _path in path:
        with open(_path, encoding='utf-8') as f:
            for line in f.readlines():
                sp = line.strip().split()
                for word in sp[1:]:
                    if word not in word2id.keys():
                        word2id[word] = len(word2id)
    if save_to_path:                    
        with open(save_to_path, 'w', encoding='utf-8') as f:
            for w in word2id:
                f.write(w+'\t')
                f.write(str(word2id[w]))
                f.write('\n')
    
    return word2id

########################################基于预训练好的 word2vec 构建训练语料中所含词语的 word2vec#################################################################3
def build_word2vec(fname, word2id, save_to_path=None):
    """
    :param fname:预训练的 word2vec
    :param word2id: 语料文本中包含的词汇集
    :param save_to_path:# 保存训练语料库中的词组对应的 word2vec 到本地
    :return:语料文本中词汇集对应的 word2vec 向量{id: word2vec}
    """
    n_words = max(word2id.values()) + 1
    model = gensim.models.KeyedVectors.load_word2vec_format(fname, binary=True)
    wordid_vecs = np.array(np.random.uniform(-1., 1., [n_words, model.vector_size]))
    for word in word2id.keys():
        try:
            wordid_vecs[word2id[word]] = model[word]
        except KeyError:
            pass
    if save_to_path:
        with open(save_to_path, 'w', encoding='utf-8') as f:
            for vec in wordid_vecs:
                vec = [str(w) for w in vec]
                f.write(' '.join(vec))
                f.write('\n')
    return wordid_vecs

########################################################定义初始化的参数##################################################################################
class CONFIG():
    update_w2v = True           # # 是否在训练中更新 w2v
    vocab_size = 58954          #词汇量，与 word2id 中的词汇量一致
    n_class = 2                 # 分类数：分别为 pos 和 neg
    embedding_dim = 50          # 词向量维度
    drop_keep_prob = 0.5        # dropout 层，参数 keep 的比例
    num_filters = 256           #  卷积层 filter 的数量
    kernel_size = 3             # 卷积核的尺寸
    pretrained_embed = build_word2vec('./Dataset/wiki_word2vec_50.bin',build_word2id('./Dataset/word2id.txt')) 
#

def load_corpus(path, word2id, max_sen_len=50):
  
    _, clas2id = class_to_id()
    contents, labels = [], []
    with open(path, encoding='utf-8') as f:
        for line in f.readlines():
            sp = line.strip().split()
            # print(sp)
            label = sp[0]
            content = [word2id.get(w, 0) for w in sp[1:]]
            content = content[:max_sen_len]
            if len(content) < max_sen_len:
                content += [word2id['_PAD_']] * (max_sen_len - len(content))
            labels.append(label)
            contents.append(content)
    counter = Counter(labels)
    print('总样本数为：%d' % (len(labels)))
    print('各个类别样本数如下：')
    for w in counter:
        print(w, counter[w])

    contents = np.asarray(contents)
    
    labels_arr = np.array([clas2id[l] for l in labels])
    
    labels_onehot = np.array([[0,0]] * len(labels))
    for idx, val in enumerate(labels):
        if val == '0':
            labels_onehot[idx][0]=1
        else:
            labels_onehot[idx][1]=1

    return contents, labels_arr, labels_onehot


def class_to_id(classes=None):
    """
    :param classes: label to classify, default is 0:pos, 1:neg
    :return: classes = ['0', '1'], {classes：id} = {'0': 0, '1': 1}
    """
    if not classes:
        classes = ['0', '1']
    clas2id = {clas: idx for (idx, clas) in enumerate(classes)}
    return classes, clas2id


def train(dataloader,train_dataset):

    # 初始化我们的模型
    model = TextCNN(config)
    if model_path:
        model.load_state_dict(torch.load(model_path))
    model.to(device)
    
    # 设置优化器和我们的损失函数
    optimizer = torch.optim.Adam(model.parameters(), lr = learning_rate)
    criterion = nn.CrossEntropyLoss()
    Loss_list=[]
    Train_acc=[]
    # 开始训练
    for epoch in range(epochs):
        train_acc = 0.0
        running_loss=0.0
        for batch_idx, (batch_x, batch_y) in enumerate(dataloader):
            batch_x, batch_y = batch_x.to(device), batch_y.to(device)
            output = model(batch_x)
            loss = criterion(output, batch_y)
            predict_y = torch.max(output, dim=1)[1]
            train_acc += torch.eq(predict_y,batch_y.to(device)).sum().item()
            running_loss += loss.item()
            if batch_idx % 200 == 0 & verbose:
                print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                    epoch+1, batch_idx * len(batch_x), len(dataloader.dataset),
                    100. * batch_idx / len(dataloader), loss.item()))
            
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
        train_accurate =train_acc / len(train_dataset)
        print('[epoch %d] train_loss: %.3f  train_accuracy: %.3f' %
              (epoch + 1, running_loss / len(dataloader),train_accurate))


        Loss_list.append(running_loss / len(dataloader))
        Train_acc.append(train_accurate)

    #绘制训练过程中的损失和准确率曲线
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

    x1 = np.arange(1, len(Train_acc) + 1)
    plt.plot(x1, Train_acc, 'o-', color='blue', label='Train_acc')
    plt.title('model acc')
    plt.ylabel('acc')
    plt.xlabel('epoch')
    plt.legend()
    plt.show()

def predict(dataloader):

    #加载训练好的模型
    model = TextCNN(config)
    model.load_state_dict(torch.load("model.pth"))
    model.eval()
    model.to(device)
    
    # 测试
    count, correct, real_predict_00, real_predict_01, real_predict_10, real_predict_11 = 0, 0, 0, 0, 0, 0
    for _, (batch_x, batch_y) in enumerate(dataloader):
        batch_x, batch_y = batch_x.to(device), batch_y.to(device)
        output = model(batch_x)
        count += len(batch_x)
        correct += (output.argmax(1) == batch_y).float().sum().item()
        real_predict_00 += np.array([(output.argmax(1)[idx] == 0 and batch_y[idx] == 0).float().cpu().numpy() for (idx, _) in enumerate(batch_y)]).sum().item()
        real_predict_01 += np.array([(output.argmax(1)[idx] == 0 and batch_y[idx] == 1).float().cpu().numpy() for (idx, _) in enumerate(batch_y)]).sum().item()
        real_predict_10 += np.array([(output.argmax(1)[idx] == 1 and batch_y[idx] == 0).float().cpu().numpy() for (idx, _) in enumerate(batch_y)]).sum().item()
        real_predict_11 += np.array([(output.argmax(1)[idx] == 1 and batch_y[idx] == 1).float().cpu().numpy() for (idx, _) in enumerate(batch_y)]).sum().item()
    
    # calculate accuracy, precision, recall, F1_score, confusion_matrix
    accuracy = correct/count
    precision = real_predict_00 / (real_predict_00 + real_predict_10)
    recall = real_predict_00 / (real_predict_00 + real_predict_01)
    F1_score = 2*precision*recall/(precision+recall)
    confusion_matrix = [[real_predict_00, real_predict_01], [real_predict_10, real_predict_11]]
    print('The accuracy, precision, recall, F1_score, confusion_matrix of test is\n{:.2f}% \n{} \n{} \n{} \n{}.'.format(100*accuracy, precision, recall, F1_score, confusion_matrix))

    
if __name__ == '__main__':
    word2id = build_word2id('./Dataset/word2id.txt')
    print(type(word2id), len(word2id))
    word2vec = build_word2vec('./Dataset/wiki_word2vec_50.bin', word2id)
    assert word2vec.shape == (58954, 50)
    print(word2vec)
    print('train corpus load: ')
    train_contents, train_labels, _ = load_corpus('./Dataset/train.txt', word2id, max_sen_len=50)
    print('\nvalidation corpus load: ')
    val_contents, val_labels, _ = load_corpus('./Dataset/validation.txt', word2id, max_sen_len=50)
    print('\ntest corpus load: ')
    test_contents, test_labels, _ = load_corpus('./Dataset/test.txt', word2id, max_sen_len=50)
    config = CONFIG()          # config the parameters of model
    learning_rate = 0.001      # learn rate     
    batch_size = 32            # batch size
    epochs = 30           # epoches
    model_path = None          # path of pre-trained model
    verbose = True             # print the training process
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    print(device)
    contents = np.vstack([train_contents, val_contents])
    labels = np.concatenate([train_labels, val_labels])
    train_dataset = TensorDataset(torch.from_numpy(contents).type(torch.float), 
                                torch.from_numpy(labels).type(torch.long))
    train_dataloader = DataLoader(dataset = train_dataset, batch_size = batch_size, 
                                shuffle = True, num_workers = 2)
    train(train_dataloader,train_dataset)
    test_dataset = TensorDataset(torch.from_numpy(test_contents).type(torch.float), 
                            torch.from_numpy(test_labels).type(torch.long))
    test_dataloader = DataLoader(dataset = test_dataset, batch_size = batch_size, 
                            shuffle = False, num_workers = 2)
    predict(test_dataloader)

