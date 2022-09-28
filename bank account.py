#!/usr/bin/env python
# coding: utf-8

# In[28]:


class Bank():
    
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
        
    def __str__(self):
        return f'Account owner:{self.owner} \nAccount Balance:{self.balance}'
    
    def deposit(self,dep_amt):
        self.balance+=dep_amt
        print("deposit accepted")
        
    def withdraw(self,with_amt):
        if self.balance>=with_amt:
            self.balance-=with_amt
            print("Withdrawn accepted")
        else:
            print("insufficient amount")
        


# In[45]:


account1=Bank('ankush',500)


# In[30]:


print(account1)


# In[31]:


account1.owner


# In[32]:


account1.balance


# In[46]:


account1.withdraw(100)


# In[44]:


print(account1)


# In[22]:


account1.withdraw(300)


# In[23]:


account1.withdraw(90)


# In[24]:


print(account1)


# In[ ]:




