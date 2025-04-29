'''
Predict “price_range”
Columns 1 to 20: properties of mobile devices
Column 21: price_range
 '''

import pandas as pd 
import numpy as np 


## Load the data 
data_train_path = 'C:\Users\ethel\KTPSkills_Assessment\data\train.csv'
data_test_path= 'C:\Users\ethel\KTPSkills_Assessment\data\test.csv'

train_df = pd.read_csv("C:\\Users\\ethel\\KTPSkills_Assessment\\data\\train.csv")
test_df = pd.read_csv(data_test_path, header= 'None')

train_df.head()

