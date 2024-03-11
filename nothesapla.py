#!/usr/bin/env python
# coding: utf-8

# In[30]:


def nothesapla(satır):
    
    satır=satır[:-1]
    
    liste=satır.split(",")
    
    isim=liste[0]
    vize1=int(liste[1])
    vize2=int(liste[2])
    final=int(liste[3])
    ort=vize1*(3/10)+vize2*(3/10)+final*(4/10)
    
    if(ort>=90):
        harf="AA"
    elif(ort>=85):
        harf="BA"
    elif(ort>=80):
        harf="BB"
    elif(ort>=75):
        harf="CB"
    elif(ort>=65):
        harf="CC"
    elif(ort>=60):
        harf="DC"
    elif(ort>=55):
        harf="DD"
    elif(ort>=50):
        harf="FD"
    else:
        harf="FF"
    return isim, ort, harf
  
 
with open("notlar.txt","r",encoding="utf-8") as file:
    eklenecekler = []
    
    for i in file:
        eklenecekler.append(nothesapla(i))
    print(eklenecekler)
    



# In[ ]:





# In[ ]:




