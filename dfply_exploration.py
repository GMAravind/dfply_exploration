
# coding: utf-8

# In[49]:


from dfply import *
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')


# # Manufacturers and Products Table

# In[50]:


manu = pd.read_csv("manufacturers.csv")
prod = pd.read_csv("products.csv")


# ## Print the first five rows of a table

# In[51]:


prod >> head(5) # prod %>% head(5)


# ## Get a unique list of product names

# In[52]:


prod >> distinct(X.name) # prod %>% distinct(name)


# ### As you can see, unlike dplyr, dfply.distinct outputs all columns and not just the "name" column

# ## Print first 5 records of the manufacturer table

# In[53]:


manu >> head(5)


# ## Filter for products with price > 100

# In[54]:


prod >> mask(X.price > 100) # prod %>% filter(price > 100)


# ## Merge Product with manufacturers dataset

# In[55]:


prod_manu = prod >> left_join(manu, by = "mfr_id") #prod %>% left_join(manu, by = "mfr_id")
prod_manu


# ### Names have to be consistent to join

# ## Filter for manufacturers with average product price of greater than 150
# 

# In[56]:


manu_150 = prod_manu >> group_by(X.mfr_id,X.mfr_name) >> summarize(avg_price = mean(X.price)) >> mask(X.avg_price >= 150)
# prod_manu %>% group_by(mfr_id,mfr_name) %>% summarise(avg_price = mean(price)) %>% filter(avg_price >= 150)


# In[57]:


manu_150


# # Baseball Dataframe

# In[58]:


baseball = pd.read_csv("baseball.csv",names = ["Player_Name","Team_Name","Bats","Hits"])
baseball >> head(5)


# ## Filter for teams with 7 or more number of players in it

# In[59]:


# Create a column with number of players by team in the dataframe
baseball >> group_by(X.Team_Name) >> summarize(player_count = n_distinct(X.Player_Name)) >> mask(X.player_count >= 7) 
# baseball %>% group_by(Team_Name) %>% summarise(player_count = n_distinct(X.Player_Name)) 
# %>% ungroup() %>% filter(player_count >= 7)


# ### Its a must to pass a column name to n or n_distinct - Need to pass the granularity of the table to obtain frequency

# ## Compute the batting average, Batting Average = Team_total_hits/ Teams total at bat

# In[60]:


#Always remember to ungroup before performing any operations
baseball = baseball >> group_by(X.Team_Name) >> summarize(bat_avg = X.Hits.sum()/X.Bats.sum()) >> ungroup()
#baseball <- baseball %>% group_by(Team_Name) %>% summarize(bat_avg = sum(Hits)/sum(Bats)) %>% ungroup()

baseball >> head(5)


# ## Filter for teams with batting average greater than .2 and less than .25

# In[61]:


baseball >> mask(X.bat_avg >= 0.2,X.bat_avg <= 0.25)
# baseball %>% filter(bat_avg >= 0.2 & bat_avg <= 0.25)


# # Explore the spread, gather, unite and seperate functions

# In[62]:


student_score = pd.read_csv("C:/3-MSBA - Summer/Stat for Data Scientists/Stat Project/student-mat.csv")
student_score >> head(5)


# ## Selecting columns using columns_to and columns_from

# In[ ]:


student_score = student_score >> select(columns_to(2,inclusive = True),columns_from(-3))
# student_score %>% select(1:3,(length(names(student_score))-2):(length(names(student_score))))
student_score >> head(5)



# ## Roll up the data by school, sex and age

# In[64]:


student_score = student_score >> group_by(X.school,X.sex,X.age) >> summarize(G1_sum = X.G1.sum(), G2_sum = X.G2.sum() , G3_sum = X.G3.sum())


# ## Gather the dataset for the aggregated grade columns G1_sum,G2_sum and G3_sum

# In[65]:


student_score = student_score >> gather('variable','value',['G1_sum','G2_sum','G3_sum'])
#student_score %>% gather("variable","value",G1:G3)


# In[66]:


student_score >> head(5)


# ## Spread the gathered columns

# In[67]:


student_score >> spread(X.variable,X.value) >> head(5)


# ## Unite function - combining the school and age columns

# In[68]:


student_score = student_score >> unite('school_age',X.school,X.age) 
# student_score <- student_score %>% unite(school_age,school,age,sep = '_')  


# In[69]:


student_score >> head(5)


# ## Separate function

# In[70]:


# You can also custom define the columns to assume NaN values based if the column consists unequal number of elements
student_score = student_score >> separate(X.school_age, ['school','age'],sep = "_",remove = True)
#student_score %>% separate(school_age, c('school','age'))
student_score >> head(5)

