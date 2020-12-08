import pandas as pd
import numpy as np
from sklearn.preprocessing import MultiLabelBinarizer


def normlize2( data ):

    data = np.array(data)

    _range = np.max(data) - np.min(data)
    return (data - np.min(data)) / _range



def normlize1( data, name1, name2, name3, name4 ):

    array = np.array(data)
    label = set(array[:,0])

    normScore = np.zeros((data.shape[0],data.shape[1] -1))
    print(normScore.shape)


    for sublabel in label:

        index = data[data['CSDM'] == sublabel].index
        newData = data[data['CSDM'] == sublabel].loc[:,list(data.columns)[1:]]

        newData = np.array(newData)


        newData = (newData-newData.min(axis=0)) / ( newData.max(axis=0) - newData.min(axis=0))

        normScore[ index ] = newData

    return normScore


filename = 'test'

data = pd.read_csv(filename+'.csv')
data.fillna(-1,inplace=True)


col = ['XBM', 'CSDM', 'ZZMMM','MZM','BKSRXFSM','PYFSM', 'DWH', 'ZYH', 'RXNY','BYLBM','KQM','KSLBM','LABEL']

subData = pd.DataFrame(data[['XBM', 'CSDM', 'ZZMMM','MZM','BKSRXFSM','PYFSM', 'DWH', 'ZYH', 'RXNY','BYLBM','KQM','KSLBM','LABEL']])

print(subData)

subData = subData.applymap(lambda x: x if isinstance(x, list) else [x])

mlb = MultiLabelBinarizer()
vals = [pd.Series(mlb.fit_transform(subData[x]).tolist()) for x in subData.columns]
df2 = pd.concat(vals, keys=subData.columns, axis=1)


print(df2)
#
# df2.to_csv('del.csv')
# print(df2['MZM'][0])
# print(len(df2['MZM'][0]))

SUM_XFCS = normlize2(data['SUM_XFCS'])
SUM_XFJE = normlize2(data['SUM_XFJE'])
CY_XFCS = normlize2(data['CY_XFCS'])
CY_XFJE = normlize2(data['CY_XFJE'])
YS_XFCS = normlize2(data['YS_XFCS'])
YS_XFJE = normlize2(data['YS_XFJE'])
JF_XFCS = normlize2(data['JF_XFCS'])
JF_XFJE = normlize2(data['JF_XFJE'])
JT_XFCS = normlize2(data['JT_XFCS'])
JT_XFJE = normlize2(data['JT_XFJE'])
JY_XFCS = normlize2(data['JY_XFCS'])
JY_XFJE = normlize2(data['JY_XFJE'])
GW_XFCS = normlize2(data['GW_XFCS'])
GW_XFJE = normlize2(data['GW_XFJE'])
JS_XFCS = normlize2(data['JS_XFCS'])
JS_XFJE = normlize2(data['JS_XFJE'])
XY_XFCS = normlize2(data['XY_XFCS'])
XY_XFJE = normlize2(data['XY_XFJE'])
QT_XFCS = normlize2(data['QT_XFCS'])
QT_XFJE = normlize2(data['QT_XFJE'])
IN_COUNT = normlize2(data['IN_COUNT'])
OUT_COUNT = normlize2(data['OUT_COUNT'])



df2.insert(0,column='SUM_XFCS', value=SUM_XFCS)
df2.insert(0,column='SUM_XFJE', value=SUM_XFJE)
df2.insert(0,column='CY_XFCS', value=CY_XFCS)
df2.insert(0,column='CY_XFJE', value=CY_XFJE)
df2.insert(0,column='YS_XFCS', value=YS_XFCS)
df2.insert(0,column='YS_XFJE', value=YS_XFJE)
df2.insert(0,column='JF_XFCS', value=JF_XFCS)
df2.insert(0,column='JF_XFJE', value=JF_XFJE)
df2.insert(0,column='JT_XFCS', value=JT_XFCS)
df2.insert(0,column='JT_XFJE', value=JT_XFJE)
df2.insert(0,column='JS_XFCS', value=JS_XFCS)
df2.insert(0,column='JS_XFJE', value=JS_XFJE)
df2.insert(0,column='GW_XFCS', value=GW_XFCS)
df2.insert(0,column='GW_XFJE', value=GW_XFJE)
df2.insert(0,column='JY_XFCS', value=JY_XFCS)
df2.insert(0,column='JY_XFJE', value=JY_XFJE)
df2.insert(0,column='XY_XFCS', value=XY_XFCS)
df2.insert(0,column='XY_XFJE', value=XY_XFJE)
df2.insert(0,column='QT_XFCS', value=QT_XFCS)
df2.insert(0,column='QT_XFJE', value=QT_XFJE)
df2.insert(0,column='IN_COUNT', value=IN_COUNT)
df2.insert(0,column='OUT_COUNT', value=OUT_COUNT)


name = 'CSDM'
name1 = 'YWCJ'
name2 = 'SXCJ'
name3 = 'WYCJ'
name4 = 'ZHCJ'

CJ = normlize1(data[[name, name1, name2, name3, name4 ]], name1, name2, name3, name4)
print(CJ.shape)

print(CJ[:,0])

name = ['YW','SX','WY', 'ZH']
for i in range(len(name1)):
    df2.insert(0,column=name[i], value=CJ[:,i])

df2.insert(0, column='ZF_RATIO', value=data['ZF_RATIO'])
df2.insert(0, column='ZF_RANK', value=data['ZF_RANK'])
df2.insert(0, column='LABEL_NUM', value=data['LABEL'])

# df2.insert(0,column=['YW','SX','WY', 'ZH'], value=CJ)

print(df2)

df2.to_csv('result3.csv')