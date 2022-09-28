#!/usr/bin/env python
# coding: utf-8

# In[12]:


# distance and slope of line
class Line():
    def __init__(self,cor1,cor2):
        self.cor1=cor1
        self.cor2=cor2
        
    def distance(self):
        x1,y1=self.cor1
        x2,y2=self.cor2
        return ((x2-x1)**2+(y2-y1)**2)**0.5

    def slope(self):
        x1,y1=self.cor1
        x2,y2=self.cor2
        return (y2-y1)/(x2-x1)


# In[ ]:





# In[16]:


cor1 = (10,22)
cor2 = (8,10)
li=Line(cor1,cor2)


# In[17]:


li.distance()


# In[18]:


li.slope()


# In[22]:


# volume and surface of the cylinder

class Cylinder():
    def __init__(self,height=1,radius=2):
        self.height=height
        self.radius=radius
        
    def volume(self):
        return self.height*3.14*(self.radius)**2
    
    def surface_area(self):
        top=3.14*(self.radius)**2
        return (2*top)+(2*3.14*self.radius*self.height)
    


# In[23]:


c=Cylinder()


# In[24]:


c.volume()


# In[25]:


c.surface_area()


# In[ ]:




