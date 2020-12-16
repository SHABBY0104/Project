import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


filename = "cccc.xlsx"

data = pd.read_excel(filename)

col = ['ZH','WY','SX','YW','OUT_COUNT','IN_COUNT','QT_XFJE','QT_XFCS','XY_XFJE','XY_XFCS','JY_XFJE','JY_XFCS','GW_XFJE','GW_XFCS','JS_XFJE','JS_XFCS','JT_XFJE','JT_XFCS','JF_XFJE','JF_XFCS','YS_XFJE','YS_XFCS','CY_XFJE','CY_XFCS','SUM_XFJE','SUM_XFCS' ]

cluster0 = data[data['cluster'] == 'cluster_0']
cluster1 = data[data['cluster'] == 'cluster_1']
cluster2 = data[data['cluster'] == 'cluster_2']
cluster3 = data[data['cluster'] == 'cluster_3']
cluster4 = data[data['cluster'] == 'cluster_4']


mean_c0 = np.array(cluster0[col].describe())[1]
mean_c1 = np.array(cluster1[col].describe())[1]
mean_c2 = np.array(cluster2[col].describe())[1]
mean_c3 = np.array(cluster3[col].describe())[1]
mean_c4 = np.array(cluster4[col].describe())[1]


# x_data = col
#
# x = np.arange(len(col))
#
# tatol_width = 0.8
# n = 2
# bar_width = tatol_width / n
# x = x - (tatol_width-bar_width)/2
#
# plt.bar(x,height=mean_c1,width=bar_width,color = 'r',label = 'cluster1', align='center', alpha = 0.5)
# plt.bar(x + bar_width,height=mean_c2,width=bar_width,color = 'g',label = 'cluster2', align='center', alpha = 0.5)
#
# plt.legend()
# plt.xticks(x,col)
# plt.ylabel('score')
# plt.title("mean of the clusters")
#
# plt.savefig("bar_mean.jpg")
#
# plt.show()


bar_width = 0.9
print(type(np.arange(1,53,2)))
print(np.arange(1,1+len(col)*3,3))

print(np.arange(len(col)))

#
plt.barh(y=np.arange(1,1+len(col)*3,3), width=mean_c1, label = 'cluster1', color = 'g', alpha = 0.5, height= bar_width)
plt.barh(y=np.arange(1,1+len(col)*3,3)+bar_width*1, width=mean_c2, label = 'cluster2', color = 'r', alpha = 0.5, height= bar_width)

# plt.barh(y=np.arange(len(col))+bar_width, width=cluster2,label='C语言基础', color='indianred', alpha=0.8, height=bar_width)


for y, x in enumerate(mean_c1):
    plt.text(x+5000, y-bar_width/2, '%s' % x, ha='center', va='bottom')

for y, x in enumerate(mean_c2):
    plt.text(x+5000, y-bar_width/2, '%s' % x, ha='center', va='bottom')


plt.yticks(np.arange(1,1+len(col)*3,3)+bar_width/2, col)

plt.axvline(x = 0.1, c = 'silver', ls = '--', lw = 0.5,alpha = 0.8)
plt.axvline(x = 0.2, c = 'silver', ls = '--', lw = 0.5,alpha = 0.8)
plt.axvline(x = 0.3, c = 'silver', ls = '--', lw = 0.5,alpha = 0.8)
plt.axvline(x = 0.4, c = 'silver', ls = '--', lw = 0.5,alpha = 0.8)
plt.axvline(x = 0.5, c = 'silver', ls = '--', lw = 0.5,alpha = 0.8)
plt.axvline(x = 0.6, c = 'silver', ls = '--', lw = 0.5,alpha = 0.8)
plt.axvline(x = 0.7, c = 'silver', ls = '--', lw = 0.5,alpha = 0.8)

plt.xlabel('score')
plt.ylabel('attribute')
plt.title("mean of the clusters")

plt.legend()
plt.savefig("bar_mean_h_2.pdf")
plt.show()
