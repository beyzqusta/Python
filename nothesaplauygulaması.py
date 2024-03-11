#!/usr/bin/env python
# coding: utf-8

# In[ ]:





    



# In[31]:


def nothesapla(satır):
    satır = satır[:-1]
    liste = satır.split(",")
    
    isim = liste[0]
    vize1 = int(liste[1])
    vize2 = int(liste[2])
    final = int(liste[3])
    ort = vize1 * (3/10) + vize2 * (3/10) + final * (4/10)
    
    if ort >= 90:
        harf = "AA"
    elif ort >= 85:
        harf = "BA"
    elif ort >= 80:
        harf = "BB"
    elif ort >= 75:
        harf = "CB"
    elif ort >= 65:
        harf = "CC"
    elif ort >= 60:
        harf = "DC"
    elif ort >= 55:
        harf = "DD"
    elif ort >= 50:
        harf = "FD"
    else:
        harf = "FF"
    
    return isim, ort, harf

with open("notlar.txt", "r", encoding="utf-8") as file:
    gecenler = []
    kalanlar = []
    
    for i in file:
        isim, ort, harf = nothesapla(i)
        
        # Her öğrencinin notlarını yazdır
        print(f"{isim}: Ortalama={ort}, Harf Notu={harf}")
        
        # Geçenleri ve kalanları ayır
        if harf == "FF":
            kalanlar.append(f"{isim}: Ortalama={ort}, Harf Notu={harf}")
        else:
            gecenler.append(f"{isim}: Ortalama={ort}, Harf Notu={harf}")

# Geçenleri dosyaya yaz
with open("geçenler.txt", "w", encoding="utf-8") as gecenler_file:
    for ogrenci in gecenler:
        gecenler_file.write(ogrenci + "\n")

# Kalanları dosyaya yaz
with open("kalanlar.txt", "w", encoding="utf-8") as kalanlar_file:
    for ogrenci in kalanlar:
        kalanlar_file.write(ogrenci + "\n")


print("Geçenler dosyasına geçen öğrenciler yazıldı.")
print("Kalanlar dosyasına kalan öğrenciler yazıldı.")


# In[ ]:




