#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import math
t = 0
v = 50
g = 9.81
liste = []
for t in np.arange (0, 20, 0.5): 
    x= v*math.cos(60*math.pi/180)*t 
    y= v*math.sin(60*math.pi/180)*t - 0.5*g*t*t
    liste.append (y) 
    print(f"Yatayda aldığı yol: {x}\nDüşeyde aldığı yol: {y}\n")
    t+=0.5
print ("Maksimum yükseklik:",max(liste))


# In[ ]:




