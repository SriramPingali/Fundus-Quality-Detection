import torch
import numpy as np
import matplotlib.pyplot as plt

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

def encode(label):
    rep = torch.zeros(3, dtype = torch.long).to(device)
    if label == 'Good':
        rep[0] = 1
    elif label == 'Bad':
        rep[1] = 1
    elif label == 'Outlier':
        rep[2] = 1
    return(rep)

def encode_batch(batch):
    encode_tensor = None
    for i, label in enumerate(batch):
        rep = encode(label)
        if encode_tensor == None:
            encode_tensor_size = list(rep.size())
            encode_tensor_size.insert(0, len(batch))
            encode_tensor = torch.empty(*encode_tensor_size, dtype=rep.dtype, device=rep.device)
        encode_tensor[i, :] = rep
    return(encode_tensor)

def imshow(img):
    npimg = img.numpy()
    plt.imshow(np.transpose(npimg, (1, 2, 0)))
    plt.show()

def visualize_results(loss_b, acc_b):
    plt.figure(figsize = (18, 6))

    plt.subplot(1, 2, 1)
    plt.ylabel('loss')
    plt.plot(loss_b)

    plt.subplot(1, 2, 2)
    plt.plot(acc_b)

def evaluate(model, data_loader):
    total, correct = 0, 0
    for data in data_loader:
        inputs, labels = data
        OH_labels = encode_batch(labels)
        inputs = inputs.to(device)
        outputs = model.forward(inputs)
        pred = torch.max(outputs, 1)[1]
        total += len(labels)
        correct += (pred == torch.max(OH_labels, 1)[1]).sum().item()

    print(100 * correct / total)