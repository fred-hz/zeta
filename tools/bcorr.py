from util import corr
import sys, os
import numpy as np

def bcorr(file1, file2):
    with open(file1, 'r') as fp1:
        cont1 = fp1.read().splitlines()
    with open(file2, 'r') as fp2:
        cont2 = fp2.read().splitlines()
    rList1 = []
    rList2 = []
    dList1 = []
    dList2 = []
    for line in cont1:
        items = line.split()
        rList1.append(float(items[1]))
        dList1.append(int(items[0]))
    for line in cont2:
        items = line.split()
        rList2.append(float(items[1]))
        dList2.append(int(items[0]))
    if dList1[0] > dList2[-1] or dList2[0] > dList1[-1]:
        print('Warning: No lapping!!!')
        return
    elif dList1[0] <= dList2[0] and dList1[-1] >= dList2[-1]:
        r1 = np.array(rList1[dList1.index(dList2[0]) : dList1.index(dList2[-1])+1])
        r2 = np.array(rList2)
    elif dList2[0] <= dList1[0] and dList2[-1] >= dList1[-1]:
        r1 = np.array(rList2[dList2.index(dList1[0]) : dList2.index(dList1[-1])+1])
        r2 = np.array(rList1)
    elif dList1[0] <= dList2[0] and dList1[-1] <= dList2[-1]:
        r1 = np.array(rList1[dList1.index(dList2[0]) : ])
        r2 = np.array(rList2[ : dList2.index(dList1[-1])+1])
    elif dList2[0] <= dList1[0] and dList2[-1] <= dList1[-1]:
        r1 = np.array(rList2[dList2.index(dList1[0]) : ])
        r2 = np.array(rList1[ : dList1.index(dList2[-1])+1])
    return corr(r1,r2)

if __name__ == '__main__':
    if len(sys.argv) == 3 and os.path.isfile(sys.argv[1]) and os.path.isfile(sys.argv[2]):
        print(bcorr(sys.argv[1], sys.argv[2]))
    else:
        print('Input Error!!!')
