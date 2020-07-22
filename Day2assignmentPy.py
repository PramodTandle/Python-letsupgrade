#!/usr/bin/env python
# coding: utf-8

# In[9]:


num=eval(input("enter numbers"))
if num<0:
    print("enter positive numbers")
else:
    while num>0:
        sum1=0
        sum1=num*(num+1)/2
        print("The sum of number is",sum1)
        break
        
    


# In[1]:


lower=int(input("enter lower range"))
upper=int(input("enter upper range"))
for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                break
            else:
                print(num)


# In[ ]:





# 

# In[ ]:





# In[ ]:




