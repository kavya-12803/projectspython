#!/usr/bin/env python
# coding: utf-8

# In[11]:





# In[32]:


class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        
    def deposite(self,money):
        self.balance = self.balance + money
        return (f"balance in your account is :{self.balance}")
    
    
    def withdraw (self,paisa):
        if self.balance > paisa : 
            self.balance = self.balance - paisa
        else :
            print (" not enough fund ")
            return (f"balance in your account is :{self.balance}")
    
    
    
    
    def __str__(self):
        return f"owner: {self.owner}, balance: {self.balance}"


# In[33]:


acc=Account("kavya",100)


# In[38]:


acc.deposite(500)


# In[ ]:




