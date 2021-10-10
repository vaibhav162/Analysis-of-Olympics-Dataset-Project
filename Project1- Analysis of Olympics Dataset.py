#!/usr/bin/env python
# coding: utf-8

# # Import Libraries and Dataset

# In[21]:


# Installing plotly Library

get_ipython().system('pip install plotly')


# In[84]:


# Importing Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly


# In[85]:


# Importing Dataset (Winter Olympics)& Dataset (Summer Olympics)

winter= pd.read_csv(r"C:\Users\shruti\Desktop\Decodr Session Recording\Project\Decodr Project\In-depth Analysis of Olympic Dataset\winter.csv")
summer= pd.read_csv(r"C:\Users\shruti\Desktop\Decodr Session Recording\Project\Decodr Project\In-depth Analysis of Olympic Dataset\summer.csv")


# In[86]:


winter.head()


# In[87]:


winter.tail()


# In[88]:


summer.head()


# In[89]:


summer.tail()


# In[90]:


# Import Dataset (Dictionary)

dicts=pd.read_csv(r"C:\Users\shruti\Desktop\Decodr Session Recording\Project\Decodr Project\In-depth Analysis of Olympic Dataset\dictionary.csv")


# In[91]:


dicts.head()


# In[92]:


dicts.tail()


# # Analyzing "summer" Dataset

# In[93]:


summer.rename(columns={"Country": "Code"}, inplace= True)


# In[94]:


summer.head()


# In[95]:


summer=pd.merge(summer, dicts, on= "Code", how= "outer")


# In[96]:


summer.head()


# In[97]:


summer.describe()


# ### Plotting Choropleth Map

# In[98]:


summer_medals= summer.groupby(["Country", "Code"])["Medal"].count().reset_index()
summer_medals= summer_medals[summer_medals["Medal"]>0]


# In[99]:


fig= px.choropleth(summer_medals, locations= "Code", color= "Medal", hover_name= "Country",
                  color_continuous_scale= px.colors.sequential.Plasma)
fig.show()


# ### Most Successful Male & Female Athlete

# In[133]:


# Most successful Male Athlete

print("Most successful male Athlete in Summer Olympics is:", summer[summer["Gender"]=="Men"]["Athlete"].value_counts()[:1].index[0],
     "with", summer[summer["Gender"]=="Men"]["Athlete"].value_counts().values[0], "medals")


# In[134]:


# Most successful Female Athlete

print("Most successful female Athlete in Summer Olympics is:", summer[summer["Gender"]=="Women"]["Athlete"].value_counts()[:1].index[0],
     "with", summer[summer["Gender"]=="Women"]["Athlete"].value_counts().values[0], "medals")


# ### Winner of most Medals in Summer Olympics

# In[142]:


medals= summer.groupby(["Athlete", "Medal"])["Sport"].count().reset_index().sort_values(by="Sport", ascending= False)


# In[143]:


medals


# In[144]:


summer_medals= medals.drop_duplicates(subset=["Medal"], keep="first")


# In[137]:


summer_medals


# In[106]:


medals.columns= [["Athlete", "Medal", "Count"]]


# In[107]:


medals


# ### Visualizing the medal distribution of Top 10 countries in Summer Olympics

# In[108]:


medals_country= summer.groupby(["Country", "Medal"])["Gender"].count().reset_index().sort_values(by="Gender", ascending= False)


# In[109]:


medals_country


# In[110]:


medals_country= medals_country.pivot("Country", "Medal", "Gender").fillna(0)


# In[111]:


medals_country


# In[112]:


top= medals_country.sort_values(by= "Gold", ascending= False)[:10]


# In[113]:


top


# In[135]:


fig= top.plot.barh(width=0.8)
fig= plt.gcf()
fig.set_size_inches(10,10)
plt.title("Medal distribution in Top 10 countries in Summer Olympics")
plt.show()


# In[ ]:





# In[ ]:





# # Analyzing "winter" Dataset

# In[115]:


winter.rename(columns={"Country": "Code"}, inplace= True)


# In[116]:


winter= pd.merge(winter, dicts, on="Code", how="outer")


# In[117]:


winter.head()


# In[119]:


winter.describe()


# ### Plotting Choropleth Map

# In[122]:


winter_medals=winter.groupby(["Country", "Code"])["Medal"].count().reset_index()
winter_medals=winter_medals[winter_medals["Medal"]>0]


# In[124]:


fig=px.choropleth(winter_medals, locations="Code", color="Medal", hover_name="Country",
                 color_continuous_scale= px.colors.sequential.Plasma)
fig.show()


# ### Most Successful Male & Female Athlete

# In[131]:


# Most successful Male Athlete

print("Most successful male Athlete in Winter Olympics is:", winter[winter["Gender"]=="Men"]["Athlete"].value_counts()[:1].index[0],
     "with", winter[winter["Gender"]=="Men"]["Athlete"].value_counts().values[0], "medals")


# In[132]:


# Most successful Female Athlete

print("Most successful female Athlete in Winter Olympics is:", winter[winter["Gender"]=="Women"]["Athlete"].value_counts()[:1].index[0],
     "with", winter[winter["Gender"]=="Women"]["Athlete"].value_counts().values[0], "medals")


# ### Winner of most Medals in Winter Olympics

# In[145]:


medals= winter.groupby(["Athlete", "Medal"])["Sport"].count().reset_index().sort_values(by="Sport", ascending= False)


# In[146]:


medals


# ### Visualizing the medal distribution of Top 10 countries in Winter Olympics

# In[147]:


medals_country= winter.groupby(["Country", "Medal"])["Gender"].count().reset_index().sort_values(by="Gender", ascending= False)


# In[148]:


medals_country


# In[149]:


medals_country= medals_country.pivot("Country", "Medal", "Gender").fillna(0)


# In[152]:


medals_country


# In[150]:


top= medals_country.sort_values(by= "Gold", ascending= False)[:10]


# In[151]:


fig= top.plot.barh(width=0.8)
fig= plt.gcf()
fig.set_size_inches(10,10)
plt.title("Medal distribution in Top 10 countries in Winter Olympics")
plt.show()


# In[ ]:




