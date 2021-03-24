#!/usr/bin/env python
# coding: utf-8

# In[3]:


#pilot navigation system
Altitude = int(input("Enter the Altitude of the plane: "))
if Altitude == 3000:
    print("It is safe to land")
elif Altitude>=3000 and Altitude<=6000:
    print("Allow the pilot to land after coming to the required altitiude")
else:
    print("Not permitted to Land")

