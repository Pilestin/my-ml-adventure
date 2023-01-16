import numpy  as np 
import pandas as pd 
import os 

main_path = '/MachineLearning/Proje2'
train_path = main_path + '/train/'
val_path = main_path + '/val' 

train_df = pd.DataFrame()
val_df = pd.DataFrame()

train_df['images'] = os.listdir(train_path+'/cat') + os.listdir(train_path+'/dog') + os.listdir(train_path+'/wild')
val_df['images'] = os.listdir(val_path+'/cat') + os.listdir(val_path+'/dog') + os.listdir(val_path+'/wild')

classes = []
paths = []
for image in train_df['images']:
    class_ = image.split('_')[1]
    classes.append(class_)
    paths.append(train_path+'/'+class_+'/'+image)

print(train_df)