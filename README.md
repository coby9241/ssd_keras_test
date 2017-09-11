# SSD Keras with Stanford 40 Actions Dataset

Testing Single Shot Multibox Detector on Stanford 40 Actions Dataset. This is just to try out the Single Short Multibox Detector port in Keras and is not meant for research or anything. (!Disclaimer: Some cherry picking here to make myself feel abit better after all the effort spent understanding the model and using this port)

Original SSD Paper: [Single Shot Multibox Detector](https://arxiv.org/abs/1512.02325)

Credits: [rykov8](https://github.com/rykov8/ssd_keras) for SSD port to Keras. [cory8249](https://github.com/cory8249/ssd_keras) for the Keras 2.0.0 support. Main change was the removal of AtrousConvolution2D, which is replaced by the dilated option in Convolution2D.

Stanford 40 Actions Dataset: [data](http://vision.stanford.edu/Datasets/40actions.html)

Most of the work done in ssd_trial_3.ipynb and get_data_from_XML.py. One issue noticed is due to the large number of classes (40 to be exact excluding nothing detected), the splitting of the data into train/val/test is very important. Further improvement could be made to the model by doing the split such that there is a equal distribution of the classes in all the 3 sets.

To do (if i have time):
1) retraining after better train/val/test split
2) computation of MAP (mean average precision) and Average Precision for all classes
