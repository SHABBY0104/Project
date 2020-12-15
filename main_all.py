import pandas as pd
import numpy as np
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.preprocessing import LabelEncoder


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


filename = 'XSCJ_RXNL_ALL'

data = pd.read_csv(filename+'.csv')
# data2 = pd.read_csv(filename+'.csv',dtype=str)

data.fillna(-1,inplace=True)
# data2.fillna('-1',inplace=True)


# col = ['XBM', 'CSDM', 'ZZMMM','MZM','BKSRXFSM','PYFSM', 'DWH', 'ZYH', 'RXNY','BYLBM','KQM','KSLBM','LABEL']
# col = ['XBM', 'CSDM', 'ZZMMM','MZM','XSDQZTM','BKSRXFSM','PYFSM','DWH','ZYH','RXNY','BYLBM','KLDM','KQM','KSLBM','SYDM','LABEL','GKZF','RXZF','YWCJ','SXCJ','WYCJ','ZHCJ','YWJB','SXJB','WYJB','ZHJB','RXNL']
# subData = pd.DataFrame(data[['XBM', 'CSDM', 'ZZMMM','MZM','BKSRXFSM','PYFSM', 'DWH', 'ZYH', 'RXNY','BYLBM','KQM','KSLBM','LABEL']])
oneHotCol = ['XBM', 'CSDM', 'ZZMMM', 'MZM', 'XSDQZTM', 'BKSRXFSM', 'PYFSM', 'DWH', 'ZYH', 'RXNY', 'BYLBM', 'KLDM', 'KSLBM', 'SYDM', 'LABEL', 'YWJB', 'SXJB', 'WYJB','ZHJB','RXNL' ]
# subData = data[['XBM', 'CSDM', 'ZZMMM','MZM','XSDQZTM','BKSRXFSM','PYFSM','DWH','ZYH','RXNY','BYLBM','KLDM','KQM','KSLBM','SYDM','LABEL','GKZF','RXZF','YWCJ','SXCJ','WYCJ','ZHCJ','YWJB','SXJB','WYJB','ZHJB','RXNL']]
# print(subData)

subData = pd.DataFrame(data[['XBM', 'CSDM', 'ZZMMM','MZM','XSDQZTM','BKSRXFSM','PYFSM','DWH','ZYH','RXNY','SYDM','LABEL','YWJB','SXJB','WYJB','ZHJB','RXNL']])

subData = subData.applymap(lambda x: x if isinstance(x, list) else [x])

mlb = MultiLabelBinarizer()
vals = [pd.Series(mlb.fit_transform(subData[x]).tolist()) for x in subData.columns]
df1 = pd.concat(vals, keys=subData.columns, axis=1)


print(df1)


# # print(type(data['KQM'][43527]))
# c = c.applymap(lambda x: x if isinstance(x, list) else [x])
#
# mlb = MultiLabelBinarizer()
# vals = [pd.Series(mlb.fit_transform(subData[x]).tolist()) for x in subData.columns]
# print(vals)


# tmp = ['XBM', 'CSDM', 'ZZMMM', 'MZM', 'XSDQZTM', 'BKSRXFSM', 'PYFSM', 'DWH', 'ZYH', 'RXNY','KLDM','SYDM','LABEL','YWJB','SXJB','WYJB','ZHJB','RXNL']
#
DEL = ['KQM','BYLBM','KSLBM']
#
#
subData2 = pd.DataFrame(data=data[DEL],dtype='int')
print(subData2)

subData2 = subData2.applymap(lambda x: x if isinstance(x, list) else [x])

mlb = MultiLabelBinarizer()
vals = [pd.Series(mlb.fit_transform(subData2[x]).tolist()) for x in subData2.columns]
df2 = pd.concat(vals, keys=subData2.columns, axis=1)

df = pd.concat([df1,df2],axis=1)


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
    df.insert(0,column=name[i], value=CJ[:,i])



print(df)
df.insert(0, column='LABEL_num', value=data['LABEL'])
df.insert(0, column='XH', value=data['XH'])

df.to_csv("result_all_20201215.csv")
