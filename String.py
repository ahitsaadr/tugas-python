#!/usr/bin/env python
# coding: utf-8

# In[1]:


full_name = "Ahitsa Dawang Ransifa"

# jmlh huruf
jumlah_huruf = len(full_name.replace(" ", ""))

# jmlh huruf vokal 
huruf_vokal = "aiueoAIUEO"
jml_vokal = len([char for char in full_name if char in huruf_vokal])

# Menghitung jumlah huruf konsonan dari nama lengkap
konsonan = jumlah_huruf - jml_vokal

print("Jumlah huruf dari nama lengkap Anda adalah           :", jumlah_huruf)
print("Jumlah huruf vokal dari nama lengkap Anda adalah     :", jml_vokal)
print("Jumlah huruf konsonan dari nama lengkap Anda adalah  :", konsonan)


# In[ ]: