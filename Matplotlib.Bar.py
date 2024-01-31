
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 21:59:24 2023

@author: Neveen.Hijazi
"""
from matplotlib import pyplot as plt

def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i,y[i],y[i],ha = 'center')
 
# creating the dataset
y= [104,	113,	120,	133,	244]
x= ['BL','L1','L2','L3','L4']
plt.rcParams['font.size'] = '15'


data= {'BL':104, 'L1':113, 'L2':120, 'L3':133, 'L4':244}

courses = list(data.keys())
values = list(data.values())

fig = plt.figure(figsize =(17, 10))

# creating the bar plot
plt.bar(x, y, color ='darkred', width=0.3)
addlabels(x, y)

plt.xlabel("Algo", fontsize = 22, labelpad=30)
plt.ylabel("Performance Measure", fontsize = 22, labelpad=30)
fig.tight_layout()
   
plt.savefig('image.jpg', format='jpg', dpi=1000)
plt.show()
