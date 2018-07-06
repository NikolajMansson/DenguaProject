
# coding: utf-8

# In[13]:


import pandas as pd

DENGUA_PATH = "https://s3.amazonaws.com/drivendata/data/44/public/dengue_features_train.csv"
def load_dengua_data(dengua_path=DENGUA_PATH):
    return pd.read_csv(dengua_path)


# In[8]:


dengua = load_dengua_data()


# In[14]:


dengua.head()


# In[17]:


import pandas as pd

DENGUA_FEATURES_PATH = "https://s3.amazonaws.com/drivendata/data/44/public/dengue_features_test.csv"
def load_dengua_features_data(dengua_features_path=DENGUA_FEATURES_PATH):
    return pd.read_csv(dengua_features_path)


# In[18]:


dengua_features = load_dengua_features_data()


# In[19]:


dengua_features.head()


# In[20]:


import pandas as pd

DENGUA_TRAINING_PATH = "https://s3.amazonaws.com/drivendata/data/44/public/dengue_labels_train.csv"
def load_dengua_training_data(dengua_training_path=DENGUA_TRAINING_PATH):
    return pd.read_csv(dengua_training_path)


# In[25]:


dengua_training = load_dengua_training_data()


# In[26]:


dengua_training.head()


# In[28]:


dengua_training.info()


# In[29]:


dengua_training["city"].value_counts()


# In[30]:


dengua_training.describe()


# In[31]:





# In[32]:


dengua_training_sj = dengua_training[(dengua_training['city'] == 'sj')]


# In[33]:


dengua_training_sj.head()


# In[34]:


dengua_training_sj.describe()


# In[35]:


dengua_training_iq = dengua_training[(dengua_training['city'] == 'iq')]


# In[36]:


dengua_training_iq.head()


# In[37]:


dengua_training_iq.describe()


# In[38]:


total_count = 936+520


# In[39]:


print(total_count)

