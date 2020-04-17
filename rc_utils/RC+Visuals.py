
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


# In[2]:

# Import the data
import os
PATH = "/home/crater/Desktop/Sem-7/RC/rouge/rouge/"
csv_files = os.listdir(PATH)
dataFrames = {}

for file in csv_files:
    dataFrames[file.split(".")[0]] = pd.read_csv(PATH + file)


# In[3]:

dataFrames['lsa'].head(5)


# In[4]:

dataFrames.keys()


# In[5]:

# Plots to understand the distribution for each algorithm and different rouges

for file in dataFrames:
    sns.kdeplot(dataFrames[file]["rouge1"], label = file)
plt.legend()
plt.title("Rogue 1 Score Distributions")
plt.show()


# In[6]:

for file in dataFrames:
    sns.kdeplot(dataFrames[file]["rouge2"], label = file)
plt.legend()
plt.title("Rogue 2 Score Distributions")
plt.show()


# In[7]:

for file in dataFrames:
    sns.kdeplot(dataFrames[file]["rougel"], label = file)
plt.legend()
plt.title("Rogue l Score Distributions")
plt.show()


# In[8]:

# Correlation between the coRank and simFusion results
sns.jointplot(x = dataFrames["coRank"]["rouge1"], y = dataFrames["simFusion"]["rouge1"], kind = "kde")
plt.title("Correlation between coRank and simFusion")
plt.show()


# In[9]:

# Correlation between the coRank and simFusion results
sns.jointplot(x = dataFrames["coRank"]["rouge1"], y = dataFrames["simFusion"]["rouge1"])
plt.title("Correlation between coRank and simFusion")
plt.show()


# In[10]:

# Statistical Analysis over the results: We can create a table on these
for file in dataFrames:
    print("Name of the Algorithm:", file)
    print(dataFrames[file].describe())
    print()


# In[11]:

plot_frame = pd.DataFrame(columns=["score", "type", "algo"])


# In[12]:

keys = ["rouge1", "rouge2", "rougel"]
for file in dataFrames:
    for index, row in dataFrames[file].iterrows():
        if index > 100:
            break
        for key in keys:
            plot_frame = plot_frame.append({"score": row[key], "type": key, "algo": file}, ignore_index = True)


# In[13]:

# Summary of the entire analysis
sns.catplot(x = "algo", y = "score", hue = "type", data = plot_frame)
plt.title("All the Information put together!")
plt.show()


# In[13]:

get_ipython().system('pip install -U seaborn')


# In[ ]:




# In[ ]:



