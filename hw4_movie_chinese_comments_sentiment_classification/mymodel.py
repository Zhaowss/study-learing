import torch.nn as nn
import torch.nn.functional as F
import torch

#定义我们的模型
class TextCNN(nn.Module):
    def __init__(self, config):
        super(TextCNN, self).__init__()
        update_w2v = config.update_w2v
        vocab_size = config.vocab_size
        n_class = config.n_class
        embedding_dim = config.embedding_dim
        num_filters = config.num_filters
        kernel_size = config.kernel_size
        drop_keep_prob = config.drop_keep_prob
        pretrained_embed = config.pretrained_embed
        
        # 使用预训练好的模型进行词向量的编码的处理
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.embedding.weight.data.copy_(torch.from_numpy(pretrained_embed))
        self.embedding.weight.requires_grad = update_w2v
        # 定义卷积层
        self.conv = nn.Conv2d(1,num_filters,(kernel_size,embedding_dim))
        # 随即失活，防止过拟合
        self.dropout = nn.Dropout(drop_keep_prob)
        # 全连接
        self.FC2= nn.Linear(num_filters,512)
        self.fc = nn.Linear(512, n_class)


    def forward(self, x):
        x = x.to(torch.int64) #[32,50]
        x = self.embedding(x) #[32,50,50]
        x = x.unsqueeze(1)    #[32,1,50,50]
        x = F.relu(self.conv(x)).squeeze(3)   #[32,256,48]卷积操作后，压缩掉第三个维度
        x = F.max_pool1d(x, x.size(2)).squeeze(2)  #[32,256]，池化操作后压缩掉第二个维度
        x = self.dropout(x)   #[32,256]              
        x=self.FC2(x)         #[32,512]
        x=self.dropout(x)
        x = self.fc(x)        #[32,2] 
        return x