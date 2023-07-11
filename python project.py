#!/usr/bin/env python
# coding: utf-8

# In[16]:


game_list=[0,1,2]


# In[2]:


def display_game (game_list ):
    print("here is current list")
    print(game_list)


# In[17]:


def Position_choice() :
    choice = "wrong "
    
    while choice not in ["0","1","2"]:
        choice = input("pick position")
        
    return int(choice)


# In[4]:


Position_choice()


# In[19]:


def replacement_choice (game_list,position ):
    user_placement = input("string ")
    
    game_list[position]= user_placement
    
    return game_list 


# In[6]:


replacement_choice (game_list,1)


# In[20]:


def gameon_choice() :
    choice = "wrong "
    
    while choice not in ["Y","N"]:
    
        choice = input("Y OR N")
        
    if choice == "Y":
        return True
    else: return False 
  


# In[8]:


gameon_choice()


# In[ ]:


game_on = True
game_list = [0,1,2]


while game_on :
    display_game(game_list)
    position = Position_choice()
    game_on = replacement_choice(game_list,position)
    game_on=gameon_choice ()


# In[ ]:




