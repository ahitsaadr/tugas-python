#!/usr/bin/env python
# coding: utf-8

# In[1]:

n = int(input())
p = 0
q = 1
for i in range(n):
	if i == 0:
		continue
	print(q, end=" ")
	for j in range(i):
		temp = p
		p = q
		q = temp + p
		print(p, end=" ")
	print()
	p = 0
	q = 1

# In[2]:

# In[ ]: