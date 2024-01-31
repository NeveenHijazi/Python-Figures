# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 21:59:24 2023

@author: Neveen.Hijazi
"""

import numpy as np
import matplotlib.pyplot as plt

barWidth = 0.12
fig, ax = plt.subplots(figsize =(17, 10))

L1= [0.76,	0.56,	0.85,	0.87,	0.63]
L2= [0.43,	0.79,	0.80,	0.86,	0.56]
L3= [0.80,	0.58,	0.60,	0.87,	0.64]
L4= [0.70,	0.77,	0.78,	0.89,   0.72]
BL= [0.81,	0.73,	0.83,	0.82,	0.81]

br1 = np.arange(len(BL))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]
br4 = [x + barWidth for x in br3]
br5 = [x + barWidth for x in br4]

# Make the plot
plt.bar(br1, BL, color ='pink', width = barWidth,
		edgecolor ='grey', label ='BL')
plt.bar(br2, L1, color ='darkgray', width = barWidth,
		edgecolor ='grey', label ='L1')
plt.bar(br3, L2, color ='cornflowerblue', width = barWidth,
		edgecolor ='grey', label ='L2')
plt.bar(br4, L3, color ='tan', width = barWidth,
		edgecolor ='grey', label ='L3')
plt.bar(br5, L4, color ='darkred', width = barWidth,
		edgecolor ='grey', label ='L5')


plt.rcParams['font.size'] = '18'

trans = ax.get_xaxis_transform()

plt.xlabel('Dataset', fontsize = 22, labelpad=30)
plt.ylabel('Performance Measure', fontsize = 22, labelpad=30)
plt.xticks([r + barWidth + barWidth/2 + barWidth/2 for r in range(len(BL))],
		[ 'DS1', 'DS2', 'DS3', 'DS4', 'DS5'])

plt.ylim(0.30, 1.000)
plt.legend(bbox_to_anchor =(0.5,1), ncol = 5, loc='lower center')
ax.xaxis.set_label_coords(.5, -.1)

fig.tight_layout()
   
plt.savefig('Image.jpg', format='jpg', dpi=1000)
plt.show()
