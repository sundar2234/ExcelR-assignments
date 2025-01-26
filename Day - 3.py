#!/usr/bin/env python
# coding: utf-8

# # Write a Python program that takes a student's marks in three subjects as input.
# •	If the average is greater than or equal to 90, print "Grade: A".
# •	If the average is between 80 and 89, print "Grade: B".
# •	If the average is between 70 and 79, print "Grade: C".
# •	Otherwise, print "Grade: Fail".
# 

# In[1]:


subject_1 = int(input("Enter marks for Subject 1: "))
subject_2 = int(input("Enter marks for Subject 2: "))
subject_3 = int(input("Enter marks for Subject 3: "))
average = (subject_1 + subject_2 + subject_3) / 3
if average >= 90:
    print("Grade: A")
elif 80 <= average < 90:
    print("Grade: B")
elif 70 <= average < 80:
    print("Grade: C")
else:
    print("Grade: Fail")


# In[ ]:




