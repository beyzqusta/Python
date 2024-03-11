#!/usr/bin/env python
# coding: utf-8

# In[1]:


önceki_karakterler =      ["ş",
                          "ç",
                          "ö",
                          "ğ",
                          "ü",
                          "ı",
                          "Ş",
                          "Ç",
                          "Ö",
                          "Ğ",
                          "Ü",
                          "İ"]

sonraki_karakterler =   ["s",
                         "c",
                         "o",
                         "g",
                         "u",
                         "i",
                         "S",
                         "C",
                         "O",
                         "G",
                         "U",
                         "I"]
metin = "Burada Türkçe karakterler kullanılmıştır. Şimdi yapacağımız işlemde türkçe karakterleri hızlıca kaldırıp onları İngilizce karakterlere çevireceğiz."
for i in range(12):
    metin=metin.replace(önceki_karakterler[i],sonraki_karakterler[i])
print(metin)


# In[ ]:




