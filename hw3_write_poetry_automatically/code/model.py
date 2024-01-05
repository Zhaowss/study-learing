import torch
import torch.nn as nn
#定义我们的模型：


class PoetryModel(nn.Module):
    def __init__(self, num_embeddings, embedding_dim, hidden_dim):
        super(PoetryModel, self).__init__()
        self.embedding = nn.Embedding(num_embeddings, embedding_dim)
        self.hidden_dim = hidden_dim
        self.lstm = nn.LSTM(embedding_dim, self.hidden_dim, num_layers=2)
        self.MYliner=nn.Linear(self.hidden_dim,256)
        self.linear = nn.Linear(256, num_embeddings)

    def forward(self, input, hidden = None):
        seq_len, batch_size = input.size()
        
        if hidden is None:
            h_0 = input.data.new(2, batch_size, self.hidden_dim).fill_(0).float()
            c_0 = input.data.new(2, batch_size, self.hidden_dim).fill_(0).float()
        else:
            h_0, c_0 = hidden

        embeds = self.embedding(input)
        output, hidden = self.lstm(embeds, (h_0, c_0))
        output=self.MYliner(output.view(seq_len * batch_size, -1))
        output = self.linear(output)
        return output, hidden