# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 21:59:24 2023

@author: Neveen.Hijazi
"""

import matplotlib.pyplot as plt
import matplotlib.lines as mlines
        
BL=	[40,	30,	88,	41,	52]
L1=	[33,	55,	66,	87,	98]
L2=	[92,	56,	75,	58,	60]
L3=	[46,	54, 44,	73,	66]
L4=	[81,	60,	78,	79, 36]

X = [(1,1,1)]
dataset=['BL','L1','L2','L3','L4']

fig = plt.figure(figsize=(22,12))
plt.rcParams['font.size'] = '18'

d=0
for nrows, ncols, plot_number in X:
    ax = plt.subplot(nrows, ncols, plot_number)
       
    j=0   
  
    line1=plt.plot(BL,'bo-', linewidth=5 ,markersize=7,markeredgecolor='b',\
        fillstyle='none',markeredgewidth='3',markevery=1)
    line2=plt.plot(L1,'rs-',linewidth=5, markersize=7,markeredgecolor='r',\
        fillstyle='none',markeredgewidth='3',markevery=1)
    line2=plt.plot(L2,'gv-',linewidth=5, markersize=7,markeredgecolor='g',\
        fillstyle='none',markeredgewidth='3',markevery=1)
    line2=plt.plot(L3,'m*-',linewidth=5, markersize=7,markeredgecolor='m',\
        fillstyle='none',markeredgewidth='3',markevery=1)
    line2=plt.plot(L4,'cD-',linewidth=5, markersize=7,markeredgecolor='c',\
        fillstyle='none',markeredgewidth='3',markevery=1)
    
    plt.xlabel('Datasets',  fontsize = 24,  labelpad=30)
    plt.ylabel('Performance Measure',  fontsize = 24, labelpad=30)
    my_xticks = [ 'DS1', 'DS2', 'DS3', 'DS4', 'DS5']
    xxx = [0, 1,2,3,4]
    plt.xticks(xxx, my_xticks, fontsize = 22)

    b_line = mlines.Line2D([], [], color='b',linewidth=5, marker='o',markersize=7, label='BL')
    r_line = mlines.Line2D([], [], color='r',linewidth=5, marker='s',markersize=7, label='L1')
    g_line = mlines.Line2D([], [], color='g',linewidth=5, marker='v',markersize=7, label='L2')
    m_line = mlines.Line2D([], [], color='m',linewidth=5, marker='*',markersize=7, label='L3')
    c_line = mlines.Line2D([], [], color='c',linewidth=5, marker='D',markersize=7, label='L4')

    plt.ylim(0 , 250)
    ax.yaxis.set_tick_params(labelsize=22)

    d=d+1
    plt.grid()
    plt.legend(handles=[b_line ,r_line,g_line,m_line,c_line], ncol = 5, fontsize = 22, loc='upper right') 
     
fig.tight_layout()
   
plt.savefig('image.jpg', format='jpg', dpi=1000)
        
plt.show()
       