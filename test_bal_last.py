import pandas as pd
import numpy as np
data = pd.read_csv("/home/bladeray/Code/fintech/4/test_input_bal.csv", header=None)
d = data.values
import csv
f_1 = csv.writer(open('/home/bladeray/Code/fintech/4/test_input_bal_uid_day7.txt', 'w'))
f_2 = csv.writer(open('/home/bladeray/Code/fintech/4/test_input_bal_day7_uid_pre.txt', 'w'))
for i in range(3000):
    tempd = d[i * 60: i * 60 + 60]
    for j in range(46):
        dayj = tempd[j: j + 8, 3]
        dayj = np.append(dayj, tempd[j + 14, 0])
        dayj = np.append(dayj, tempd[j + 14, 3])
        f_1.writerow(dayj)
    dtest = tempd[52: 60, 3]
    dtest = np.append(dtest, tempd[0, 0])
    f_2.writerow(dtest)