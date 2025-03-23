#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd


# In[10]:


import seaborn as sns
import matplotlib.pyplot as plt 


# In[11]:


data=pd.read_csv(r"C:\Users\vsvij\OneDrive\Desktop\Pandas Dataset\IMBD Movie\IMDB-Movie-Data.csv")


# In[12]:


data


# In[14]:


data.head()  #Q1
data.head(10)


# In[16]:


data.tail()   #Q2
data.tail(10)


# In[17]:


data.shape  #Q3


# In[19]:


print("Number of Rows",data.shape[0])
print("Number of Columns",data.shape[1])


# In[21]:


data.info()     #Q4


# In[22]:


print("Any missing value?",data.isnull().values.any())   #Q5


# In[23]:


data.isnull()


# In[24]:


data.isnull().sum()


# In[25]:


sns.heatmap(data.isnull())


# In[27]:


per_missing = data.isnull().sum()*100 / len(data)
per_missing


# In[28]:


data.dropna(axis=0)  #Q6


# In[31]:


dup_data=data.duplicated().any()    #Q7


# In[32]:


print("Are there any duplicate values?",dup_data)


# In[33]:


data=data.drop_duplicates()
data


# In[34]:


data.describe()     #Q8


# In[35]:


data.describe(include='all')     


# In[36]:


data.columns  #Q9


# In[37]:


data['Runtime (Minutes)'] >= 180


# In[38]:


data[data['Runtime (Minutes)'] >= 180] ['Title']


# In[39]:


data.columns     #Q10


# In[41]:


data.groupby('Year')['Votes'].mean()


# In[43]:


data.groupby('Year')['Votes'].mean().sort_values(ascending=False)


# In[45]:


sns.barplot(x='Year',y='Votes',data=data)


# In[46]:


sns.barplot(x='Year',y='Votes',data=data)
plt.title("Votes By Year")
plt.show()


# In[47]:


data.columns    #Q11


# In[50]:


data.groupby('Year')['Revenue (Millions)'].mean().sort_values(ascending=False)


# In[51]:


sns.barplot(x='Year',y='Revenue (Millions)',data=data)
plt.title("Revenue By Year")
plt.show()


# In[52]:


data.columns      #Q12


# In[54]:


data.groupby('Director')['Rating'].mean()


# In[55]:


data.groupby('Director')['Rating'].mean().sort_values()


# In[56]:


data.groupby('Director')['Rating'].mean().sort_values(ascending=False)


# In[57]:


data.columns    #Q13


# In[59]:


data.nlargest(10,'Runtime (Minutes)')[['Title','Runtime (Minutes)']]


# In[60]:


top10_len=data.nlargest(10,'Runtime (Minutes)')[['Title','Runtime (Minutes)']]\
.set_index('Title')


# In[61]:


top10_len


# In[62]:


sns.barplot(x='Runtime (Minutes)',y=top10_len.index,data=top10_len)


# In[63]:


data.columns  #Q14


# In[64]:


data['Year'].value_counts()


# In[65]:


sns.countplot(x='Year',data=data)


# In[66]:


sns.countplot(x='Year',data=data)
plt.title("Number of Movies Per Year")


# In[67]:


data.columns      #Q15


# In[68]:


data['Revenue (Millions)'].max()


# In[69]:


data['Revenue (Millions)'].max()==data['Revenue (Millions)']


# In[70]:


data[data['Revenue (Millions)'].max()==data['Revenue (Millions)']]


# In[71]:


data[data['Revenue (Millions)'].max()==data['Revenue (Millions)']]['Title']


# In[72]:


data.columns   #Q16


# In[73]:


top10_len=data.nlargest(10,'Rating')[['Title','Rating','Director']]\
.set_index('Title')


# In[74]:


top10_len


# In[76]:


sns.barplot(x='Rating',y=top10_len.index,data=top10_len)


# In[77]:


sns.barplot(x='Rating',y=top10_len.index,data=top10_len,hue='Director')


# In[81]:


sns.barplot(x='Rating',y=top10_len.index,data=top10_len,hue='Director',dodge=False)
plt.legend(bbox_to_anchor=(1.05,1),loc=2)


# In[82]:


data.columns  #Q17


# In[83]:


data.nlargest(10,'Revenue (Millions)')


# In[84]:


data.nlargest(10,'Revenue (Millions)')['Title']


# In[85]:


data.nlargest(10,'Revenue (Millions)')[['Title','Revenue (Millions)']]


# In[86]:


top_10=data.nlargest(10,'Revenue (Millions)')[['Title','Revenue (Millions)']].set_index('Title')


# In[87]:


top_10


# In[2]:


import pandas as pd


# In[3]:


import seaborn as sns
import matplotlib.pyplot as plt 


# In[4]:


data=pd.read_csv(r"C:\Users\vsvij\OneDrive\Desktop\Pandas Dataset\IMBD Movie\IMDB-Movie-Data.csv")


# In[6]:


data


# In[9]:


data.head()
data.head(10)


# In[10]:


data.tail()
data.tail(10)


# In[11]:


data.columns   #Q18


# In[14]:


data.groupby('Year')['Rating'].mean().sort_values(ascending=False)


# In[15]:


data.columns    #Q19


# In[18]:


sns.barplot(x=="Rating",y="Revenue (Millions)",data=data)


# In[19]:


data.columns        #Q20


# In[20]:


def rating(rating):
    if rating>=7.0:
        return "Excellent"
    elif rating>=6.0:
        return "Good"
    else:
        return "Average"


# In[22]:


data['Rating_cat']=data['Rating'].apply(rating)


# In[23]:


data.head


# In[24]:


data.columns      #Q21


# In[25]:


data['Genre'].dtype


# In[26]:


data['Genre'].str.contains('Action')


# In[28]:


data[data['Genre'].str.contains('Action',case=False)]


# In[29]:


len(data[data['Genre'].str.contains('Action',case=False)])


# In[ ]:




