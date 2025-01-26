#!/usr/bin/env python
# coding: utf-8

# # Write a Python program to calculate the sum of all even numbers between 1 and a given positive integer n.

# In[2]:


n = int(input("Enter a positive integer: "))
even_sum = 0
for num in range(2, n + 1, 2):  #initial, terminal, step-condition
    even_sum += num
print(f"The sum of all even numbers between 1 and {n} is: {even_sum}")


# In[ ]:




