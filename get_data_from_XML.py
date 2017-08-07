import numpy as np
import os
from xml.etree import ElementTree

class XML_preprocessor(object):

    def __init__(self, data_path):
        self.path_prefix = data_path
        self.num_classes = 40
        self.data = dict()
        self._preprocess_XML()

    def _preprocess_XML(self):
        filenames = os.listdir(self.path_prefix)
        for filename in filenames:
            tree = ElementTree.parse(self.path_prefix + filename)
            root = tree.getroot()
            bounding_boxes = []
            one_hot_classes = []
            size_tree = root.find('size')
            width = float(size_tree.find('width').text)
            height = float(size_tree.find('height').text)
            for object_tree in root.findall('object'):
                for bounding_box in object_tree.iter('bndbox'):
                    xmin = float(bounding_box.find('xmin').text)/width
                    ymin = float(bounding_box.find('ymin').text)/height
                    xmax = float(bounding_box.find('xmax').text)/width
                    ymax = float(bounding_box.find('ymax').text)/height
                bounding_box = [xmin,ymin,xmax,ymax]
                bounding_boxes.append(bounding_box)
                class_name = object_tree.find('action').text
                one_hot_class = self._to_one_hot_2(class_name)
                one_hot_classes.append(one_hot_class)
            image_name = root.find('filename').text
            bounding_boxes = np.asarray(bounding_boxes)
            one_hot_classes = np.asarray(one_hot_classes)
            image_data = np.hstack((bounding_boxes, one_hot_classes))
            self.data[image_name] = image_data

    def _to_one_hot(self,name):
        one_hot_vector = [0] * self.num_classes
        if name == 'aeroplane':
            one_hot_vector[0] = 1
        elif name == 'bicycle':
            one_hot_vector[1] = 1
        elif name == 'bird':
            one_hot_vector[2] = 1
        elif name == 'boat':
            one_hot_vector[3] = 1
        elif name == 'bottle':
            one_hot_vector[4] = 1
        elif name == 'bus':
            one_hot_vector[5] = 1
        elif name == 'car':
            one_hot_vector[6] = 1
        elif name == 'cat':
            one_hot_vector[7] = 1
        elif name == 'chair':
            one_hot_vector[8] = 1
        elif name == 'cow':
            one_hot_vector[9] = 1
        elif name == 'diningtable':
            one_hot_vector[10] = 1
        elif name == 'dog':
            one_hot_vector[11] = 1
        elif name == 'horse':
            one_hot_vector[12] = 1
        elif name == 'motorbike':
            one_hot_vector[13] = 1
        elif name == 'person':
            one_hot_vector[14] = 1
        elif name == 'pottedplant':
            one_hot_vector[15] = 1
        elif name == 'sheep':
            one_hot_vector[16] = 1
        elif name == 'sofa':
            one_hot_vector[17] = 1
        elif name == 'train':
            one_hot_vector[18] = 1
        elif name == 'tvmonitor':
            one_hot_vector[19] = 1
        else:
            print('unknown label: %s' %name)

        return one_hot_vector
        
    def _to_one_hot_2(self,name):
        one_hot_vector = [0] * self.num_classes
        if name == 'applauding':
            one_hot_vector[0] = 1
        elif name == 'blowing_bubbles':
            one_hot_vector[1] = 1
        elif name == 'brushing_teeth':
            one_hot_vector[2] = 1
        elif name == 'cleaning_the_floor':
            one_hot_vector[3] = 1
        elif name == 'climbing':
            one_hot_vector[4] = 1
        elif name == 'cooking':
            one_hot_vector[5] = 1
        elif name == 'cutting_trees':
            one_hot_vector[6] = 1
        elif name == 'cutting_vegetables':
            one_hot_vector[7] = 1
        elif name == 'drinking':
            one_hot_vector[8] = 1
        elif name == 'feeding_a_horse':
            one_hot_vector[9] = 1
        elif name == 'fishing':
            one_hot_vector[10] = 1
        elif name == 'fixing_a_bike':
            one_hot_vector[11] = 1
        elif name == 'fixing_a_car':
            one_hot_vector[12] = 1
        elif name == 'gardening':
            one_hot_vector[13] = 1
        elif name == 'holding_an_umbrella':
            one_hot_vector[14] = 1
        elif name == 'jumping':
            one_hot_vector[15] = 1
        elif name == 'looking_through_a_microscope':
            one_hot_vector[16] = 1
        elif name == 'looking_through_a_telescope':
            one_hot_vector[17] = 1
        elif name == 'playing_guitar':
            one_hot_vector[18] = 1
        elif name == 'playing_violin':
            one_hot_vector[19] = 1
        elif name == 'pouring_liquid':
            one_hot_vector[20] = 1
        elif name == 'pushing_a_cart':
            one_hot_vector[21] = 1
        elif name == 'reading':
            one_hot_vector[22] = 1
        elif name == 'phoning':
            one_hot_vector[23] = 1
        elif name == 'riding_a_bike':
            one_hot_vector[24] = 1
        elif name == 'riding_a_horse':
            one_hot_vector[25] = 1
        elif name == 'rowing_a_boat':
            one_hot_vector[26] = 1
        elif name == 'running':
            one_hot_vector[27] = 1
        elif name == 'shooting_an_arrow':
            one_hot_vector[28] = 1
        elif name == 'smoking':
            one_hot_vector[29] = 1
        elif name == 'taking_photos':
            one_hot_vector[30] = 1
        elif name == 'texting_message':
            one_hot_vector[31] = 1
        elif name == 'throwing_frisby':
            one_hot_vector[32] = 1
        elif name == 'using_a_computer':
            one_hot_vector[33] = 1
        elif name == 'walking_the_dog':
            one_hot_vector[34] = 1
        elif name == 'washing_dishes':
            one_hot_vector[35] = 1
        elif name == 'watching_TV':
            one_hot_vector[36] = 1
        elif name == 'waving_hands':
            one_hot_vector[37] = 1
        elif name == 'writing_on_a_board':
            one_hot_vector[38] = 1
        elif name == 'writing_on_a_book':
            one_hot_vector[39] = 1
        else:
            print('unknown label: %s' %name)

        return one_hot_vector


## example on how to use it
# import pickle
# data = XML_preprocessor('VOC2007/Annotations/').data
# pickle.dump(data,open('VOC2007.p','wb'))

