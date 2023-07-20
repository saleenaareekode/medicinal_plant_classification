#!/usr/bin/env python
# coding: utf-8

def train_test_split():
    ''' To split the images into train and validation folders.
    TRAIN_RATIO : The train test split ratio
    imsize : resize the image into desired size
    Arrange all different classes in separate folder inside source directory. 
    In the destination folder(train and val), the data will be splitted in specified ratio
    with same folder names.
    Eg: The directory, 'thulsi_dataset' contains folders 
    'Karpoora Tulsi','Rama Tulsi','Bhasma Tulsi','Mint Tulsi' and corresponding images
    '''

    import os
    import copy
    import shutil
    from PIL import Image

    TRAIN_RATIO = 0.80
    imsize = 256

    data_dir = '/home/saleena/ICFOSS/medicinal_plant'    
    images_dir = os.path.join(data_dir, 'thulsi_dataset') ##source folder
    train_dir = os.path.join(data_dir, 'train') ## destination folder
    test_dir = os.path.join(data_dir, 'val')## destination folder

    ## if the folders already exists, remove that and create again
    if os.path.exists(train_dir):
        shutil.rmtree(train_dir) 
    if os.path.exists(test_dir):
        shutil.rmtree(test_dir)

    os.makedirs(train_dir)
    os.makedirs(test_dir)

    classes = os.listdir(images_dir)

    for c in classes:    
        class_dir = os.path.join(images_dir, c)    
        images = os.listdir(class_dir)       
        n_train = int(len(images) * TRAIN_RATIO)    
        train_images = images[:n_train]
        test_images = images[n_train:]

        os.makedirs(os.path.join(train_dir, c), exist_ok = True)
        os.makedirs(os.path.join(test_dir, c), exist_ok = True)

        for image in train_images:           
            image_src = os.path.join(class_dir, image)
            image_dst = os.path.join(train_dir, c, image) 
            shutil.copyfile(image_src, image_dst)

        for image in test_images:
            image_src = os.path.join(class_dir, image)
            image_dst = os.path.join(test_dir, c, image) 
            shutil.copyfile(image_src, image_dst)

