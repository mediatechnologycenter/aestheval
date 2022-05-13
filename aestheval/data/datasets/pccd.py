# Originally found in https://github.com/lucidrains/DALLE-pytorch
from pathlib import Path
import os
import io
import json
import torch
from torchvision import transforms
from PIL import Image
from torch.utils.data import Dataset
import pandas as pd

class PCCD(Dataset):
    def __init__(self,
                 split: str,
                 data_path: str = "data/PCCD",
                 split_path: str = "aestheval/data/datasets/datasplits/PCCD",
                 transform=None,
                 ):
        """Create a text image dataset from a directory with congruent text and image names.

        Args:
            folder (str): Folder containing images and text files matched by their paths' respective "stem"
        """
        data_path = Path(data_path)
        split_file = os.path.join(split_path, f"guru_{split.lower()}.json")

        with open(split_file, 'r') as f:
            data = json.load(f)

        self.image_folder = os.path.join(data_path, "images", "full")
        
        # The order of these attributes it's important to match with the order of scores
        self.attributes = ['general_impression', 'subject_of_photo', 'composition',
                         'use_of_camera', 'depth_of_field', 'color_lighting',
                         'focus']
        self.selected_keys = self.attributes + ['description','title', 'score', 'category']

        #If sentiment is already in data
        if "sentiment" in data[0].keys():
            self.selected_keys = self.selected_keys + ["sentiment"]
        
        
        self.dataset = []
        for d in data:
            dic = {k: d[k] for k in self.selected_keys}
            dic['im_name'] = dic.pop('title') # Rename for readibility
            self.dataset.append(dic)
                
        self.transform = transform

        if transform is None:
            self.transform = transforms.ToTensor()
        self.is_train = True if split.lower() == 'train' else False

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, ind):
        data = self.dataset[ind]
        image_file = os.path.join(self.image_folder, data['im_name'])
        image = Image.open(image_file).convert('RGB')
        image = self.transform(image)

        return image, data