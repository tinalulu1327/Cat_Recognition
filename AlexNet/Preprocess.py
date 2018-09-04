"""
 PURPOSE : Dataset preprocess
 Modified by Xiaolu Zhang based on
    https://github.com/kratzert/finetune_alexnet_with_tensorflow/
"""

import numpy as np
import cv2
import tensorflow as tf


class ImageDataGenerator:
    def __init__(self, class_list, horizontal_flip=False, shuffle=False,
                 # mean value need to calculate later
                 mean=np.array ([104., 117., 124.]), scale_size=(227, 227),
                 # need to change to 15 later
                 nb_classes=12):

        # Init params
        self.horizontal_flip = horizontal_flip
        self.n_classes = nb_classes
        self.shuffle = shuffle
        self.mean = mean
        self.scale_size = scale_size
        self.pointer = 0

        self.read_class_list (class_list)

        if self.shuffle:
            self.shuffle_data ()

    def read_class_list(self, class_list):
        """
        Scan the image file and get the image paths and labels
        """
        with open (class_list) as f:
            lines = f.readlines ()
            self.images = []
            self.labels = []
            for l in lines:
                items = l.split ()
                self.images.append (items[0])
                self.labels.append (int (items[1]))

            # store total number of data
            self.data_size = len (self.labels)

    # normally used in ML
    def shuffle_data(self):
        """
        Random shuffle the images and labels
        """
        images = self.images[:]
        labels = self.labels[:]
        self.images = []
        self.labels = []

        # create list of permutated index and shuffle data according to list
        idx = np.random.permutation (len (labels))
        for i in idx:
            self.images.append (images[i])
            self.labels.append (labels[i])

    def reset_pointer(self):
        """
        reset pointer to begin of the list
        """
        self.pointer = 0

        if self.shuffle:
            self.shuffle_data ()

    def next_batch(self, batch_size):
        """
        This function gets the next n ( = batch_size) images from the path list
        and labels and loads the images into them into memory 
        """
        # Get next batch of image (path) and labels
        paths = self.images[self.pointer:self.pointer + batch_size]
        labels = self.labels[self.pointer:self.pointer + batch_size]

        # update pointer
        self.pointer += batch_size

        # Read images
        images = np.ndarray ([batch_size, self.scale_size[0], self.scale_size[1], 3])
        for i in range (len (paths)):
            print('../image/' + paths[i] + '.jpg')
            img = cv2.imread ('../image/' + paths[i] + '.jpg')
            
            # flip image at random if flag is selected
            if self.horizontal_flip and np.random.random () < 0.5:
                img = cv2.flip (img, 1)

            # rescale image
            #print(img)
            #print(self.scale_size[0])
            #print(self.scale_size[1])
            img = cv2.resize (img, (self.scale_size[0], self.scale_size[1]))
            img = img.astype (np.float32)

            # subtract mean
            img -= self.mean

            images[i] = img

        # Expand labels to one hot encoding
        # one_hot_labels = np.zeros ((batch_size, self.n_classes))
        # one_hot_labels = tf.one_hot(labels, self.n_classes)
        labels = [l-1 for l in labels]
        one_hot_labels = np.zeros([len(labels), self.n_classes])
        one_hot_labels[np.arange(len(labels)),
            list(map(int, labels))] = 1.0

        # return array of images and labels
        return images, one_hot_labels
