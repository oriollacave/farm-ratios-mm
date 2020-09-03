#from time import time
#import numpy as np
import pandas as pd
#import xarray as xr
import matplotlib.pyplot as plt
import seaborn as sns
#from scipy import stats
#from pandas.plotting import register_matplotlib_converters
#import math
#register_matplotlib_converters()

data=pd.read_csv("data-hh60.csv",sep=";")
melted=pd.melt(data,id_vars=['mmid'])
sns.barplot(data=melted,x='mmid',y='value',hue='variable')
plt.legend()
plt.title("Project 3 MM Wind speeds")
plt.show()
metmasts=data['mmid'].to_numpy()
data=data.set_index('mmid')
cols=data.columns
ratios={}
i=int(0)
fig, axs = plt.subplots(2,3, figsize=(15, 6), facecolor='w', edgecolor='k')
#fig.subplots_adjust(hspace = .5, wspace=.001)
axs = axs.ravel()
for col in cols:
	print("##############  "+str(col)+"  #############")
	dfratio=pd.DataFrame(columns=data.index,index=data.index)
	for index, row in data.iterrows():
		rowratio=[]
		for index2, row2 in data.iterrows():
			r=row[col]/row2[col]
			rowratio.append(r)
		dfratio.loc[index]=pd.to_numeric(rowratio,errors='coerce')
	ratios[col]=dfratio
#	axs[i].plot(dfratio,label=metmasts)
	dfratio.plot(ax=axs[i])
	axs[i].hlines(1,0,4)
	axs[i].set_title(col)
#	axs[i].set_ylim([0.85,1.15])
	axs[i].get_legend().remove()
	i=i+1
handles, labels = axs[5].get_legend_handles_labels()
fig.legend(handles, labels, loc='upper right')
plt.show()



