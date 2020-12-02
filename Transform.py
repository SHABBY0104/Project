import numpy as np
import pandas as pd

def onehot( data ):

    # data = np.array(data)
    list_data = list(data)
    label = set(list_data)
    dict_label = { value : no for no , value in enumerate(label)}
    array2 = np.identity(len(label))

    one_hot = []
    for no, value in enumerate(list_data):
        one_hot.append(array2[dict_label[value]])

    one_hot = np.array(one_hot)
    return one_hot

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

def normlize2( data ):

    data = np.array(data)

    _range = np.max(data) - np.min(data)
    return (data - np.min(data)) / _range

def normlize3( data ):

    data = np.array(data)

    mu = np.mean(data, axis=0)
    sigma = np.std(data, axis=0)
    return (data - mu) / sigma


col = ['XBM', 'CSDM', 'ZZMMM','MZM','BKSRXFSM','PYFSM', 'DWH', 'ZYH', 'RXNY','BYLBM','KQM','KSLBM','LABEL','GKZF','RXZF','YWCJ','SXCJ','WYCJ','ZHCJ','SUM_XFCS','SUM_XFJE','CY_XFCS','CY_XFJE','YS_XFCS','YS_XFJE','JF_XFCS','JF_XFJE','JT_XFCS','JT_XFJE','GW_XFCS','GW_XFJE','JS_XFCS','JS_XFJE','XY_XFCS','XY_XFJE','QT_XFCS','QT_XFJE','IN_COUNT','OUT_COUNT']

filename = "test"
newfilename = 'result'

# new_data = pd.DataFrame(columns=['XBM', 'CSDM', 'ZZMMM','MZM','BKSRXFSM','PYFSM', 'DWH', 'ZYH', 'RXNY','BYLBM','KQM','KSLBM','LABEL','GKZF','RXZF','YWCJ','SXCJ','WYCJ','ZHCJ','SUM_XFCS','SUM_XFJE','CY_XFCS','CY_XFJE','YS_XFCS','YS_XFJE','JF_XFCS','JF_XFJE','JT_XFCS','JT_XFJE','GW_XFCS','GW_XFJE','JS_XFCS','JS_XFJE','XY_XFCS','XY_XFJE','QT_XFCS','QT_XFJE','IN_COUNT','OUT_COUNT'])


data = pd.read_csv(filename+'.csv')
data.fillna(-1,inplace=True)

columns = data.columns
# print(columns)

xbm = data['XBM']
xbm = onehot( xbm )
print(xbm)
print(xbm.shape)

new_data = pd.DataFrame(xbm)
print(new_data)

new_data.to_csv(newfilename+'.csv',sep=',')




csdm = data['CSDM']
csdm = onehot(csdm)

ZZMMM = onehot(data['ZZMMM'])
print("ZZMMM", ZZMMM.shape)

MZM = onehot(data['MZM'])
print("MZM", MZM.shape)

BKSRXFSM = onehot(data['BKSRXFSM'])
print("BKSRXFSM", BKSRXFSM.shape)

PYFSM = onehot(data['PYFSM'])
print("PYFSM", PYFSM.shape)

DWH = onehot(data['DWH'])
print("DWH", DWH.shape)

ZYH = onehot(data['ZYH'])
print("ZYH", ZYH.shape)

RXNY = onehot(data['RXNY'])
print("RXNY", RXNY.shape)


BYLBM = onehot(data['BYLBM'])
print("BYLBM", BYLBM.shape)

KQM = onehot(data['KQM'])
print("KQM", KQM.shape)

KSLBM = onehot(data['KSLBM'])
print("KSLBM", KSLBM.shape)

LABEL = onehot(data['LABEL'])
print("LABEL", LABEL.shape)



SUM_XFCS = normlize2(data['SUM_XFCS'])
print(SUM_XFCS)
print(SUM_XFCS.shape)

SUM_XFJE = normlize2(data['SUM_XFJE'])
CY_XFCS = normlize2(data['CY_XFCS'])
CY_XFJE = normlize2(data['CY_XFJE'])
YS_XFCS = normlize2(data['YS_XFCS'])
YS_XFJE = normlize2(data['YS_XFJE'])
JF_XFCS = normlize2(data['JF_XFCS'])
JF_XFJE = normlize2(data['JF_XFJE'])
JT_XFCS = normlize2(data['JT_XFCS'])
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


name = 'CSDM'
name1 = 'YWCJ'
name2 = 'SXCJ'
name3 = 'WYCJ'
name4 = 'ZHCJ'

YWCJ = normlize1(data[[name, name1, name2, name3, name4 ]], name1, name2, name3, name4)
print(YWCJ)


