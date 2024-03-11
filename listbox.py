#!/usr/bin/env python
# coding: utf-8

# In[2]:


from tkinter import *
 
from tkinter import messagebox
 
pencere = Tk()
 
pencere.title("www.yazilimkodlama.com")
pencere.geometry("400x300")
 
#grid form çizdirme
uygulama = Frame(pencere)
uygulama.grid()
 
 
Lb1=Listbox(uygulama)
Lb1.insert(1, "Python")
Lb1.insert(2, "C#")
Lb1.insert(3, "JAVA")
Lb1.insert(4, "JAVASCRIPT")
Lb1.grid(padx=110, pady=10)
 
#formu çiz
pencere.mainloop()
 


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




