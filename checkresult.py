import numpy as np
import pickle, os
import subprocess

with open('log/alphas_for_blk.txt', 'r') as fp:
    names = fp.read().splitlines()

for name in names:
	subprocess.call(['python', 'tools/simsummary.py', 'pnl/'+name+'.csv'])
