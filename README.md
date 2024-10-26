# PandasDemo

import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
print("Setup Complete")

# Set up code checking
import os
if not os.path.exists("../input/ign_scores.csv"):
    os.symlink("../input/data-for-datavis/ign_scores.csv", "../input/ign_scores.csv") 
from learntools.core import binder
binder.bind(globals())
from learntools.data_viz_to_coder.ex3 import *
print("Setup Complete")

# Set the width and height of the figure
plt.figure(figsize=(10,10))

# Path of the file to read
csvfilepath = "../input/myfile1.csv"

# Fill in the line below to read the file into a variable csv_data
csv_data = pd.read_csv(csvfilepath, index_col='ColumnName1')

sns.barplot(x=csv_data['Racing'], y=csv_data.index) 
sns.heatmap(csv_data, annot=True)

