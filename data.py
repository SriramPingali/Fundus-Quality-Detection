import torch
import numpy as np
from PIL import Image
from os import listdir
from os.path import isfile, join
from torch.utils.data import Dataset
import torchvision.transforms as transforms
from torch.utils.data.sampler import SubsetRandomSampler

# Custom Dataset for DRIMDB dataset

class dataset(Dataset):
    def __init__(self, image_root):
        
        # Image root is the path to DRIMDB folder
        self.image_root = image_root
        self.data_len = 0
        
        # DRIMDB contains three folders which indicate the label of images.
        self.labels = listdir(image_root)
        self.data = {}
        
        # Augmentation
        self.transform = transforms.Compose([
            transforms.Resize((224)),
            transforms.RandomVerticalFlip(p=0.5),
            transforms.RandomHorizontalFlip(p=0.5),
            transforms.ToTensor(),
        ])
        
        for label in self.labels:
            for f in listdir('./DRIMDB/' + label):
                if isfile(join('./DRIMDB/' + label, f)):
                    self.data[join('./DRIMDB/', label, f)] = label
                    self.data_len += 1

    def __len__(self):
        return(self.data_len)
    
    def __getitem__(self, idx):
        img_path = list(self.data.keys())[idx]
        label = list(self.data.values())[idx]
        img = Image.open(img_path)
        img = img.convert('RGB')
        img = self.transform(img)
        return(img, label, img_path)

def dataloader(dataset, batch_size, validation_split, shuffle_dataset):
    random_seed= 42

    # Creating data indices for training and validation splits:
    dataset_size = len(dataset)
    indices = list(range(dataset_size))
    split = int(np.floor(validation_split * dataset_size))
    if shuffle_dataset :
        np.random.seed(random_seed)
        np.random.shuffle(indices)
    train_indices, val_indices = indices[split:], indices[:split]

    # Creating PT data samplers and loaders:
    train_sampler = SubsetRandomSampler(train_indices)
    valid_sampler = SubsetRandomSampler(val_indices)

    train_loader = torch.utils.data.DataLoader(dataset, batch_size=batch_size, 
                                               sampler=train_sampler)
    val_loader = torch.utils.data.DataLoader(dataset, batch_size=batch_size,
                                                    sampler=valid_sampler)
    return(train_loader, val_loader)