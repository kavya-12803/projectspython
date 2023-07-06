#!/usr/bin/env python
# coding: utf-8

# In[1]:


mylist = [" " ,"O"," "]


# In[3]:


from random import shuffle 


# In[4]:


def shuffle_ball(mylist):
    shuffle(mylist )
    return mylist     


# In[10]:


shuffle_ball(mylist)


# In[15]:


def player_guess():
    guess = ""
    while guess not in ["0","1","2"]:
        guess= input("enter from 0,1,2")
    return int(guess)


# In[17]:


myindex = player_guess()


# In[26]:


def check_guess (mylist , guess):
    if mylist[guess]== "O":
        print("correct")
        print(mylist)
    else :
        print("worng ")
        print(mylist)
    


# In[27]:


# list
mylist 

# shuffle
mix = shuffle_ball(mylist)

# take guess 
playerguess= player_guess()

check_guess(mix,playerguess)

# check guess


# myindex

# In[28]:


pdw

