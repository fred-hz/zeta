import os, pickle
import numpy as np

with open('data/cache/di_list', 'rb') as fp:
    di_list = pickle.load(fp)
with open('data/cache/ii_list', 'rb') as fp:
    ii_list = pickle.load(fp)

alpha = np.zeros((len(di_list),len(ii_list)))
with open('log/alphas_for_blk.txt', 'r') as fp:
	files = fp.read().splitlines()
with open('log/weights_for_blk.txt', 'r') as fp:
	weights = fp.read().splitlines()

for i, file_ in enumerate(files):
    with open('log/'+file_, 'rb') as fp:
        alphaMap = pickle.load(fp)
    for di_ in range(len(di_list)):
    	if di_list[di_] in alphaMap:
    		temp = alphaMap[di_list[di_]]
    		temp[np.isnan(temp)] = 0.
    		alpha[di_] += temp*float(weights[i])

with open('data/cache/combo_alphas/fitness_weight', 'wb') as output:
	pickle.dump(alpha, output)
