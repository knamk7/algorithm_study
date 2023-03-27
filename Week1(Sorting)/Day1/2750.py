#!/usr/bin/env python
# coding: utf-8

# In[2]:


N = int(input()) # 개수 입력
l = list() # 저장할 리스트

for i in range(N): # 배열 안에 입력
    l.append(int(input()))
    
l.sort()

for i in l:
    print(i)


# In[ ]:




