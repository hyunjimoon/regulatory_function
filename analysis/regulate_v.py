#!/usr/bin/env python
# coding: utf-8

# # Process Fedscope data

# In[3]:


import pickle 

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
import os
import statsmodels.formula.api as sm
plt.rcParams.update({'font.size': 16})


# Load the main data frame 

# In[6]:


dfMain = pd.read_csv("data/Sep18/FACTDATA_SEP2018.TXT",
                  header=0,
                  low_memory=False)

# In[7]:


dfMain


# Agency data frame

# In[4]:


agy = pd.read_csv("data/DTagy.txt",
                  header=0, 
                  low_memory=False)


# Occupations

# In[5]:


occ = pd.read_csv("/Users/vcy/Dropbox/1 Work/Data bank/Fedscope/2018 Sept/DTocc.txt",header=0, low_memory=False)


# In[6]:


occ.head()


# ## Restructure data

# In[7]:


merged = pd.merge(dfMain, agy[["AGYSUB", "AGY"]], on = "AGYSUB", how = "left")


# In[8]:


total = merged.groupby("AGY")["EMPLOYMENT"].count()


# In[9]:


occBreakdown = merged.groupby(["AGY", "OCC"])["EMPLOYMENT"].count().reset_index()


# In[10]:


occBreakdown.head()


# Save to pickle

# In[16]:


occBreakdown.to_pickle('fedOccFine2018')


# ## Get total

# In[12]:


total = total.reset_index().rename(columns = {"EMPLOYMENT": "total"})


# In[13]:


total.head()


# ## Get bureaucrat counts

# In[14]:


# a dictionary for various bureaucrats
Bdict = {"secretaries": ["0318"], 
         "HR": ["0201", "0203", "0299"], 
         "legal": list(occ[occ.OCCFAM == "09"].OCC.unique()),  # these are defined by family
         "admins" : list(occ[occ.OCCFAM == "03"].OCC.unique()),
         "accounting" : list(occ[occ.OCCFAM == "05"].OCC.unique()),
         "maintenance" : list(occ[occ.OCCFAM == "47"].OCC.unique()), # GENERAL MAINTENANCE AND OPERATIONS 
        "facilities_service" : list(occ[occ.OCCFAM == "16"].OCC.unique()), # EQUIPMENT, FACILITIES, AND SERVICES GROUP
         "custodian": ["3566"]
        }


# In[15]:


# Function to get varioys bureaucracts in agency
def getB(occBreakdown, key, Bdict):
    temp = occBreakdown[occBreakdown.OCC.isin(Bdict[key])]
    B = temp.groupby("AGY").EMPLOYMENT.sum().reset_index()
    B.rename(columns = {"EMPLOYMENT": key}, inplace = True)
    B = B.set_index("AGY")
    return B


# In[16]:


Blist = []
for i, key in enumerate(Bdict.keys()):
    B = getB(occBreakdown, key, Bdict)
    Blist.append(B)


# In[17]:


agyB = pd.concat(Blist, axis = 1, sort=False).fillna(0).reset_index().rename(columns = {"index": "AGY"})


# In[18]:


agyB.head()


# In[19]:


# merge total into the bureaucrat data frame
B = pd.merge(total, agyB, on = "AGY")


# In[20]:


B.head()


# ## Get supervisory status; supertyp; 1, 2 vs 3..7

# In[21]:


superv = pd.read_csv("/Users/vcy/Dropbox/1 Work/Data bank/Fedscope/2018 Sept/DTsuper.txt",header=0, low_memory=False)
superv.head()


# In[ ]:





# In[ ]:





# In[ ]:




