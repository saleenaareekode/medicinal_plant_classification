#!/usr/bin/env python
# coding: utf-8


def resize_image():
    '''Resize all the images captured into a common size of 1048
    The images have been captured in various dimensions. 
    The size 1048 has choosen so that the compression won't affect the clarity of the image much.
    This will also reduce the storage space required
    '''
    import cv2
    import os
    import shutil


    shape = 1048

    data_dir = '/home/saleena/ICFOSS/medicinal_plant/8classes'
    images_dir = os.path.join(data_dir, 'images')
    resized_img_dir = os.path.join(data_dir, 'resized_imges')
    classes = os.listdir(images_dir)

    #remove the destination folder if it already exists
    if os.path.exists(resized_img_dir):
    shutil.rmtree(resized_img_dir) 

    #create new destination folder
    os.makedirs(resized_img_dir)

    for c in classes:    
    count = 0
    #source directory
    class_dir = os.path.join(images_dir, c)
    #destination directory
    os.makedirs(os.path.join(resized_img_dir, c), exist_ok = True)

    destination_dir = os.path.join(resized_img_dir, c)

    #print(destination_dir)
    images = os.listdir(class_dir)  

    for img in images:
        img_path = os.path.join(class_dir, img)
        img = cv2.imread(img_path)

        img = cv2.resize(img, (shape, shape)) 
        cv2.imwrite(destination_dir+'/img_'+str(count)+'.jpg',img)
        count = count+1
        pass







