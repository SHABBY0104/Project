import numpy as np
import pandas as pd


col = ['XBM', 'CSDM', 'ZZMMM','MZM','BKSRXFSM','PYFSM', 'DWH', 'ZYH', 'RXNY','BYLBM','KQM','KSLBM','LABEL','GKZF','RXZF','YWCJ','SXCJ','WYCJ','ZHCJ','SUM_XFCS','SUM_XFJE','CY_XFCS','CY_XFJE','YS_XFCS','YS_XFJE','JF_XFCS','JF_XFJE','JT_XFCS','JT_XFJE','GW_XFCS','GW_XFJE','JS_XFCS','JS_XFJE','XY_XFCS','XY_XFJE','QT_XFCS','QT_XFJE','IN_COUNT','OUT_COUNT']

filename = "test"

f = pd.read_csv(filename+'.csv')

# f = pd.DataFrame(f)
print(f.describe())


print(f.index)
